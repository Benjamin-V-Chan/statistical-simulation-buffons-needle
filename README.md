# statistical-simulation-buffons-needle

## Project Overview

Buffon's Needle is a classical probability problem that estimates the value of $\pi$ by dropping needles on a plane with parallel lines and calculating the proportion that cross the lines. Our project extends this experiment by applying Monte Carlo simulations, analyzing convergence rates, and incorporating various probability distributions.



## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_generate_simulation.py   # Runs Buffon's Needle trials
│   ├── 02_analyze_results.py       # Computes statistics
│   ├── 03_monte_carlo_variation.py # Simulates with different distributions
│   ├── 04_visualize_results.py     # Creates graphs
├── outputs/                        # Stores results
│   ├── simulation_results.csv
│   ├── analysis_summary.csv
│   ├── monte_carlo_normal.csv
│   ├── needle_angle_distribution.png
├── requirements.txt                 # Python dependencies
├── README.md                         # Project documentation
```

## Usage

### 1. Setup the Project:

Clone the repository. Ensure you have Python installed. Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

### 2. Run Buffon's Needle Simulation:
Run the simulation with 10,000 trials and store results in `outputs/simulation_results.csv`:
```sh
python scripts/01_generate_simulation.py
```

### 3. Analyze Simulation Results:
Compute estimated $\pi$ and statistical properties:
```sh
python scripts/02_analyze_results.py
```

### 4. Run Monte Carlo Variants:
Test Buffon’s Needle under different probability distributions:
```sh
python scripts/03_monte_carlo_variation.py
```

### 5. Visualize Results:
Generate plots for analysis:
```sh
python scripts/04_visualize_results.py
```

## Requirements

- Python 3.7+
- Required libraries (installed via `requirements.txt`):
  - numpy
  - pandas
  - matplotlib
  - seaborn