import queue as Q
hn = {
    'Mumbai': 336, 'Delhi': 0, 'Bangalore': 160, 'Hyderabad': 242,
    'Chennai': 161, 'Pune': 77, 'Ahmedabad': 151, 'Jaipur': 226
}

gn = {
    'Mumbai': {'Pune': 75, 'Ahmedabad': 118, 'Bangalore': 140},
    'Delhi': {'Jaipur': 85, 'Ahmedabad': 90, 'Bangalore': 101, 'Hyderabad': 211},
    'Bangalore': {'Hyderabad': 120, 'Chennai': 138, 'Mumbai': 146},
    'Hyderabad': {'Bangalore': 120, 'Delhi': 211},
    'Chennai': {'Bangalore': 138},
    'Pune': {'Mumbai': 75},
    'Ahmedabad': {'Mumbai': 118, 'Delhi': 90},
    'Jaipur': {'Delhi': 85}
}

# A* search function
def astar(start, goal):
    q = Q.PriorityQueue()
    q.put((hn[start], start, [start]))

    while not q.empty():
        cost, city, path = q.get()

        if city == goal:
            print("Path:", " -> ".join(path), "| Total cost:", cost)
            return

        for neighbor, distance in gn[city].items():
            new_cost = cost - hn[city] + distance + hn[neighbor]
            q.put((new_cost, neighbor, path + [neighbor]))

# Run A* search
astar('Mumbai','Delhi')
