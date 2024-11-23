"""
This module defines the `Map` class, which represents a two-dimensional 
grid for managing entities in a simulation. The class provides methods 
to add, delete, and retrieve entities, as well as to perform pathfinding 
operations.

Classes:
    Map: A class representing a two-dimensional grid that holds entities 
         and provides methods for managing them.

Usage:
    Create an instance of the Map class with specified dimensions, 
    then use its methods to manage entities and perform operations 
    like pathfinding.
"""

from collections import deque
from typing import Dict, List, Tuple

from enity import Enity
from point import Point


class Map:
    """
    A class that represents a two-dimensional map for simulation entities.

    Attributes:
        height (int): The height of the map.
        weight (int): The width of the map.
        map_coord (dict): A dictionary mapping coordinates to entities.

    Methods:
        get_size() -> Tuple[int]: Returns the dimensions of the map.
        get_area() -> int: Returns the area of the map.
        add_object(obj: Enity) -> Enity: Adds an entity to the map.
        delete_object(point: Point) -> None: Removes an entity from the map.
        get_object(point: Point) -> Enity | bool: Retrieves an entity at 
                                    a given point.
        get_all_object(sprite: str) -> List[Enity]: Returns all entities 
                                       with a specific sprite.
        check_have_object(point: Point) -> bool: Checks if a point is within 
                                           map bounds.
        search_path(start: Point, target: Point) -> List[Point]: Finds a path 
                                                    from start to target.
    """
    def __init__(self, height: int, weight: int) -> None:
        """
        Initializes a Map instance with specified dimensions.

        Args:
            height (int): The height of the map.
            weight (int): The width of the map.
        """
        self.height = height
        self.weight = weight
        self.map_coord = {}

    def get_size(self) -> Tuple[int]:
        """
        Returns the dimensions of the map.

        Returns:
            Tuple[int]: A tuple containing the height and width of the map.
        """
        return self.height, self.weight

    def get_area(self) -> int:
        """
        Returns the area of the map.

        Returns:
            int: The area of the map (height * width).
        """
        return self.height*self.weight

    def add_object(self, obj: Enity) -> Dict:
        """
        Adds an entity to the map at its coordinate.

        Args:
            obj (Enity): The entity to be added.

        Returns:
            Enity: The added entity.
        """
        point = obj.coordinate
        self.map_coord[point] = obj
        return self.map_coord[point]

    def delete_object(self, point) -> None:
        """
        Removes an entity from the map at the specified point.

        Args:
            point (Point): The coordinate of the entity to be removed.
        """
        del self.map_coord[point]

    def get_object(self, point) -> Enity | bool:
        """
        Retrieves an entity at a given point.

        Args:
            point (Point): The coordinate to check for an entity.

        Returns:
            Enity | bool: The entity at the point, or False if not found.
        """
        if point in self.map_coord:
            return self.map_coord[point]
        return False

    def get_all_object(self, sprite: str) -> List[Enity]:
        """
        Returns all entities with a specific sprite.

        Args:
            sprite (str): The sprite representation to filter entities.

        Returns:
            List[Enity]: A list of entities matching the specified sprite.
        """
        return [point for point,
                enity in self.map_coord.items() if enity.sprite == sprite]

    def check_have_object(self, point: Point) -> bool:
        """
        Checks if a point is within the bounds of the map.

        Args:
            point (Point): The point to check.

        Returns:
            bool: True if the point is within bounds, False otherwise.
        """
        return 0 <= point.x < self.weight and 0 <= point.y < self.height

    def search_path(self, start: Point, target: Point) -> List[Point]:
        """
        Finds a path from the start point to the target point using BFS.

        Args:
            start (Point): The starting coordinate.
            target (Point): The target coordinate.

        Returns:
            List[Point]: A list of points representing the path, or an empty
                         list if no path exists.
        """
        queue = deque([(start, [start])])
        visited = set([start])
        neighbor_target = target.get_neighboors()
        while queue:
            current, path = queue.popleft()

            if current in neighbor_target:
                return path

            for neighbor in current.get_neighboors():
                if not self.check_have_object(neighbor):
                    continue
                if neighbor in self.map_coord:
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return []
