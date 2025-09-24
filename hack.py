import tkinter as tk
from tkinter import ttk
from fishingbot import FishingBot
from puzzle import PuzzleBot

# Bot nesneleri
fishbot = FishingBot()
puzzleBot = PuzzleBot()

# Tkinter ana pencere
root = tk.Tk()
root.title("Metin2 Fishing BOT")
root.geometry("700x450")

# ttk tema
style = ttk.Style()
style.theme_use("clam")

# Notebook (sekme sistemi)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# ================= BOT TAB ================= #
bot_tab = ttk.Frame(notebook)
notebook.add(bot_tab, text="🎣 BOT")

ttk.Label(bot_tab, text="Welcome To Metin2 Fishing BOT", font=("Arial", 14, "bold")).pack(pady=15)

frame_stop = ttk.LabelFrame(bot_tab, text="⏱ Bot stop conditions", padding=10)
frame_stop.pack(pady=15)

endtime_var = tk.BooleanVar()
endtime_value = tk.StringVar()

ttk.Checkbutton(frame_stop, text="Total Time (Minutes)", variable=endtime_var).pack(side="left", padx=5)
ttk.Entry(frame_stop, textvariable=endtime_value, width=7).pack(side="left", padx=5)

fish_btn_text = tk.StringVar(value="START")
fish_btn = tk.Button(bot_tab, textvariable=fish_btn_text, command=lambda: toggle_fishbot(),
                     bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=18, height=2)
fish_btn.pack(pady=15)

# ================= OPTIONS TAB ================= #
options_tab = ttk.Frame(notebook)
notebook.add(options_tab, text="⚙ OPTIONS")

ttk.Label(options_tab, text="You can set the values of cooldowns.", font=("Arial", 13)).pack(pady=10)

frame_time = ttk.LabelFrame(options_tab, text="⌛ Time configuration (in seconds)", padding=15)
frame_time.pack(pady=15)

baittime = tk.DoubleVar(value=2)
throwtime = tk.DoubleVar(value=2)
startgame = tk.DoubleVar(value=2)

def update_labels():
    lbl_bait.config(text=f"{baittime.get():.0f}s")
    lbl_throw.config(text=f"{throwtime.get():.0f}s")
    lbl_start.config(text=f"{startgame.get():.0f}s")

# Baittime
ttk.Label(frame_time, text="Wait to put bait").grid(row=0, column=0, padx=15, pady=5)
tk.Scale(frame_time, from_=2, to=30, variable=baittime, orient="vertical", length=150, command=lambda e: update_labels()).grid(row=1, column=0)
lbl_bait = ttk.Label(frame_time, text="2s")
lbl_bait.grid(row=2, column=0, pady=5)

# Throwtime
ttk.Label(frame_time, text="Wait to throw").grid(row=0, column=1, padx=15, pady=5)
tk.Scale(frame_time, from_=2, to=30, variable=throwtime, orient="vertical", length=150, command=lambda e: update_labels()).grid(row=1, column=1)
lbl_throw = ttk.Label(frame_time, text="2s")
lbl_throw.grid(row=2, column=1, pady=5)

# Startgame
ttk.Label(frame_time, text="Wait to start game").grid(row=0, column=2, padx=15, pady=5)
tk.Scale(frame_time, from_=2, to=5, variable=startgame, orient="vertical", length=150, command=lambda e: update_labels()).grid(row=1, column=2)
lbl_start = ttk.Label(frame_time, text="2s")
lbl_start.grid(row=2, column=2, pady=5)

# ================= PUZZLE TAB ================= #
puzzle_tab = ttk.Frame(notebook)
notebook.add(puzzle_tab, text="🧩 PUZZLE")

ttk.Label(puzzle_tab, text="Welcome To Metin2 Fishing BOT", font=("Arial", 14, "bold")).pack(pady=15)

puzzle_btn_text = tk.StringVar(value="START")
puzzle_btn = tk.Button(puzzle_tab, textvariable=puzzle_btn_text, command=lambda: toggle_puzzlebot(),
                       bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=18, height=2)
puzzle_btn.pack(pady=15)

# ================== VALUES DICT ================== #
def get_values():
    return {
        "-ENDTIMEP-": endtime_var.get(),
        "-ENDTIME-": endtime_value.get(),
        "-BAITTIME-": baittime.get(),
        "-THROWTIME-": throwtime.get(),
        "-STARTGAME-": startgame.get(),
    }

# ================== EVENTLER ================== #
def toggle_fishbot():
    values = get_values()
    fishbot.set_to_begin(values)
    fishbot.botting = not fishbot.botting
    if fishbot.botting:
        puzzleBot.botting = False
        fish_btn_text.set("STOP")
    else:
        fish_btn_text.set("START")

def toggle_puzzlebot():
    values = get_values()
    puzzleBot.set_to_begin(values)
    puzzleBot.botting = not puzzleBot.botting
    if puzzleBot.botting:
        fishbot.botting = False
        puzzle_btn_text.set("STOP")
    else:
        puzzle_btn_text.set("START")

# ================== LOOP ================== #
def update_loop():
    if fishbot.botting:
        fishbot.runHack()
        fish_btn_text.set("STOP")
    else:
        fish_btn_text.set("START")



    if puzzleBot.botting:
        try:
            puzzleBot.runHack()
            puzzle_btn_text.set("STOP")
        except:
            puzzleBot.botting = False
            fishbot.botting = False
            puzzle_btn_text.set("START")
    else:
        puzzle_btn_text.set("START")

    root.after(10, update_loop)

# Başlat
update_labels()
update_loop()
root.mainloop()
