from Screen import Screen
from Keys import Keys

from json import load
from time import sleep

import cv2
import keyboard
import numpy

def main():
  with open('config.json') as data_file:
    config = load(data_file)

  sleep(config["delay"])

  screen = Screen(config["x"], config["y"], config["width"], config["height"])
  frame = screen.capture()

  TRAINING_DATA_FILE = config["training_data_file"]

  training_data = []

  keys = Keys()

  while True:
    feature_set = [0, 0, 0]

    cv2.imshow("self-driving-car", frame)

    key_press = keys.read_valid_key()

    if key_press:
      feature_set = keys.convert_to_feature_set(key_press)
    
    print(feature_set)

    training_data.append([screen, feature_set])

    if len(training_data) % 100 == 0:
      print("training data size:", len(training_data))
      
      if len(training_data) == 500:
          numpy.save(TRAINING_DATA_FILE, training_data)
          print('=== training data saved')
          training_data = []

    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break

main()
