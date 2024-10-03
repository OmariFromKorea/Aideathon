#탈출구까지 최단경로 계산 기술적 구현(예시)

import heapq  
def dijkstra(graph, start): #다익스트라 최단경로 함수
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    return distances, previous_nodes


def get_shortest_path(previous_nodes, start, target):  # 최단경로 탐색 함수
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()  
    return path
    
# 가중치가 있는 무방향 그래프
graph = {
    'gate1': {'gate3': 1, 'gate4': 3, 'gate5': 6},
    'gate2': {}, 
    'gate3': {'gate1': 1, 'gate5': 2},
    'gate4': {'gate1': 3, 'gate5': 5},
    'gate5': {'gate1': 6, 'gate3': 2, 'gate4': 5, 'exit': 2},
    'exit' : {'gate5': 2}
}

# gate1에서 exit 최단경로 계산
start_node = 'gate1'
target_node = 'exit'
shortest_paths, previous_nodes = dijkstra(graph, start_node) 

# gate1에서 exit까지 최단 경로 출력
path = get_shortest_path(previous_nodes, start_node, target_node)
print(f"최단 경로 from {start_node} to {target_node}: {path} with distance {shortest_paths[target_node]}")
