import numpy as np
import matplotlib.pyplot as plt

# Define a data structure to hold information for beverages and fuels
items = {
    'Liquor': {'type': 'beverage', 'alcohol_content': 40, 'calories_per_100ml': 250},
    'Wine': {'type': 'beverage', 'alcohol_content': 12, 'calories_per_100ml': 85},
    'Beer': {'type': 'beverage', 'alcohol_content': 5, 'calories_per_100ml': 43},
    'Cider': {'type': 'beverage', 'alcohol_content': 6, 'calories_per_100ml': 50},
    'Vodka': {'type': 'beverage', 'alcohol_content': 40, 'calories_per_100ml': 231},
    'Sake': {'type': 'beverage', 'alcohol_content': 15, 'calories_per_100ml': 134},
    'Tequila': {'type': 'beverage', 'alcohol_content': 40, 'calories_per_100ml': 231},
    'Gin': {'type': 'beverage', 'alcohol_content': 37.5, 'calories_per_100ml': 263},
    'Whiskey': {'type': 'beverage', 'alcohol_content': 40, 'calories_per_100ml': 250},
    'Champagne': {'type': 'beverage', 'alcohol_content': 12, 'calories_per_100ml': 85},
    'Gasoline': {'type': 'fuel', 'energy_content': 34.2, 'carbon_emissions_per_mj': 2.31},  # MJ/L, kg CO2/MJ
    'Diesel': {'type': 'fuel', 'energy_content': 38.6, 'carbon_emissions_per_mj': 2.68},
    'Natural Gas': {'type': 'fuel', 'energy_content': 35.8, 'carbon_emissions_per_mj': 2.75},
    'Ethanol': {'type': 'fuel', 'energy_content': 24.0, 'carbon_emissions_per_mj': 1.94},
    'Hydrogen': {'type': 'fuel', 'energy_content': 120.0, 'carbon_emissions_per_mj': 0.0}
}

# Function to compare alcohol content for beverages
def compare_alcohol_content(items):
    for name, properties in items.items():
        if properties['type'] == 'beverage':
            print(f"{name}: {properties['alcohol_content']}% alcohol")

# Function to compare calories for beverages
def compare_calories(items):
    for name, properties in items.items():
        if properties['type'] == 'beverage':
            print(f"{name}: {properties['calories_per_100ml']} calories per 100ml")

# Function to compare energy content for fuels
def compare_energy_content(items):
    for name, properties in items.items():
        if properties['type'] == 'fuel':
            print(f"{name}: {properties['energy_content']} MJ/L")

# Function to compare carbon emissions for fuels
def compare_carbon_emissions(items):
    for name, properties in items.items():
        if properties['type'] == 'fuel':
            print(f"{name}: {properties['carbon_emissions_per_mj']} kg CO2/MJ")

# Function to plot comparisons
def plot_comparisons(items):
    beverages = {name: properties for name, properties in items.items() if properties['type'] == 'beverage'}
    fuels = {name: properties for name, properties in items.items() if properties['type'] == 'fuel'}

    # Plot beverages
    beverage_names = list(beverages.keys())
    alcohol_content = [properties['alcohol_content'] for properties in beverages.values()]
    calories = [properties['calories_per_100ml'] for properties in beverages.values()]
    
    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:red'
    ax1.set_xlabel('Beverage')
    ax1.set_ylabel('Alcohol Content (%)', color=color)
    ax1.bar(beverage_names, alcohol_content, color=color, alpha=0.6, label='Alcohol Content')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Calories per 100ml', color=color)
    ax2.plot(beverage_names, calories, color=color, marker='o', label='Calories')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Comparison of Alcohol Content and Calories in Beverages')
    plt.show()

    # Plot fuels
    fuel_names = list(fuels.keys())
    energy_content = [properties['energy_content'] for properties in fuels.values()]
    carbon_emissions = [properties['carbon_emissions_per_mj'] for properties in fuels.values()]
    
    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:green'
    ax1.set_xlabel('Fuel')
    ax1.set_ylabel('Energy Content (MJ/L)', color=color)
    ax1.bar(fuel_names, energy_content, color=color, alpha=0.6, label='Energy Content')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Carbon Emissions (kg CO2/MJ)', color=color)
    ax2.plot(fuel_names, carbon_emissions, color=color, marker='o', label='Carbon Emissions')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Comparison of Energy Content and Carbon Emissions in Fuels')
    plt.show()

# Compare alcohol content for beverages
print("Alcohol Content Comparison for Beverages:")
compare_alcohol_content(items)
print("\nCalories Comparison for Beverages:")
compare_calories(items)

# Compare energy content for fuels
print("\nEnergy Content Comparison for Fuels:")
compare_energy_content(items)
print("\nCarbon Emissions Comparison for Fuels:")
compare_carbon_emissions(items)

# Plot the comparisons
plot_comparisons(items)
