from pygame import mixer
from time import sleep

def alarm(file,stopper):
    mixer.init(33100)
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            print("Keep Coding :)")
            break

def again_work():
    print("Want to Code again: yes/no ? ")
    user_choice = input()
    if user_choice == 'yes' or user_choice == "YES" or user_choice == "Yes":
        global keep_coding
        keep_coding = True
    else:
        keep_coding = False


if __name__ == "__main__":
   print("Select time for coding:\n")
   sleep(1)
   print("1. Enter Hours\n2. Enter minuts")
   print("Select Option 1(One) or 2(Two)")
   hour_input = input()
   keep_coding = True

   while keep_coding:
       if hour_input == 'One' or hour_input == "one" or hour_input=="ONE" or hour_input=="1":
           print("How many hour you want to code")
           code_time = int(input())
           print("Alarm set successfully. keep coding :)")
           convert_sec = code_time*60*60
           sleep(convert_sec)
           print("Type Stop for stoping alarm")
           alarm('emi.mp3','Stop')
           again_work()

       elif hour_input == 'two' or hour_input == "Two" or hour_input=="TWO" or hour_input=='2':
           print("How many minutes you want to code")
           code_time = int(input())
           print("Alarm set successfully. keep coding :)")
           convert_sec = code_time*60
           sleep(convert_sec)
           print("Type Stop for stoping alarm")
           alarm('emi.mp3', 'Stop')
           again_work()

       else:
           print("Wrong input")
