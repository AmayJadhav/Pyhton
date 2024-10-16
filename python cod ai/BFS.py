from collections import deque
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

def bfs(start, goal):
    queue, visited = deque([start]), {start}
    path = []

    while queue:
        node = queue.popleft()
        path.append(node)
        if node == goal: 
            return path
        for neighbor in gn[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
    print(" -> ".join(bfs('Mumbai', 'Delhi')))
