# def get_and_make_dicts():
#     ltr = input("Введите вершину или `end` для окончания ввода")

infinity = float("inf")

graph = {}
graph["A"] = {}
graph["A"]["B"] = 5
graph["A"]["C"] = 2
graph["B"] = {}
graph["B"]["D"] = 4
graph["B"]["E"] = 2
graph["C"] = {}
graph["C"]["B"] = 8
graph["C"]["E"] = 7
graph["D"] = {}
graph["D"]["F"] = 3
graph["D"]["E"] = 6
graph["E"] = {}
graph["E"]["F"] = 1
graph["F"] = {}

coast = {}
coast["B"] = 5
coast["C"] = 2
coast["D"] = infinity
coast["E"] = infinity
coast["F"] = infinity

parents = {}
parents["B"] = "A"
parents["C"] = "A"
parents["D"] = None
parents["E"] = None
parents["F"] = None

class Dijkstra():
    """Реализует алгоритм Дейкстры"""

    def __init__(self) -> None:
        infinity = float("inf")
        self.processed = []

    def find_min_path(self, graph:dict, costs:dict, parents:dict) -> int:
        node = self._find_lowest_cost_node(costs=costs)
        while node is not None:
            cost = costs[node]
            neighbors:dict = graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
            self.processed.append(node)
            node = self._find_lowest_cost_node(costs=costs)
        return costs["F"]

    def _find_lowest_cost_node(self, costs:dict) -> str:
        lowest_cost = infinity
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

d = Dijkstra()
result = d.find_min_path(
    graph=graph,
    costs=coast,
    parents=parents,
)
print(result)
