import matplotlib.pyplot as plt

# Function to configure plot titles and labels
def plot_configs():
  plt.title("Simple Plot")
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")

# Function to create a line plot and a bar plot in a subplot
def line_plot():
  x = [1, 2, 3, 4, 5]
  y = [1, 4, 9, 16, 25]
  plot_configs()

  # Create the first subplot with a line plot
  plt.subplot(1, 4, 1)  # 1 row, 4 columns, 1st plot
  plt.plot(x, y, color="red", linestyle="--", marker="*")

  # Create the second subplot with a bar plot
  plt.subplot(1, 4, 2)
  categories = ["apple", "mango", "banana", "cherry", "strawberry"]
  values = [10, 32, 12, 40, 43]
  plt.bar(categories, values)

  # Display the plots
  plt.show()  

# Function to create a bar plot
def bar_plot():
  categories = ["apple", "mango", "banana", "cherry", "strawberry"]
  values = [10, 32, 12, 40, 43]
  plt.bar(categories, values)
  plot_configs()
  plt.show()

# Function to create a scatter plot
def scatter_plot():
  x = [1, 2, 3, 4, 5]
  y = [5, 4, 3, 2, 1]
  plt.scatter(x, y)
  plot_configs()
  plt.show()

# Function to create a histogram
def histogram():
  data = [1, 1, 1, 2, 2, 2, 3, 3, 1, 2, 3, 4, 4]
  plt.hist(data, bins=4)
  plt.show()

# Function to create a pie chart
def pie_chart():
  sizes = [20, 10, 35, 25, 5]
  labels = ["A", "B", "C", "D", "E"]
  plt.pie(sizes, labels=labels)
  plt.show()

# Call the line_plot function to execute the code
line_plot()