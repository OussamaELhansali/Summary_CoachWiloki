from coach_stat1 import tableau_données
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sc
import json
from IPython.core.display import display, HTML


def histogramme_moyen(file_names, column_name):
    def histogram_to_dict(histogram, column):
        data = {}
        for patch, value in zip(histogram.patches, column.unique()):
            height = patch.get_height()
            data[value] = height
        return data

    def dico_matière(dico1, dico2):
        def unsqueeze_lists(input_list):
            unsqueezed_list = []
            for item in input_list:
                if isinstance(item, list):
                    unsqueezed_list.extend(item)
                else:
                    unsqueezed_list.append(item)
            return unsqueezed_list

        d = {}
        keys_1 = list(dico1.keys())
        keys_2 = list(dico2.keys())
        for i in keys_1:
            if i in keys_2:
                d[i] = unsqueeze_lists([dico1[i], dico2[i]])
                keys_2.remove(i)
            else:
                d[i] = dico1[i]
        for j in keys_2:
            d[j] = dico2[j]
        return d

    l = []
    label_dict = {
        0: "culture générale",
        1: "maths",
        2: "francais",
        3: "anglais",
        4: "histoire",
        5: "géographie",
        6: "sciences",
        11: "Physiques chimie",
    }

    # List of file names

    j = 1
    l1 = []
    if column_name != "diff_relatif":
        plt.figure(
            figsize=(
                30,
                ((len(file_names)) // 3 + int(np.heaviside(len(file_names) % 3, 0)))
                * 5,
            )
        )
    else:
        plt.figure(
            figsize=(
                30,
                ((len(file_names)) // 3 + int(np.heaviside(len(file_names) % 3, 0)))
                * 5
                * 2,
            )
        )
    for file_name in file_names:
        if column_name != "diff_relatif" and column_name != "matière_nom":
            tableau = tableau_données(file_name)[0]
            tableau["diff_relatif"] = (
                tableau["diff"].astype(int) + tableau["level"] - 10
            )
            tableau["matière_nom"] = tableau["matiere"].map(lambda x: label_dict[x])
            sorted_data = tableau.sort_values(column_name)
            plt.subplot(
                int(((len(file_names)) // 3 + np.heaviside(len(file_names) % 3, 0))),
                3,
                j,
            )
            ax = sc.histplot(
                sorted_data[column_name],
                stat="probability",
                alpha=0.5,
                color="blue",
                edgecolor="white",
                linewidth=1.2,
                discrete=True,
            )
            for rect in ax.containers[0]:
                height = rect.get_height()
                rect.set_height(round((height * 100), 2))
            ax.bar_label(ax.containers[0])
            plt.ylabel(f"Pourcentage des {column_name} par session", fontsize=8)
            plt.xlabel(f"{column_name}")
            plt.ylim(0, 100)
            plt.title(f"Pourcentage des {column_name} par session {j}")
            l.append(histogram_to_dict(ax, sorted_data[column_name]))

            j += 1
        elif column_name == "matière_nom":
            tableau = tableau_données(file_name)[0]
            tableau["diff_relatif"] = (
                tableau["diff"].astype(int) + tableau["level"] - 10
            )
            tableau["matière_nom"] = tableau["matiere"].map(lambda x: label_dict[x])
            sorted_data = tableau.sort_values("matiere")
            plt.subplot(
                int(((len(file_names)) // 3 + np.heaviside(len(file_names) % 3, 0))),
                3,
                j,
            )
            ax = sc.histplot(
                sorted_data[column_name],
                stat="probability",
                alpha=0.5,
                color="blue",
                edgecolor="white",
                linewidth=1.2,
                discrete=True,
            )
            for rect in ax.containers[0]:
                height = rect.get_height()
                rect.set_height(round((height * 100), 2))
            ax.bar_label(ax.containers[0])
            plt.ylabel(f"Pourcentage des {column_name} par session", fontsize=8)
            plt.xlabel(f"{column_name}")
            plt.ylim(0, 100)
            plt.title(f"Pourcentage des {column_name} par session {j}")
            l.append(histogram_to_dict(ax, sorted_data[column_name]))

            j += 1
        else:
            tableau = tableau_données(file_name)[0]
            tableau["diff_relatif"] = (
                tableau["diff"].astype(int) + tableau["level"] - 10
            )
            tableau["type"] = tableau["type"].astype(str)
            quizz = tableau[tableau["type"] == "quiz"]
            coach = tableau[tableau["type"] == "coach"]
            plt.subplot(
                int(((len(file_names)) // 3 + np.heaviside(len(file_names) % 3, 0)))
                * 2,
                3,
                j,
            )
            ax = sc.histplot(
                coach[column_name],
                stat="probability",
                alpha=0.5,
                color="blue",
                edgecolor="white",
                linewidth=1.2,
                discrete=True,
            )
            for rect in ax.containers[0]:
                height = rect.get_height()
                rect.set_height(round((height * 100), 2))
            ax.bar_label(ax.containers[0])
            plt.ylabel(
                f"Pourcentage des {column_name} par session pour type VOC", fontsize=8
            )
            plt.xlabel(f"{column_name}")
            plt.ylim(0, 100)
            plt.title(f"Pourcentage des {column_name} par session {j} pour type VOC")
            l.append(histogram_to_dict(ax, tableau[column_name]))
            ########################################
            plt.subplot(
                int(((len(file_names)) // 3 + np.heaviside(len(file_names) % 3, 0)))
                * 2,
                3,
                j + len(file_names) + 3 - len(file_names) % 3,
            )
            ax = sc.histplot(
                quizz[column_name],
                stat="probability",
                alpha=0.5,
                color="blue",
                edgecolor="white",
                linewidth=1.2,
                discrete=True,
            )
            for rect in ax.containers[0]:
                height = rect.get_height()
                rect.set_height(round((height * 100), 2))
            ax.bar_label(ax.containers[0])
            plt.ylabel(
                f"Pourcentage des {column_name} par session pour type quizz", fontsize=8
            )
            plt.xlabel(f"{column_name}")
            plt.ylim(0, 100)
            plt.title(f"Pourcentage des {column_name} par session {j} pour type quizz")
            l1.append(histogram_to_dict(ax, tableau[column_name]))
            j += 1

    plt.show()
    print(
        "################################################################################"
    )

    if column_name != "diff_relatif":
        plt.figure(figsize=(8, 5))
    else:
        plt.figure(figsize=(18, 5))
    if len(l) > 1 and len(l1) == 0:
        display(
            HTML(
                '<h1 style="color: cyan;">Pourcentages moyens par session</h1> 🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻'
            )
        )
        d = {}

        for i in range(len(l)):
            d = dico_matière(d, l[i])
        d = {i: round(np.mean(np.array(d[i])), 2) for i in d}
        d
        x = list(d.keys())
        y = list(d.values())
        plt.ylim(0, 100)
        plt.ylabel(
            f"Pourcentages moyens des {column_name} des {j-1} sessions", fontsize=8
        )
        plt.title(f"Pourcentages moyens des {column_name} des {j-1} sessions")
        plt.grid(color="lightblue")
        plt.bar(
            x,
            y,
            alpha=0.5,
            color="cyan",
            edgecolor="white",
            linewidth=1.2,
        )
        for i in range(len(x)):
            plt.text(x[i], y[i], y[i], ha="center", va="bottom")
        plt.show()
    elif len(l) > 1 and len(l1) > 0:
        display(
            HTML(
                '<h1 style="color: cyan;">Pourcentages moyens par session</h1> 🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻'
            )
        )
        d = {}
        for i in range(len(l)):
            d = dico_matière(d, l[i])
        d = {i: round(np.mean(np.array(d[i])), 2) for i in d}
        x = list(d.keys())
        y = list(d.values())
        plt.subplot(1, 2, 1)
        plt.ylim(0, 100)
        plt.ylabel(
            f"Pourcentages moyens des {column_name} des {j-1} sessions type VOC",
            fontsize=8,
        )
        plt.title(f"Pourcentages moyens des {column_name} des {j-1} sessions type VOC")
        plt.grid(color="lightblue")
        plt.bar(
            x,
            y,
            alpha=0.5,
            color="cyan",
            edgecolor="white",
            linewidth=1.2,
        )
        for i in range(len(x)):
            plt.text(x[i], y[i], y[i], ha="center", va="bottom")
        d1 = {}
        for i in range(len(l1)):
            d1 = dico_matière(d, l1[i])
        d1 = {i: round(np.mean(np.array(d1[i])), 2) for i in d1}
        x = list(d1.keys())
        y = list(d1.values())
        plt.subplot(1, 2, 2)
        plt.ylim(0, 100)
        plt.ylabel(
            f"Pourcentages moyens des {column_name} des {j-1} sessions type QUIZZ",
            fontsize=8,
        )
        plt.title(
            f"Pourcentages moyens des {column_name} des {j-1} sessions type QUIZZ"
        )
        plt.grid(color="lightblue")
        plt.bar(
            x,
            y,
            alpha=0.5,
            color="cyan",
            edgecolor="white",
            linewidth=1.2,
        )
        for i in range(len(x)):
            plt.text(x[i], y[i], y[i], ha="center", va="bottom")
        plt.show()
    else:
        pass
