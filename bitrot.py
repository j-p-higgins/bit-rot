from pathlib import Path
import random
from playsound import playsound

count = 0

while True:
    
 playsound('test.mp3')
 print("audio played")
 
 audiofile = Path("test.mp3")
 data = bytearray(audiofile.read_bytes())
 for x in range(100):
  flipbyte = random.randrange(0, len(data))
  data[flipbyte] ^= 1 << random.randrange(0, 8)
 audiofile.write_bytes(data)

 print("audio corrupted")

 count += 1

 print(count)
