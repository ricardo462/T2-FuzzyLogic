# Decision suport system
from model.Premise import Premise
from model.Rule import Rule

class DSS:
    def __init__(self, membership_functions, certains, threshold = 0.8):
        self.premises = [Premise(fuzzy_set) for fuzzy_set in membership_functions]
        self.rules = [Rule(certain) for certain in certains]
        self.threshold = threshold

    def __call__(self, baskets, height, time) -> float:
        baskets_ = self.premises[0](baskets)
        height_ = self.premises[1](height)
        time_ = self.premises[2](time)
        stats = [baskets_, height_, time_]
        #print(f' values: {baskets, height, time}')

        r1 = self.rules[0].feed(baskets_, height_)
        r2 = self.rules[1].feed(baskets_, time_  )
        r3 = self.rules[1].feed(height_,   time_  )
        
        text = ''
        
        b, h, t = round(baskets_, 2), round(height_, 2), round(time_, 2)
        if stats[0] >= self.threshold:
            text += f'\n Se evaluó como buen encestador, con un valor de certeza {b} (anotó {baskets} canastas)'

        if stats[1] >= self.threshold:
            text += f'\n Se evaluó como alto, con un valor de certeza {h} (mide {height} cm)'

        if stats[2] >= self.threshold:
            text += f'\n Se evaluó como rápido, con un valor de certeza {t} (demoró {time} s)'
        
        if text == '':
            text = f'El jugador no posee ninguna estadística mayor a {self.threshold} (Encestador: {b}, Altura: {h}, Tiempo{t})' 

        return (max(max(r1, r2), r3)), text