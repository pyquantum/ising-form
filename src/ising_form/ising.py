"""Classes for defining Ising models"""

class Ising:
    def __init__(self, N: int):
        """Initialize an Ising spin model.

        Args:
            N (int): Number of  spin variables
        """
        self.N = N
