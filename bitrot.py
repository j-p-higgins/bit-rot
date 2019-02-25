from pathlib import Path
import random
import subprocess

count = 240

while True:
 
 audio_file = "test.mp3"
 return_code = subprocess.call(["afplay", audio_file])

 print("audio played")

 for x in range(24):
  file1 = Path("test.mp3")
  data = bytearray(file1.read_bytes())
  flipbyte = random.randrange(0, len(data))
  data[flipbyte] ^= 1 << random.randrange(0, 8)
  file1.write_bytes(data)
  print(x)

 print("audio corrupted")

 count += 1

 print(count)
