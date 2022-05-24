import matplotlib.pyplot as plt
import numpy

order = {0:0.0, 1:1.0, 2:1.0, 3:0.0}

def membresy(value: float, fuzzy_set:list) -> float:
    if value < fuzzy_set[0]:
        if fuzzy_set[0] == fuzzy_set[1]:
            return 1.0
        else:
            return 0.0

    if value > fuzzy_set[3]:
        if fuzzy_set[3] == fuzzy_set[2]:
            return 1.0
        else: 
            return 0.0

    
    




def pertenencia(value: float, fuzzy_set:list) -> float :
    if len(fuzzy_set) == 0:
        return 0
    if fuzzy_set[0] == fuzzy_set[1] and value <= fuzzy_set[0]:
        return 1
    if fuzzy_set[2] == fuzzy_set[3] and value >= fuzzy_set[3]:
        return 1

    if value >fuzzy_set[3] or value < fuzzy_set[0]:
        return 0

    lenght = len(fuzzy_set)
    for i in range(lenght - 1):
        value_set = fuzzy_set[i]
        if value == value_set:
            return order[i]
        
        next_value_set = fuzzy_set[i+1]
        if value_set < value and value < next_value_set:
            m = (order[i+1] - order[i]) / (next_value_set - value_set)
            return m * (value - value_set) + order[i]
    if value == next_value_set:
        return order[i+1]


def d_a(fuzzy_set_1:list , fuzzy_set_2:list) -> list:
    result = []
    for i in range(2):
        element_1, element_2 = fuzzy_set_1[i], fuzzy_set_2[i]
        element = element_1 if element_1 <= element_2 else element_2
        result.append(element)

    for i in range(2,4):
        element_1, element_2 = fuzzy_set_1[i], fuzzy_set_2[i]
        element = element_1 if element_1 > element_2 else element_2
        result.append(element)
    return result

def plot_rule(e1: list, e2:list, rule_number:int):
    y = [0, 1.0, 1.0, 0]
    plt.figure()
    plt.plot(e1, y, label='E1')
    plt.plot(e2, y, label='E2')
    plt.title(f'Regla {rule_number}')
    plt.ylabel('Grado de pertenencia')
    plt.grid()
    plt.legend()
    plt.show()

def get_rules(e1, e2):
    ng = [-1.0, -1.0, -0.7, -0.5]
    np = [-0.7, -0.5, -0.2, 0]
    ce = [-0.2, 0, 0, 0.2]
    pp = [0.0, 0.2, 0.5, 0.7]
    pg = [0.5, 0.7, 1.0, 1.0]
    rules = []

    #Regla 1
    if e1 <= 0 and e2 <=0:
        rules += [pg]
    
    #Regla 2
    if -0.7 <= e1 and e2 <= -0.5:
        rules += [pg]

    #Regla 3 
    if e1 >= 0 and -0.7 <= e2 <= 0:
        rules += [pp]

    #Regla 4 
    if -0.2 <= e1 <= 0.2 and -0.7 <= e2 <= 0:
        rules += [ce]

    #Regla 5 
    if -0.2 <= e1 <= 0.2 and 0 <= e2 <= 0.7: 
        rules += [ce]

    #Regla 6
    if e1 <= 0 and 0 <= e2 <= 0.7:
        rules += [np]

    #Regla 7
    if e1 <= 0.7 and e2 <= -0.5:
        rules += [ng]

    #Regla 8
    if 0 <= e1 and 0 <= e2:
        rules += [ng]

    return rules


def unir_reglas(rules):
    if len(rules) == 0:
        return []
    rule = rules[0]
    while len(rules) >1:
        rule = d_a(rules[0], rules[1])
        rules.pop(0)
    return rule 

def centro_de_gravedad(regla, num_points=41):
    values = []
    X = numpy.linspace(-1, 1, num_points)
    for x in X:
        #print(x, regla, pertenencia(x, regla))
        values += [pertenencia(x, regla)*x]
    
    values = numpy.array(values)
    return values.sum()
    

def maquina_de_inferencia(e1, e2):
    rules = get_rules(e1, e2)
    regla = unir_reglas(rules)
    return centro_de_gravedad(regla)