import pulp
import os
import pandas as pd
import random

# -----------------------------
# Server data
# -----------------------------

servers = ["S1", "S2", "S3"]

power_cost = {
    "S1": 3,
    "S2": 5,
    "S3": 4
}

capacity = {
    "S1": 50,
    "S2": 60,
    "S3": 70
}

# -----------------------------
# Simulate hourly demand (24 hours)
# -----------------------------

hours = list(range(24))

demand_data = {
    h: random.randint(80, 150) for h in hours
}

results = []

# -----------------------------
# Optimization for each hour
# -----------------------------

for h in hours:

    demand = demand_data[h]

    model = pulp.LpProblem(f"Optimization_Hour_{h}", pulp.LpMinimize)

    x = pulp.LpVariable.dicts("load", servers, lowBound=0)

    # Objective
    model += sum(power_cost[s] * x[s] for s in servers)

    # Demand constraint
    model += sum(x[s] for s in servers) == demand

    # Capacity constraints
    for s in servers:
        model += x[s] <= capacity[s]

    model.solve()

    for s in servers:
        results.append({
            "hour": h,
            "server": s,
            "allocation": x[s].value(),
            "demand": demand
        })

# -----------------------------
# Convert results to dataframe
# -----------------------------

df = pd.DataFrame(results)

# -----------------------------
# Ensure results folder exists
# -----------------------------

os.makedirs("results", exist_ok=True)

# Save results
df.to_csv("results/hourly_optimization_results.csv", index=False)

print("Optimization completed for 24 hours")
print("Results saved to results/hourly_optimization_results.csv")