import time

class StopwatchLogic:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True

    def pause(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def get_time(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

    def get_formatted_time(self):
        elapsed = self.get_time()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed % 1) * 1000)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"