import random

waypoints = [[-50, 310], [171, 309], [170, 420], [330, 420], [330, 310], [450, 310], [450, 190], [680, 190], [680, 310], [800, 310]]

scatter = []
for point in waypoints:
    x = point[0] + random.randint(0, 30) - random.randint(0, 30)
    y = point[1] + random.randint(0, 30) - random.randint(0, 30)
    tup = (x, y)
    scatter.append(tup)
print(scatter)