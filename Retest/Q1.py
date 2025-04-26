#print("Hello, World!!") ## real test

## defining the true connected graph here
graph = []
while True:
    list_from_user = input("Give me pairs of data that you need to connect:\n").strip().lower()
    input_to_graph = list_from_user.split(",")
    graph.append([int(i.strip()) for i in input_to_graph])
    print(f"The graph is now!, {graph}") 
    
    further = input("Do u want to continue? Type either 'yes' or 'no', else 'y' or 'n':\n").strip().lower()
    if further == "yes" or further == "y":
        continue
    else:
        break
        
        

adjlst = {}
for i in graph:
    ## adding the elements into the dictionary to have all the elements 
    for j in i:
        if j not in adjlst:
            adjlst[j] = []
    
# Populate the adjacency list with the connections
for i in graph:
    for j in range(len(i)):
        # Connect i[j] to i[k] (bidirectional)
        for k in range(j + 1, len(i)):
            # Adding edge between i[j] and i[k]
            adjlst[i[j]].append(i[k])
            adjlst[i[k]].append(i[j])

# Remove duplicates from the lists (because the graph is undirected)
for node in adjlst:
    adjlst[node] = list(set(adjlst[node]))

print(f"Final adjacency list: {adjlst}")
    
