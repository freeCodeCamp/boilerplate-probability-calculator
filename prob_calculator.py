import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    self.ball_dist = {}

    for i, color in enumerate(list(kwargs.keys())):
      self.add_balls_to_list(color, list(kwargs.values())[i])

    for color in self.ball_dist.keys():
      for i in range(self.ball_dist[color]):
        self.contents.append(color)

  def add_balls_to_list(self, color, amount):
    self.ball_dist[color] = amount

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass
