import math

def get_player_pos() -> tuple:
    coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        x, y , z = coordinates.split(",")
        x = float(x)
        y = float(y)
        z = float(z)
    except ValueError:
        print ("Invalid syntax")
        get_player_pos()
    print(f"Got a first tuple: {coordinates}")

if __name__ == "__main__":
    get_player_pos()
