"""Іконка застосунку 1024x1024: вертикальний кадр із позначкою відтворення.

Задум простий і читається навіть у 48 пікселів: вертикальна рамка — це
формат шортсів, трикутник усередині — відео, зріз кута — нарізка.
"""
import cv2
import numpy as np

S = 1024
BG_TOP = (26, 18, 14)        # BGR, темно-синій кут
BG_BOTTOM = (60, 30, 20)
ACCENT_A = (255, 92, 124)    # BGR: фіолетово-синій
ACCENT_B = (109, 76, 255)    # малиновий

img = np.zeros((S, S, 3), dtype=np.uint8)

# фон: мʼякий діагональний градієнт
yy, xx = np.mgrid[0:S, 0:S].astype(np.float32)
t = np.clip((xx + yy) / (2 * S), 0, 1)[..., None]
img[:] = (np.array(BG_TOP) * (1 - t) + np.array(BG_BOTTOM) * t).astype(np.uint8)

# вертикальна рамка 9:16 — форма короткого відео
fw, fh = 360, 640
x0, y0 = (S - fw) // 2, (S - fh) // 2
frame = np.zeros_like(img)
tt = np.clip((yy - y0) / fh, 0, 1)[..., None]
frame[:] = (np.array(ACCENT_A) * (1 - tt) + np.array(ACCENT_B) * tt).astype(np.uint8)

mask = np.zeros((S, S), dtype=np.uint8)
r = 64
cv2.rectangle(mask, (x0 + r, y0), (x0 + fw - r, y0 + fh), 255, -1)
cv2.rectangle(mask, (x0, y0 + r), (x0 + fw, y0 + fh - r), 255, -1)
for cx, cy in ((x0 + r, y0 + r), (x0 + fw - r, y0 + r),
               (x0 + r, y0 + fh - r), (x0 + fw - r, y0 + fh - r)):
    cv2.circle(mask, (cx, cy), r, 255, -1)

# зріз правого верхнього кута — натяк на відрізаний фрагмент
cut = np.array([[x0 + fw - 150, y0], [x0 + fw, y0], [x0 + fw, y0 + 150]], np.int32)
cv2.fillPoly(mask, [cut], 0)

mask_soft = cv2.GaussianBlur(mask, (0, 0), 1.2).astype(np.float32)[..., None] / 255.0
img = (img * (1 - mask_soft) + frame * mask_soft).astype(np.uint8)

# трикутник відтворення всередині
cx, cy, size = S // 2, S // 2, 108
play = np.array([[cx - size // 2, cy - size],
                 [cx - size // 2, cy + size],
                 [cx + size, cy]], np.int32)
layer = np.zeros((S, S), dtype=np.uint8)
cv2.fillPoly(layer, [play], 255)
layer = cv2.GaussianBlur(layer, (0, 0), 1.0).astype(np.float32)[..., None] / 255.0
img = (img * (1 - layer) + np.full_like(img, 255) * layer).astype(np.uint8)

cv2.imwrite("logo.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 6])
print("logo.png", img.shape)
