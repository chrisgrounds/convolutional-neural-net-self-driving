from Screen import Screen

def main():
  screen = Screen(0, 40, 800, 640)
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
