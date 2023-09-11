def teploty(tep):
    if "f" in tep.lower():
        tep = round(float(tep[:-1]),1)
        c = (tep-32)/1.8
        if round(tep) == tep:
            print(f"{int(tep)}F = {round(c,1)}C")
        else:
            print(f"{tep}F = {round(c,1)}C")
    elif "c" in tep.lower():
        tep = round(float(tep[:-1]),1)
        f = (tep*1.8)+32
        if round(tep) == tep:
            print(f"{int(tep)}C = {round(f,1)}F")
        else:
            print(f"{tep}C = {round(f,1)}F")
    else:
        print("Toto prekonvertovat neviem.")

teploty("45F")
teploty("37.6257C")
teploty("2 c")
teploty("157 f")
teploty("157 K") 

