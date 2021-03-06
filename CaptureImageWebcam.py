import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Capture Fotos")
img_counter = 0
path = "./lego_fotos/train/nespresso_green/"



while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)

    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = path + "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()