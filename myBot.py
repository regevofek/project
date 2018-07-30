def do_turn(pw):
    if len(pw.my_planets()) == 0:
        return
    if pw.turn_number() > 68:
        return
    for my_planet in pw.my_planets():
        playFirstTurn(my_planet, pw)



def playFirstTurn(planet, pw):
    num_planets_to_get = 5
    nearbyPlanets = get_num_nearby_planets(planet, num_planets_to_get, pw)
    remaining_ships = planet.num_ships()
    for neutral_planet in nearbyPlanets:
        shipsToSend = neutral_planet.num_ships() + 5
        pw.debug(shipsToSend)
        pw.debug(planet.num_ships())
        if remaining_ships > shipsToSend:
            pw.issue_order(planet, neutral_planet, shipsToSend)
            remaining_ships -= shipsToSend


def get_num_nearby_planets(planet, num, pw):
    nearbyPlanets = list()
    planetsList = list()
    for neutral in pw.neutral_planets():
        planetsList.append((pw.distance(planet, neutral), neutral))

    for i in range(0, num, 1):
        minDistance = 1000000
        minIndex = 0
        for x in range(0, len(planetsList), 1):
            if planetsList[x][0] < minDistance:
                minDistance = planetsList[x][0]
                minIndex = x
        nearbyPlanets.append(planetsList[minIndex][1])
        planetsList.remove((planetsList[minIndex][0], planetsList[minIndex][1]))

    return nearbyPlanets



