"""
This module defines the `Enity` class and its subclasses `Grass`, 
`Rock`, and `Tree`. These classes represent different entities in a 
simulation environment, each having a position and a visual representation.

Classes:
    Enity: An abstract base class for all entities in the simulation.
    Grass: A class representing grass entities on the map.
    Rock: A class representing rock entities on the map.
    Tree: A class representing tree entities on the map.

Usage:
    To create entities, instantiate the `Grass`, `Rock`, or `Tree` 
    classes with the appropriate parameters. Each entity can be placed 
    on the map and will have a specific visual representation.
"""

from abc import ABC
import logging

import logging_config
from point import Point


logging_config.setup_logging()
logger = logging.getLogger("EntityLogger")


class Enity(ABC):
    """
    Abstract base class for all entities in the simulation.

    Attributes:
        coordinate (Point): The position of the entity on the map.
        sprite (str): A visual representation of the entity.
    """
    def __init__(self, point: Point, sprite: str) -> None:
        """
        Initializes an Enity instance.

        Args:
            point (Point): The initial position of the entity.
            sprite (str): The visual representation of the entity.
        """
        self.coordinate = point
        self.sprite = sprite
        logger.info(f"{self.__class__.__name__} created at {point} with sprite '{sprite}'.")

    def get_coord(self) -> tuple:
        """
        Returns the coordinates of the entity.

        Returns:
            tuple: A tuple containing the x and y coordinates of the entity.
        """

        return self.coordinate.x, self.coordinate.y


class Grass(Enity):
    """
    Class representing grass entities on the map.

    Inherits from the Enity class and initializes with a default sprite.
    """
    def __init__(self, point: Point, sprite: str = "🌱") -> None:
        """
        Initializes a Grass instance.

        Args:
            point (Point): The initial position of the grass.
            sprite (str): The visual representation of the grass 
                          (default is "🌱").
        """
        super().__init__(point, sprite)


class Rock(Enity):
    """
    Class representing rock entities on the map.

    Inherits from the Enity class and initializes with a default sprite.
    """
    def __init__(self, point: Point, sprite: str = "⛰️ ") -> None:
        """
        Initializes a Rock instance.

        Args:
            point (Point): The initial position of the rock.
            sprite (str): The visual representation of the rock 
                          (default is "⛰️").
        """
        super().__init__(point, sprite)


class Tree(Enity):
    """
    Class representing tree entities on the map.

    Inherits from the Enity class and initializes with a default sprite.
    """

    def __init__(self, point: Point, sprite: str = "🌲") -> None:
        """
        Initializes a Tree instance.

        Args:
            point (Point): The initial position of the tree.
            sprite (str): The visual representation of the tree 
                          (default is "🌲").
        """
        super().__init__(point, sprite)
