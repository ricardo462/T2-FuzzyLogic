# Decision suport system
class DSS:
    def __init__(self, rules):
        self.rules = rules

    def __call__(self, basckets, height, time) -> float:
        r1 = self.rules[0](basckets, height)
        r2 = self.rules[1](basckets, time  )
        r3 = self.rules[1](height,   time  )

        return (max(max(r1, r2), r3))