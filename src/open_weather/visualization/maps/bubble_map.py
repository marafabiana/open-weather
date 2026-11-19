import plotly.express as px


def bubble_map(df, title):
    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lon",
        size="pressure",
        color="temperature",
        hover_name="country",
        title=title,
    )
    fig.show()