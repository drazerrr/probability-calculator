import copy
import random
# Consider using the modules imported above.

class Hat:
  """Represents a hat with balls of different colors.
  
  A hat has a list of balls, each of which has a color and a count. The hat has
  a method ball_colors that returns a list of all of the ball colors in the hat.
  A hat has a method balls that returns a list of all of the balls in the hat.
  A hat has a method draw that returns a random ball from the hat. If the hat
  is empty, the method should raise an exception.
  """

  def __init__(self, **kwargs):
    """Initializes a new hat with a list of balls.
    
    Each ball is represented by a color and a count. The ball color is a string
    and the ball count is an integer.
    
    Args:
      **kwargs: A dictionary of ball colors and their counts.
    """
    self.contents = []
    for color, count in kwargs.items():
      for i in range(count):
        self.contents.append(color)

  def draw(self, number):
    """Returns a random ball from the hat.
    
    If the hat is empty, the method should raise an exception.
    
    Args:
      number: The number of balls to draw.
    
    Returns:
      A random ball from the hat.
    """
    if number > len(self.contents):
      return self.contents
    drawn_balls = []
    for i in range(number):
      drawn_balls.append(random.choice(self.contents))
      self.contents.remove(drawn_balls[i])
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    for ball in drawn_balls:
      if ball in expected_copy:
        expected_copy[ball] -= 1
    if(all(x <=0 for x in expected_copy.values())):
      count += 1
  return count/num_experiments
  
