import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        self.end_time = None

    def stop(self):
        """Stop the timer."""
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        self.end_time = time.time()

    def elapsed(self):
        """Return the elapsed time in seconds."""
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time