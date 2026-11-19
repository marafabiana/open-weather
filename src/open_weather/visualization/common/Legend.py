from open_weather.visualization.common.LegendPosition import LegendPosition


class Legend:
    def __init__(self, title: str, position: LegendPosition = LegendPosition.BEST):
        self.title = title
        self.position = position
