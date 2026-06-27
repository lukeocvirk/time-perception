import cat
import timer

def main() -> None:
    try:
        interval: int = int(input("Please enter your chosen interval (in minutes): "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Create cat
    cat = cat.Cat()

    # Start the timer
    timer = timer.Timer()
    timer.start()

    # Run the timer and swap the cat's state at the specified interval
    i: int = 1
    while True:
        if timer.elapsed() * 60 >= interval * i:
            i += 1
            cat.swap()

if __name__ == "__main__":
    main()
    