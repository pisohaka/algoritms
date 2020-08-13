def ConquestCampaign(N: int, M: int, L: int, battalion) -> int:
    days = 1
    size = L
    points = []
    for val in battalion:
        points.append(val - 1)
    battleMap = [[0 for col in range(M)] for row in range(N)]
    while True:
        x_points = points[0:][::2]
        y_points = points[1:][::2]
        for i in range(size):
            battleMap[x_points[i]][y_points[i]] = 1
        for row in battleMap:
            if 0 in row:
                break
        else:
            return days
        points = []
        for i in range(size):
            if (x_points[i] + 1) <= N - 1:
                if battleMap[x_points[i] + 1][y_points[i]] == 0:
                    points.append(x_points[i] + 1)
                    points.append(y_points[i])
            if (x_points[i] - 1) >= 0:
                if battleMap[x_points[i] - 1][y_points[i]] == 0:
                    points.append(x_points[i] - 1)
                    points.append(y_points[i])
            if (y_points[i] + 1) <= M - 1:
                if battleMap[x_points[i]][y_points[i] + 1] == 0:
                    points.append(x_points[i])
                    points.append(y_points[i] + 1)
            if (y_points[i] - 1) >= 0:
                if battleMap[x_points[i]][y_points[i] - 1] == 0:
                    points.append(x_points[i])
                    points.append(y_points[i] - 1)
        size = int(len(points)/2)
        days += 1
