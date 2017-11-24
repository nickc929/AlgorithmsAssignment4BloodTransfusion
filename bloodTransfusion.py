supply = {
'O'  : 50,
'A'  : 36,
'B'  : 11,
'AB' : 8
}

demand = {
'O'  : 45,
'A'  : 42,
'B'  : 8,
'AB' : 3
}

def bloodTransfusion(supplyInput, demandInput):
    supply = supplyInput
    demand = demandInput
    print("supply =", supply)
    print("demand =", demand)

    # Is there enough type O blood for the type O patients
    if supply['O'] - demand['O'] < 0:
        supply['O'] -= demand['O']
        print("Not enough type O blood.")
        if supply['O'] == -1:
            print("1 more unit of type O blood required.")
        else:
            print(abs(supply['O']), "more units of type O blood required.")
        demand['O'] = abs(supply['O'])
        supply['O'] = 0
    else:
        supply['O'] -= demand['O']
        demand['O'] = 0

    # Is there enough type A blood or leftover type O blood for the type A patients
    if supply['A'] - demand['A'] < 0:
        demand['A'] -= supply['A']
        supply['A'] = 0
        if supply['O'] - demand['A'] < 0:
            supply['O'] -= demand['A']
            print("Not enough type A blood.")
            if supply['O'] == -1:
                print("1 more unit of type A or O blood required.")
            else:
                print(abs(supply['O']), "more units of type A or O blood required.")
            demand['A'] = abs(supply['O'])
            supply['O'] = 0
        else:
            supply['O'] -= demand['A']
            demand['A'] = 0
    else:
        supply['A'] -= demand['A']
        demand['A'] = 0

    # Is there enough type B blood or leftover type O blood for the type B patients
    if supply['B'] - demand['B'] < 0:
        demand['B'] -= supply['B']
        supply['B'] = 0
        if supply['O'] - demand['B'] < 0:
            supply['O'] -= demand['B']
            print("Not enough type B blood.")
            if supply['O'] == -1:
                print("1 more unit of type A, B, or O blood required.")
            else:
                print(abs(supply['O']), "more units of type A, B, or O blood required.")
            demand['B'] = abs(supply['O'])
            supply['O'] = 0
        else:
            supply['O'] -= demand['B']
            demand['B'] = 0
    else:
        supply['B'] -= demand['B']
        demand['B'] = 0

    # Is there enough type A blood or leftover type A, B, or O blood for the type AB patients
    if supply['AB'] - demand['AB'] < 0:
        demand['AB'] -= supply['AB']
        supply['AB'] = 0
        if supply['B'] - demand['AB'] < 0:
            demand['AB'] -= supply['B']
            supply['B'] = 0
            if supply['A'] - demand['AB'] < 0:
                demand['AB'] -= supply['A']
                supply['A'] = 0
                if supply['O'] - demand['AB'] < 0:
                    supply['O'] -= demand['AB']
                    print("Not enough type AB blood.")
                    if supply['O'] == -1:
                        print("1 more unit of type A, B, AB, or O blood required.")
                    else:
                        print(abs(supply['O']), "more units of type A, B, AB, or O blood required.")
                    demand['AB'] = abs(supply['O'])
                    supply['O'] = 0
            else:
                supply['A'] -= demand['AB']
                demand['AB'] = 0
        else:
            supply['B'] -= demand['AB']
            demand['AB'] = 0
    else:
        supply['AB'] -= demand['AB']
        demand['AB'] = 0

    print("Remaining blood supply:", supply)
    print("Remaining blood demand:", demand)
    print('')
    return supply, demand

bloodTransfusion(supply, demand)
bloodTransfusion(supplyInput = {'O'  : 40, 'A'  : 37, 'B'  : 8, 'AB' : 8} ,
                 demandInput = {'O'  : 45, 'A'  : 37, 'B'  : 8, 'AB' : 30})
bloodTransfusion(supplyInput = {'O'  : 50, 'A'  : 37, 'B'  : 8, 'AB' : 8} ,
                 demandInput = {'O'  : 45, 'A'  : 39, 'B'  : 10, 'AB' : 5})
