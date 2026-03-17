def buy(x, o):
    full_rent = o - 1470
    half_rent = o - 490
    if (x == 1):
        return full_rent
    if (x == 2):
        return half_rent
        
        
def asterite(x, a, r):
    radiant_tide = r * 160
    total_asterite_amount = radiant_tide + a
    total_pull_amount = (a / 160) + r
    if (x == 1):
        return total_asterite_amount
    if (x == 2):
        return total_pull_amount

def afterglow_coral(ac):
    afterglow_to_radiant_tide = ac / 8
    return afterglow_to_radiant_tide

current_asterite = 8770
current_radiant_tides = 5
current_oscillated_coral = 690
current_afterglow_coral = 25

print(f"you will have {buy(1, current_oscillated_coral)} left after fully buying out the oscillated coral shop")
print(f"you will have {buy(2, current_oscillated_coral)} left after partially buying out the oscillated coral shop")
print(f"you have a total of {asterite(1, current_asterite, current_radiant_tides)} which will make {asterite(2, current_asterite, current_radiant_tides)} gacha pulls!")
print(f"if you decide to use your afterglow corals, you can buy {afterglow_coral(current_afterglow_coral)} more pulls, totalling {(afterglow_coral(current_afterglow_coral) + asterite(2, current_asterite, current_radiant_tides))} pulls!")