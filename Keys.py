import keyboard

valid_keys = "abcdefghijklmnopqrstuvwxyz"

class Keys():
  def read_valid_key(self):
    if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
      return "A"
    elif keyboard.is_pressed("w") or keyboard.is_pressed("up"):
      return "W"
    elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
      return "D"
    elif keyboard.is_pressed("t"):
      return "T"
    elif keyboard.is_pressed("q"):
      return "Q"
    else:
      return "W"

  def convert_to_feature_set(self, key):
    if key == "A":
      return [1, 0, 0]
    elif key == "D":
      return [0, 0, 1]
    else:
      return [0, 1, 0]
