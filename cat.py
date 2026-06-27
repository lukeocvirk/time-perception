
class Cat:
    def __init__(self) -> None:
        self.state: str = "alive"

    def swap(self) -> None:
        """Swap the state of the cat between alive and dead."""
        if self.state == "alive":
            self.state = "dead"
            print("The cat is dead.")
        else:
            self.state = "alive"
            print("The cat is alive.")

    def state_at(self, elapsed_minutes: float, interval: float) -> str:
        """Return the cat's state given elapsed time and the swap interval."""
        swaps: int = int(elapsed_minutes // interval)
        return "alive" if swaps % 2 == 0 else "dead"