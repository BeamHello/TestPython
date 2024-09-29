import random
from utility import MarbleBag

#random.seed(10)
#for i in range(10):
#    print(int(random.uniform(0, 10)))

#print(random.choices([0, 1], weights=[0.1, 0.9]))

class Predetermination():
    def __init__(self, max_attempts) -> None:
        self.attempts = 0
        self.success_at = random.randint(1, max_attempts)
        self.max_attampts = max_attempts
    
    def attempt(self):
        self.attempts =+ 1
        if self.attempts >= self.success_at:
            self.attempts = 0
            return True
        return False

class FixedRateProb():
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

class Progressive_Prob():
    def __init__(self, success_rate, increment) -> None:
        self.base_success_rate = success_rate
        self.current_success_rate = self.base_success_rate
        self.increment = increment
    
    def reset_probability(self):
        self.current_success_rate = self.base_success_rate

    def attempt(self):
        p = random.uniform(0, 100)
        if p < self.current_success_rate:
            print(f"successful {self.current_success_rate}")
            self.reset_probability()
            return True
        else:
            self.current_success_rate += self.increment
            print(f"failed {self.current_success_rate}")
            return False


def attempt(success_rate = 50):
    assert success_rate >= 0 and success_rate <= 100, "sucess rate must be between 0-100"
    p = random.uniform(0, 100)
    base_probabolity = success_rate
    if p < base_probabolity:
        print("successful")
        return True
    else:
        print("failed")
        return False

# -------------------------------------------------------------
def main():
    #marble_random = MarbleBag([0, 1, 2, 3])
    #for i in range(10):
    #    print(marble_random.draw())

    pro = Progressive_Prob(10, 10)
    #fix = FixedRateProb(10, 3)
    #pre = Predetermination(3)
    for _ in range(2):
        #attempt()
        pro.attempt()
        #fix.attempt()
        #pre.attempt()


# -------------------------------------------------------------
if __name__ == '__main__':
    main()