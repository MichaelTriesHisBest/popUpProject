import json
from datetime import date
import tkinter as tk


LARGE_FONT = ("Helvetica", 22)
MED_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)



def loads():
    x = '{"name": "John", "age": 30, "city": "New York"}'
    y = json.loads(x)
    print(y["age"])



def dumps():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)


def input2Json():
    record = str(input("What is the date of the occassion?  Acceptable Input: 01/31/2019:"))

    reminder_data = {}

    for i in range(0, 1):
        Name = input("What is the occasion? :").split()
        Age = input(
            "Do you want to be reminded the day of the {0} or the day before? Enter 'Of' for Day Of or 'B' for Before  :".format(
                Name))
        Nam_key = Name[0]
        Age_value = Age[0]
        reminder_data[Nam_key] = (record, Age_value)

    y = json.dumps(reminder_data)
    with open('data.txt', 'w') as outfile:
        json.dump(reminder_data, outfile)

def alertMsg(msg):
    msg = msg.capitalize()
    pupup = tk.Tk()
    pupup.wm_title("!!!!!")
    label = tk.Label(pupup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(pupup, text="Thanks!", command=pupup.destroy)
    B1.pack()
    pupup.mainloop()


def readingJson():
    today = date.today()
    today = today.strftime("%m/%d/%y").replace('/','')
    today_length = len(today)
    current_year = today[(today_length - 2)::]
    current_day = today[0:4].strip('/')
    with open('data.txt', 'r') as outfile:
        data = json.load(outfile)
        for key in data:
            date_length = len(data[key][0])
            year_of = str(data[key][0][8:10]).replace("/", "")
            day_of = str(data[key][0][0:6]).replace("/", "")
            if day_of == current_day and current_year == year_of:
                # alertMsg("This is a reminder of {0}".format(data))
                alertMsg(("IT'S TIME BITCH"))
            # if str(day_of) == current_day:
            #     print("It is {0}".format(year_of))
            #     print("Length of year_of_length = {0}".format(date_length))
            #     print("Yeear of =  {0}".format(year_of))

            # if data[key][1] == "B" or 'b':
            #     print(today)
        # print("Today is {0}".format(today))
        # print(current_year)



if __name__ == '__main__':
    input2Json()
    readingJson()
