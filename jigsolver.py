import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the jigsaw image

image = cv2.imread('photos/jigsaw.jpg')

imagecopy=image.copy()

#print(image.shape[0]);
#print(image.shape[1]);

submatrix1 = image[0:200, 0:190]
submatrix2 = imagecopy[200:410, 0:190]
submatrix3 = image[150:330, 515:700]
submatrix4 = image[370:421, 370:797]

solved_image = image

solved_image[200:400,0:190]=submatrix1

image1 = img_v = cv2.flip(submatrix2, 0)

solved_image[0:210,0:190]=image1
image2 = img_v = cv2.flip(submatrix3, 1)
solved_image[150:330, 515:700]=image2
image3 = img_v = cv2.flip(submatrix4, 0)
solved_image[370:421, 370:797]=image3

#cv2_imshow(solved_image)


plt.axis('off')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()