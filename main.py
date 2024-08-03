import cv2
from cvzone.HandTrackingModule import HandDetector
from mediapipe.python.solutions import hands


class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 48, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)


# Webcam
cap = cv2.VideoCapture(1)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating Buttons
buttonListValues = [['7', '8', '9', '*'],
                   ['4', '5', '6', '-'],
                   ['1', '2', '3', '+'],
                   ['0', '/', '.', '=']]


buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 800
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos),100, 100,buttonListValues[y][x]))

# Variables
myEquation = '10+5'


# Loop
while True:
    # Get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detection of hand
    var = hands, img
    detector.findHands(img, flipType=False)

    cv2.rectangle(img, (100, 100), (200, 200), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (100, 100), (200, 200), (50, 50, 50), 3)
    cv2.putText(img, "9", (100 + 20, 100 + 50), cv2.FONT_HERSHEY_PLAIN,
                2, (50, 50, 50, 2))

    # Draw all buttons
    cv2.rectangle(img, (800,40), (800 + 400, 70 + 100),
                      (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800,40), (800 + 400, 70 + 100),
                      (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)

# Processing


# Display the Equation/result
        cv2.putText(img, myEquation, (810, 130), cv2.FONT_HERSHEY_PLAIN,
                3,(50, 50, 50), 3)




# Display Image
cv2.imshow("Image", img)
cv2.waitKey(1)

