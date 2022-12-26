# Programmed by Dogan Yigit Yenigun (toUpperCase78)
"""
Happy New Year 2023 with Squares and Tree!
Implemented with OpenCV - TR Version
"""
import numpy as np
import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX
AA = cv2.LINE_AA
COLORS = [(0,0,255),(0,128,255),(0,255,255),(0,255,0),
          (255,255,0),(255,100,0),(255,0,0),(128,0,192)]
COLORS_DARK = [(0,0,128),(0,64,128),(0,128,128),(0,128,0),
               (128,128,0),(128,50,0),(128,0,0),(64,0,96)]
COLORS_SQ = [(0,0,255),(0,255,0),(0,160,220),(255,0,0)]
COLORS_DARK_SQ = [(0,0,128),(0,128,0),(0,80,110),(128,0,0)]

image = np.zeros((795,795,3))
image = image.astype(np.uint8)

c = 0
for i in range(12):
    cv2.rectangle(image, (15+(i*60),15), (55+(i*60),55), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (20+(i*60),20), (50+(i*60),50), COLORS_SQ[c%4], -1)
    c += 1
for i in range(12):
    cv2.rectangle(image, (735,15+(i*60)), (775,55+(i*60)), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (740,20+(i*60)), (770,50+(i*60)), COLORS_SQ[c%4], -1)
    c += 1
for i in range(12):
    cv2.rectangle(image, (735-(i*60),735), (775-(i*60),775), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (740-(i*60),740), (770-(i*60),770), COLORS_SQ[c%4], -1)
    c += 1
for i in range(12):
    cv2.rectangle(image, (15,735-(i*60)), (55,775-(i*60)), COLORS_DARK_SQ[c%4], -1)
    cv2.rectangle(image, (20,740-(i*60)), (50,770-(i*60)), COLORS_SQ[c%4], -1)
    c += 1

cv2.putText(image, "MUTLU YILLAR!", (133,135), FONT, 2.3, (0,255,255), 4, AA)
cv2.putText(image, "2", (85,310), FONT, 3.5, (0,255,255), 6, AA)
cv2.putText(image, "0", (85,410), FONT, 3.5, (0,255,255), 6, AA)
cv2.putText(image, "2", (85,510), FONT, 3.5, (0,255,255), 6, AA)
cv2.putText(image, "3", (85,610), FONT, 3.5, (0,255,255), 6, AA)

cv2.putText(image, "2", (635,310), FONT, 3.5, (0,255,255), 6, AA)
cv2.putText(image, "0", (635,410), FONT, 3.5, (0,255,255), 6, AA)
cv2.putText(image, "2", (635,510), FONT, 3.5, (0,255,255), 6, AA)
cv2.putText(image, "3", (635,610), FONT, 3.5, (0,255,255), 6, AA)

root_out = np.array([[300,670],[500,670],[500,658],[440,620],[430,510],
                 [370,510],[360,620],[300,658]], np.int32)
root_out = root_out.reshape((-1,1,2))
cv2.fillPoly(image, [root_out], (0,41,68), lineType=AA)
root_in = np.array([[305,665],[495,665],[495,663],[435,625],[425,505],
                 [375,505],[365,625],[305,663]], np.int32)
cv2.fillPoly(image, [root_in], (0,62,102), lineType=AA)

grass1 = np.array([[210,630],[400,590],[590,630],[590,624],[400,465],
                   [210,624]], np.int32)
grass1 = grass1.reshape((-1,1,2))
cv2.fillPoly(image, [grass1], (0,80,0), lineType=AA)

grass2 = np.array([[240,550],[400,510],[560,550],[560,544],[400,380],
                   [240,544]], np.int32)
grass2 = grass2.reshape((-1,1,2))
cv2.fillPoly(image, [grass2], (0,90,0), lineType=AA)

grass3 = np.array([[270,480],[400,430],[530,480],[530,474],[400,295],
                   [270,474]], np.int32)
grass3 = grass3.reshape((-1,1,2))
cv2.fillPoly(image, [grass3], (0,100,0), lineType=AA)

grass4 = np.array([[300,410],[400,350],[500,410],[500,404],[400,220],
                   [300,404]], np.int32)
grass4 = grass4.reshape((-1,1,2))
cv2.fillPoly(image, [grass4], (0,110,0), lineType=AA)

star1 = np.array([[348,214],[386,214],[400,180],[414,214],[452,214],
                 [422,236],[440,275],[400,250],[360,275],[378,236]], np.int32)
