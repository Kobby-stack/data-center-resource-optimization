import pandas as pd
import matplotlib.pyplot as plt
import os

# Load optimization results
df = pd.read_csv("results/hourly_optimization_results.csv")

# Pivot data for visualization
pivot_df = df.pivot(index="hour", columns="server", values="allocation")

# Plot server workload over time
pivot_df.plot(kind="line", marker="o")

plt.title("Server Workload Allocation Over 24 Hours")
plt.xlabel("Hour of Day")
plt.ylabel("Allocated Workload")
plt.grid(True)

# Ensure results directory exists
os.makedirs("results", exist_ok=True)

# Save visualization
plt.savefig("results/server_workload_visualization.png")

plt.show()

print("Visualization saved to results/server_workload_visualization.png")