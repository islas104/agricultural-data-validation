import pandas as pd

# Define the sample dataset
data = [
    {"Field ID": "INAA100-001-01-001", "Hectares": 0.5, "Volume in KG": 300, "Volume KG per Hectare": 600},
    {"Field ID": "INAA100-001-02-001", "Hectares": 0.75, "Volume in KG": 200, "Volume KG per Hectare": 266.67},
    {"Field ID": "INAA100-001-03-001", "Hectares": 1, "Volume in KG": 280, "Volume KG per Hectare": 280},
    {"Field ID": "INAA100-001-04-001", "Hectares": 2, "Volume in KG": 500, "Volume KG per Hectare": 250},
    {"Field ID": "INAA100-001-05-001", "Hectares": 3, "Volume in KG": 850, "Volume KG per Hectare": 283.33},
    {"Field ID": "INAA100-001-06-001", "Hectares": 3.5, "Volume in KG": 427, "Volume KG per Hectare": 122},
    {"Field ID": "INAA100-001-07-001", "Hectares": 0.5, "Volume in KG": 112.5, "Volume KG per Hectare": 225},
    {"Field ID": "INAA100-001-08-001", "Hectares": 0.75, "Volume in KG": 206.25, "Volume KG per Hectare": 275},
    {"Field ID": "INAA100-001-09-001", "Hectares": 1, "Volume in KG": 250, "Volume KG per Hectare": 250},
    {"Field ID": "INAA100-001-10-001", "Hectares": 2, "Volume in KG": 450, "Volume KG per Hectare": 225},
    {"Field ID": "INAA100-001-11-001", "Hectares": 3, "Volume in KG": 0.3, "Volume KG per Hectare": 0.1},
    {"Field ID": "INAA100-001-12-001", "Hectares": 3.5, "Volume in KG": 725, "Volume KG per Hectare": 207.14},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Define expected range for KG per hectare
EXPECTED_RANGE = (200, 500)

# Function to validate data
def validate_data(row):
    errors = []
    if not (EXPECTED_RANGE[0] <= row["Volume KG per Hectare"] <= EXPECTED_RANGE[1]):
        errors.append("Volume KG per Hectare out of range")
    
    # Check if 'Volume in KG' is unrealistically small, indicating it might be in grams
    if row["Volume in KG"] < 1:  # Assuming volumes in KG should be >= 1
        errors.append("Volume in KG might be in grams")
    return errors

# Apply validation to each row
df["Errors"] = df.apply(validate_data, axis=1)

# Function to correct units
def correct_units(row):
    if "Volume in KG might be in grams" in row["Errors"]:
        row["Volume in KG"] = row["Volume in KG"] / 1000  # Convert grams to kilograms
        row["Volume KG per Hectare"] = row["Volume in KG"] / row["Hectares"]
        row["Errors"].remove("Volume in KG might be in grams")
    return row

# Apply corrections
df = df.apply(correct_units, axis=1)

# Save corrected dataset
df.to_csv("corrected_data.csv", index=False)

# Save flagged issues separately
flagged_issues = df[df["Errors"].apply(len) > 0]
flagged_issues.to_csv("flagged_issues.csv", index=False)

# Display flagged issues in a user-friendly way
print("Flagged Issues for Review:")
for index, row in flagged_issues.iterrows():
    print(f"Field ID: {row['Field ID']}, Errors: {', '.join(row['Errors'])}")

print("\nCorrected dataset saved to 'corrected_data.csv'.")
print("Flagged issues saved to 'flagged_issues.csv' for review.")
