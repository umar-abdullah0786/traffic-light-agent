table = {
    "Red": "Stop",
    "Yellow": "Slow Down",
    "Green": "Go",
    "Flashing Red": "Stop and Proceed with Caution",
}


def traffic_light_agent(percept):
    return table.get(percept, "Unknown")


def run_agent(percept_sequence):
    print("Percept\tAction")
    for percept in percept_sequence:
        action = traffic_light_agent(percept)
        print(f"{percept}\t{action}")


if __name__ == "__main__":
    percept_sequence = ["Red", "Green", "Yellow", "Red"]
    run_agent(percept_sequence)