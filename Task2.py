
print("=== Stress and Strain Analysis System ===")

# predefined materials
materials = {
    "1": {"name": "Steel", "yield_strength": 250e6},
    "2": {"name": "Aluminum", "yield_strength": 150e6},
    "3": {"name": "Copper", "yield_strength": 70e6}
}

# min factor of safety for the materials
required_safety_factor = 1.5

while True:
    print("\n=== Material Selection ===")
    print("1. Steel")
    print("2. Aluminum")
    print("3. Copper")
    print("4. Custom Material")
    print("Q. Quit")

    material_choice = input("Choose a material: ").strip().lower()

    if material_choice == "q":
        print("\nProgram ended. Thank you!")
        break

    # material in choices
    if material_choice in materials:
        material_name = materials[material_choice]["name"]
        yield_strength = materials[material_choice]["yield_strength"]

    # custom material
    elif material_choice == "4":
        material_name = input("Enter the material name: ").strip()

        if material_name == "":
            print("Material name cannot be empty.")
            continue

        while True:
            try:
                yield_strength_mpa = float(
                    input("Enter yield strength (MPa): ")
                )

                if yield_strength_mpa <= 0:
                    print("Yield strength must be greater than 0.")
                else:
                    yield_strength = yield_strength_mpa * 1_000_000
                    break

            except ValueError:
                print("Please enter a valid number.")

    else:
        print("Invalid material choice. Please try again.")
        continue

    print(f"\nMaterial selected: {material_name}")

    # force input and validity
    while True:
        try:
            force = float(input("Enter applied force (N): "))

            if force <= 0:
                print("Force must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # area input and validity
    while True:
        try:
            area = float(input("Enter cross-sectional area (m^2): "))

            if area <= 0:
                print("Area must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # length input
    while True:
        try:
            original_length = float(
                input("Enter original length (m): ")
            )

            if original_length <= 0:
                print("Original length must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # change in length input
    while True:
        try:
            change_in_length = float(
                input("Enter change in length (m): ")
            )

            if change_in_length < 0:
                print("Change in length cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # calculations
    stress = force / area
    strain = change_in_length / original_length


    factor_of_safety = yield_strength / stress

    # safe/unsafe
    if factor_of_safety >= required_safety_factor:
        safety_result = "SAFE"
    else:
        safety_result = "UNSAFE"

    # Display results
    print("\n=== Results ===")
    print(f"Material: {material_name}")
    print(f"Stress: {stress:,.2f} Pa")
    print(f"Strain: {strain:.6f}")
    print(f"Yield Strength: {yield_strength:,.2f} Pa")
    print(f"Factor of Safety: {factor_of_safety:.2f}")
    print(f"Safety Result: {safety_result}")

    # ask if user wants another calculation
    while True:
        again = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()

        if again == "y":
            break
        elif again == "n":
            print("\nProgram ended. Thank you!")
            raise SystemExit
        else:
            print("Kindly enter if y or n.")