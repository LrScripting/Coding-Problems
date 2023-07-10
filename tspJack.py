import cv2
import numpy as np
import itertools
from itertools import combinations
image = cv2.imread('kek.jpg')


image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])


mask = cv2.inRange(image_hsv, lower_green, upper_green)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


centers = [np.round(np.mean(contour, axis=0)[0]).astype(int) for contour in contours]


distance_matrix = np.array([[np.linalg.norm(np.array(point1)-np.array(point2)) for point1 in centers] for point2 in centers])

print('Centers:', centers)
print('Distance Matrix:', distance_matrix)



def tsp_dp(distances):
    N = len(distances)

    dp = {(frozenset([i]), i): (dist, [i]) for i, dist in enumerate(distances[0])}

    for r in range(2, N + 1):
        for visited in combinations(range(1, N), r - 1):
            for last in visited:
                if len(visited) <= 1:
                    continue
                candidates = [(dp[frozenset(visited) - {last}, i][0] + distances[i][last], dp[frozenset(visited) - {last}, i][1] + [last]) for i in visited if i != last]
                dp[frozenset(visited), last] = min(candidates)

    opt_tour = min((dp[frozenset(range(1, N)), i][0] + distances[i][0], dp[frozenset(range(1, N)), i][1] + [0]) for i in range(1, N))

    return opt_tour


distances = [
  [0, 204.41624202, 251.44780771, 582.72549284, 367.83827968],
  [204.41624202, 0, 244.07375934, 378.35036672, 274.69437562],
  [251.44780771, 244.07375934, 0, 526.80641606, 144.8067678],
  [582.72549284, 378.35036672, 526.80641606, 0, 436.22471273],
  [367.83827968, 274.69437562, 144.8067678, 436.22471273, 0]
]


min_distance, tour = tsp_dp(distances)
print(f"Minimal tour distance: {min_distance}")
print(f"Tour: {tour}")
print(centers)
print(distance_matrix)
tour_indices = [1, 3, 4, 2, 0]


for center in centers:
    cv2.circle(image, tuple(center), 3, (255, 0, 0), -1)  # draw a red circle

for i in range(len(tour_indices) - 1):
    cv2.line(image, tuple(centers[tour_indices[i]]), tuple(centers[tour_indices[i + 1]]), (0, 255, 0), 2)  # draw a green line


cv2.line(image, tuple(centers[tour_indices[-1]]), tuple(centers[tour_indices[0]]), (0, 255, 0), 2)

cv2.imshow("Tour", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
