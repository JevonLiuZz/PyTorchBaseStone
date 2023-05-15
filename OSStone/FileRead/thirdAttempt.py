import cv2

img_dir_cv = 'p1/p2/Nami.jpeg'
img_cv = cv2.imread(img_dir_cv)
cv2.imshow('test', img_cv)
cv2.waitKey()
image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
cv2.imshow('test', image)
cv2.waitKey()
