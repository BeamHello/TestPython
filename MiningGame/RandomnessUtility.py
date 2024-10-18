import random

class Marblebag_random():
    def __init__(self, origin_box) -> None:
        self.box = []
        self.origin_box = origin_box

    def render(self):
        if not self.box:
            self.box = self.origin_box.copy()
            random.shuffle(self.box)
        return self.box.pop()

class Progressive_random():
    def __init__(self, success_rate, increment) -> None:
        self.base_success_rate = success_rate
        self.current_success_rate = self.base_success_rate
        self.increment = increment
        self.probability = None
    
    def reset_probability(self):
        self.current_success_rate = self.base_success_rate

    def attempt(self):
        self.probability = random.uniform(0, 100)
        if self.probability < self.current_success_rate:
            self.reset_probability()
            return True
        else:
            self.current_success_rate += self.increment
            return False

class FixedRate_random():
    def __init__(self, probability, fixed_success_rate) -> None:
        self.attempt_count = 0
        self.fixed_success_rate = fixed_success_rate
        self.base_probability = probability
    
    def attempt(self):
        self.attempt_count += 1
        if self.attempt_count >= self.fixed_success_rate:
            self.attempt_count = 0
            return True
        
        roll = int(random.uniform(0, 100))
        if roll < self.base_probability:
            self.attempt_count = 0
            return True
        else:
            return False

class Predetermination_random():
    def __init__(self, max_attempts) -> None:
        self.attempts = 0
        self.max_attempts = max_attempts
    
    def attempt(self):
        self.attempts += 1
        if self.attempts >= self.max_attempts:
            self.attempts = 0
            return True
        return False

