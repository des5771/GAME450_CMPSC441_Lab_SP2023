'''
Lab 3: Travel Cost

Your player will need to move from one city to another in order to complete the game.
The player will have to spend money to travel between cities. The cost of travel depends 
on the difficulty of the terrain.
In this lab, you will write a function that calculates the cost of a route between two cities,
A terrain is generated for you 
'''
import numpy as np

def get_route_cost(route_coordinate, game_map):
    """
    This function takes in a route_coordinate as a tuple of coordinates of cities to connect, 
    example:  and a game_map as a numpy array of floats,
    remember from previous lab the routes looked like this: [(A, B), (A, C)]
    route_coordinates is just inserts the coordinates of the cities into a route like (A, C).
    route_coordinate might look like this: ((0, 0), (5, 4))

    For each route this finds the cells that lie on the line between the
    two cities at the end points of a route, and then sums the cost of those cells
      -------------
    1 | A |   |   |
      |-----------|
    2 |   |   |   |
      |-----------|
    3 |   | C |   |
      -------------
        I   J   K 

    Cost between cities A and C is the sum of the costs of the cells 
        I1, I2, J2 and J3.
    Alternatively you could use a direct path from A to C that uses diagonal movement, like
        I1, J2, J3

    :param route_coordinates: a list of tuples of coordinates of cities to connect
    :param game_map: a numpy array of floats representing the cost of each cell

    :return: a floating point number representing the cost of the route
    """
    # Build a path from start to end that looks like [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 4)]
    
    # Bresenham's line algorithm
    # plotLine(x0, y0, x1, y1)
    # dx = x1 - x0
    # dy = y1 - y0
    # D = 2*dy - dx
    # y = y0

    # for x from x0 to x1
    #     plot(x, y)
    #     if D > 0
    #         y = y + 1
    #         D = D - 2*dx
    #     end if
    #     D = D + 2*dy

    # Converted tuples:
    # [1][0] = x1
    # [0][1] = y0
    
    # Implementation:
    # print("X0 is: ",route_coordinate[0][0])
    # print("X1 is: ",route_coordinate[1][0])
    # print("Y0 is: ",route_coordinate[0][1])
    # print("Y1 is: ",route_coordinate[1][1])

    # Get distance of X and Y and slope
    dx = route_coordinate[1][0] - route_coordinate[0][0]
    dy = route_coordinate[1][1] - route_coordinate[0][1]
    D = 2*dy - dx
    # print("dx is: ",dx)
    # print("dy is: ",dy)

    # Account for negative dy
    if dy >=0:
      y = route_coordinate[0][1]
    else:
      y = route_coordinate[1][1]

    # Initialize path
    path = [[],]

    # Loop dat bish
    if dx >= 0:
      for x in range(route_coordinate[0][0], route_coordinate[1][0]):
        # print("Current X is: ", x)
        # print("Current Y is: ", y)
        path = path + [(x,y)]
        if D > 0:
          if dy >= 0:
            y = y + 1
          else:
            y = y - 1
          D = D - 2*dx
        D = D + 2*dy
    # Account for negative dx
    else:
        for x in range(route_coordinate[1][0], route_coordinate[0][0]):
          # print("Current X is: ", x)
          # print("Current Y is: ", y)
          path = path + [(x,y)]
          if D < 0:
            if dy >= 0:
              y = y + 1
            else:
              y = y - 1
            D = D - 2*dx
          D = D + 2*dy

    # Remove first element of path because of dumb python
    path = path[1:]
    # print(path)
 
    return game_map[tuple(zip(*path))].sum()


def route_to_coordinates(city_locations, city_names, routes):
    """ get coordinates of each of the routes from cities and city_names"""
    route_coordinates = []
    for route in routes:
        start = city_names.index(route[0])
        end = city_names.index(route[1])
        route_coordinates.append((city_locations[start], city_locations[end]))
    return route_coordinates


def generate_terrain(map_size):
    """ generate a terrain map of size map_size """
    return np.random.rand(*map_size)


def main():
    # Ignore the following 4 lines. This is bad practice, but it's just to make the code work in the lab.
    import sys
    from pathlib import Path
    sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
    from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta', 
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    map_size = 300, 200

    n_cities = len(city_names)
    game_map = generate_terrain(map_size)
    print(f'Map size: {game_map.shape}')

    city_locations = get_randomly_spread_cities(map_size, n_cities)
    routes = get_routes(city_names)
    np.random.shuffle(routes)
    routes = routes[:10]
    route_coordinates = route_to_coordinates(city_locations, city_names, routes)

    for route, route_coordinate in zip(routes, route_coordinates):
        print(f'Cost between {route[0]} and {route[1]}: {get_route_cost(route_coordinate, game_map)}')


if __name__ == '__main__':
    main()