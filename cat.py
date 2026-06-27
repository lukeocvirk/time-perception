
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