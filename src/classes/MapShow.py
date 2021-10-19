from osmread import parse_file, Way, Node
from src.classes.Build import Build
import matplotlib.pyplot as plt


class MapShow:
    def __init__(self, filepath):
        self.parsed_data = parse_file(filepath)
        self.houses = {}
        self.nodes = {}
        self.roads = {}
        self.parse_nodes()

    def parse_nodes(self):
        for entity in self.parsed_data:
            if isinstance(entity, Way):
                self.houses[entity.id] = Build(entity)
                pass
            elif isinstance(entity, Node):
                self.nodes[entity.id] = entity
        pass

    def parse_node_cords(self, nodes):
        node_cords_lat = []
        node_cords_lon = []
        for node_id in nodes:
            node = self.nodes[node_id]
            node_cords_lat.append(node.lat)
            node_cords_lon.append(node.lon)
        return node_cords_lat, node_cords_lon

    def show_map(self):
        fig, ax = plt.subplots()
        for house_id in self.houses:
            house = self.houses[house_id]
            house_lat, house_lon = self.parse_node_cords(house.nodes)
            ax.scatter(house_lon, house_lat,
                       color=house.color, s=house.line_width, zorder=house.z_order)

            if house.filled:
                ax.fill(
                    house_lon, house_lat,
                    color=house.color,
                    zorder=0
                )
            else:
                ax.plot(
                    house_lon, house_lat,
                    color=house.color, linewidth=house.line_width,
                    zorder=house.z_order)

        plt.show()

        pass
