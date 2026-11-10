# Converts NASA thermo.inp into thermo.json

import json


# read the lines in the inp file
def read_lines(path):
    lines = []
    with open(path) as f:
        for line in f:
            if line.startswith("!"):
                continue
            clean = line.rstrip("\n") 
            lines.append(clean)
    return lines

# convert data to a floating point number
def to_float(text):
    text= text.replace("D", "E")
    return float(text)


# parse a species in the inp file based on its formatting
#
# Species record in thermo.inp (2 + 3*n_ranges lines):
#
#    name line:  first word = name
#    info line:  [0:2] n_ranges  [50:52] phase  [52:65] molar mass  [65:80] hf298
#       
#    per range:
#        header:   [0:11] t_min  [11:22] t_max
#        coef1:    a1-a5, 16 chars each
#        coef2:    a6 a7 [blank] b1 b2, 16 chars each
def parse_species(lines, start):
    name_line = lines[start]
    info_line = lines[start + 1]
    
    name = name_line.split()[0]
    n_ranges = int(info_line[0:2])
    phase = int(info_line[50:52])
    molar_mass = float(info_line[52:65])
    hf298 = float(info_line[65:80])
    
    ranges = []
    i = start + 2 
    for k in range(n_ranges): 
        header = lines[i]
        coef1  = lines[i + 1]
        coef2  = lines[i + 2]
    
        t_min = to_float(header[0:11])
        t_max = to_float(header[11:22])
    
        a1 = to_float(coef1[0:16])
        a2 = to_float(coef1[16:32])
        a3 = to_float(coef1[32:48])
        a4 = to_float(coef1[48:64])
        a5 = to_float(coef1[64:80])

        a6 = to_float(coef2[0:16])
        a7 = to_float(coef2[16:32])

        b1 = to_float(coef2[48:64])
        b2 = to_float(coef2[64:80])

        rng = {
            "t_min": t_min,
            "t_max": t_max,
            "a": [a1, a2, a3, a4, a5, a6, a7],
            "b": [b1, b2],
        }
        ranges.append(rng)
        i = i + 3 
    
    if n_ranges == 0:
        i = start + 3
    
    species = {
        "name": name,
        "phase": phase,
        "molar_mass": molar_mass,
        "hf298": hf298,
        "ranges": ranges,
    }
    return species, i



# ---------- Step 4: parse the whole file ----------
def parse_all(lines):
    # data = empty dictionary
    # i = 2   (after skipping ! lines, lines[0] is "thermo"
    #          and lines[1] is the overall temperature line)
    # section = "product"
    #
    # while i < number of lines:
    #     line = lines[i]
    #     if line starts with "END PRODUCTS":
    #         section = "reactant"
    #         i = i + 1
    #         go back to the top of the loop
    #     if line starts with "END REACTANTS":
    #         stop the loop
    #
    #     species, i = parse_species(lines, i)
    #     add section to species
    #     if species name is already in data: print a warning
    #     data[species name] = species
    #
    # return data
    pass


# ---------- Step 5: write the JSON ----------
def write_json(data, path):
    # open path for writing
    # json.dump the data into it (indent=2 makes it readable)
    pass


# ---------- Run it ----------
# lines = read_lines("thermo.inp")
# data  = parse_all(lines)
# write_json(data, "thermo.json")
# print how many species were written
