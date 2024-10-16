graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List for visited nodes.
stack = []    # Initialize a stack.

def dfs(visited, graph, node):  # Function for DFS
    visited.append(node)        # Mark the node as visited
    stack.append(node)          # Push the node to the stack
    
    while stack:
        m = stack.pop()         # Pop the top node from the stack
        print(m, end=" ")       # Print the node
        
        # Add neighbors to stack in reverse order to control the traversal order
        for neighbour in reversed(graph[m]):  
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)  # Push unvisited neighbors onto the stack

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
