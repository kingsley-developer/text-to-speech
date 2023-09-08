import ttkbootstrap as tb
import pyttsx3
import Text_config
import tkinter
from tkinter import filedialog
import threading
from tkinter import messagebox

def tab1_convert_button():
    def new_thread():
        try:
            text = text_area.get("1.0", tkinter.END)
            pyttsx3.speak(text=text)
        except Exception as error:
            error = str(error)
            messagebox.showerror(title="Text-To-Speech", message=error)
        
    new_thread_var = threading.Thread(name="new_Tab1_Thread", target=new_thread, daemon=True)
    new_thread_var.start()

def tab2_convert_button():
    def new_thread():

        filepath = filedialog.askopenfilename(title="Open a file",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))
        try:
            file = open(filepath, "r")
            progress_bar.start()
            w.update_idletasks()
            pyttsx3.speak(text=file.read())
            file.close()
            progress_bar.stop()
            progress_bar["value"] = 100
            w.update_idletasks()

        except Exception as error:
            error = str(error)
            progress_bar.stop()
            progress_bar["value"] = 0
            w.update_idletasks()
            messagebox.showerror(title="Text-To-Speech", message=error)

    new_thread_var = threading.Thread(name="new_Tab2_Thread", target=new_thread, daemon=True)
    new_thread_var.start()

w = tb.Window(themename="cyborg")
w.title("Text-To-Speech-Converter")
#CENTER WINDOW
win_width = 1000
win_height = 640
screen_width = w.winfo_screenwidth()
ycreen_height = w.winfo_screenheight()
x = int((screen_width / 2)-(win_width / 2))
y = int((ycreen_height / 2)-(win_height / 2))
w.geometry("{}x{}+{}+{}".format(win_width, win_height, x, y))
w.resizable(width=False, height=False)

version_number = tb.Label(w, text=Text_config.version_number,
                 font=("Impact", 13),
                 bootstyle="success").place(x=0, y=0)


title = tb.Label(w, text="Text-To-Speech",
                 font=("Impact", 25),
                 bootstyle="warning").pack()

tabs = tb.Notebook(w, bootstyle="white")
tabs.pack(pady=40, expand=True, fill="both")

tab1 = tb.Frame(tabs, width=700, height=400)
tab2 = tb.Frame(tabs, width=700, height=400)

enter_text = tb.Label(tab1,
                      text="Enter Texts",
                      font=("Aerial", 17),
                      bootstyle="white")
enter_text.pack(pady=10)

text_area = tkinter.Text(tab1, width=160, height=10, fg="white", font=("Aerial", 20))
text_area.pack(pady=20)

text_B_style = tb.Style()
text_B_style.configure("success.TButton", font=("Aerial", 10))

text_B = tb.Button(tab1,
                   command=tab1_convert_button,
                   text="Convert To Speech", bootstyle="success",
                   style="success.TButton")
text_B.pack(pady=5)

click_button = tb.Label(tab2,
                      text="Click Button to open any file and convert to speech",
                      font=("Aerial", 30),
                      bootstyle="warning")
click_button.pack(pady=40)


button_style = tb.Style()
button_style.configure("success.TButton", font=("Aerial", 20))

button = tb.Button(tab2,
                   command=tab2_convert_button,
                   text="Open a file",
                   bootstyle="success", style="success.TButton",
                   width=30)
button.pack(pady=70)

progress_bar = tb.Progressbar(tab2, value=0, maximum=100, bootstyle="success")
progress_bar.pack(pady=30, fill=tkinter.X, padx=50)

tabs.add(tab1, text="Write text")
tabs.add(tab2, text="Open file")

w.mainloop()