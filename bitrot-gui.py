from pathlib import Path
import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from playsound import playsound

filetocorrupt = 'nofile'
e = 1

class App:
    
    def __init__(self, master):
        global e
        e = Entry(master)
        e.pack()
        
        e.delete(0, END)
        e.insert(0, 8)
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="Load", fg="red", command=self.upload
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Corrupt", command=self.corrupt)
        self.hi_there.pack(side=LEFT)

    def upload(self):
        global filetocorrupt
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
        print(root.filename)
        filetocorrupt = root.filename
        print(filetocorrupt)

    def corrupt(self):
        global filetocorrupt
        global e
        corruptionamount = int(e.get())
        print(corruptionamount)
        if filetocorrupt in 'nofile':
            print('Error no file')
            messagebox.showerror("Error", "No file uploaded.")
        else:
            filetocorrupt = Path(filetocorrupt)
            data = bytearray(filetocorrupt.read_bytes())
            for x in range(corruptionamount):
                flipbyte = random.randrange(0, len(data))
                data[flipbyte] ^= 1 << random.randrange(0, 8)
            filetocorrupt.write_bytes(data)

            print("file corrupted")

root = Tk()

app = App(root)

root.mainloop()



