from tkinter import *
# tkinter is a python library to create basic graphical interfaces
from PIL import Image
# pillow is the refrence python library to work with images 


# define the screen's paramters and setting the background image
screen = Tk()
screen.geometry("800x500")
screen.title("Branch and Bound")
bg = PhotoImage(file="fdtkinter.png") 
canvas1 = Canvas(screen, width=400, height=400)   
canvas1.pack(fill="both", expand=True) 
canvas1.create_image(0, 0, image=bg,  anchor = NW) 

label = Label(screen,text="Trouver l'ordonnancement optimal pour vos tâhches: ", bg="grey", font=("Arial Black",20))
label.place(x=0, y=0)

label_duration = Label(screen, text="Durée", font=("Arial", 12))
label_duration.place(x=170, y=100)
label_due_date = Label(screen, text="Date Limite (en jours)", font=("Arial", 12))
label_due_date.place(x=300, y=100)


label_A = Label(screen, text="A", font=("Arial", 20))
label_A.place(x=100, y=150)
label_B = Label(screen, text="B", font=("Arial", 20))
label_B.place(x=100, y=220)
label_C = Label(screen, text="C", font=("Arial", 20))
label_C.place(x=100, y=290)


# this check function is defined to make sure that the entries only accept numerical values
def check(input):
      
    if input.isdigit():
        return True
                          
    elif input == "":
        return True

    else:
        return False


reg = screen.register(check)
# Now our check function is registered
duration_A = IntVar(None)
Duration_A = Entry(screen, width= 8)
Duration_A.config(validate="key", validatecommand =(reg, '%P'))
# this line simply tells python that the check function should be called whenever a keystroke happens in this enry field
Duration_A.place(x=179, y=159)
Duration_A.config(textvariable=duration_A)


duration_B = IntVar()
Duration_B = Entry(screen, width= 8, textvariable=duration_B)
Duration_B.config(validate ="key", validatecommand =(reg, '%P'))
Duration_B.place(x=179, y=229)

duration_C = IntVar()
Duration_C = Entry(screen, width= 8, textvariable=duration_C)
Duration_C.config(validate ="key", validatecommand =(reg, '%P'))
Duration_C.place(x=179, y=299)

due_date_A = IntVar()
Due_Date_A = Entry(screen, width= 8, textvariable=due_date_A)
Due_Date_A.config(validate="key", validatecommand=(reg, '%P'))
Due_Date_A.place(x=309, y=159)

due_date_B = IntVar()
Due_Date_B = Entry(screen, width= 8, textvariable=due_date_B)
Due_Date_B.config(validate="key", validatecommand=(reg, '%P'))
Due_Date_B.place(x=309, y=229)

due_date_C = IntVar()
Due_Date_C = Entry(screen, width= 8, textvariable=due_date_C)
Due_Date_C.config(validate="key", validatecommand=(reg, '%P'))
Due_Date_C.place(x=309, y=299)


# this is the main function, it takes as an argument a dictionnary representing a project, 
# it returns the optimized way to organize the work flow using the branch and bound method
# it is simplified version, given that I will have exactly three tasks to do
def branch_and_bound(project):

    delays = [] 
    sum_durations = sum(task[0] for task in project)
    for i in range(3):
        # for each possibilty for the third job
        due_date = project[i][1]
        t1 = max(sum_durations - due_date, 0)
        # 15 - 12 = 3
        # t is the delay assuming that the ith job is the last
        for j in range(3):
            if j != i:
                # for each possibilty for the second job
                t2 = max(sum_durations - project[i][0] - project[j][1], 0)

                # sum_durations - duration of the ith task - due date of the jth task 
                for k in range(3):

                    if k != i and k != j:
                        t3 = max(sum_durations - project[i][0] - project[j][0] - project[k][1], 0)
                        delays.append(((project[k][2], project[j][2], project[i][2]), t1+t2+t3))                   

       

    # delay = min(delays)
    # return delays
    minim = 0
    for _ in range(1, 6):
        if delays[_][1] < delays[minim][1]:
            minim = _
    return delays[minim][0], delays[minim][1]

def submit():
    project = [
    (duration_A.get(), due_date_A.get(), 'A'),
    (duration_B.get(), due_date_B.get(), 'B'),
    (duration_C.get(), due_date_C.get(), 'C')
    ]
    reponse = "La solution optimale est de suivre\n l'enchaînement suivant: "
    reponse += str(branch_and_bound(project)[0])
    reponse += ".\n \n On aura un retard de T= " + str(branch_and_bound(project)[1]) + " jours."
    response = Label(screen, text=reponse, font=("Arial", 17))
    response.place(x=100, y=490)



    #print(branch_and_bound(project))


submit_btn = Button(screen, text = "exécuter", bg="#e6772a", command = submit)
submit_btn.place(x = 320, y =400)

screen.mainloop()


# we have 3 jobs, A B and C
# for job in project: job = (duration, due date)
project = [
    (6, 8, 'A'),
    (4, 4, 'B'),
    (5, 12, 'C')
]






