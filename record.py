import csv
import os

RESULTS_FILE = os.path.join(os.path.dirname(__file__), "results.csv")
HEADER = ["elapsed_seconds", "interval_minutes", "true_state", "guess", "correct"]

def record_guess(elapsed_seconds, interval, true_state, guess) -> None:
    """Append one guess result to results.csv."""
    correct: bool = guess == true_state
    new_file: bool = not os.path.exists(RESULTS_FILE) or os.path.getsize(RESULTS_FILE) == 0

    with open(RESULTS_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(HEADER)
        writer.writerow([round(elapsed_seconds, 1), interval, true_state, guess, correct])
