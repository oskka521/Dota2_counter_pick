import threading
import interface
import image_process
import tkinter as tk
import queue
import time


def interface_function(q):
    root = tk.Tk()
    root.geometry("800x600")
    interface.run(root, q)
    return root


def image_process_function(q1):
    image_list = image_process.run(q1)
    q1.put(image_list)

    # for i in range(10):
    #    q1.put(i)
    #    time.sleep(1)
    # q1.task_done()


if __name__ == "__main__":
    OPTIONS = 2
    q1 = queue.Queue()
    t1 = threading.Thread(target=image_process_function, args=(q1, OPTIONS))
    t1.start()
    # app = interface_function(q1)
    # app.mainloop()
    t1.join()
    q1.join()
