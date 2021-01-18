import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    init_ball_dist = {}

    for i, color in enumerate(list(kwargs.keys())):
      self.add_balls_to_list(color, list(kwargs.values())[i], init_ball_dist)

    for color in init_ball_dist.keys():
      for i in range(init_ball_dist[color]):
        self.contents.append(color)

  def add_balls_to_list(self, color, amount, init_ball_dist):
    init_ball_dist[color] = amount

  def draw(self, number):
    removed_balls = []

    if number > len(self.contents):
      number = len(self.contents)

    for i in range(number):
      idx_to_remove = random.randint(0, len(self.contents)-1)
      removed_balls.append(self.contents[idx_to_remove])
      self.contents.remove(self.contents[idx_to_remove])

    return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  original_balls = hat.contents.copy()
  expected_outcomes = 0

  for i in range(num_experiments):
    outcome = True
    draw_balls_count = dict()
    hat.contents = original_balls.copy()
    drawn_balls = hat.draw(num_balls_drawn)

    for ball in drawn_balls:
      draw_balls_count[ball] = draw_balls_count.get(ball, 0) + 1

    for ball in expected_balls.keys():
      outcome = outcome and (expected_balls[ball] <= draw_balls_count.get(ball, 0))

    if outcome:
      expected_outcomes += 1

  return expected_outcomes/num_experiments
    

    

    


