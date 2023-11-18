from serial.tools import list_ports


def getCOM() -> str:
    coms = list_ports.comports()
    print("Select COM from list: \n")
    print(*coms, sep="\n")

    if len(coms) == 1:
        print(f"Auto Selected : {coms[0]}")
        return coms[0].device
    elif len(coms) == 0:
        print("NO COMs")
        exit()

    return input(">>> ")
