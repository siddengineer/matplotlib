# 📊 When Line Chart is Used

# A line chart is used when you want to show how values change over time or across a continuous range.

# ✅ Common Use Cases:

# Trends over time

# Example: Stock prices each day, monthly sales growth, daily temperatures.

# Comparing changes

# Plot multiple lines to compare two or more datasets.

# Example: Comparing website traffic between two months.

# Showing progress or growth

# Example: Number of students enrolled each year, weight loss tracking.

# Continuous data visualization

# Example: Sensor readings, population growth, rainfall over days.

# 📌 Example Situations

# Business → Showing revenue increasing month by month.

# Education → Student test scores improving across exams.

# Health → Tracking patient’s blood pressure over weeks.

# Weather → Temperature changes throughout a day.

# ⚖️ When NOT to Use a Line Chart

# If the data is categorical (like colors, fruits, cities) → use a bar chart or pie chart instead.

# If you only want to show totals, not trends.

# 👉 So, line charts are best for trend analysis and for showing relationships between numbers across a continuous scale (like time or measurements).


# line_chart_plot.py

import matplotlib.pyplot as plt

def plot_line_chart(x, y, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
    """
    Function to plot a simple line chart.
    
    Parameters:
        x (list): Values for the X-axis
        y (list): Values for the Y-axis
        title (str): Title of the chart
        xlabel (str): Label for the X-axis
        ylabel (str): Label for the Y-axis
    """
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Data Line")
    
    # Add labels and title
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Grid + Legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    # Show chart
    plt.show()

    plt.savefig("chart.png")
if __name__ == "__main__":
    # Example data
    x_values = [1, 2, 3, 4, 5, 6, 7]
    y_values = [2, 5, 8, 6, 10, 12, 15]
    
    # Plot the line chart
    plot_line_chart(x_values, y_values, title="Sample Line Chart", xlabel="Days", ylabel="Values")
    