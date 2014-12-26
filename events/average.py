# Averaging class



xs = []



def add_sample(x) :
  xs.append(x)


def calculate():
  reduce(lambda x, y: x+y, xs) / xs.count()
