"""
This module defines the `Render` and `Simulation` classes for managing 
the visualization and execution of a simulation involving entities on a map.

Classes:
    Render: A class responsible for rendering the map and displaying 
            information about entities.
    Simulation: A class that manages the simulation's state, including 
                the progression of turns and user interactions.

Usage:
    Create an instance of the Simulation class to start the simulation, 
    which will handle rendering and game logic.
"""

import time

from action import Action
from const import PATH
from mapping import Map
from point import Point


class Render:
    """
    A class responsible for rendering the map and displaying information 
    about entities.

    Attributes:
        map_matrix (Map): The map instance containing entities to render.

    Methods:
        print_info() -> None: Displays information about entity types.
        draw_map() -> None: Renders the current state of the map.
    """
    def __init__(self, map_coord: Map) -> None:
        """
        Initializes a Render instance with a specified map.

        Args:
            map_coord (Map): The map to be rendered.
        """
        self.map_matrix = map_coord

    @staticmethod
    def print_info() -> None:
        """
        Displays information about the types of entities in the simulation.
        """
        dict_info_object = {
            'P': 'predator',
            'H': 'herbivores',
            'G': 'grass',
            'R': 'rock',
            'T': 'tree',
        }
        for key, value in dict_info_object.items():
            print(f'{key} - {value}')
        print("Нажмите Enter для переключения паузы:")

    def draw_map(self) -> None:
        """
        Renders the current state of the map, displaying each entity or an 
        empty space if none exists.
        """
        for i in range(self.map_matrix.height):
            for j in range(self.map_matrix.weight):
                obj = self.map_matrix.get_object(Point(j, i))
                if obj:
                    print("|" + obj.sprite + "|", end="")
                else:
                    print("|  |", end="")
            print()


class Simulation:
    """
    A class that manages the simulation's state, including the progression 
    of turns and user interactions.

    Attributes:
        move_count (int): The current count of simulation turns.
        matrix (Map): The map instance representing the simulation area.
        render (Render): The render instance for visualizing the map.
        action (Action): The action instance for managing entity actions.
        is_paused (bool): Indicates whether the simulation is currently paused.

    Methods:
        next_turn() -> None: Advances the simulation by one turn.
        start_simulation() -> None: Starts the simulation loop.
        listen_for_pause() -> None: Listens for user input to 
                                    pause/resume the simulation.
    """
    def __init__(self, height: int, weight: int) -> None:
        """
        Initializes a Simulation instance with specified map dimensions.

        Args:
            height (int): The height of the map.
            weight (int): The width of the map.
        """
        self.move_count = 0
        self.matrix = Map(height, weight)
        self.render = Render(map_coord=self.matrix)
        self.action = Action(map_coord=self.matrix, proportion_file=PATH)
        self.is_paused = False

    def next_turn(self) -> None:
        """
        Advances the simulation by one turn, rendering the map and 
        executing entity actions.
        """
        self.render.draw_map()
        self.action.turn_actions()
        self.move_count += 1

    def start_simulation(self) -> None:
        """
        Starts the simulation loop, continuously updating the state and 
        rendering the map until interrupted.
        """
        self.render.print_info()
        self.action.init_actions()
        while True:
            if not self.is_paused:
                print(f"Итерация: {self.move_count}")
                self.next_turn()
                if not self.move_count % 3:
                    self.action.calculate_more_enity()
            time.sleep(1.5)

    def listen_for_pause(self):
        """
        Listens for user input to pause or resume the simulation.
        The simulation can be toggled between paused and running states.
        """
        while True:
            input()
            self.is_paused = not self.is_paused
            if self.is_paused:
                print("Игра на паузе. Для продолжения тыкните Enter")
            else:
                print("Игра продолжается.")
