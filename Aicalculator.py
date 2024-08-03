import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


class Button:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def draw(self, img):
        cv2.rectangle(img, (self.x, self.y), (self.x + self.w, self.y + self.h), (255, 0, 0), -1)
        cv2.putText(img, self.text, (self.x + 20, self.y + 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)


buttons = [Button(50, 50, 50, 50, '1'), Button(110, 50, 50, 50, '2'), ...]  # Define all buttons
for button in buttons:
    if button.is_pressed(finger_x, finger_y):
        print(f"Button {button.text} pressed")
