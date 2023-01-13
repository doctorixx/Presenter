from serial.tools import list_ports


def getCOM() -> str:
    coms = list_ports.comports()
    print("Select COM from list: \n")
    print(*coms, sep="\n")

    return input(">>> ")
