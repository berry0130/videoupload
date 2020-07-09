import os
if os.path.exists("Videos/saved.mp4"):
  os.remove("Videos/saved.mp4")
else:
  print("The file does not exist")