import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    # Load the data
    data = pd.read_csv(input_file)

    # Validate input
    if data.shape[1] < 3:
        raise Exception("Input file must have at least three columns (Identifier and Criteria).")

    # Extract matrix and names
    criteria = data.iloc[:, 1:].values  # Exclude the first column (Fund Name)
    names = data.iloc[:, 0].values  # First column (Fund Name)

    # Convert weights and impacts to lists
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    # Check for matching dimensions
    if len(weights) != criteria.shape[1] or len(impacts) != criteria.shape[1]:
        raise Exception("Number of weights and impacts must match the number of criteria.")

    # Normalize the decision matrix
    norm_criteria = criteria / np.sqrt((criteria**2).sum(axis=0))

    # Apply weights
    weighted_criteria = norm_criteria * weights

    # Determine ideal best and ideal worst
    ideal_best = [max(weighted_criteria[:, i]) if impacts[i] == '+' else min(weighted_criteria[:, i]) for i in range(len(impacts))]
    ideal_worst = [min(weighted_criteria[:, i]) if impacts[i] == '+' else max(weighted_criteria[:, i]) for i in range(len(impacts))]

    # Calculate distances
    distance_best = np.sqrt(((weighted_criteria - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_criteria - ideal_worst) ** 2).sum(axis=1))

    # Calculate performance scores
    scores = distance_worst / (distance_best + distance_worst)

    # Rank the alternatives
    data['Topsis Score'] = scores
    data['Rank'] = data['Topsis Score'].rank(ascending=False)

    # Save the results to a CSV file
    data.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

# To run the script interactively in Colab
if __name__ == "__main__":
    # Modify these parameters as needed
    input_file = "102203621-data.csv"  # Your input file name
    weights = "1,1,1,1,1"  # Provide weights (one for each criterion)
    impacts = "+,+,+,+,+"  # Provide impacts (one for each criterion)
    output_file = "102203621-result.csv"  # Desired output file name

    # Call the function
    topsis(input_file, weights, impacts, output_file)
