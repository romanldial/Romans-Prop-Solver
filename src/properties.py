# properties file

import json
import math


# load the data
def load_data(path):
    with open(path) as file:
        return json.load(file)

DATA = load_data("src/thermo.json")


# find a species by name
def get_species(name):
    if name not in DATA:
        raise ValueError("S P E C I E S   N O T   F O U N D :   " + name)
    species = DATA[name]
    return species


# get temp range for a species
def get_temp_range(species, T):
    for rng in species["ranges"]:
        if rng["t_min"] <= T <= rng["t_max"]:
            return rng
        else:
            raise ValueError("T E M P  N O T   I N   R A N G E :   " + str(T))

        
# NASA 9 Cp Equation J/(mol*K)
def nasa9_cp(species, T):
    R = 8.314462618 # J/(mol*K)
    rng = get_temp_range(get_species(species), T)
    a1, a2, a3, a4, a5, a6, a7 = rng["a"]
    
    cp = ( (a1 * T**-2) + (a2 * T**-1) + a3 + (a4 * T) + (a5 * T**2) + (a6 * T**3) + (a7 * T**4 ) )  * R

    return cp


# NASA 9 H Equation J/mol
def nasa9_H(species, T):
    R = 8.314462618 # J/(mol*K)
    rng = get_temp_range(get_species(species), T)
    a1, a2, a3, a4, a5, a6, a7 = rng["a"]

    H = ( (-a1 * T**-2) + (a2 * math.log(T) / T) + a3 + (a4 * T / 2) + (a5 * T**2 / 3) + (a6 * T**3 / 4) + (a7 * T**4 / 5) + (rng["b"][0] / T) ) * (R * T)

    return H 







# testing
data = load_data("src/thermo.json")
print(nasa9_cp("N", 300))
print(nasa9_cp("CO2", 298.15))
print(nasa9_H("CO2", 298.15))


