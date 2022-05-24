class Premise:
    def __init__(self, fuzzy_set):
        self.fuzzy_set = fuzzy_set
        self.order = {0:0.0, 1:1.0, 2:1.0, 3:0.0}


    def __call__(self, value: float) -> float:
        if len(self.fuzzy_set) == 0:
            return 0
        if self.fuzzy_set[0] == self.fuzzy_set[1] and value <= self.fuzzy_set[0]:
            return 1
        if self.fuzzy_set[2] == self.fuzzy_set[3] and value >= self.fuzzy_set[3]:
            return 1

        if value >self.fuzzy_set[3] or value < self.fuzzy_set[0]:
            return 0

        lenght = len(self.fuzzy_set)
        for i in range(lenght - 1):
            value_set = self.fuzzy_set[i]
            if value == value_set:
                return self.order[i]
            
            next_value_set = self.fuzzy_set[i+1]
            if value_set < value and value < next_value_set:
                m = (self.order[i+1] - self.order[i]) / (next_value_set - value_set)
                return m * (value - value_set) + self.order[i]
        if value == next_value_set:
            return self.order[i+1]