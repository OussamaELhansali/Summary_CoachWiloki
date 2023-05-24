import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sc
import json


def add(a, b):
    return a + b


def tableau_données(tab_event):
    with open(tab_event) as file:
        data = file.read()
        # This converts json into a Python object
        data = json.loads(data)
    parsed_data = data["data"]
    for element in parsed_data:
        if element[0] == 40:
            parsed_data.remove(element)
    array1 = parsed_data
    exercices = []
    jingles = []
    fun = []
    for i in array1:
        if i[0] == 1:
            exercices.append(i)
        if i[0] == 20:
            jingles.append(i)
        if i[0] == 10:
            fun.append(i)
    ## Adding time value
    for i in exercices:
        i[1]["time"] = i[2]
    ## Adding student's level
    for i in exercices:
        i[1]["level"] = data["lev"]
        if len(i[1]["video"]) == 0 or len(i[1]["kp"]) == 0:
            i[1]["video"] = [""]
            i[1]["kp"] = [""]
    tableau = pd.DataFrame(exercices[0][1])
    for i in exercices[1:]:
        tableau = pd.concat([tableau, pd.DataFrame(i[1])], ignore_index=True)

    tableau["chgtMatiere"] = tableau["chgtMatiere"].apply(
        lambda x: "N" if x not in ("Y", "N") else x
    )
    tableau["chgtNotion"] = tableau["chgtNotion"].apply(
        lambda x: "N" if x not in ("Y", "N") else x
    )
    tableau["video"] = tableau["video"].replace("", value=None)
    tableau["kp"] = tableau["kp"].replace("", value=None)
    return (tableau, jingles, fun)


#########################################################################
def plot_pourcentage(data_json):
    tableau = tableau_données(data_json)[0]
    # preparing the data
    tableau["chgtMatiere"] = tableau["chgtMatiere"].apply(
        lambda x: "N" if x not in ("Y", "N") else x
    )
    tableau["chgtNotion"] = tableau["chgtNotion"].apply(
        lambda x: "N" if x not in ("Y", "N") else x
    )
    tableau["video"] = tableau["video"].replace("", value=None)
    tableau["kp"] = tableau["kp"].replace("", value=None)

    # adding matière_nom column
    label_dict = {
        0: "culture générale",
        1: "maths",
        2: "francais",
        3: "anglais",
        4: "histoire",
        5: "géographie",
        6: "sciences",
    }
    tableau["matière_nom"] = tableau["matiere"].map(lambda x: label_dict[x])

    ##############################################################################
    plt.figure(figsize=(20, 20))
    # jingle_perc=round(len(tableau_données(data_json)[1])/sum(len(i) for i in tableau_données(data_json) ),2)
    fun_perc = round(
        len(tableau_données(data_json)[2])
        / (len(tableau_données(data_json)[2]) + len(tableau_données(data_json)[0])),
        2,
    )
    exo_perc = round(
        len(tableau_données(data_json)[0])
        / (len(tableau_données(data_json)[2]) + len(tableau_données(data_json)[0])),
        2,
    )
    print(f"le pourcentage des fun : {fun_perc}\nle pourcentage des exo : {exo_perc}")
    x = ["fun", "exercies"]
    y = [round(fun_perc * 100, 2), round(exo_perc * 100, 2)]
    plt.subplot(4, 2, 1)
    plt.ylim(0, 100)
    plt.ylabel("Pourcentages des contenus par session")
    plt.title("Pourcentages des contenus par session")
    plt.bar(x, y, alpha=0.5, color="blue", edgecolor="white", linewidth=1.2)
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], ha="center", va="bottom")

    ####################################################################################
    plt.subplot(4, 2, 2)
    ax = sc.histplot(
        tableau["matière_nom"],
        stat="probability",
        alpha=0.5,
        color="blue",
        edgecolor="white",
        linewidth=1.2,
    )
    for rect in ax.containers[0]:
        height = rect.get_height()
        rect.set_height(round((height * 100), 2))
    ax.bar_label(ax.containers[0])
    plt.ylabel("Pourcentage des matière par session", fontsize=8)
    plt.xlabel("matière")
    plt.ylim(0, 100)
    plt.title("Pourcentage des matières par session ")
    ####################################################################################
    plt.subplot(4, 2, 3)
    ax = sc.histplot(
        tableau["mod"],
        stat="probability",
        alpha=0.5,
        color="blue",
        edgecolor="white",
        linewidth=1.2,
    )
    for rect in ax.containers[0]:
        height = rect.get_height()
        rect.set_height(round((height * 100), 2))
    ax.bar_label((ax.containers[0]))
    plt.ylim(0, 100)
    plt.ylabel("Pourcentage des modes par session")
    plt.title("Pourcentage des modes par session")
    #####################################################################################
    plt.subplot(4, 2, 4)
    ax = sc.histplot(
        tableau["type"],
        stat="probability",
        alpha=0.5,
        color="blue",
        edgecolor="white",
        linewidth=1.2,
    )
    for rect in ax.containers[0]:
        height = rect.get_height()
        rect.set_height(round((height * 100), 2))
    ax.bar_label((ax.containers[0]))
    plt.ylim(0, 100)
    plt.ylabel("Pourcentage des types exercice par session")
    plt.title("Pourcentage des types exercice  par session")
    plt.show()
