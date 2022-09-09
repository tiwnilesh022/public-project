#Enactus is a GBC student run business that has staffing requirements for different numbers of students on different days of the week.
# Day of the Week Minimum Number of Students Required
# Monday             17
# Tuesday           13
# Wednesday         15
# Thursday          19
# Friday            14
# Saturday          16
# Sunday            11

# Develop an LP model that relates five-day shift schedules to daily numbers of students available and implement a solution to find a schedule that uses the fewest number of students and meets all daily workforce requirements.


import pulp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_model(data):
    """
    Creates a pulp model for the LP problem.
    """
    model = pulp.LpProblem("Enactus", pulp.LpMinimize)
    # Create variables
    x = pulp.LpVariable.dicts("x", (data.index, data.columns), 0, 1, pulp.LpInteger)
    # Create objective function
    model += pulp.lpSum([x[i][j] * data.loc[i, j] for i in data.index for j in data.columns])
    # Create constraints
    for i in data.index:
        for j in data.columns:
            model += x[i][j] <= data.loc[i, j]
    return model


def solve_model(model):
    """
    Solves the pulp model.
    """
    model.solve()
    return model.variables()


def get_solution(variables):
    """
    Gets the solution from the pulp model.
    """
    solution = pd.DataFrame(index=variables.keys(), columns=variables.keys())
    for i in variables.keys():
        for j in variables.keys():
            solution.loc[i, j] = variables[i][j].varValue
    return solution


def get_solution_values(solution):
    """
    Gets the solution values from the pulp model.
    """
    solution_values = pd.DataFrame(index=solution.index, columns=solution.columns)
    for i in solution.index:
        for j in solution.columns:
            solution_values.loc[i, j] = solution.loc[i, j].varValue
    return solution_values


def get_solution_values_rounded(solution):
    """
    Gets the solution values from the pulp model, rounded to the nearest integer.
    """
    solution_values = pd.DataFrame(index=solution.index, columns=solution.columns)
    for i in solution.index:
        for j in solution.columns:
            solution_values.loc[i, j] = int(round(solution.loc[i, j].varValue))
    return solution_values


def main():
    """
    Main function.
    """
    # Read in data
    data = pd.read_csv("data.csv")
    # Create model
    model = create_model(data)
    # Solve model
    variables = solve_model(model)
    # Get solution
    solution = get_solution(variables)
    # Get solution values
    solution_values = get_solution_values(solution)
    # Get solution values rounded to nearest integer
    solution_values_rounded = get_solution_values_rounded(solution)
    # Print solution
    print(solution_values)
    # Print solution rounded to nearest integer
    print(solution_values_rounded)
    # Plot solution
    sns.heatmap(solution_values, annot=True, fmt="d")
    plt.show()
    # Plot solution rounded to nearest integer
    sns.heatmap(solution_values_rounded, annot=True, fmt="d")
    plt.show()


if __name__ == "__main__":
    main()

