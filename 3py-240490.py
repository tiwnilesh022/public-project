# Krishna Copiers sells and services copy machines to customers in 11 cities throughout the country. The
# company want to set up service centres in three of these cities. After Krishna Copiers chooses the
# location of the service centres, it must assign customers in each city to one of the service centres. For
# example, if it decides to locate a service centre in New York and then assigns its Boston customers to the
# New York service centre, a service representative from New York will travel from Boston when services
# are required there. The distances (in miles) between the cities are listed in the table below:

# Boston Chicago Dallas Denver LA Miami New
# York
# Phoenix Pittsburgh San
# Francisco
# Seattle
# Boston 0 983 1815 1991 3036 1593 213 2664 792 2385 2612
# Chicago 0 1205 1050 2112 1390 840 1729 457 2212 2052
# Dallas 0 801 1425 1332 1604 1027 1237 1765 2404
# Denver 0 1174 2041 1780 836 1411 1765 1373
# LA 0 2757 2825 398 2456 403 1909
# Miami 0 1258 2359 1250 3097 3389
# New York 0 2442 386 3036 2900
# Phoenix 0 2073 800 1482
# Pittsburgh 0 2653 2517
# San Fransisco 0 817
# Seattle 0

#The estimated annual number of trips to the various customer s are listed in the following table:
# City Annual
# Trips to
# Customers
# Boston 885
# Chicago 760
# Dallas 1124
# Denver 708
# LA 1224
# Miami 1152
# New York 1560
# Phoenix 1222
# Pittsburgh 856
# San Francisco 1443
# Seattle 612

# Develop and implement an LP solution, using binary variables that determines the locations of service centres and then assigns customers to these service centres to minimize the total annual distance travelled.

import pulp


def main():
    # Create the 'prob' variable to contain the problem data
    prob = pulp.LpProblem("Service Centre Assignment", pulp.LpMinimize)

    # Create a dictionary of the variables and set the lower and upper bounds
    x = {}
    for i in range(1, 11):
        for j in range(1, 11):
            x[i, j] = pulp.LpVariable("x_" + str(i) + "_" + str(j), cat='Binary')

    # The objective function is added to 'prob' first
    prob += pulp.lpSum([x[i, j] * distance[i, j] for i in range(1, 11) for j in range(1, 11)])

    # The constraints are entered
    for i in range(1, 11):
        prob += pulp.lpSum([x[i, j] for j in range(1, 11)]) == 1
        prob += pulp.lpSum([x[j, i] for j in range(1, 11)]) == 1

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print("Status:", pulp.LpStatus[prob.status])

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # The optimised objective function value is printed to the screen
    print("Total Distance = ", pulp.value(prob.objective))


if __name__ == '__main__':
    distance = {(1, 2): 983, (1, 3): 1815, (1, 4): 1991, (1, 5): 3036, (1, 6): 1593, (1, 7): 213, (1, 8): 2664, (1, 9): 792, (1, 10): 2385, (2, 3): 1205, (2, 4): 1050, (2, 5): 2112, (2, 6): 1390, (2, 7): 840, (2, 8): 1729, (2, 9): 457, (2, 10): 2212, (3, 4): 801, (3, 5): 1425, (3, 6): 1332, (3, 7): 1604, (3, 8): 1027, (3, 9): 1237, (3, 10): 1765, (4, 5): 1174, (4, 6): 2041, (4, 7): 1780, (4, 8): 836, (4, 9): 1411, (4, 10): 1765, (5, 6): 2757, (5, 7): 2825, (5, 8): 398, (5, 9): 2456, (5, 10): 403, (6, 7): 1258, (6, 8): 2359, (6, 9): 1250, (6, 10): 3097, (7, 8): 2442, (7, 9): 386, (7, 10): 3036, (8, 9): 2442, (8, 10): 2900, (9, 10): 817}
    main()
    print(distance)



