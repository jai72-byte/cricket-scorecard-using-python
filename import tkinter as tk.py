import tkinter as tk
import random
from tkinter import simpledialog, messagebox

def simmatch():
    ovr = int(etr.get())
    bls = ovr * 6
    totrun = 0
    wks = 0
    allrun = 0
    allwks = 0

    for i in range(bls):
        predictball = random.randint(0, 6)  

        scrball = int(
            tk.simpledialog.askinteger("Actual Score !", "Enter the real score of the ball {}: ".format(i + 1)))

        if scrball > 6 or scrball<0:
            tk.messagebox.showerror("Invalid Score !!", "Invalid Score! Please enter the score of the ball between 0 to 6.")
            scrball = int(
                tk.simpledialog.askstring("Actual Score !", " Enter the real score of the ball {}: ".format(i + 1)))

        if scrball == -1:
            wks += 1
        elif scrball == -2:
            totrun += 1
            i -= 1
        else:
            totrun += scrball

        if (i + 1) % 6 == 0:
            allrun += totrun
            allwks += wks
         
            tk.messagebox.showinfo("Over Ended !!",
                                   "An Over has ended{}.\nScore = {}/{}".format((i + 1) // 6, totrun, wks))
            totrun = 0
            wks = 0

        tk.messagebox.showinfo("Score of the Ball",
                               "Ball {}: Predicted score is {}, while Actual score  is{}".format(i + 1, predictball,
                                                                                         scrball))
    tk.messagebox.showinfo("Match End Summary", "Total Score of the Match = {}/{}".format(allrun, allwks))

window = tk.Tk()
window.title("CricBuzz")

window.geometry("400x300")
window.resizable(False, False)

bgimg = tk.PhotoImage(file="cric.png")

bglbl = tk.Label(window, image=bgimg)
bglbl.place(x=0, y=0, relwidth=1, relheight=1)

lbl = tk.Label(window, text="Enter total no of overs played by the team: ")
lbl.pack()
etr = tk.Entry(window)
etr.pack()

bt = tk.Button(window, text="Enter certain no of Overs", command=simmatch)
bt.pack()



window.mainloop()
