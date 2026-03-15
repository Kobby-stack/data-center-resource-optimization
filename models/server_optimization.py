import pulp

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

demand = 120

model = pulp.LpProblem("DataCenterOptimization", pulp.LpMinimize)

x = pulp.LpVariable.dicts("load", servers, lowBound=0)

model += sum(power_cost[s] * x[s] for s in servers)

model += sum(x[s] for s in servers) == demand

for s in servers:
    model += x[s] <= capacity[s]

model.solve()
# Save results to file
with open("results/optimization_results.txt", "w") as f:
    f.write("Optimal Server Workload Allocation\n\n")

    for s in servers:
        result = f"{s}: {x[s].value()}\n"
        print(result)
        f.write(result)

    total_cost = pulp.value(model.objective)

    f.write(f"\nTotal Power Cost: {total_cost}")
    print("\nTotal Power Cost:", total_cost)

print("Optimal Allocation")

for s in servers:
    print(s, x[s].value())
