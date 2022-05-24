class Rule:
    def __init__(self, certain):
        self.certain = certain

    def __call__(self, value_premise_1: float, value_premise_2: float) -> float:
        
        return min(self.premises[0](value_premise_1), self.premises[1](value_premise_2)) * self.certain 

    def feed(self, membresy_1, membresy_2):
        return min(membresy_1, membresy_2) * self.certain