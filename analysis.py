from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "study_habits.csv"
OUTPUT_DIR = Path(__file__).parent / "output"


def main():
    data = pd.read_csv(DATA_PATH)
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("=== RESUMO ===")
    print(data.describe().round(2))
    print("\nMédia de horas de estudo:", round(data["hours_study"].mean(), 2))
    print("Média das notas:", round(data["grade"].mean(), 2))
    print("Correlação entre estudo e nota:", round(data["hours_study"].corr(data["grade"]), 2))

    plt.figure(figsize=(7, 5))
    plt.scatter(data["hours_study"], data["grade"])
    plt.xlabel("Horas de estudo")
    plt.ylabel("Nota")
    plt.title("Horas de estudo x Nota")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_vs_grade.png")
    plt.close()

    category = pd.cut(
        data["hours_study"],
        bins=[0, 2, 4, float("inf")],
        labels=["Até 2h", "2h a 4h", "Mais de 4h"],
    )
    grouped = data.groupby(category, observed=False)["grade"].mean()

    plt.figure(figsize=(7, 5))
    grouped.plot(kind="bar")
    plt.xlabel("Faixa de estudo")
    plt.ylabel("Nota média")
    plt.title("Nota média por faixa de horas de estudo")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "average_grade_by_study_time.png")
    plt.close()

    print("\nGráficos salvos em output/.")


if __name__ == "__main__":
    main()
