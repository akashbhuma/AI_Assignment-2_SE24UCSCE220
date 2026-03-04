from collections import deque
import heapq

start = (3,3,0)
goal = (0,0,1)

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def valid(mLeft,cLeft):

    mRight = 3 - mLeft
    cRight = 3 - cLeft

    if mLeft < 0 or cLeft < 0 or mLeft > 3 or cLeft > 3:
        return False

    if mLeft > 0 and mLeft < cLeft:
        return False

    if mRight > 0 and mRight < cRight:
        return False

    return True


def nextStates(state):

    m,c,boat = state
    states = []

    for mMove,cMove in moves:

        if boat == 0:
            newState = (m-mMove, c-cMove, 1)
        else:
            newState = (m+mMove, c+cMove, 0)

        if valid(newState[0], newState[1]):
            states.append(newState)

    return states



def bfs():

    queue = deque([(start,[start])])
    visited = set()

    while queue:

        state,path = queue.popleft()

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for s in nextStates(state):
                queue.append((s,path+[s]))


def dfs():

    stack = [(start,[start])]
    visited = set()

    while stack:

        state,path = stack.pop()

        if state == goal:
            return path

        if state not in visited:
            visited.add(state)

            for s in nextStates(state):
                stack.append((s,path+[s]))



def dls(limit):

    stack = [(start,[start],0)]
    visited = set()

    while stack:

        state,path,depth = stack.pop()

        if state == goal:
            return path

        if depth < limit and state not in visited:

            visited.add(state)

            for s in nextStates(state):
                stack.append((s,path+[s],depth+1))

    return None



def iddfs():

    depth = 0

    while True:

        result = dls(depth)

        if result:
            return result

        depth += 1



def ucs():

    pq = []
    heapq.heappush(pq,(0,start,[start]))

    visited = set()

    while pq:

        cost,state,path = heapq.heappop(pq)

        if state == goal:
            return path,cost

        if state not in visited:

            visited.add(state)

            for s in nextStates(state):
                heapq.heappush(pq,(cost+1,s,path+[s]))


print("BFS:", bfs())
print("\nDFS:", dfs())
print("\nDepth Limited Search:", dls(20))
print("\nIterative Deepening DFS:", iddfs())
ucsPath,cost = ucs()
print("\nUCS:", ucsPath)
print("Cost:",cost)
