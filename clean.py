import numpy as np
import cv2
import sys
from cv2.ximgproc import guidedFilter



input_file = sys.argv[1]
output_file = input_file.split('.png')[0] + '-over.png'


img = cv2.imread(input_file).astype(np.float32)



y = img.copy()
for _ in range(64):
    y = cv2.bilateralFilter(y, 5, 8, 8)
for _ in range(4):
    y = guidedFilter(img, y, 4, 16)
cv2.imwrite(output_file, y.clip(0, 255).astype(np.uint8))

