import numpy as np
import pandas as pd
import os

def monte_carlo_buffon(trials, distribution="uniform", seed=None):
    if seed is not None:
        np.random.seed(seed)

    crossings = 0
    results = []

    for _ in range(trials):
        if distribution == "uniform":
            x_center = np.random.uniform(0, 1)
        elif distribution == "normal":
            x_center = np.abs(np.random.normal(0.5, 0.2))
        elif distribution == "exponential":
            x_center = np.random.exponential(0.5)

        theta = np.random.uniform(0, np.pi)
        x_tip1 = x_center + 0.5 * np.cos(theta)
        x_tip2 = x_center - 0.5 * np.cos(theta)

        if int(x_tip1 / 1.0) != int(x_tip2 / 1.0):
            crossings += 1

        results.append([x_center, theta, int(x_tip1 / 1.0), int(x_tip2 / 1.0)])

    pi_estimate = (2 * 1.0 * trials) / (1.0 * crossings) if crossings else None
    return results, pi_estimate

if __name__ == "__main__":
    trials = 10000
    distribution = "normal"
    results, pi_value = monte_carlo_buffon(trials, distribution)

    df = pd.DataFrame(results, columns=["x_center", "theta", "x_tip1_region", "x_tip2_region"])
    
    os.makedirs("../outputs", exist_ok=True)
    df.to_csv(f"../outputs/monte_carlo_{distribution}.csv", index=False)

    print(f"Estimated π ({distribution}): {pi_value}")
