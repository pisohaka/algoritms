def odometer(oksana) -> int:
    speed = oksana[0:][::2]
    time = oksana[1:][::2]
    distance = 0
    for i in range(len(speed)):
        if i == 0:
            distance = distance + speed[i] * time[i]
        else:
            distance = distance + speed[i] * (time[i] - time[i-1])
    return distance
