import numpy as np
import matplotlib.pyplot as plt

# Step 1: Dataset
X = np.array([500, 800, 1000, 1200, 1500])
y = np.array([10, 15, 20, 24, 30])

# Step 2: Calculate mean
X_mean = np.mean(X)
y_mean = np.mean(y)

# Step 3: Calculate slope (m) and intercept (b)
numerator = np.sum((X - X_mean) * (y - y_mean))
denominator = np.sum((X - X_mean) ** 2)

m = numerator / denominator
b = y_mean - m * X_mean

print("Model trained successfully!")
print("Slope (m):", m)
print("Intercept (b):", b)

# Step 4: User input
new_size = float(input("Enter house size in sqft: "))
predicted_price = m * new_size + b

print("Predicted Price:", round(predicted_price, 2), "lakhs")

# Step 5: Generate prediction line
prediction_line = m * X + b

# Step 6: Create graph
plt.scatter(X, y)
plt.plot(X, prediction_line)
plt.scatter(new_size, predicted_price)  # mark predicted point

plt.xlabel("House Size (sqft)")
plt.ylabel("Price (lakhs)")
plt.title("House Price Prediction Model")

# Step 7: Save image file
plt.savefig("house_price_prediction.png")

print("Image generated successfully!")
print("Check your project folder for: house_price_prediction.png")

plt.show()
