from Screen import Screen
from Keys import Keys
from json import load

import pandas as pd
import numpy as np

import time
import cv2
import keyboard

def main():
  with open('config.json') as data_file:
    config = load(data_file)

  screen = Screen(config["x"], config["y"], config["width"], config["height"])

  cv2_window_name = "self-driving-car"

  TRAINING_DATA_FILE = config["training_data_file"]

  training_data = []

  keys = Keys()

  pause = False
  iteration = 0

  print("Press 't' to start training")
  keyboard.wait("T")
  print("Starting...")

  while True:
    feature_set = [0, 0, 0]
    frame = screen.capture()
    # cv2.imshow(cv2_window_name, frame)

    key_press = keys.read_valid_key()

    if pause == False:
      if key_press:
        feature_set = keys.convert_to_feature_set(key_press)
      
      training_data.append([frame, feature_set])

      if len(training_data) >= 50:
          np.save(TRAINING_DATA_FILE, training_data)
          iteration = iteration + len(training_data)
          print('[{}] training data saved'.format(iteration))
          training_data = []

    if key_press == "T":
      pause = True if pause == False else False
      print("Pause: {}".format(pause))

    if key_press == "Q":
      print("Quiting...")
      cv2.destroyWindow(cv2_window_name)
      break

  df = np.load(TRAINING_DATA_FILE, allow_pickle=True)
  df = pd.DataFrame(df)

  print(df)

  cv2.destroyAllWindows()

main()
