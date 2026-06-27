import os
import tkinter as tk

import cat
import timer
import record

ASSETS = os.path.join(os.path.dirname(__file__), "assets")


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Schrödinger's Cat")
        self.root.geometry("640x480")
        self.root.minsize(640, 480)
        self.timer = timer.Timer()
        self.cat = cat.Cat()
        self.interval = None

        # Hold references so the images are not garbage collected.
        self.alive_img = tk.PhotoImage(file=os.path.join(ASSETS, "alive.png"))
        self.dead_img = tk.PhotoImage(file=os.path.join(ASSETS, "dead.png"))

        self.frame = tk.Frame(root, padx=40, pady=40)
        self.frame.pack(expand=True)
        self.show_start()

    def clear(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_start(self) -> None:
        self.clear()
        tk.Label(self.frame, text="Interval (minutes):", font=("Helvetica", 14)).pack(pady=(0, 10))

        entry = tk.Entry(self.frame, font=("Helvetica", 14), justify="center")
        entry.pack(pady=(0, 10))
        entry.focus()

        error = tk.Label(self.frame, text="", fg="red")
        error.pack()

        def start() -> None:
            try:
                self.interval = int(entry.get())
                if self.interval <= 0:
                    raise ValueError
            except ValueError:
                error.config(text="Please enter a positive whole number.")
                return
            self.timer.start()
            self.show_guess()

        tk.Button(self.frame, text="Start", font=("Helvetica", 14), command=start).pack(pady=10)
        entry.bind("<Return>", lambda event: start())

    def show_guess(self) -> None:
        self.clear()
        tk.Label(self.frame, text="Is the cat alive or dead?", font=("Helvetica", 16)).pack(pady=(0, 20))

        buttons = tk.Frame(self.frame)
        buttons.pack()
        tk.Button(buttons, text="Alive", font=("Helvetica", 14), width=10,
                  command=lambda: self.guess("alive")).pack(side="left", padx=10)
        tk.Button(buttons, text="Dead", font=("Helvetica", 14), width=10,
                  command=lambda: self.guess("dead")).pack(side="left", padx=10)

    def guess(self, choice: str) -> None:
        elapsed = self.timer.elapsed()
        true_state = self.cat.state_at(elapsed / 60, self.interval)
        record.record_guess(elapsed, self.interval, true_state, choice)
        self.show_result(choice, true_state)

    def show_result(self, choice: str, true_state: str) -> None:
        self.clear()
        image = self.alive_img if true_state == "alive" else self.dead_img
        tk.Label(self.frame, image=image).pack()

        correct = choice == true_state
        verdict = "Correct!" if correct else "Wrong!"
        tk.Label(self.frame, text=f"The cat is {true_state}. {verdict}",
                 font=("Helvetica", 16), fg="green" if correct else "red").pack(pady=20)
        tk.Button(self.frame, text="Play again", font=("Helvetica", 14),
                  command=self.show_start).pack()


def main() -> None:
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
