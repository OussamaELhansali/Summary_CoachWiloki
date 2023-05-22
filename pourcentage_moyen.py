from coach_stat1 import tableau_données
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sc
import json
from IPython.core.display import display, HTML

def pourcetage_moyen_contenu(files):
    avg_fun = 0
    avg_exo = 0
    j = 1
    plt.figure(
        figsize=(
            30,
            ((len(files)) // 3 + int(np.heaviside(len(files) % 3, 0))) *5,
        )
    )
    if len(files) != 1:
      for data_json in files:
        
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
          x = ["fun", "exercies"]
          y = [round(fun_perc * 100, 2), round(exo_perc * 100, 2)]
          plt.subplot(int(((len(files)) // 3 + np.heaviside(len(files) % 3, 0))), 3, j)

          plt.ylim(0, 100)
          plt.ylabel("Pourcentages des contenus par session")
          plt.title(f"Pourcentages des contenus session{j}")
          plt.bar(x, y, alpha=0.5, color="blue", edgecolor="white", linewidth=1.2)
          for i in range(len(x)):
              plt.text(x[i], y[i], y[i], ha="center", va="bottom")
          j += 1
      
      plt.show()
    else:
      pass
    for i in files:
        fun_perc = round(
            len(tableau_données(i)[2])
            / (len(tableau_données(i)[2]) + len(tableau_données(i)[0])),
            2,
        )
        exo_perc = round(
            len(tableau_données(i)[0])
            / (len(tableau_données(i)[2]) + len(tableau_données(i)[0])),
            2,
        )
        avg_fun += fun_perc
        avg_exo += exo_perc
    print("\n \n ")
    display(
    HTML(
        '<h1 style="color: cyan;">Pourcentages moyens par session</h1> 🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻'
    )
)
    avg_fun /= len(files)
    avg_exo /= len(files)
    print(
        f"le pourcentage moyen des fun : {avg_fun}\nle pourcentage moyen des exo : {avg_exo}"
    )
    x = ["fun", "exercies"]
    y = [round(avg_fun * 100, 2), round(avg_exo * 100, 2)]
    plt.figure(
        figsize=(
            8,
             5,
        )
    )
    plt.ylim(0, 100)
    plt.ylabel("Pourcentages moyens des contenus ")
    plt.title("Pourcentages moyens des contenus ")
    plt.grid(color="lightblue")
    plt.bar(x, y, alpha=0.5, color="cyan", edgecolor="white", linewidth=1.2)
    for i in range(len(x)):
        plt.text(x[i], y[i], y[i], ha="center", va="bottom")
    plt.show()
