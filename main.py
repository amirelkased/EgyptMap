import webbrowser
from tkinter import *
from tkinter import ttk
import searchAlgo as algo
import tkintermapview

root = Tk()
root.geometry('900x700+500+200')
root.title('Egypt Map')
root.iconbitmap('Photo/IconApp.ico')
root.resizable(False, False)

home_frame = Frame(root)
about_frame = Frame(root)
map_frame = Frame(root)

# const color
button_mode = True  # light is on
light_blue = '#267DFF'
dark_blue = '#154B9D'
dark_side = '#111212'
light_side = '#FFFFFF'


# change theme
def change_theme():
    global button_mode
    if button_mode:
        config_banner(dark_blue)
        config_labels(dark_side, 'white')
        theme_button.config(image=dark_mode, bg=dark_side, activebackground=dark_side)
        button_mode = False
    else:
        config_banner(light_blue)
        config_labels(light_side, 'black')
        theme_button.config(image=light_mode, bg=light_side, activebackground=light_side)
        button_mode = True


def config_banner(bg_color):
    left_side.config(bg=bg_color)
    welcome_label.config(bg=bg_color)
    welcome_description_label.config(bg=bg_color)


def config_labels(bg_color, fg_color):
    result.config(bg=bg_color)
    map_frame.config(bg=bg_color)
    labelFrom.config(bg=bg_color, fg=fg_color)
    labelTo.config(bg=bg_color, fg=fg_color)
    labelAlgo.config(bg=bg_color, fg=fg_color)
    btnGo.config(bg=bg_color, activebackground=bg_color)
    map_button.config(bg=bg_color, activebackground=bg_color)
    about_button.config(bg=bg_color, activebackground=bg_color)
    back_button_about.config(bg=bg_color, activebackground=bg_color)
    back_button_map.config(bg=bg_color, activebackground=bg_color)
    right_side.config(bg=bg_color)
    about_frame.config(bg=bg_color)
    choice_label.config(bg=bg_color, fg=fg_color)
    header.config(bg=bg_color, fg=fg_color)
    team_name.config(bg=bg_color, fg=fg_color)
    team_member.config(bg=bg_color, fg=fg_color)
    amir.config(bg=bg_color, fg=fg_color)
    ahmed.config(bg=bg_color, fg=fg_color)
    omnia.config(bg=bg_color, fg=fg_color)
    mayar.config(bg=bg_color, fg=fg_color)
    shrouq.config(bg=bg_color, fg=fg_color)
    team_supervise.config(bg=bg_color, fg=fg_color)
    ahmed_ghozia.config(bg=bg_color, fg=fg_color)


def change_frame(Next):
    if Next == 'about':
        home_frame.forget()
        map_frame.forget()
        about_frame.pack(fill='both', expand=1)
    elif Next == 'home':
        about_frame.forget()
        map_frame.forget()
        home_frame.pack(fill='both', expand=1)
    else:
        home_frame.forget()
        about_frame.forget()
        map_frame.pack(fill='both', expand=1)


def callback(url):
    webbrowser.open_new_tab(url)


# # Home Frame
left_side = Frame(home_frame, width=450, bg=light_blue)
left_side.pack(side=LEFT, fill=Y)

welcome_label = Label(left_side, text='Welcome to Egypt Map! 👋', cursor='hand2',
                      font=('roboto', 20, 'bold', 'underline'), bg=light_blue, fg='white')
welcome_label.place(x=18, y=180)

description = 'This is a simulation of Google Maps\nthat we applies different Algorithms.\n\nLike: BFS, DFS, ' \
              'and A*.\n\nTo get best result for your journey\nI hope best wish for you!. ❤️ '
welcome_description_label = Label(left_side, text=description, cursor='hand2',
                                  font=('roboto', 15, 'italic'), wraplength=400, bg=light_blue, fg='white')
welcome_description_label.place(x=18, y=240)

right_side = Frame(home_frame, width=450, bg=light_side)
right_side.pack(side=RIGHT, fill=Y)

choice_label = Label(right_side, bg=light_side, text='Let\'s Go...', font=('roboto', 20, 'bold'), fg='black')
choice_label.place(x=180, y=100)

map_button_photo = PhotoImage(
    file=r'Photo/egypt_map.png')
map_button = Button(right_side, image=map_button_photo, command=lambda: change_frame('map'), borderwidth=0,
                    bg=light_side, activebackground=light_side)
map_button.place(x=170, y=250)

about_button_photo = PhotoImage(
    file=r'Photo/about.png')
about_button = Button(right_side, image=about_button_photo, command=lambda: change_frame('about'), borderwidth=0,
                      bg=light_side, activebackground=light_side)
about_button.place(x=180, y=350)

light_mode = PhotoImage(file=r'Photo/light.png')
dark_mode = PhotoImage(file=r'Photo/dark.png')
theme_button = Button(right_side, image=light_mode, bg=light_side, borderwidth=0, activebackground=light_side,
                      command=change_theme)
theme_button.place(x=355, y=1)

# About Frame
about_frame.config(bg=light_side)

back_image = PhotoImage(file=r'Photo/back.png')
back_button_about = Button(about_frame, image=back_image, bd=0,
                           command=lambda: change_frame('home'), bg=light_side, activebackground=light_side)
back_button_about.place(x=5, y=5)

