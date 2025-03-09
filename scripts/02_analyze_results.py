import pandas as pd
import numpy as np
import os

def analyze_simulation_results(file_path):
    df = pd.read_csv(file_path)
    trials = len(df)
    crossings = sum(df["x_tip1_region"] != df["x_tip2_region"])

    pi_estimate = (2 * 1.0 * trials) / (2.0 * crossings) if crossings else None
    confidence_interval = 1.96 * (np.sqrt((pi_estimate ** 2) / trials))

    summary = {
        "Trials": trials,
        "Crossings": crossings,
        "Estimated Pi": pi_estimate,
        "Confidence Interval": (pi_estimate - confidence_interval, pi_estimate + confidence_interval)
    }
    
    return summary

if __name__ == "__main__":
    file_path = "../outputs/simulation_results.csv"
    summary = analyze_simulation_results(file_path)
    
    os.makedirs("../outputs", exist_ok=True)
    pd.DataFrame([summary]).to_csv("../outputs/analysis_summary.csv", index=False)

    print(summary)
