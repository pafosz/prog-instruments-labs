"""
This module runs a simulation using multithreading. It initializes a 
simulation instance and manages concurrent execution of simulation 
processes, allowing for interactive control.

Functions:
    main: The entry point of the program that sets up and starts the 
          simulation using a thread pool.

Usage:
    Run this module to start the simulation. It will create a 
    simulation environment and allow for concurrent listening for 
    pause commands.
"""

import concurrent.futures

from simulation import Simulation


def main():
    """
    Initializes and starts the simulation.

    This function creates an instance of the Simulation class and 
    runs the simulation and pause listener in separate threads. 
    It uses a ThreadPoolExecutor to manage concurrency.

    Raises:
        Exception: If there is an error during simulation initialization 
                    or execution.
    """
    try:
         # Initialize the simulation with a grid of 5x5
        simulation = Simulation(5, 5)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # Start the simulation
            executor.submit(simulation.start_simulation)
            # Listen for pause commands
            executor.submit(simulation.listen_for_pause)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
