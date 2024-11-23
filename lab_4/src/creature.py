"""
This module defines the `Creature` class and its subclasses `Herbivore` 
and `Predator`. These classes represent different types of entities in 
a simulation, allowing for movement and interaction with the environment.

Classes:
    Creature: An abstract base class for all creatures in the simulation.
    Herbivore: A class representing herbivorous creatures that can eat grass.
    Predator: A class representing predatory creatures that can attack 
              herbivores.

Usage:
    To create a creature, instantiate either the `Herbivore` or `Predator` 
    class with the appropriate parameters. The creatures can move and 
    perform attacks based on their defined behaviors.
"""

from abc import ABC, abstractmethod
import logging

from enity import Enity, Grass
import logging_config
from mapping import Map
from point import Point


logging_config.setup_logging()
logger = logging.getLogger('CreatureLogger')


class Creature(Enity, ABC):
    """
    Abstract base class for all creatures in the simulation.

    Attributes:
        point (Point): The current position of the creature on the map.
        sprite (str): A visual representation of the creature.
        speed (int): The movement speed of the creature.
        health (int): The health points of the creature.
    """
    def __init__(self,
                 point: Point,
                 sprite: str,
                 speed: int,
                 health: int
        ) -> None:
        """
        Initializes a Creature instance.

        Args:
            point (Point): The initial position of the creature.
            sprite (str): The visual representation of the creature.
            speed (int): The movement speed of the creature.
            health (int): The health points of the creature.
        """
        super().__init__(point, sprite)
        self.speed = speed
        self.health = health
        logger.info(f"{self.__class__.__name__} created at {point} with speed \
                     {speed} and health {health}.")

    def make_move(self, new_x: int, new_y: int) -> None:
        """
        Moves the creature to a new position on the map.

        Args:
            new_x (int): The new x-coordinate.
            new_y (int): The new y-coordinate.
        """
        logger.info(f"{self.__class__.__name__} moving from {self.point} to ({new_x}, {new_y}).")
        self.point = Point(new_x, new_y)

    @abstractmethod
    def attack(self, map_matrix: Map) -> None:
        """
        Abstract method to be implemented by subclasses for attacking.

        Args:
            map_matrix (Map): The map object containing all entities.
        """
        pass


class Herbivore(Creature):
    """
    Class representing herbivorous creatures.

    Inherits from the Creature class and implements the attack method 
    to consume grass.

    Attributes:
        attack (int): The attack power of the herbivore 
                      (default is not applicable).
    """
    def __init__(self,
                 point: Point,
                 speed: int = 1,
                 health: int = 5,
                 sprite: str = "🐇"
        ) -> None:
        """
        Initializes a Herbivore instance.

        Args:
            point (Point): The initial position of the herbivore.
            speed (int): The movement speed of the herbivore (default is 1).
            health (int): The health points of the herbivore (default is 5).
            sprite (str): The visual representation of the herbivore 
                          (default is "🐇").
        """
        super().__init__(point, sprite, speed, health)

    def attack(self, map_matrix: Map) -> None:
        """
        Attacks nearby grass on the map.

        Args:
            map_matrix (Map): The map object containing all entities.
        """
        coord = self.coordinate.get_neighboors()
        for i in coord:
            if isinstance(map_matrix.get_object(i), Grass):
                logger.info(f"{self.__class__.__name__} attacking grass at {i}.")
                map_matrix.delete_object(i)


class Predator(Creature):
    """
    Class representing predatory creatures.

    Inherits from the Creature class and implements the attack method 
    to attack herbivores.

    Attributes:
        attack (int): The attack power of the predator.
    """
    def __init__(self,
                 point: Point,
                 speed: int = 2,
                 health: int = 8,
                 atack: int = 5,
                 sprite: str = '🐺'
        ) -> None:
        """
        Initializes a Predator instance.

        Args:
            point (Point): The initial position of the predator.
            speed (int): The movement speed of the predator (default is 2).
            health (int): The health points of the predator (default is 8).
            attack (int): The attack power of the predator (default is 5).
            sprite (str): The visual representation of the predator 
                          (default is '🐺').
        """
        super().__init__(point, sprite, speed, health)
        self.atack = atack

    def attack(self, map_matrix: Map) -> None:
        """
        Attacks nearby herbivores on the map.

        Args:
            map_matrix (Map): The map object containing all entities.
        """
        coord = self.coordinate.get_neighboors()
        for i in coord:
            if isinstance(map_matrix.get_object(i), Herbivore):
                enit = map_matrix.get_object(i)
                enit.health -= self.atack
                logger.info(f"{self.__class__.__name__} attacking {enit.__class__.__name__} at {i}.")
                if enit.health <= 0:
                    logger.info(f"{enit.__class__.__name__} at {i} has been killed.")
                    map_matrix.delete_object(i)
                break
