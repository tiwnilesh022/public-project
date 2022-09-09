#Tesla manufactures cars in three plants and then ships them to four regions of the country as follows:
# Region 1 Region 2 Region 3 Region 4 Capacity
# Plant 1 $131 $218 $266 $120 450
# Plant 2 $250 $116 $263 $278 600
# Plant 3 $178 $132 $122 $180 500
# Demand 450 200 300 300

# A plant’s capacity is listed in the rightmost column, while a regions demand is represented in the bottom
# row. The unit costs to ship one vehicle from each plant to each region are listed in the middle.


# Unit Production Cost Tax Rate
# Plant 1 $14,350 30%
# Plant 2 $16,270 35%
# Plant 3 $16,940 22%

# Unit Selling Price
# Region 1 $19,290
# Region 2 $20,520
# Region 3 $17,570
# Region 4 $18,320

# For example, if Plant 1 produces an auto and ships it to Region 2, the before tax profit will be the unit’s
# selling price in the Region, less the production costs from the Plant, less the shipping costs from the
# Plant to the Region (= $20,520 - $14,350 - $218 = $5,952). Since it was produced at Plant 1, the
# applicable after-tax profit would be; $5,952*(1-30%) = $4,166.40

# Develop an LP optimization model that finds the cheapest way of shipping the automobiles from the plants to the regions that stays within the plant’s capacities while also meeting regional demands. The objective is to minimize the total cost of shipping the automobiles.
# The model should use binary variables to represent the assignment of automobiles to regions.


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
        for j in range(1, 11):
            prob += x[i, j] <= capacity[i]
            prob += x[i, j] <= demand[j]
            prob += x[i, j] >= 0

    # The problem data is written to an .lp file
    prob.writeLP("service_centre_assignment.lp")

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print("Status:", pulp.LpStatus[prob.status])

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # The optimised objective function value is printed to the screen
    print("Total Cost of Shipping = ", pulp.value(prob.objective))


if __name__ == '__main__':
    main()

