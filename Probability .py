#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:17:03 2023

@author: Jeremy
"""

import prob_calculator
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Initialize a variable to count the successful experiments
    num_successful_experiments = 0
    
    # Perform the specified number of experiments
    for _ in range(num_experiments):
        # Create a copy of the original hat to avoid modifying it
        hat_copy = copy.deepcopy(hat)
        
        # Draw the specified number of balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Check if the drawn balls match the expected balls
        if all(drawn_balls.count(ball) >= count for ball, count in expected_balls.items()):
            num_successful_experiments += 1
    
    # Calculate the probability as the ratio of successful experiments to total experiments
    probability = num_successful_experiments / num_experiments
    
    return probability
prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)