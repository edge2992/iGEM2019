import numpy as np
import matplotlib.pyplot as plt

# 高さ、幅
h, w = 100, 100

grid = np.ones((h+1, w+1))


def search(i, j, r1, r2):
    a = np.array([i, j])
    a_right = np.array([i-w, j])
    a_left = np.array([i+w, j])
    a_top = np.array([i, j-h])
    a_bottom = np.array([i, j+h])
    print(a[1])
    count = 0
    for s in range(1, h + 1):
        for t in range(1, 1 + w):
            b = np.array([s, t])
            l = min(np.linalg.norm(b - a), np.linalg.norm(b - a_right), np.linalg.norm(b - a_left), np.linalg.norm(b - a_top), np.linalg.norm(b - a_bottom))
            if l < r2:
                if l < r1:
                    #内側の円
                    # print("count1")
                    count = count + 1
                    grid[s, t] = 20
                else:
                    #外側の円
                    # print("count2")
                    grid[s, t] = 10
    return count


print(search(25, 25, 25, 50))

fig, ax = plt.subplots()
ax.imshow(grid)
plt.show()

