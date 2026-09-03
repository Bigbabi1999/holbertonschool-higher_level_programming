#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classs"""


class Fish:
    """Represents a fish"""

    def swim(self):
        """Print that the fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat"""
        print("The fish lives in water")


class Bird:
    """Represents a bird"""

    def fly(self):
        """Print that the bird is fliying"""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish"""

    def fly(self):
        """Print that the flying fish is soaring"""
        print("The flying fish is saoring")

    def swim(self):
        """Print that the flying fish is swimming"""
        print("The flying fish is swimming")

    def habitat(self):
        """Print the flying fish's habitat"""
        print("The flying fish lives both in the water and the sky")
