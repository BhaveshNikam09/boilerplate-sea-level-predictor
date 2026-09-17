import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import the data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Linear regression using all the data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create years from the first year to 2050
    years = pd.Series(range(df["Year"].min(), 2051))

    # Calculate predicted sea levels
    sea_level = slope * years + intercept

    # Plot first line of best fit
    ax.plot(
        years,
        sea_level,
        label="Line of best fit"
    )

    # Filter data from year 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    # Linear regression using data from 2000 onwards
    slope_recent, intercept_recent, _, _, _ = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Create years from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))

    # Calculate predicted sea levels
    sea_level_recent = (
        slope_recent * years_recent + intercept_recent
    )

    # Plot second line of best fit
    ax.plot(
        years_recent,
        sea_level_recent,
        label="Line of best fit since 2000"
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return
    fig.savefig("sea_level_plot.png")
    return fig