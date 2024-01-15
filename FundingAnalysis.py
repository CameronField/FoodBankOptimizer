import pandas as pd
import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt

# --------------- User-defined Parameters --------------- #
D = 50  # Maximum distance a person can travel from their home to a pantry in miles.
Budget = 1000000  # Total budget for the network.
Cost_per_meal_per_mile = 0.006  # Average cost per mile to transport food from a bank to a pantry.
Meals_Per_Person = 20 #Over a two week period, how many meals are given/served to that person
Minimum_Meals_Per_Pantry = 100  # Set the minimum number of meals to be delivered to each pantry

High_Risk = 0.5 #Minimum Proportion of FI population fed by food network for high risk counties
Medium_Risk = 0.30 #Minimum Proportion of FI population fed by food network for medium risk counties
Low_Risk = 0.2 #Minimum Proportion of FI population fed by food network for low risk counties

# Read the input data from the CSV files
banks_df = pd.read_csv('MSBankLatLong.csv')
pantries_df = pd.read_csv('MSPantryLatLong.csv')
demand_df = pd.read_csv('MS_City_Demand.csv')
bank_to_pantry_distance_df = pd.read_csv('BankToPantryDistanceMatrix.csv', index_col=0)
pantry_to_demand_distance_df = pd.read_csv('PantryToCityDistanceMatrix.csv', index_col=0)
county_risk_df = pd.read_csv("CountyRisk.csv", index_col=0)

def map_risk_to_p_min(risk):
    if risk == 'High':
        return High_Risk
    elif risk == 'Medium':
        return Medium_Risk
    elif risk == 'Low':
        return Low_Risk
    else:
        return None  # In case the risk is not one of the specified categories

# Apply the function to the 'Risk' column to create the 'P_Min' column
county_risk_df['P_Min'] = county_risk_df['Risk'].apply(map_risk_to_p_min)

# Display the updated dataframe
county_risk_df.head()

def FI_Satisfied_vs_Budget(Budget):    
    # Initialize the model
    model = gp.Model("Food_Distribution_Optimization")

    # Decision Variables

    # x_bp: Amount of food delivered from bank b to pantry p.
    x_bp = model.addVars(banks_df['Name'], pantries_df['Name'], vtype=GRB.INTEGER, name="x_bp")


    # y_pc: Amount of FI persons fed from pantry p to demand node c.
    y_pc = model.addVars(pantries_df["Name"], demand_df["City"], vtype=GRB.INTEGER, name="y_pc")

    # Constraints

    # Distance constraint for pantries
    model.addConstrs((pantry_to_demand_distance_df.loc[p, c]*y_pc[p,c] <= D*y_pc[p,c] for p in pantries_df['Name'] for c in demand_df['City']), name='pantry_distance')


    # Aggregate food insecure population by county
    county_fi_population_df = demand_df.groupby('County')['FI Population 2025'].sum()

    # P_min constraint: Each county must have at least its specified P_min percent of its food insecure people fed
    for county in county_fi_population_df.index:
        total_fi_population = county_fi_population_df.loc[county]
        p_min_for_county = county_risk_df.loc[county, 'P_Min']
        model.addConstr(gp.quicksum(y_pc[p, c] for p in pantries_df['Name'] for c in demand_df[demand_df['County'] == county]['City']) >= p_min_for_county * total_fi_population, name=f'P_min_constraint_{county}')
        
    # Budget constraint
    total_transport_cost = gp.quicksum(x_bp[b, p] * bank_to_pantry_distance_df.loc[b, p] * Cost_per_meal_per_mile 
                                    for b in banks_df['Name'] for p in pantries_df['Name'])
    meal_cost_df = demand_df[['City', '2025 Cost Per Meal']].set_index('City')
    total_procurement_cost = gp.quicksum(y_pc[p, c] * meal_cost_df.loc[c, '2025 Cost Per Meal'] 
                                        for p in pantries_df['Name'] for c in demand_df['City'])

    total_cost = total_transport_cost + total_procurement_cost
    model.addConstr(total_cost <= Budget, name='budget')

    # Meals per person constraint
    for p in pantries_df['Name']:
        for c in demand_df['City']:
            model.addConstr(y_pc[p, c] * Meals_Per_Person <= x_bp.sum('*', p), name=f'meals_per_person_constraint_{p}_{c}')

    # Maximum FI population fulfillment constraint for each city
    for c in demand_df['City']:
        fi_population = demand_df.loc[demand_df['City'] == c, 'FI Population 2025'].iloc[0]
        model.addConstr(gp.quicksum(y_pc[p, c] for p in pantries_df['Name']) <= fi_population, name=f'max_fulfillment_constraint_{c}')

    # Max capacity constraint for each pantry
    for p in pantries_df['Name']:
        max_capacity = pantries_df.loc[pantries_df['Name'] == p, 'Capacity'].iloc[0]
        model.addConstr(gp.quicksum(x_bp[b, p] for b in banks_df['Name']) <= max_capacity, name=f'max_capacity_constraint_{p}')

    # Minimum meal delivery constraint for each pantry
    for p in pantries_df['Name']:
        model.addConstr(gp.quicksum(x_bp[b, p] for b in banks_df['Name']) >= Minimum_Meals_Per_Pantry, name=f'min_meal_delivery_constraint_{p}')

    # Supply and demand constraint
    model.addConstrs((gp.quicksum(y_pc[p, c] for c in demand_df['City']) <= gp.quicksum(x_bp[b, p] for b in banks_df['Name']) for p in pantries_df['Name']), name='supply_demand')

    # Non-negativity constraint
    model.addConstrs((x_bp[b, p] >= 0 for b in banks_df['Name'] for p in pantries_df['Name']), name='non-negativity_x')
    model.addConstrs((y_pc[p, c] >= 0 for p in pantries_df['Name'] for c in demand_df['City']), name='non-negativity_y')

    # Objective Function
    model.setObjective(gp.quicksum(y_pc[p, c] for p in pantries_df['Name'] for c in demand_df["City"]), GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    return model.ObjVal

budgets = [850000, 860000, 870000, 880000, 890000, 900000, 950000, 1000000, 1100000, 1200000, 1300000, 1400000,1500000, 1600000, 1700000, 1800000, 1900000, 2000000,
           2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000]
FI_served = []

for budget in budgets:
    FI_served.append(FI_Satisfied_vs_Budget(budget))

# Creating the plot
plt.plot(budgets, FI_served)

# Adding titles and labels
plt.title('FI Population Fed vs Bi-Weekly Operations Budget')
plt.xlabel('Bi-weekly Operations Budget')
plt.ylabel('Food Insecure Population Fed')

# Displaying the plot
plt.show()
