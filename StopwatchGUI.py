import tkinter as tk
from StopwatchLogic import StopwatchLogic

class StopwatchGUI:
    def __init__(self, master):
        self.master = master
        self.stopwatch = StopwatchLogic()
        self.running = False

        self.time_label = tk.Label(master, text="00:00.000", font=("Arial", 24))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Старт", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(master, text="Пауза", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Сброс", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_time()

    def start(self):
        if not self.running:
            self.stopwatch.start()
            self.running = True
            self.start_button.config(state=tk.DISABLED)

    def pause(self):
        if self.running:
            self.stopwatch.pause()
            self.running = False
            self.start_button.config(state=tk.NORMAL)

    def reset(self):
        self.stopwatch.reset()
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.update_time()

    def update_time(self):
        if self.running:
            self.time_label.config(text=self.stopwatch.get_formatted_time())
        self.master.after(10, self.update_time)