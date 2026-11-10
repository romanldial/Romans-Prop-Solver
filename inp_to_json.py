# Converts NASA thermo.inp into thermo.json

import json

def read_lines(path):
    with open(path) as f:
    for lines in f:
        if line.startswith("!"):
            continue
        clean = line.rstrip("\n") 
        line.append(clean)
    return lines

lines = read_lines("init/thermo.inp")
print(len(lines))
print(lines[0:3])

# ---------- Step 2: turn "1.23D+04" into a number ----------
def to_float(text):
    # replace "D" with "E"
    # convert to float and return it
    pass


# ---------- Step 3: parse ONE species ----------
# lines = the full list of lines
# start = index of this species' name line
# returns two things: the species dict, and the index
#         where the NEXT species starts
def parse_species(lines, start):
    # name_line = lines[start]
    # info_line = lines[start + 1]
    #
    # name       = first word of name_line
    # n_ranges   = int   of info_line[0:2]
    # phase      = int   of info_line[50:52]
    # molar_mass = float of info_line[52:65]
    # hf298      = float of info_line[65:80]
    #
    # ranges = empty list
    # i = start + 2        (first range header line)
    # repeat n_ranges times:
    #     header = lines[i]
    #     coef1  = lines[i + 1]
    #     coef2  = lines[i + 2]
    #
    #     t_min = float of header[0:11]
    #     t_max = float of header[11:22]
    #
    #     a1..a5 = to_float of coef1, 16 chars each:
    #              [0:16] [16:32] [32:48] [48:64] [64:80]
    #     a6, a7 = to_float of coef2[0:16] and coef2[16:32]
    #     (coef2[32:48] is the blank gap, skip it)
    #     b1, b2 = to_float of coef2[48:64] and coef2[64:80]
    #
    #     add {"t_min", "t_max", "a": [a1..a7], "b": [b1, b2]}
    #         to ranges
    #     i = i + 3        (jump to the next range)
    #
    # if n_ranges == 0:
    #     some reactants have one extra line instead of
    #     ranges; we'll look at these later
    #     i = start + 3
    #
    # species = {"name", "phase", "molar_mass", "hf298", "ranges"}
    # return species, i
    pass


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
