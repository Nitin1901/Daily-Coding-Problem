class Element:
    def __init__(self, X, Y, distance):
        self.X = X
        self.Y = Y
        self.distance = distance

def isValid(tiles, m, n, visited, i, j):
    if i<0 or j<0:
        return False
    if i>=m or j>=n:
        return False
    if tiles[i][j]:
        return False
    if visited[i][j]:
        return False
    return True

def findPath(tiles, startX, startY, endX, endY):
    m = len(tiles)
    n = len(tiles[0]) if m>0 else 0
    visited = [[False for _ in range(m)] for _ in range(m)]
    queue = []

    if isValid(tiles, m, n, visited, startX, startY):
        queue.append(Element(startX, startY, 0))
        visited[startX][startY] = True
    
    while queue:
        ele = queue.pop(0)
        print(ele.X, ele.Y)
        if ele.X == end[0] and ele.Y == end[1]:
            return ele.distance
        if isValid(tiles, m, n, visited, ele.X+1, ele.Y):
            queue.append(Element(ele.X+1, ele.Y, ele.distance+1))
        if isValid(tiles, m, n, visited, ele.X, ele.Y+1):
            queue.append(Element(ele.X, ele.Y+1, ele.distance+1))
        if isValid(tiles, m, n, visited, ele.X-1, ele.Y):
            queue.append(Element(ele.X-1, ele.Y, ele.distance+1))
        if isValid(tiles, m, n, visited, ele.X, ele.Y-1):
            queue.append(Element(ele.X, ele.Y-1, ele.distance+1))

    return -1

tiles = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]

start = (2, 0)
end = (0, 0)

print(findPath(tiles, start[0], start[1], end[0], end[1]))