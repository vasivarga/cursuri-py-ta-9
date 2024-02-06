def sir_numere_pare(range_end, range_begin=0, range_step=1):
    for i in range(range_begin, range_end, range_step):
        if i % 2 == 0:
            print(f"Numarul {i} este par")

sir_numere_pare(21)
print("--------------------")

sir_numere_pare(21, range_begin=10)
print("--------------------")

sir_numere_pare(210, range_begin=20, range_step=3)