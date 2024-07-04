# Name: Rachel Xing
# OSU Email: xingru@oregonstate.edu
# Course: CS 325 - Analysis of Algorithms
# Assignment: Assignment #8
# Due Date: May 30 2023
# Description: Implement Dijkstra's algorithm to find the shortest
#              path from the source and the destination on a 2-D puzzle.
import heapq


def solve_puzzle(Board, Source, Destination):
    """
    Find the path covering the minimum number of cells from Source to
    Destination on a 2-D puzzle of size M*N (N rows and M columns).
    The movement can only be left (L), right (R), upper (U), and lower (L).
    Each cell might be empty '-' or have a barrier '#', so the movement can
    only proceed to an empty cell.

    The code is adapted from the code in Exploration 7.3:
    https://github.com/DURepo/CS_325_Exercises/blob/main/Graph-calculate_distances.py

    :param Board: a 2-D puzzle with N rows and M columns that might have
                  some barriers
    :param Source: The initial cell of the path to be found
    :param Destination: The final cell of the path to be found
    :return: a list containing a list of tuples that indices of each node
             in the path and a string that represents the moving directions;
             None if there is no such a path
    """
    # Check if the board is empty. If so, return None
    if len(Board) == 0:
        return None

    # Initialize a 2-D array to track the visited nodes during traversal
    Board_result = [[None for m in Board[0]] for n in Board]

    # Initialize a list that stores the possible moving directions and
    # a min-heap for implementing traversal
    moving_direction = {"L":(0, -1), "R":(0, 1), "U":(-1, 0), "D":(1, 0)}
    heap = [[Source, ""]]

    while len(heap) > 0:
        current_vertex = heapq.heappop(heap)
        curr_n, curr_m = current_vertex[0]

        # If reaching the destination, track the path based on the moving
        # directions, and return a tuple containing the path and moving
        # directions
        if (curr_n, curr_m) == Destination:
            sol = current_vertex[1]
            source_n, source_m = Source
            route = [Source]
            for direction in sol:
                n, m = moving_direction[direction]
                route.append((source_n + n, source_m + m))
                source_n += n
                source_m += m
            return (route, sol)

        # Since a cell can be added to the min-heap several times, we only
        # consider the unvisited cell to avoid unnecessary check
        if Board_result[curr_n][curr_m] is not None \
                and (len(current_vertex[1]) > len(Board_result[curr_n][curr_m])):
            continue

        # Check the neighbors of the selected node and updates the minimal path
        # from the source node
        for direction in moving_direction:
            n, m = moving_direction[direction]
            neighbor_n, neighbor_m = curr_n+n, curr_m+m

            # Check whether the cell is valid or a barrier. If so, skip and
            # continue iteration
            if 0 <= neighbor_n <= (len(Board)-1) and 0 <= neighbor_m <= (len(Board[0])-1) \
                    and Board[neighbor_n][neighbor_m] == '-':
                new_sol = current_vertex[1]+direction

                # Only consider the new path if it is a better path than
                # previously found paths
                if (Board_result[neighbor_n][neighbor_m] is None) or \
                        (len(new_sol) < len(Board_result[neighbor_n][neighbor_m])):
                    Board_result[neighbor_n][neighbor_m] = new_sol
                    heapq.heappush(heap, [(neighbor_n, neighbor_m), new_sol])

    # If the traversal didn't traverse the destination, there is no such a
    # minimal path for the destination and return None
    return None
