import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from find_motion1 import find_motion
from PIL import Image, ImageTk

# Main Window
window = tk.Tk()
window.title("Smart CCTV")
window.geometry("1080x760")
window.configure(bg="#FFDDC1")  # Bright RGB color for the background

# Notebook for tabs
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

# Tab 1: Smart CCTV
tab1 = tk.Frame(notebook, bg="#FFDDC1")
notebook.add(tab1, text="Smart CCTV")

# Tab 2: Find Stolen
tab2 = tk.Frame(notebook, bg="#FFDDC1")
notebook.add(tab2, text="Find Stolen")

# ====================== Tab 1: Smart CCTV ====================== #
frame1 = tk.Frame(tab1, bg="#FFDDC1")

label_title = tk.Label(frame1, text="Smart CCTV Camera", bg="#FFDDC1")
label_font = font.Font(size=35, weight="bold", family="Helvetica")
label_title["font"] = label_font
label_title.pack(pady=(10, 10))

icon = Image.open("icons/spy.png")
icon = icon.resize((150, 150), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg="#FFDDC1")
label_icon.pack(pady=(5, 10))

btn1_image = Image.open("icons/lamp.png").resize((50, 50), Image.Resampling.LANCZOS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open("icons/rectangle-of-cutted-line-geometrical-shape.png").resize(
    (50, 50), Image.Resampling.LANCZOS
)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open("icons/exit.png").resize((50, 50), Image.Resampling.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open("icons/security-camera.png").resize((50, 50), Image.Resampling.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open("icons/incognito.png").resize((50, 50), Image.Resampling.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open("icons/recording.png").resize((50, 50), Image.Resampling.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# Buttons
btn_font = font.Font(size=25)
btn1 = tk.Button(
    frame1, text="Monitor", height=90, width=180, fg="green", image=btn1_image, compound="left"
)
btn1["font"] = btn_font
btn1.pack(pady=(10, 10))

btn2 = tk.Button(
    frame1,
    text="Rectangle",
    height=90,
    width=180,
    fg="orange",
    command=rect_noise,
    compound="left",
    image=btn2_image,
)
btn2["font"] = btn_font
btn2.pack(pady=(10, 10))

btn3 = tk.Button(
    frame1,
    text="Noise",
    height=90,
    width=180,
    fg="green",
    command=noise,
    image=btn3_image,
    compound="left",
)
btn3["font"] = btn_font
btn3.pack(pady=(10, 10))

btn4 = tk.Button(
    frame1,
    text="Record",
    height=90,
    width=180,
    fg="orange",
    command=record,
    image=btn4_image,
    compound="left",
)
btn4["font"] = btn_font
btn4.pack(pady=(10, 10))

btn6 = tk.Button(
    frame1,
    text="In Out",
    height=90,
    width=180,
    fg="green",
    command=in_out,
    image=btn6_image,
    compound="left",
)
btn6["font"] = btn_font
btn6.pack(pady=(10, 10))

btn5 = tk.Button(
    frame1, height=90, width=180, fg="red", command=window.quit, image=btn5_image
)
btn5["font"] = btn_font
btn5.pack(pady=(10, 10))

frame1.pack()

# ====================== Tab 2: Find Stolen ====================== #
label_tab2 = tk.Label(tab2, text="Welcome", bg="#FFDDC1")
label_tab2.pack(pady=(20, 10))
label_tab2["font"] = font.Font(size=35, weight="bold", family="Helvetica")

# Button Font
btn_tab2_font = font.Font(size=15, weight="bold", family="Helvetica")

# Buttons for Tab 2
btn_find_motion = tk.Button(
    tab2, text="Spot Diff", fg="green", height=3, width=10, command=find_motion
)
btn_find_motion["font"] = btn_tab2_font
btn_find_motion.pack(pady=(25, 10))

btn_exit_tab2 = tk.Button(
    tab2, text="Exit", fg="red", height=3, width=10, command=window.quit
)
btn_exit_tab2["font"] = btn_tab2_font
btn_exit_tab2.pack(pady=(10, 10))

# Footer
label_footer = tk.Label(tab2, text="Thanks for Using", bg="#FFDDC1")
label_footer.pack(pady=(20, 10))
label_footer["font"] = font.Font(size=20, weight="bold", family="Helvetica")

# Run the Application
window.mainloop()