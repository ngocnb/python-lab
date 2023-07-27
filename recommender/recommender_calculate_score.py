import math
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the score based on logarithmic decay
def calculate_score(created_date, half_life, hour_diff):
    max_score = 100
    
    # Convert the created_date to a datetime object
    created_date = datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
    
    # Calculate the new datetime by subtracting the hour difference from the created_date
    new_date = created_date - timedelta(hours=int(hour_diff))
    
    # Calculate the time difference in hours between the new_date and the created_date
    time_diff_hours = (created_date - new_date).total_seconds() / 3600
    
    # Apply the logarithmic decay formula to calculate the score
    score = max_score * math.exp(-math.log(2) * time_diff_hours / half_life)
    
    return score

# Generate data points for the chart
created_date = "2023-07-01 00:00:00"
half_life = 30
hours = np.arange(0, 168, 1)  # Generate data points for the first week (168 hours)
scores = [calculate_score(created_date, half_life, h) for h in hours]

# Plot the chart
plt.plot(hours, scores)
plt.xlabel("Hour Difference")
plt.ylabel("Score")
plt.title("Score Decay Over Time")
plt.grid(True)
plt.show()

# Calculate and print the scores to the console
for h in hours:
    score = calculate_score(created_date, half_life, h)
    print(f"Hour Diff: {h}, Score: {score}")