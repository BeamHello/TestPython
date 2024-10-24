import random

class MarbleBag:
    def __init__(self, bag) -> None:
        self.bag = bag

    def draw(self):
        if not self.bag:
            #self.bag = original_bag.copy()
            random.shuffle(self.bag)
        return self.bag.pop()

#original_bag = [0, 1, 2, 3]