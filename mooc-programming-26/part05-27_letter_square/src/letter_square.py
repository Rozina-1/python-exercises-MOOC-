def square_pattern(alphabet:dict, layer: int):
    if layer == 1:
        print(alphabet[layer])
        return
    half_part(alphabet, layer)
    n = layer
    while layer > 0:
        print(alphabet[layer], end="")
        layer -= 1
    half_part(alphabet, n)
    half_part()
    
def half_part(alphabet:dict, layer: int):
    n = layer
    if n



alphabet = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q",
            18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
square_pattern(1)