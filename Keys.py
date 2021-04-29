import keyboard

valid_keys = "abcdefghijklmnopqrstuvwxyz"

class Keys():
  def read_valid_key(self):
    if keyboard.is_pressed("a"):
      return "A"
    elif keyboard.is_pressed("w"):
      return "W"
    elif keyboard.is_pressed("d"):
      return "D"
    else:
      return None

  def convert_to_feature_set(self, key):
    if key == "A":
      return [1, 0, 0]
    elif key == "D":
      return [0, 0, 1]
    else:
      return [0, 1, 0]
