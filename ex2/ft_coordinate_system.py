import math

def get_player_pos() -> None:
    coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        x, y , z = coordinates.split(",")
        x = float(x)
        y = float(y)
        z = float(z)
        print(f"Got a first tuple: {coordinates}")
        print(f"It includes: X={x}, Y={y}, Z={z}")
        from_center = round(math.sqrt(x**2 + y**2 + z**2), 4)
        print(f"Distance to center: {from_center}\n")
        get_2nd_pos(x, y, z)
    except ValueError:
        print ("Invalid syntax")
        get_player_pos()

def get_2nd_pos( x: float, y: float, z:float ) -> None:
    print("Get a second set of coordinates")
    coordinates2 = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        x2, y2 , z2 = coordinates2.split(",")
        x2 = float(x2)
        y2 = float(y2)
        z2 = float(z2)
        from_first = round(math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2), 4)
        print(f"Distance between the 2 sets of coordinates: {from_first}\n")
    except ValueError:
        print ("Invalid syntax")
        get_2nd_pos(x, y, z)

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    get_player_pos()



