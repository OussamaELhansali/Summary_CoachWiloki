from coach_stat1 import tableau_données
import seaborn as sc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.core.display import display, HTML


def affichage_periodicité(tab_event):
    tableau = tableau_données(tab_event)[0]
    Y = tableau["chgtMatiere"][tableau["chgtMatiere"] == "Y"].index
    l = []
    l_mod = []
    if len(Y) < 2:
        print("Il n'y a pas de changement de matière")
    else:
        for i in range(len(Y) - 1):
            l.append(Y[i + 1] - Y[i])
            l_mod.append(str(Y[i + 1] - Y[i]) + str(tableau["mod"][i])[0])
        l = np.array(l)
        print("le nombre de questions avant chaque changement de matière :", l_mod)
        print(
            f"le nombre de questions moyen avant changement de matière est : {round(np.mean(l))}"
        )
        print(
            f"l'ecart type du nombre de questions avant changement de notion est : {round(np.std(l))}"
        )
        print(
            "################################################################################"
        )

    W = tableau["chgtNotion"][tableau["chgtNotion"] == "Y"].index
    n = []
    if len(W) < 2:
        print("Il n'y a pas de changement de notion")
    else:
        for i in range(len(W) - 1):
            n.append(W[i + 1] - W[i])
        n = np.array(n)
        print("le nombre de questions avant chaque changement de notion :", n)
        print(
            f"le nombre de questions moyen avant changement de notion est : {round(np.mean(n))}"
        )
        print(
            f"l'ecart type du nombre de questions avant changement de notion est : {round(np.std(n))}"
        )
        print(
            "################################################################################"
        )

    indices = np.where(tableau["mod"].ne(tableau["mod"].shift()))[0]
    w = []
    w_mode = []
    if len(indices) < 2:
        print("Il n'y a pas de changement de mode")
    else:
        for i in range(len(indices) - 1):
            w.append(indices[i + 1] - indices[i])
            w_mode.append(
                str(indices[i + 1] - indices[i]) + str(tableau["mod"][indices[i]])[0]
            )
        w = np.array(w)
        print("le nombre de questions avant chaque changement de mode  :", w_mode)
        print(
            f"le nombre de questions moyen avant changement de mode est : {round(np.mean(w))}"
        )
        print(
            f"l'ecart type du nombre de questions avant changement de mode est : {round(np.std(w))}"
        )

    print(
        "################################################################################"
    )

    if len(indices) >= 2 and len(W) >= 2 and len(Y) >= 2:
        dico = {
            "mean": [round(np.mean(l)), round(np.mean(n)), round(np.mean(w))],
            "std": [round(np.std(l)), round(np.std(n)), round(np.std(w))],
        }
        indexes = [
            "changement de matière",
            "changement de notion",
            "changement de mode",
        ]
        mean_std = pd.DataFrame(dico, index=indexes)
        return mean_std
    elif len(indices) < 2 and len(W) >= 2 and len(Y) >= 2:
        dico = {
            "mean": [round(np.mean(l)), round(np.mean(n)), tableau.shape[0]],
            "std": [round(np.std(l)), round(np.std(n)), 0],
        }
        indexes = [
            "changement de matière",
            "changement de notion",
            "changement de mode",
        ]
        mean_std = pd.DataFrame(dico, index=indexes)
        return mean_std
    elif len(W) >= 2 and len(Y) < 2 and len(indices) < 2:
        dico = {
            "mean": [tableau.shape[0], round(np.mean(n)), tableau.shape[0]],
            "std": [0, round(np.std(n)), 0],
        }
        indexes = [
            "changement de matière",
            "changement de notion",
            "changement de mode",
        ]
        mean_std = pd.DataFrame(dico, index=indexes)
        return mean_std
    elif len(indices) >= 2 and len(Y) < 2 and len(W) < 2:
        dico = {
            "mean": [tableau.shape[0], tableau.shape[0], round(np.mean(w))],
            "std": [0, 0, round(np.std(w))],
        }
        indexes = [
            "changement de matière",
            "changement de notion",
            "changement de mode",
        ]
        mean_std = pd.DataFrame(dico, index=indexes)
        return mean_std
    else:
        dico = {
            "mean": [round(np.mean(l)), round(np.mean(n)), round(np.mean(w))],
            "std": [round(np.std(l)), round(np.std(n)), round(np.std(w))],
        }
        indexes = [
            "changement de matière",
            "changement de notion",
            "changement de mode",
        ]
        mean_std = pd.DataFrame(dico, index=indexes)
        return mean_std


def periodicity_average(files):
    dico = {"mean": [[] for i in range(3)], "std": [[] for i in range(3)]}
    j = 0
    for i in files:
        display(
            HTML(
                "<h2>Session "
                + str(j + 1)
                + "</h2>⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
            )
        )
        x = affichage_periodicité(i)
        x
        dico["mean"][0].append(x["mean"][0])
        dico["mean"][1].append(x["mean"][1])
        dico["mean"][2].append(x["mean"][2])
        dico["std"][0].append(x["std"][0])
        dico["std"][1].append(x["std"][1])
        dico["std"][2].append(x["std"][2])
        j += 1
    dico["mean"] = [round(np.mean(np.array(i))) for i in dico["mean"]]
    dico["std"] = [round(np.mean(np.array(i))) for i in dico["std"]]
    indexes = [
        "changement de matière moyen",
        "changement de notion moyen",
        "changement de mode moyen",
    ]
    display(
        HTML(
            '🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻<h1 style="color: cyan;">Périodicité moyenne</h1>'
        )
    )
    dico = pd.DataFrame(dico, index=indexes)
    return dico
