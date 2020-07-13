from tkinter import *
import main
import queue
import time


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.pack(fill=BOTH, expand=1)
        self.configure(bg="white")

        self.master.title("Dota 2 Picker, By OSKAR KARLSSON")

        self.label1 = Label(self, text="INPUT COM PORT (default is COM4)", bg="white")
        self.label1.place(x=50, y=375)

        self.collect_b = Button(self, text="Collect", command=self.execute_collect_b)
        self.collect_b.place(x=50, y=425)

    def execute_collect_b(self):
        print("wow")


def run(root, q):
    Window(root)
    for i in range(5):
        time.sleep(2)
        if not q.empty():
            print(q.get(timeout=1.5))

        print("empty")
