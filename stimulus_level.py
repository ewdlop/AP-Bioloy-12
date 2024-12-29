import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for dopamine, serotonin, and hormone
parameters = {
    'dopamine': {'stimulus_intensity': 1.0, 'baseline_secretion': 0.2, 'decay_rate': 0.1},
    'serotonin': {'stimulus_intensity': 0.8, 'baseline_secretion': 0.3, 'decay_rate': 0.05},
    'hormone': {'stimulus_intensity': 0.5, 'baseline_secretion': 0.1, 'decay_rate': 0.02}
}

time_steps = 100  # Number of time steps to simulate
time_interval = 0.1  # Time interval between steps

# Initialize levels for each substance
levels = {key: np.zeros(time_steps) for key in parameters}
time_points = np.arange(0, time_steps * time_interval, time_interval)

# Function to model secretion
def secretion_model(stimulus, baseline, decay, time_steps):
    levels = np.zeros(time_steps)
    for t in range(1, time_steps):
        # Secretion increases with stimulus and decays over time
        levels[t] = levels[t-1] + stimulus * baseline - decay * levels[t-1]
    return levels

# Calculate levels for each substance using the model
for substance, params in parameters.items():
    levels[substance] = secretion_model(params['stimulus_intensity'], params['baseline_secretion'], params['decay_rate'], time_steps)

# Plot the results
plt.figure(figsize=(10, 6))
for substance, level in levels.items():
    plt.plot(time_points, level, label=f"{substance.capitalize()} Levels")
plt.xlabel("Time")
plt.ylabel("Level")
plt.title("Simulation of Dopamine, Serotonin, and Hormone Secretion Over Time")
plt.legend()
plt.grid(True)
plt.show()
