# tkinter module required for gui designing
import tkinter as tk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
# timeit module required to start timer in seconds
from timeit import default_timer as timer
# datetime module to store current date and time with the records
from datetime import datetime
# random module to choose random sentence from a file
import random
  
# creating home window and defining its size
window = Tk()
window.geometry("450x250")
window.configure(bg="chartreuse")
  
# defining used to destroy window
x = 0
  
# defining the function to start the test
def test():
    # following 'if' validates for empty name of user
    if name.get()=="":
        reqLab = Label(window,text="*required", font="times 13", fg="Red", bg="chartreuse")
        reqLab.place(x=310,y=40)
        return
    
    global x
    sent = ""
    accr = ""
    speed = ""
  
    # 'if' for destroying the "window" after on test
    if x == 0:
        window.withdraw()
        x = x+1

    # defining function to check results of test
    def check_result():
        userinput = entry.get("1.0",tk.END)
        if userinput == sent+'\n':
            end = timer()
            # speed calculation formula
            windows.speed = "Speed: "+str(round((len(userinput.split(" "))/((end-start)/60)),2))+" wpm"
            # setting speed and accuracy to labels
            wpmLab["text"]= windows.speed
            accrLab["text"] = windows.accr
        else:
            # if input is wrong:
            windows.speed = "Wrong Input!!"
            wpmLab["text"]=windows.speed
        
    # function to check accuracy 
    def check_accuracy(event):
        count = 0
        for i,c in enumerate(sent):
            try:
                if entry.get("1.0",tk.END)[i] == c:
                    count += 1
                else:
                    pass
            except:
                pass
        # accuracy caluculation formula 
        windows.accr = "Accuracy: "+str(round((count/len(sent))*100,2))+"%"

    # function to record stats of test in a file
    def record_stat():
        # now stores current date time
        now = datetime.now()
        fp = open("records.txt","a")
        fp.write("Date: "+now.strftime("%d-%m-%Y")+", "+"Time: "+now.strftime("%H:%M:%S")+", "+"Name: "+name.get()+", "+windows.speed+", "+windows.accr+"\n")
        fp.close()
        recstat = Label(windows,text="Record inserted successfuly for "+name.get(), font="times 13", fg="Green", bg="chartreuse")
        recstat.place(x=400,y=730)
    
        
    # function which returns random sentence/para from a file
    def get_sentence():
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    # function called wheb click on restart game
    def restart_test():
        windows.destroy()
        test()


    
  
    # start timer using timeit
    start = timer()
    # creating test window and defining its size
    windows = Tk()
    windows.geometry("1000x850")
    windows.configure(bg="light sky blue")

    # get random sentence
    sent = get_sentence()
  
    # using label method of tkinter for labling in window
    # 'Hii' greet
    greet = Label(windows, text="Hii "+name.get()+" start typing the given paragraph below......", font="times 20", bg="light sky blue")
    greet.place(x=30,y=60)
    # sentence/paragraph for test
    para = Label(windows, text=sent, font="times 16", wraplength=640, justify="left")
    para.place(x=210, y=150)
    # indicates where to start
    startIndic = Label(windows, text="Start Typing:", font="times 20",bg="light sky blue")
    startIndic.place(x=30, y=280)
    # indicates for where to start
    paraLab = Label(windows, text="Paragraph:", font="times 20",bg="light sky blue")
    paraLab.place(x=30, y=150)
    # scrolledText to write the sentence/paragraph 
    entry = ScrolledText(windows,font="times 16")
    entry.place(x=210, y=280,width=610, height=200)
    entry.bind('<Key>', check_accuracy)
    # wpnLab shows the speed of typing
    wpmLab = Label(windows,text="", font="times 20", bg="light sky blue")
    wpmLab.place(x=250, y=600)
    # accrLab shows the speed of typing
    accrLab = Label(windows,text="", font="times 20", bg="light sky blue")
    accrLab.place(x=650, y=600)
    # done button used to check result 
    done = Button(windows, text="Done",command=check_result, width=12, font="OemFixed 14 bold", bg="light sky blue3")
    done.place(x=250, y=650)
    # try again button used to restart the test 
    tryAgain = Button(windows, text="Try Again",command=restart_test, font="OemFixed 14 bold", width=12, bg="light sky blue3")
    tryAgain.place(x=450, y=650)
    # record button calls the record_stat to save stats of test in a file
    record = Button(windows, text="Record",command=record_stat, font="OemFixed 14 bold", width=12, bg="light sky blue3")
    record.place(x=650, y=650)
    
    windows.mainloop()


# label
msg = Label(window, text="Enter Name to continue....", font="times 14",bg="chartreuse")
msg.place(x=10, y=80)
# name label
nameLab = Label(window,text="Name:",font="times 16",bg="chartreuse")
nameLab.place(x=10,y=40)
# entry to enter name
name = Entry(window,font="times 16")
name.place(x=80,y=40)
# button to start the test
test_start = Button(window, text="Go", command=test, width=12, font="OemFixed 14 bold", bg='OliveDrab4')
test_start.place(x=150, y=120)
# calling window
window.mainloop()

