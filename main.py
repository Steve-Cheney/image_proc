from skimage import io
import numpy as np
from matplotlib import pyplot as plt

my_image = io.imread("images/test_image.jpg")
print(my_image)
my_image2 = my_image*2

random_image = np.random.random([500,500])
plt.imshow(my_image)
plt.show()

plt.imshow(my_image2)
plt.show()