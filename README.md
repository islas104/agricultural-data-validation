# Data Validation and Correction Script

## Overview
This script processes agricultural field data, identifies inconsistencies in input values, and applies corrections where necessary. The main objectives are to:

- Flag data inconsistencies (e.g., values outside expected ranges, incorrect units).
- Correct errors (e.g., converting grams to kilograms).
- Save corrected data and flagged issues for further review.

The solution is designed to be user-friendly and provides actionable insights for partners and farmers.

## Features

1. **Validation of Input Data**:
   - Checks if `Volume KG per Hectare` falls outside the expected range (200-500).
   - Identifies rows where `Volume in KG` may be incorrectly reported in grams (values < 1).

2. **Automatic Corrections**:
   - Converts `Volume in KG` from grams to kilograms when flagged.
   - Recalculates `Volume KG per Hectare` after corrections.

3. **Outputs**:
   - **Corrected Data**: Saved to `corrected_data.csv`.
   - **Flagged Issues**: Rows with errors are saved separately in `flagged_issues.csv` for easy review.

4. **User-Friendly Console Output**:
   - Displays flagged issues in a readable format, including `Field ID` and specific errors.


## Installation

1. Clone this repository or copy the script to your local machine.
2. Ensure Python is installed on your system.
3. Install the required libraries:
   ```bash
   pip install pandas
   ```

## Usage

1. Place the script (`data_validation.py`) in your working directory.
2. Run the script using the following command:
   ```bash
   python data_validation.py
   ```
3. After execution, the script generates the following files:
   - **`corrected_data.csv`**: Contains the full dataset with corrections applied.
   - **`flagged_issues.csv`**: Contains rows with errors for further review.

## Example Output

### Console Output:
```
Flagged Issues for Review:
Field ID: INAA100-001-01-001, Errors: Volume KG per Hectare out of range
Field ID: INAA100-001-06-001, Errors: Volume KG per Hectare out of range
Field ID: INAA100-001-11-001, Errors: Volume KG per Hectare out of range

Corrected dataset saved to 'corrected_data.csv'.
Flagged issues saved to 'flagged_issues.csv' for review.
```

### `corrected_data.csv` Example:
| Field ID            | Hectares | Volume in KG | Volume KG per Hectare | Errors                                  |
|---------------------|----------|--------------|------------------------|-----------------------------------------|
| INAA100-001-01-001 | 0.5      | 300.0        | 600.0                  | ['Volume KG per Hectare out of range'] |
| INAA100-001-02-001 | 0.75     | 200.0        | 266.67                | []                                      |
| INAA100-001-11-001 | 3.0      | 0.0003       | 0.0001                | ['Volume KG per Hectare out of range'] |

### `flagged_issues.csv` Example:
| Field ID            | Hectares | Volume in KG | Volume KG per Hectare | Errors                                  |
|---------------------|----------|--------------|------------------------|-----------------------------------------|
| INAA100-001-01-001 | 0.5      | 300.0        | 600.0                  | ['Volume KG per Hectare out of range'] |
| INAA100-001-06-001 | 3.5      | 427.0        | 122.0                  | ['Volume KG per Hectare out of range'] |

1. **Adjust Expected Range**:
   Modify the `EXPECTED_RANGE` variable in the script to change the acceptable range for `Volume KG per Hectare`.
   ```python
   EXPECTED_RANGE = (200, 500)
   ```

2. **Expand Validation Rules**:
   Add more validation checks by extending the `validate_data` function.

## Limitations

- Assumes input data is in the correct structure (e.g., columns like `Field ID`, `Hectares`, `Volume in KG`).
- Does not handle missing or malformed data.

## Future Enhancements

1. Develop a web-based interface for users to view and correct flagged issues interactively.
2. Integrate the solution with a database for real-time corrections.
3. Add support for multilingual error descriptions.

## Contact
For questions or support, please contact **Islas Ahmed Nawaz** at `islas104@gmail.com`.
