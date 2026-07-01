import sys


def get_inventory() -> None:
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            key, value_str = arg.split(":")
            if key in inventory:
                print(f"Redundant item {key} - discarding")
            else:
                value = int(value_str)
                inventory[key] = value
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
    if len(inventory) == 0:
        print("No items provided")
        return
    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    print(f"Total quantity of the {len(inventory.keys())} items: {total}")
    for key in inventory:
        percent = float(inventory[key] / total * 100)
        print(f"Item {key} represents: {round(percent, 1)}%")

    def quantity(item: str) -> int:
        return inventory[item]

    most = max(inventory, key=quantity)
    least = min(inventory, key=quantity)
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"legendary_useless_item": 1})
    print(f"Updated inventory:{inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    get_inventory()
    print()
