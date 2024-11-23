"""
This module defines the `Point` class, which represents a point in a 
two-dimensional space. The class provides methods for manipulating 
points and retrieving their neighbors.

Classes:
    Point: A class representing a point in a 2D space with x and y coordinates.

Usage:
    Create an instance of the Point class with specified x and y 
    coordinates. Use its methods to access neighbors or modify the 
    coordinates.
"""

import logging

import logging_config


logging_config.setup_logging()
logger = logging.getLogger("PointLogger")


class Point:
    """
    A class that represents a point in 2D space.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.

    Methods:
        __hash__() -> int: Returns a hash of the point.
        __eq__(other) -> bool: Checks equality with another point.
        __str__() -> str: Returns a string representation of the point.
        __repr__() -> str: Returns a detailed string representation of 
                           the point.
        get_neighboors() -> list: Returns a list of neighboring points.
        point() -> tuple: Property to get the coordinates as a tuple.
    """
    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a Point instance with specified coordinates.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
        """
        self.x = x
        self.y = y
        logger.info(f"Point created at coordinates: ({x}, {y})")

    def __hash__(self) -> int:
        """
        Returns a hash of the point based on its coordinates.

        Returns:
            int: The hash value of the point.
        """
        hash_value = hash((self.x, self.y))
        logger.debug(f"Hash for point {self}: {hash_value}")
        return hash_value

    def __eq__(self, other) -> bool:
        """
        Checks equality with another point.

        Args:
            other (Point): The point to compare with.

        Returns:
            bool: True if the points are equal, False otherwise.
        """
        equal = self.x == other.x and self.y == other.y
        logger.debug(f"Comparing {self} with {other}: Equal = {equal}")
        return equal

    def __str__(self) -> str:
        """
        Returns a string representation of the point.

        Returns:
            str: A string describing the point in a readable format.
        """
        return f"X: {self.x} Y: {self.y}"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the point.

        Returns:
            str: A string that includes the coordinates of the point.
        """
        return f"Point(X:{self.x}, Y:{self.y})"

    def get_neighboors(self, width: int, height: int) -> list:
        """
        Returns a list of neighboring points.

        Returns:
            list: A list containing the points directly adjacent 
                   (up, down, left, right) to the current point.
        """
        neighbors = []

        # Проверка верхней границы
        if self.y + 1 < height:
            neighbors.append(Point(self.x, self.y + 1))  # Up

        # Проверка нижней границы
        if self.y - 1 >= 0:
            neighbors.append(Point(self.x, self.y - 1))  # Down

        # Проверка правой границы
        if self.x + 1 < width:
            neighbors.append(Point(self.x + 1, self.y))   # Right

        # Проверка левой границы
        if self.x - 1 >= 0:
            neighbors.append(Point(self.x - 1, self.y))    # Left

        logger.debug(f"Neighbors for point {self}: {neighbors}")
        return neighbors

    @property
    def point(self) -> tuple:
        """
        Property to get the coordinates as a tuple.

        Returns:
            tuple: A tuple containing the x and y coordinates of the point.
        """
        return self.x, self.y

    @point.setter
    def point(self, coords: tuple) -> None:
        """
        Property to set the coordinates of the point.

        Args:
            coords (tuple): A tuple containing the new x and y coordinates.
        """
        self.x, self.y = coords
        logger.info(f"Point coordinates updated to: {coords}")
