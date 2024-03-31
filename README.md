# nfl-combine

**Abstract**
Question: Does the NFL Combine help predict the quality of an NFL prospect?
Hypothesis: the Combine will help predict the career statistics but not the career lifespan.

We want to predict the career performance and lifespan of professional athletes, specifically focusing on football players, using a Multivariable Regression and Correlation Matrix analysis. We believe that a player's NFL Combine performance metrics, such as their speed, strength, agility, and endurance, can provide valuable insights into their performance and longevity in the sport. By collecting and analyzing historical data on player Combine performances and their career trajectories, we intend to develop a predictive model that can estimate the potential duration and performance of a player's career. 

**Repository:**

**Data Files in WUSTL Box**
- Combine Data
    - Includes the data of every player's NFL Combine performance since 2000. Some helpful features include player name, weight, vertical, bench, broad jump, 40-yard dash, and drafting details. Players did not necessarily have to be drafted to be included in this dataset; they only had to participate in the combine. The dataset includes 7999 players.
- Fantasy PPR
    - Includes the data of 10,000 players' performances throughout their NFL careers, since 1920. Features include player name, fantasy PPR points per game, age, and career length. We chose to use fantasy PPR points per game to determine how successful a player's career is because it is a relatively standardized metric that can help determine a player's value, regardless of their position. See [this](https://www.rookieroad.com/fantasy-football/how-does-scoring-work/) page to learn more about how Fantasy PPR Scoring works. 


**Functions**
- *extract.py*
    - This function reads in the master CSV from the WUSTL Box API. This will automatically be run when any features are called.
- *transform.py*
    - This function gets the CSV from the *extract.py* function and then cleans the data. It does this by filtering the datasets to only include matching players, and then merges the two data frames to make one data frame called "merged_data". This will automatically be run when any features are called. 
- *feature_1.py*
      - This feature generates and visualizes correlation matrices showing the relationships between combine performance metrics and career performance for NFL players, with the capability to filter the analysis based on specific player positions. 
- *feature_2.py*
    - This feature utilizes a linear regression model to predict the length of an NFL player's career, based on various combine performance metrics, and includes functionality for training, making predictions, and evaluating the model's performance.
- *feature_3.py*
    - Similar to feature 2, this feature employs a linear regression model to predict the total fantasy points an NFL player might accumulate, based on combine data, and comes with comprehensive model training, prediction, and evaluation capabilities.
- *load.py*
    - This function loads the transformed data from *transform.py* into a csv file that can be downloaded by the user for external use.

**Jupyter Notebook Playground:**
Overview

This Jupyter Notebook provides an interactive platform for analyzing NFL players' performance. It allows users to explore correlation matrices for player performance metrics and make predictions based on NFL Combine data. The notebook is designed to be user-friendly, offering intuitive controls for data input and visualization.

*Features:*
Feature 1: Position-Specific Correlation Matrices

- *Interactive Correlation Analysis:*
    - Users can select a specific player position (like 'QB', 'RB', 'WR', etc.) from a dropdown menu to generate a correlation matrix. This matrix visualizes the relationships between combine performance metrics and career performance for players in the selected position.
- *Flexible Data Exploration:*
    - An option to select 'All' positions is available for users who wish to analyze data across all positions.
    - Player Count Display: Upon generating a correlation matrix, the notebook displays the number of players included in the analysis for the selected position, providing context to the visualization.

Features 2 and 3: Career Lifespand and Player Pefromance Prediction Calculator

    Player Performance Prediction: This feature allows users to input specific combine performance data such as weight ('Wt'), 40-yard dash time ('40yd'), vertical jump height ('Vertical'), etc.
    Customizable Input Fields: Users can enter player data into designated fields and submit it to receive predictions.
    Two Prediction Models:
        Career Length Prediction: Based on the input data, the notebook predicts the number of years a player is likely to play (originally Feature 2).
        Fantasy Points Prediction: Alternatively, it predicts the total fantasy points a player might accumulate (originally Feature 3).
    Model Insights: After submitting the data, users receive immediate predictive insights displayed directly in the notebook.

How to Use:
    Select a Feature: Choose between correlation analysis and performance prediction.
    Input Data: For correlation analysis, select a position. For performance and lifespan prediction, fill in the player's combine data.
    View Results: Visualize the correlation matrix or receive predictions based on the model.
