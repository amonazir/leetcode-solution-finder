import requests
from bs4 import BeautifulSoup
from customtkinter import *
from PIL import ImageTk, Image
import pyperclip as pc 


def getSol(problem):

    q = problem
    url = f'https://walkccc.me/LeetCode/problems/{q:04}'

    try:
        req = requests.get(url)
    except:
        T2.configure(text = "Couldn't connect to network!", bg_color = "red")


    if req.status_code == 404:
         T2.configure(text = "Couldn't Find Question!", bg_color = "red")

    soup = BeautifulSoup(req.content, "html.parser")
    problem = soup.title.string[:-21]

    return [soup.find_all("code"), problem]

def on_clicked():
    pc.copy(T.cget("text"))

root = CTk() 
root.title("leetCode Solutions")

img = ImageTk.PhotoImage(Image.open("img/LeetCode_Logo_2.png"))
frame = CTkFrame(root, width=700, height=200)
frame.pack(fill = BOTH, expand = True)
logo = CTkLabel(frame,text = "", image = img)
logo.pack(side = LEFT, padx = 20, pady = 20)
SC = CTkLabel(frame, text = "LeetCode Solutions", font= ("Menlo", 30))
SC.pack(side = LEFT, pady = 30)


pane1 = CTkFrame(root)
pane1.pack(fill = BOTH, expand = True)


L1 = CTkLabel(pane1, text = " Enter the LeetCode Problem Number: ", anchor = 'center', justify = 'left')
L1.pack(side = LEFT, padx = 10, pady = 10)

txt = CTkEntry(pane1, width=300, placeholder_text= "Type Here...")
txt.pack(side = LEFT, padx = 2, pady = 10)

pane = CTkFrame(root)
pane.pack(fill = BOTH, expand = True)

var = IntVar()
R1 = CTkRadioButton(pane, text="CPP", variable=var, value=0, fg_color="#e7a41f", hover_color="grey")
R1.pack(side = LEFT, padx = 10, pady = 10, anchor = W )
R2 = CTkRadioButton(pane, text="Java", variable=var, value=1, fg_color="#e7a41f", hover_color="grey")
R2.pack(side = LEFT, padx = 10, pady = 10, anchor = W )
R3 = CTkRadioButton(pane, text="Python", variable=var, value=2, fg_color="#e7a41f", hover_color="grey")
R3.pack(side = LEFT, padx = 10, pady = 10, anchor = W)

copy_img = ImageTk.PhotoImage(Image.open("img/copy-94 copy 2.png"))
btn_copy = CTkButton(pane, text = "Copy Code" , image = copy_img,command=on_clicked, bg_color="grey", fg_color= "grey", hover_color="darkgrey")
btn_copy.pack(side = RIGHT, padx = 10)

code_frame = CTkScrollableFrame(root, width=700, height=370)

T = CTkLabel(code_frame, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", anchor="w", justify="left",) 
T2 = CTkLabel(root, text = "Problem name:", anchor="center", font = ("Ariel", 14),justify="left", width = 700, bg_color="#e7a41f")

def clicked():
    solve = getSol(int(txt.get()))
    T.configure(text = solve[0][var.get()].get_text(), font = ("Menlo", 12))
    T2.configure(text = solve[1],  bg_color="#e7a41f")

T2.pack(padx = 10,pady = 10, ipadx = 10, ipady = 10, fill = BOTH, expand = True, ) 
code_frame.pack()
T.pack(padx = 10, ipadx = 10, ipady = 10, fill = BOTH, expand = True)  

btn = CTkButton(root, text = "Get Solution" , command=clicked, bg_color="#e7a41f", fg_color= "#e7a41f", hover_color="grey")
btn.pack(padx= 10, pady= 10, fill = BOTH, expand = True)

root.mainloop() 
