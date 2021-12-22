import cv2
import numpy as np

im = cv2.imread('images/wacv2022.png')
h, w, _ = im.shape
target_w = 160.0
target_h = float(h) * target_w / float(w)
rs_im = cv2.resize(im, (int(target_w), int(target_h)))

target_im = np.ones((160, 160, 3), dtype=np.int) * 255
h_start = int((160 - int(target_h)) / 2)
h_end = h_start + int(target_h)

target_im[h_start:h_end, :, :] = rs_im
cv2.imwrite('images/wacv2022_rs.png', target_im)