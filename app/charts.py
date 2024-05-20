import matplotlib.pyplot as plt
from datetime import datetime

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
  filename = f'chart_pie_{timestamp}.png'
  plt.savefig(f'./imgs/{filename}')
  plt.close()
  print(f'Pie chart saved as {filename}')

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)