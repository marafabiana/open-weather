import matplotlib.pyplot as plt
import pandas as pd
from open_weather.visualization.common.Orientation import Orientation
from open_weather.visualization.common.Legend import Legend


def barchart(
        df: pd.DataFrame,
        title: str,
        x_label: str,
        y_label: str,
        is_grid_visible: bool = True,
        is_stacked: bool = False,
        legend: Legend = None,
        orientation: Orientation = Orientation.VERTICAL,
        fig_size: tuple = plt.rcParams["figure.figsize"], # (width = 6.4, height = 4.8) in inches
        x_axis_tick_orientation: Orientation = Orientation.HORIZONTAL
):
    # Create the figure and axis
    fig, ax = plt.subplots(figsize = fig_size)

    # Plot the chart
    bar_orientation = 'barh' if orientation == Orientation.HORIZONTAL else 'bar'
    df.plot(kind=bar_orientation, stacked=is_stacked, ax=ax) 

    # Customize the chart
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Customize the grid
    if is_grid_visible:
        ax.grid(True, linestyle="--", alpha=0.6)

    # Customize the legend
    if legend != None:
        ax.legend(title=legend.title, loc=legend.position.value)

    # Customize the tick orientation
    for tick in ax.get_xticklabels():
        tick.set_rotation(x_axis_tick_orientation.value)

    
    # Adjust the layout
    fig.tight_layout()
    
    # Show the plot
    plt.show()

    