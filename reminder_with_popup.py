LARGE_FONT = ("Helvetica", 12)
MED_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

import tkinter as tk
import time

fields = 'What?', 'When?'


def alertMsg(msg):
    msg = msg.capitalize()
    pupup = tk.Tk()
    pupup.wm_title("!!!!!")
    label = tk.Label(pupup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(pupup, text="Thanks!", command=pupup.destroy)
    B1.pack()
    pupup.mainloop()


def reminder():
    to_be_reminded_of = str(input("What do you need to be reminded of?"))
    what_time = float(input("In how long?"))
    local_time = what_time * 60
    time.sleep(local_time)
    i = 0
    alertMsg((to_be_reminded_of))
    while i < 4:
        alertMsg(to_be_reminded_of)
        i+=1


# def fetch(entries):
#     for entry in entries:
#         print('Input => "%s"' % entry.get())  # get text
#
#
# def makeform(root, fields):
#     entries = []
#     for field in fields:
#         row = tk.Frame(root)
#         lab = tk.Label(row, width=15, text=field, anchor='w')
#         ent = tk.Entry(row)
#         row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
#         lab.pack(side=tk.LEFT)
#         ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#         entries.append(field, ent)
#         return entries
#
#
if __name__ == '__main__':
    # root = tk.Tk()
    # ents = makeform(root, fields)
    # root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    # b1 = tk.Button(root, text='Enter',
    #                command=(lambda e=ents: fetch(e)))
    # b1.pack(side=tk.LEFT, padx=5, pady=5)
    # b2 = tk.Button(root, text='Quit', command=root.quit)
    # b2.pack(side=tk.LEFT, padx=5, pady=5)
    # root.mainloop()
    # root = tk.Tk()
    # ents = makeform(root, fields)
    # root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    # tk.Button(root, text='Fetch',
    #           command=(lambda e=ents: fetch(e))).pack(side='left')
    # root.mainloop()
    reminder()
