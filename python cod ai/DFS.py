# Neighbors (g) values
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

def dfs(start, goal):
    stack, visited, result = [start], set(), ''
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            result += current + ' '
            if current == goal:
                return result
            stack.extend(reversed([n for n in gn[current] if n not in visited]))

start, goal = 'Mumbai', 'Delhi'
result = dfs(start, goal)
if isinstance(result, str):  
    result = result.split() 
print(f"DFS Traversal from {start} to {goal}:")
print(' -> '.join(result))
