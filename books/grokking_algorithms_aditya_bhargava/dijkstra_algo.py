# create a graph
graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['final'] = 1
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['final'] = 5
# the end node has no neighbors
graph['final'] = {}

# create a hash table with costs of all nodes
infinity = float("inf")
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['final'] = infinity


# create a hash table with parents for all nodes
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['final'] = None

# create a list with processed nodes
processed = []


def find_lowest_cost_node(hash_table_with_costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in hash_table_with_costs:
        cost = hash_table_with_costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# find the node with the lowest cost
node = find_lowest_cost_node(costs)
# the loop will end if all nodes are processed
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # if it's possible to get to the neighbor faster through the current node
        if new_cost < costs[n]:
            # update the cost of this node
            costs[n] = new_cost
            # current node will be a parent for this neighbor
            parents[n] = node
    # mark the node as processed
    processed.append(node)
    # find the next node with lowest cost
    node = find_lowest_cost_node(costs)


def main():
    lowest_way = f"start --> {parents[parents['final']]} --> {parents['final']} --> final"
    lowest_way_cost = costs['final']
    print(f'Lowest way "{lowest_way}", with cost {lowest_way_cost}.')


if __name__ == '__main__':
    main()
