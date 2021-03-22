import time
def reminder():
    to_be_reminded_of = str(input("What do you need to be reminded of?"))
    what_time = float(input("In how long?"))
    local_time = what_time * 60
    time.sleep(local_time)
    print(to_be_reminded_of + " IS NOW.")

if __name__ == '__main__':
    reminder()
