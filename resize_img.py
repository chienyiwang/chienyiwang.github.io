import cv2
import numpy as np

im = cv2.imread('images/iv2018.png')
h, w, _ = im.shape
# target_w = 160.0
# target_h = float(h) * target_w / float(w)
# rs_im = cv2.resize(im, (int(target_w), int(target_h)))

target_im = np.ones((w, w, 3), dtype=np.int) * 255
h_start = int((w - h) / 2)
h_end = h_start + h

target_im[h_start:h_end, :, :] = im
cv2.imwrite('images/iv2018_pad.png', target_im)