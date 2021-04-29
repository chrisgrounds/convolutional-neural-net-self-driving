from Screen import Screen
from json import load
from time import sleep

def main():
  with open('data.json') as data_file:
    config = load(data_file)

  sleep(config["delay"])

  screen = Screen(config["x"], config["y"], config["width"], config["height"])
  screen.capture()

main()

# sleep
# get keys
# capture screen
# save (screen, keys) to model
# model.fit on (screen, keys)
# use model.predict to work out what key to press next
# alexnet
#
