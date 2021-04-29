from PIL import ImageGrab
import numpy as np
import cv2

class Screen():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def capture(self):
        img = np.array(ImageGrab.grab(bbox=(self.x, self.y, self.width, self.height)))
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        while True:
            cv2.imshow("test", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break