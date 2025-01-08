# Matplotlib Module Notes

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Below are some key points and examples from the provided `main.py` file.

## Basic Plot Configuration

The `plot_configs` function sets the title and labels for the x and y axes:
```python
def plot_configs():
  plt.title("Simple Plot")
  plt.xlabel("x-axis")
  plt.ylabel("y-axis")
```

## Line Plot and Bar Plot in Subplots

The `line_plot` function demonstrates how to create a line plot and a bar plot within subplots:
```python
def line_plot():
  x = [1, 2, 3, 4, 5]
  y = [1, 4, 9, 16, 25]
  plot_configs()

  plt.subplot(1, 4, 1)  # Line plot
  plt.plot(x, y, color="red", linestyle="--", marker="*")

  plt.subplot(1, 4, 2)  # Bar plot
  categories = ["apple", "mango", "banana", "cherry", "strawberry"]
  values = [10, 32, 12, 40, 43]
  plt.bar(categories, values)

  plt.show()
```

## Bar Plot

The `bar_plot` function creates a simple bar plot:
```python
def bar_plot():
  categories = ["apple", "mango", "banana", "cherry", "strawberry"]
  values = [10, 32, 12, 40, 43]
  plt.bar(categories, values)
  plot_configs()
  plt.show()
```

## Scatter Plot

The `scatter_plot` function creates a scatter plot:
```python
def scatter_plot():
  x = [1, 2, 3, 4, 5]
  y = [5, 4, 3, 2, 1]
  plt.scatter(x, y)
  plot_configs()
  plt.show()
```

## Histogram

The `histogram` function creates a histogram:
```python
def histogram():
  data = [1, 1, 1, 2, 2, 2, 3, 3, 1, 2, 3, 4, 4]
  plt.hist(data, bins=4)
  plt.show()
```

## Pie Chart

The `pie_chart` function creates a pie chart:
```python
def pie_chart():
  sizes = [20, 10, 35, 25, 5]
  labels = ["A", "B", "C", "D", "E"]
  plt.pie(sizes, labels=labels)
  plt.show()
```

## Execution

The `line_plot` function is called at the end of the script to execute the code:
```python
line_plot()
```

These examples cover basic plotting techniques using Matplotlib, including line plots, bar plots, scatter plots, histograms, and pie charts.