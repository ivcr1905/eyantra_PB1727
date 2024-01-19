
import cv2 as cv
from cv2 import aruco

marker_dict=aruco.Dictionary_get(aruco.DICT_4X4_50)
param_markers=aruco.DetectorParameters_create()
img=cv.imread("G:\E-YATRA ROBOTICS COMPETITIONS\PB_Task1_Windows\PB_Task1_Windows\Task1B\public_test_cases\aruco_0.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
marker_corners,marker_IDs,reject=aruco.detectMarkers(img,marker_dict,parameters=param_markers)
print(marker_IDs)
cv.imshow("Aruco",img)
cv.waitKey(0)
