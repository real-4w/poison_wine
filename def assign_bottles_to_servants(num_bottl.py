def assign_bottles_to_servants(num_bottles):
    """
    Assigns bottles to servants based on binary representation.
    Returns a list where each element is a set of bottle numbers for a servant.
    """
    num_servants = 10
    servants = [set() for _ in range(num_servants)]
    
    for bottle in range(num_bottles):
        # Convert bottle number to 10-bit binary string, padded with leading zeros
        binary = format(bottle, '010b')  # 10 bits, zero-padded
        # Assign bottle to servants where bit is 1
        for servant in range(num_servants):
            # Bit 0 (LSB) -> Servant 1, Bit 9 (MSB) -> Servant 10
            if binary[9 - servant] == '1':  # Read from right (LSB) to left (MSB)
                servants[servant].add(bottle)
    
    return servants

def simulate_poisoning(servants, poisoned_bottle):
    """
    Simulates which servants get sick based on the poisoned bottle.
    Returns a list of 0s and 1s (1 if sick, 0 if not).
    """
    num_servants = len(servants)
    sick_servants = [0] * num_servants
    
    for servant in range(num_servants):
        if poisoned_bottle in servants[servant]:
            sick_servants[servant] = 1
    
    return sick_servants

def identify_poisoned_bottle(sick_servants):
    """
    Identifies the poisoned bottle from the list of sick servants.
    Converts the sick pattern to a binary number and then to decimal.
    """
    # Convert sick_servants list to binary string (Servant 1 is LSB, Servant 10 is MSB)
    binary = ''.join(str(bit) for bit in sick_servants[::-1])  # Reverse to make MSB leftmost
    poisoned_bottle = int(binary, 2)  # Convert binary string to decimal
    return poisoned_bottle

def run_simulation(num_bottles, poisoned_bottle):
    """
    Runs the full simulation for a given poisoned bottle.
    """
    print(f"Simulating with {num_bottles} bottles, poisoned bottle is #{poisoned_bottle}")
    
    # Step 1: Assign bottles to servants
    servants = assign_bottles_to_servants(num_bottles)
    
    # Uncomment to verify assignments for a specific bottle
    # bottle_to_check = poisoned_bottle
    # print(f"Bottle {bottle_to_check} binary: {format(bottle_to_check, '010b')}")
    # for i, servant_set in enumerate(servants, 1):
    #     if bottle_to_check in servant_set:
    #         print(f"Servant {i} drinks from bottle {bottle_to_check}")
    
    # Step 2: Simulate poisoning after 24 hours
    sick_servants = simulate_poisoning(servants, poisoned_bottle)
    print(f"After 24 hours, sick servants (1=sick, 0=healthy): {sick_servants}")
    
    # Step 3: Identify the poisoned bottle
    identified_bottle = identify_poisoned_bottle(sick_servants)
    print(f"Identified poisoned bottle: #{identified_bottle}")
    
    # Verify correctness
    if identified_bottle == poisoned_bottle:
        print("Success! The poisoned bottle was correctly identified.")
    else:
        print("Error: Identification failed.")

# Test the simulation with a few examples
num_bottles = 1000
test_cases = [0, 1, 3, 999]  # Example poisoned bottles

for poisoned_bottle in test_cases:
    run_simulation(num_bottles, poisoned_bottle)
    print("-" * 50)