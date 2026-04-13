#! /bin/env pỳthon


# Plot the normalized data contrasting Brent and oil prices.


import pandas as pd
import matplotlib.pyplot as plt


def load_data(nf) -> pd.DataFrame:
    return pd.read_csv(nf)



def show_data_when_Brent_is_high(df):
    df_by_year = df[df.Brent > 110].groupby("Año")[['Semana', 'Brent', 'Gasolina', 'Gasóil']]

    print(df_by_year)
    for year, group in df_by_year:
        print(f"\nYear: {year}")
        print(group)


def show_graph_evolution(df):
    plt.figure(figsize=(12, 6))
    plt.grid(True)
    plt.plot(df.Fecha, df.Brent,
            label="Brent", marker=".", color="black")
    plt.plot(df.Fecha, df.Gasolina.multiply(100),
            label="Gasolina", marker="o", color="turquoise")
    plt.plot(df.Fecha, df.Gasóil.multiply(100),
            label="Gasóil", marker="x", color="orange")
    plt.yticks(range(0, 220, 10))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    df = load_data("normalized_data.csv")
    show_data_when_Brent_is_high(df)
