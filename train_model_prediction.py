import numpy as np
import matplotlib.pyplot as plt

# Step 1: User input
n = int(input("Enter number of houses: "))
noise_level = float(input("Enter prediction error level (example 10000): "))

# Step 2: Generate actual prices
actual_prices = np.linspace(100000, 500000, n)

# Step 3: Generate predicted prices with noise
np.random.seed(42)
predicted_prices = actual_prices + np.random.normal(0, noise_level, n)

# Step 4: Create figure
plt.figure(figsize=(12, 5))

# ---- Plot 1: Actual vs Predicted ----
plt.subplot(1, 2, 1)
plt.scatter(actual_prices, predicted_prices)
plt.plot(actual_prices, actual_prices, linestyle='--')

plt.title("Actual vs Predicted")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")

# ---- Plot 2: Price Distribution ----
plt.subplot(1, 2, 2)
plt.hist(actual_prices, bins=20)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.tight_layout()

# Step 5: Save image
plt.savefig("generated_house_analysis.png")

print("Image generated successfully!")
print("Saved as: generated_house_analysis.png")

plt.show()
