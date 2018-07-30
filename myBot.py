import random
def do_turn(pw):
    if len(pw.my_planets()) == 0:
        return
    if pw.turn_number()%4 == 1:
        if len(pw.neutral_planets()) > 0:
            all_neutral_planets = pw.neutral_planets()
            tempName = []
            for plant in all_neutral_planets:
                tempName.append(plant.num_ships())
            idx = tempName.index(min(tempName))
            pw.issue_order(pw.my_planets()[random.randint(0,len(pw.my_planets())-1)], all_neutral_planets[idx], pw.my_planets()[0].num_ships()/2)

        if pw.turn_number()>50:
            if len(pw.enemy_planets()) >0:
                enemy_planets = pw.enemy_planets()
                ratio = []
                for planet in enemy_planets:
                    ratio.append(planet.num_ships())
                index = ratio.index(min(ratio))

                my_planets = pw.my_planets()
                distance = []
                for planet in my_planets:
                    distance.append(pw.distance(planet, enemy_planets[index]))
                attackers = []
                try:
                    for num in (0, 1, 2):
                        i = min(distance)
                        i = distance.index(i)
                        attackers.append(my_planets[i])
                        my_planets.remove(my_planets[i])
                        distance.remove(distance[i])
                    pw.issue_order(attackers[0], enemy_planets[index], attackers[0].num_ships()/3)
                    pw.issue_order(attackers[1], enemy_planets[index], attackers[1].num_ships()/3)
                    pw.issue_order(attackers[2], enemy_planets[index], attackers[2].num_ships()/3)
                except:
                    pw.issue_order(attackers[0], enemy_planets[index], attackers[0].num_ships()/3)










