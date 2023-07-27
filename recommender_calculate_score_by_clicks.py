import math
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

def calculate_score(click_count, weight_factor, hours):
    decay_factor_half_life = 40  # Adjust this value to control the rate of decay
    
    # Calculate the decay factor based on the time difference in hours
    decay_factor = math.exp(-math.log(2) * hours / decay_factor_half_life)
    
    # Calculate the score by multiplying click_count, weight_factor, and decay_factor
    score = click_count * weight_factor * decay_factor
    
    return score

# Example click count data
click_counts = {
    0: 5,
    30: 10,
    50: 20,
    60: 30,
    80: 50,
    90: 100,
    120: 200,
    140: 300,
    160: 500
}

# Other parameters
weight_factor = 2
created_date = datetime(2023, 7, 7, 12, 0, 0)  # Replace with the actual created date

# Generate data points for the chart
hours = np.arange(0, 300, 1)  # Generate data points for the first week (168 hours)

# Calculate scores for each click count and hour
click_count = 0
scores = []
for h in hours:
    if h in click_counts:
        click_count = click_counts[h]
    score = calculate_score(click_count, weight_factor, h)
    scores.append(score)

plt.plot(hours, scores)
plt.xlabel("Time (hours)")
plt.ylabel("Score")
plt.title("Scores based on Click Counts and Hours")
plt.legend()
plt.grid(True)
plt.show()