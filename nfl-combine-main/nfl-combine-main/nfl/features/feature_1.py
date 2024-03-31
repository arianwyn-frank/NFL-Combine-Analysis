import pandas as pd
from transform import transform_data
import matplotlib.pyplot as plt
import seaborn as sns

def filter_data():
    merged_data = transform_data()
    columns_to_drop = ['Pos', 'School', 'Position', 'Team', 'TotalFantasyPoints', 'TotalPprFantasyPoints', 'FantasyPointsPerGame',
       'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)
    return merged_data

def get_qb_data():
    merged_data = transform_data()
    columns_to_drop = ['Pos', 'School', 'Team', 'TotalFantasyPoints', 'TotalPprFantasyPoints', 'FantasyPointsPerGame', 'PprFantasyPointsPerGame', 'Player', 'DraftedTeam']
    merged_data.drop(columns=columns_to_drop, inplace=True)

    # Filter to include only QBs
    qb_data = merged_data[merged_data['Position'] == 'QB']
    qb_data.drop(columns='Position', inplace=True)

    return qb_data

if __name__ == "__main__":
    # Get the filtered data
    filtered_data = filter_data()

    # Compute the correlation matrix
    corr_matrix_all = filtered_data.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr_matrix_all, annot=True, fmt=".2f", cmap='coolwarm')

    # Show the plot
    plt.show()
    plt.savefig('correlation_heatmap.png')

    # Get the filtered data for QBs
    qb_data = get_qb_data()

    # Compute the correlation matrix
    corr_matrix_qb = qb_data.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr_matrix_qb, annot=True, fmt=".2f", cmap='coolwarm')

    # Show the plot
    plt.show()
    plt.savefig('correlation_heatmap_QBs.png')

    #print(filtered_data.columns)