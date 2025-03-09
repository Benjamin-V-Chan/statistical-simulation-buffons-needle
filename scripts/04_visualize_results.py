import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_simulation_results(file_path):
    df = pd.read_csv(file_path)
    
    plt.figure(figsize=(8, 6))
    plt.hist(df["theta"], bins=50, alpha=0.75)
    plt.xlabel("Theta (radians)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Needle Angles")
    plt.grid(True)

    os.makedirs("../outputs", exist_ok=True)
    plt.savefig("../outputs/needle_angle_distribution.png")

if __name__ == "__main__":
    file_path = "../outputs/simulation_results.csv"
    plot_simulation_results(file_path)
