import pickle
import pandas as pd

# Load the trained SVM regression model
model_svm = pickle.load(open('path_to_your_svm_model.pkl', 'rb'))

# Get user input for diamond details
carat = float(input("Enter carat: "))
cut = input("Enter cut (e.g., 'Ideal', 'Premium', 'Very Good', 'Good', 'Fair'): ")
color = input("Enter color (e.g., 'D', 'E', 'F', 'G', 'H', 'I', 'J'): ")
clarity = input("Enter clarity (e.g., 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'): ")
depth = float(input("Enter depth: "))
table = float(input("Enter table: "))

# Create a DataFrame from user inputs
input_data = {
    'carat': [carat],
    'cut': [cut],
    'color': [color],
    'clarity': [clarity],
    'depth': [depth],
    'table': [table]
}

input_df = pd.DataFrame(input_data)

# Make predictions using the SVM model
predicted_price = model_svm.predict(input_df)

# Display the predicted diamond price
print(f"The predicted price for the diamond is: ${predicted_price[0]:.2f}")