header = Label(about_frame, bg=light_side, text='---- Egypt Maps Application ----', font=('courier', 25, 'bold italic'),
               fg='black')
header.pack(pady=30)

team_name = Label(about_frame, bg=light_side, text='Team : Falcons', font=('courier', 25, 'bold italic'),
                  fg='black')
team_name.pack(pady=10)

team_member = Label(about_frame, bg=light_side, text='Team member : ', font=('courier', 18, 'bold'),
                    fg='black')
team_member.place(x=40, y=290)

linkedin_logo = PhotoImage(file=r'Photo/linkedin.png')

amir = Label(about_frame, bg=light_side, text='  Amir Ibrahim Elkased', image=linkedin_logo,
             fg='black', font=('courier', 18, 'bold'), cursor='hand2', compound=LEFT)
amir.place(x=280, y=320)
amir.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/amirelkased'))

ahmed = Label(about_frame, bg=light_side, text='  Ahmed Gaber', image=linkedin_logo,
              fg='black', font=('courier', 18, 'bold'), cursor='hand2', compound=LEFT)
ahmed.place(x=280, y=370)
ahmed.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/ahmed-gaber-a2a733235'))

omnia = Label(about_frame, bg=light_side, text='  Omnia Saad', image=linkedin_logo,
              fg='black', font=('courier', 18, 'bold'), cursor='hand2', compound=LEFT)
omnia.place(x=280, y=420)
omnia.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/omnia-saad-19b4801b7/'))

mayar = Label(about_frame, bg=light_side, text='  Mayar Emad', image=linkedin_logo,
              fg='black', font=('courier', 18, 'bold'), cursor='hand2', compound=LEFT)
mayar.place(x=280, y=470)
mayar.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/mayar-emad-6b9374206'))

shrouq = Label(about_frame, bg=light_side, text='  Shrouq El naggar', image=linkedin_logo,
               fg='black', font=('courier', 18, 'bold'), cursor='hand2', compound=LEFT)
shrouq.place(x=280, y=520)
shrouq.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/shrouqelnaggar1'))

team_supervise = Label(about_frame, bg=light_side, text='Supervisor : ', font=('courier', 18, 'bold'),
                       fg='black')
team_supervise.place(x=40, y=200)

ahmed_ghozia = Label(about_frame, bg=light_side, text='  Dr Ahmed Ghozia', image=linkedin_logo,
                     fg='black', font=('courier', 18, 'bold'), cursor='hand2', compound=LEFT)
ahmed_ghozia.place(x=280, y=230)
ahmed_ghozia.bind('<Button-1>', lambda e: callback('https://www.linkedin.com/in/ghozia/'))


# Map Frame


def searchFrom(event):
    value = event.widget.get()
    if value == '':
        choseFrom['values'] = algo.city
    else:
        choseFrom['values'] = algo.find_city(value)


def searchTo(event):
    value = event.widget.get()
    if value == '':
        choseTo['values'] = algo.city
    else:
        choseTo['values'] = algo.find_city(value)


global message1, message2, message3


def show(src, des, algoo, root):
    path = []
    if algoo == 'bfs':
        path = algo.bfs(src, des)[0]
    elif algoo == 'dfs':
        path = algo.dfs(src, des)[0]
    elif algoo == 'aStar':
        path = algo.aStar(src, des)[0]
    else:
        path = algo.uCost(src, des)[0]
    result.config(text=algo.drawPath(path, root))


map_frame.config(bg=light_side)

back_button_map = Button(map_frame, image=back_image, bd=0, command=lambda: change_frame('home'), bg=light_side,
                         activebackground=light_side)
back_button_map.place(x=5, y=5)

map_widget = tkintermapview.TkinterMapView(map_frame, width=850, height=500)
map_widget.set_position(30.06263, 31.24967, text='Egypt')
map_widget.set_zoom(6)

map_widget.place(x=25, y=175)
labelFrom = Label(map_frame, bg=light_side, text="From", font=('courier', 13, 'bold'), fg='black')
choseFrom = ttk.Combobox(map_frame, values=algo.city)
labelTo = Label(map_frame, bg=light_side, text="To", font=('courier', 13, 'bold'), fg='black')
choseTo = ttk.Combobox(map_frame, values=algo.city)
labelAlgo = Label(map_frame, bg=light_side, text="Chose Algorithm", font=('courier', 13, 'bold'), fg='black')
choseAlgo = ttk.Combobox(map_frame, values=['bfs', 'dfs', 'aStar', 'uniformCost'])

go_button = PhotoImage(file=r'Photo/button.png')
btnGo = Button(map_frame, image=go_button,
               command=lambda: show(choseFrom.get(), choseTo.get(), choseAlgo.get(), map_frame),
               bg=light_side, activebackground=light_side, bd=0)

result = Label(map_frame, bg=light_side, font=('courier', 16, 'bold'), fg='#0064FF')
result.place(x=70, y=110)

labelFrom.place(x=50, y=15)
choseFrom.place(x=100, y=15)
labelTo.place(x=315, y=15)
choseTo.place(x=350, y=15)
labelAlgo.place(x=550, y=15)
choseAlgo.place(x=720, y=15)
btnGo.place(x=400, y=45)

choseFrom.bind('<KeyRelease>', searchFrom)
choseTo.bind('<KeyRelease>', searchTo)

home_frame.pack(fill='both', expand=1)
root.mainloop()
