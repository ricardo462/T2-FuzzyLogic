class Rule:
    def __init__(self, premises, certain):
        self.premises = premises
        self.certain = certain

    def __call__(self, value_premise_1: float, value_premise_2: float) -> float:
        print(self.premises[0](value_premise_1), self.premises[1](value_premise_2))
        return min(self.premises[0](value_premise_1), self.premises[1](value_premise_2)) * self.certain 
