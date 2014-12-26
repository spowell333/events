# Averaging class

class Average:
  def __init__(self):
    self.xs = []


  def add_sample(self, x) :
    self.xs.append(x)


  def calculate(self):
    return sum(self.xs) / len(self.xs)


