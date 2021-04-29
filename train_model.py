from Screen import Screen
from Keys import Keys
from json import load

import pandas as pd
import numpy as np

import time
import cv2
import keyboard

from alexnet import alexnet

def main():
  with open('config.json') as data_file:
    config = load(data_file)

  TRAINING_DATA_FILE = config["training_data_file"]

  df = np.load(TRAINING_DATA_FILE, allow_pickle=True)

  train = train_data[:-30]
  test = train_data[-30:]

  WIDTH = 480
  HEIGHT = 270
  LR = 1e-3
  EPOCHS = 30

  X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 3)
  Y = [i[1] for i in train]

  test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 3)
  test_y = [i[1] for i in test]

  model = alexnet(WIDTH, HEIGHT, LR)

  model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=25, show_metric=True, run_id="MODEL_NAME")

  model.save("MODEL_NAME")

main()
