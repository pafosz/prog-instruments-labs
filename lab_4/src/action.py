"""
This module defines the `Action` class, which is responsible for managing
the actions of entities on a map within a simulation. It handles the 
creation, movement, and interaction of different entities such as 
predators, herbivores, and plants.

Classes:
    Action: Manages the actions and interactions of entities on the map.

Usage:
    To use this module, create an instance of the `Action` class with a 
    `Map` object and a JSON file containing the proportions of different 
    entities. Call the appropriate methods to initialize entities and 
    manage their actions during the simulation.
"""

import logging
from math import floor
from random import randint

from creature import Herbivore, Predator
from enity import Grass, Rock, Tree
from hellper import Reader
import logging_config
from mapping import Map
from point import Point


logging_config.setup_logging()
logger = logging.getLogger('ActionLogger')


class Action:
    """
    Class to perform actions on the map, including managing objects 
    and their interactions.

    Attributes:
        map_matrix (Map): The map object containing coordinates and objects.
        proportion (dict): The ratio of objects loaded from a JSON file.
        object_map (dict): A dictionary mapping object names to their classes.
    """
    def __init__(self, map_coord: Map, proportion_file: str) -> None:
        """
        Initializes the Action class.

        Args:
            map_coord (Map): The map object.
            proportion_file (str): Path to the file with object proportions.
        """
        self.map_matrix = map_coord
        self.proportion = Reader.read_json(proportion_file)
        self.object_map = {
            "Grass": Grass,
            "Rock": Rock,
            "Tree": Tree,
            "Herbivore": Herbivore,
            "Predator": Predator
        }
        logger.info("Action initialized successfully.")

    def procnet_enity(self) -> list:
        """
        Counts the number of entities on the map.

        Returns:
            list: A list containing the counts of predators, 
                  herbivores, and grass.
        """
        list_count = [0]*3
        for enit in self.map_matrix.map_coord.values():
            if isinstance(enit, Predator):
                list_count[0] += 1
            elif isinstance(enit, Herbivore):
                list_count[1] += 1
            elif isinstance(enit, Grass):
                list_count[2] += 1
        logger.debug(f"Entity counts: {list_count}")
        return list_count

    def calculate_more_enity(self):
        """
        Calculates how many objects need to be added to the map
        and adds them accordingly.
        """
        list_count = self.procnet_enity()
        list_enity = ["Predator", "Herbivore", "Grass"]
        for i in range(len(list_enity)):
            needed_count = self.calculate_count(self.proportion[list_enity[i]]) - list_count[i]
            logger.info(f"Adding {needed_count} {list_enity[i]}(s) to the map.")
            self.add_objects(needed_count, self.object_map[list_enity[i]])

    def calculate_count(self, proportion: float) -> int:
        """
        Calculates the number of objects that need to be created
        based on the proportion and the area of the map.

        Args:
            proportion (float): The proportion of the object.

        Returns:
            int: The number of objects to be created.
        """
        count = floor(self.map_matrix.get_area() * proportion)
        logger.debug(f"Calculated count for proportion {proportion}: {count}")
        return count

    def add_objects(self, count: int, object_class) -> None:
        """
        Adds objects to the map until the specified count is reached.

        Args:
            count (int): The number of objects to add.
            object_class: The class of the object to be created.
        """
        while count:
            point = Point(randint(0, self.map_matrix.weight - 1),
                          randint(0, self.map_matrix.height - 1))
            if not self.map_matrix.get_object(point):
                obj = object_class(point)
                self.map_matrix.add_object(obj)
                logger.info(f"Added {obj.__class__.__name__} at {point}.")
                count -= 1
            else:
                logger.debug(f"Point {point} is already occupied.")

    def init_actions(self) -> None:
        """
        Initializes actions by adding objects to the map according to
        the specified proportions.
        """
        for obj_name, proportion in self.proportion.items():
            count = self.calculate_count(proportion)
            logger.info(f"Initializing {count} {obj_name}(s) on the map.")
            self.add_objects(count, self.object_map[obj_name])

    def search_short_path(self, sprite, obj) -> list:
        """
        Searches for the shortest path from the sprite to the specified 
        type of object.

        Args:
            sprite: The sprite from which the search begins.
            obj: The class of the object to find a path to.

        Returns:
            list: A list of the shortest paths to the found objects.
        """
        all_short_path = []
        for cord, enit in self.map_matrix.map_coord.items():
            if isinstance(enit, obj):
                grass = self.map_matrix.get_all_object(sprite)
                short_path = []
                for i in grass:
                    path = self.map_matrix.search_path(cord, i)
                    if path:
                        short_path.append(path)
                if short_path:
                    min_path = min(short_path, key=len)
                    all_short_path.append(min_path)
                    logger.debug(f"Shortest path found: {min_path}")
        return all_short_path

    def action_enity(self, lists: list) -> None:
        """
        Executes actions for entities, moving them along the shortest path
        and performing attacks if necessary.

        Args:
            lists (list): A list of shortest paths for entities.
        """
        for shortest_list in lists:
            cord = shortest_list[0]
            enit = self.map_matrix.get_object(cord)
            logger.info(f"Moving entity {enit.__class__.__name__} from {cord} to {shortest_list[-1]}.")
            if (len(shortest_list) - 1) < enit.speed:
                self.map_matrix.delete_object(cord)
                enit.coordinate = shortest_list[-1]
                self.map_matrix.add_object(enit)
                enit.attack(self.map_matrix)
                logger.info(f"{enit.__class__.__name__} attacked after moving.")
            else:
                self.map_matrix.delete_object(cord)
                enit.coordinate = shortest_list[enit.speed]
                self.map_matrix.add_object(enit)

    def turn_actions(self) -> None:
        """
        Executes actions for entities, moving them along the shortest path
        and performing attacks if necessary.

        Args:
            lists (list): A list of shortest paths for entities.
        """
        predator_paths = self.search_short_path("🐇", Predator)
        herbivore_paths = self.search_short_path("🌱", Herbivore)
        logger.info(f"Executing actions for {len(predator_paths)} predators and {len(herbivore_paths)} herbivores.")
        self.action_enity(predator_paths)
        self.action_enity(herbivore_paths)
