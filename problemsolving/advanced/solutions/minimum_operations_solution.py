"""
There are n boxes in front of you. For each ,i box i contains r[i] red balls, g[i] green balls, and b[i] blue balls.
You want to separate the balls by their color. In each operation, you can pick a single ball from some box and put it into another box. The balls are separated if no box contains balls of more than one color.
Debug the given function min_operations and compute the minimal number of operations required to separate the balls.
Note: In this problem you can modify at most six lines of code and you cannot add any new lines.

Input Format

The first line contains a single integer n.
The next n lines i contain three space-separated integers,r[i] ,g[i] , and b[i], respectively.
Print the minimal number of operations required to separate the balls. If this is impossible, return .

Sample Input
3
1 1 1
1 1 1
1 1 1
Sample Output
6
"""


def min_operations(red, green, blue):
    dp = [[(1 << 30) for x in range(7)] for y in range(101)]
    n = len(red)
    dp[0][0] = 0
    for i in range(0, n):
        for j in range(0, 7):
            dp[i + 1][j | 1] = min(dp[i + 1][j | 1], dp[i][j] + green[i] + blue[i])
            dp[i + 1][j | 2] = min(dp[i + 1][j | 2], dp[i][j] + red[i] + blue[i])
            dp[i + 1][j | 4] = min(dp[i + 1][j | 4], dp[i][j] + blue[i] + green[i])

    j = 0
    for i in range(0, n):
        if green[i]:
            j |= 1
        if red[i]:
            j |= 2
        if blue[i]:
            j |= 4

    if dp[n][j] >= (1 << 30):
        dp[n][j] = -1

    return dp[n][j]


n = int(input())
red = []
green = []
blue = []
for i in range(n):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)
print(min_operations(red, green, blue))
