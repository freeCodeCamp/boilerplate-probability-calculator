
import random



class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = Hat(**dict(hat.contents))  # Create a copy of the original hat for each experiment
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls match the expected_balls
        drawn_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        if all(drawn_count.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