star1 = star1.reshape((-1,1,2))
cv2.fillPoly(image, [star1], (0,150,150), lineType=AA)
star2 = np.array([[360,219],[391,219],[400,190],[409,219],[440,219],
                 [417,236],[434,269],[400,245],[366,269],[383,236]], np.int32)
star2 = star2.reshape((-1,1,2))
cv2.fillPoly(image, [star2], (0,200,200), lineType=AA)
star3 = np.array([[372,224],[396,224],[400,200],[404,224],[428,224],
                 [412,236],[428,263],[400,240],[372,263],[388,236]], np.int32)
star3 = star3.reshape((-1,1,2))
cv2.fillPoly(image, [star3], (0,255,255), lineType=AA)

cv2.circle(image, (376,295), 12, COLORS_DARK[5], -1, AA)
cv2.circle(image, (376,295), 9, COLORS[5], -1, AA)
cv2.circle(image, (424,295), 12, COLORS_DARK[4], -1, AA)
cv2.circle(image, (424,295), 9, COLORS[4], -1, AA)
cv2.circle(image, (330,380), 12, COLORS_DARK[2], -1, AA)
cv2.circle(image, (330,380), 9, COLORS[2], -1, AA)
cv2.circle(image, (400,344), 12, COLORS_DARK[1], -1, AA)
cv2.circle(image, (400,344), 9, COLORS[1], -1, AA)
cv2.circle(image, (470,380), 12, COLORS_DARK[6], -1, AA)
cv2.circle(image, (470,380), 9, COLORS[6], -1, AA)

cv2.circle(image, (290,465), 12, COLORS_DARK[3], -1, AA)
cv2.circle(image, (290,465), 9, COLORS[3], -1, AA)
cv2.circle(image, (345,440), 12, COLORS_DARK[4], -1, AA)
cv2.circle(image, (345,440), 9, COLORS[4], -1, AA)
cv2.circle(image, (400,420), 12, COLORS_DARK[7], -1, AA)
cv2.circle(image, (400,420), 9, COLORS[7], -1, AA)
cv2.circle(image, (455,440), 12, COLORS_DARK[0], -1, AA)
cv2.circle(image, (455,440), 9, COLORS[0], -1, AA)
cv2.circle(image, (510,465), 12, COLORS_DARK[2], -1, AA)
cv2.circle(image, (510,465), 9, COLORS[2], -1, AA)

cv2.circle(image, (264,540), 12, COLORS_DARK[7], -1, AA)
cv2.circle(image, (264,540), 9, COLORS[7], -1, AA)
cv2.circle(image, (330,520), 12, COLORS_DARK[1], -1, AA)
cv2.circle(image, (330,520), 9, COLORS[1], -1, AA)
cv2.circle(image, (400,500), 12, COLORS_DARK[3], -1, AA)
cv2.circle(image, (400,500), 9, COLORS[3], -1, AA)
cv2.circle(image, (470,520), 12, COLORS_DARK[5], -1, AA)
cv2.circle(image, (470,520), 9, COLORS[5], -1, AA)
cv2.circle(image, (536,540), 12, COLORS_DARK[0], -1, AA)
cv2.circle(image, (536,540), 9, COLORS[0], -1, AA)

cv2.circle(image, (236,620), 12, COLORS_DARK[5], -1, AA)
cv2.circle(image, (236,620), 9, COLORS[5], -1, AA)
cv2.circle(image, (290,605), 12, COLORS_DARK[6], -1, AA)
cv2.circle(image, (290,605), 9, COLORS[6], -1, AA)
cv2.circle(image, (345,592), 12, COLORS_DARK[2], -1, AA)
cv2.circle(image, (345,592), 9, COLORS[2], -1, AA)
cv2.circle(image, (400,580), 12, COLORS_DARK[4], -1, AA)
cv2.circle(image, (400,580), 9, COLORS[4], -1, AA)
cv2.circle(image, (455,592), 12, COLORS_DARK[1], -1, AA)
cv2.circle(image, (455,592), 9, COLORS[1], -1, AA)
cv2.circle(image, (510,605), 12, COLORS_DARK[7], -1, AA)
cv2.circle(image, (510,605), 9, COLORS[7], -1, AA)
cv2.circle(image, (564,620), 12, COLORS_DARK[3], -1, AA)
cv2.circle(image, (564,620), 9, COLORS[3], -1, AA)

cv2.imshow("MUTLU YILLAR 2023", image)
k = cv2.waitKey(0) & 0xFF
if k == ord('s'):
    cv2.imwrite("newyear_2023_tr.png", image)

cv2.destroyAllWindows()
