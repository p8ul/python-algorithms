def color_nodes(graph):
    # Order nodes in descending degree
    nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
    color_map = {}

    for node in nodes:
        available_colors = [True] * len(nodes)
        for child in graph[node]:
            if child in color_map:
                color = color_map[child]  # if child is colored, then the parent cannot have that color
                available_colors[color] = False

        for color, available in enumerate(available_colors):

            if available:
                color_map[node] = color
                break

    return color_map


if __name__ == '__main__':
    graph = {
        'a': list('bcd'),
        'b': list('ac'),
        'c': list('abdef'),
        'd': list('ace'),
        'e': list('cdf'),
        'f': list('ce')
    }

    print(color_nodes(graph))
