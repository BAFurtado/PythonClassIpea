""" Segundo exemplo
"""


# Sempre use a linha abaixo. É convenção Python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[0, 0].hist(data[1], alpha=.7, color='red')
# axs[0, 0].hist(data[1], alpha=.5, bins=100)
axs[0, 1].scatter(data[0], data[1], marker='.', c='orange')
axs[1, 0].scatter(data[0], data[1], marker='.')
axs[1, 1].hist2d(data[0], data[1])

plt.tight_layout()
plt.show()

#
fig2, ax2 = plt.subplots()
data2 = np.random.randn(20, 20)
# imshow display data as an image, i.e., on a 2D regular raster.
plt.imshow(data2)
plt.show()




