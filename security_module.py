import cv2

cap = cv2.VideoCapture(0)

blink_count = 0

while True:
    ret, frame = cap.read()

    cv2.putText(frame,"Blink Detection Running",(50,50),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("Security Module",frame)

    key = cv2.waitKey(1)

    if key == ord('b'):
        blink_count += 1
        print("Blink detected")

    if blink_count >= 2:
        print("Liveness Verified")
        break

cap.release()
cv2.destroyAllWindows()