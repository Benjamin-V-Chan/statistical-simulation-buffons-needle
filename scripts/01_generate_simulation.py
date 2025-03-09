import numpy as np
import pandas as pd
import os

def buffon_needle_simulation(trials, needle_length=1.0, line_spacing=2.0, seed=None):
    if seed is not None:
        np.random.seed(seed)

    crossings = 0
    results = []

    for _ in range(trials):
        x_center = np.random.uniform(0, line_spacing / 2)  # Needle center position
        theta = np.random.uniform(0, np.pi)  # Random angle

        x_tip1 = x_center + (needle_length / 2) * np.cos(theta)
        x_tip2 = x_center - (needle_length / 2) * np.cos(theta)

        if int(x_tip1 / line_spacing) != int(x_tip2 / line_spacing):  # Check if it crosses a line
            crossings += 1
        
        results.append([x_center, theta, int(x_tip1 / line_spacing), int(x_tip2 / line_spacing)])

    pi_estimate = (2 * needle_length * trials) / (line_spacing * crossings) if crossings else None
    return results, pi_estimate

if __name__ == "__main__":
    trials = 10000
    results, pi_value = buffon_needle_simulation(trials)

    df = pd.DataFrame(results, columns=["x_center", "theta", "x_tip1_region", "x_tip2_region"])
    
    os.makedirs("../outputs", exist_ok=True)
    df.to_csv("../outputs/simulation_results.csv", index=False)

    print(f"Estimated π: {pi_value}")
