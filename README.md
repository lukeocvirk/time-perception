# Human Time Perception Experiment
This program is meant to a facilitate a small study I am running on human time perception.

The idea behind this program is a variation on that of Schrödinger's Cat.
 - Schrödinger's Cat will swap between two states 'dead' and 'alive' every X minutes.
 - The user gets to define X at the start of the program.
 - The program starts with the cat in the 'alive' state.
 - The user will then go off and do other things with their day.
 - At some point, whenever the user feels like it/remembers, the user will return to the program
   and make a guess, on whether the cat is 'dead' or 'alive'.
 - At the point the user makes their guess, a log will be recorded in the `results.csv` including:
   1. A timestamp of the time elapsed since the program begun.
   2. The user's chosen interval, 'X'.
   3. The true state of the cat (i.e., 'dead' or 'alive').
   4. The user's guess of the state of the cat.
 - Once enough data is collected on a set of intervals, we can use the recorded data to get a
   better understanding of human time perception. We will be able to see what % of the time
   the user was accurate on each interval and with each length of time.

## Running the program
Requires Python 3 with Tkinter (included in standard Python installs).

```
python3 main.py
```

1. Enter your chosen interval (in minutes) and press **Start**.
2. Go about your day. Return whenever you like and press **Alive** or **Dead** to guess.
3. The true state is revealed after each guess, and the result is appended to `results.csv`.
4. Press **Guess again** to keep collecting data points without restarting.

