import time
import csv
import timer

def record_time(current_time, elapsed_time, user_guess, cat_state) -> None:
    """Record time when user makes a guess."""
    if user_guess == cat_state:
        answer: bool = True
    else:
        answer: bool = False

    with open('results.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow([current_time, elapsed_time, user_guess, cat_state, answer])
