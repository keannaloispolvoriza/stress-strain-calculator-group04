print("=== Stress and Strain Analysis System ===")

# predefined materials
materials = {
    "1": {"name": "Steel", "yield_strength": 250e6, "youngs_modulus": 200e9},
    "2": {"name": "Aluminum", "yield_strength": 150e6, "youngs_modulus": 69e9},
    "3": {"name": "Copper", "yield_strength": 70e6, "youngs_modulus": 117e9}
}

# min factor of safety for the materials
required_safety_factor = 1.5

# calculation history
calculation_history = []

# unique materials used
materials_used = set()

# measurement units
units = ("N", "m^2", "m", "Pa")


while True:
    print("\n=== Material Selection ===")
    print("1. Steel")
    print("2. Aluminum")
    print("3. Copper")
    print("4. Custom Material")
    print("Q. Quit")

    material_choice = input("Choose a material: ").strip().lower()

    if material_choice == "q":
        break

    # material in choices
    if material_choice in materials:
        material_name = materials[material_choice]["name"]
        yield_strength = materials[material_choice]["yield_strength"]
        youngs_modulus = materials[material_choice]["youngs_modulus"]

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

        while True:
            try:
                youngs_modulus_gpa = float(
                    input("Enter Young's modulus (GPa): ")
                )

                if youngs_modulus_gpa <= 0:
                    print("Young's modulus must be greater than 0.")
                else:
                    youngs_modulus = youngs_modulus_gpa * 1_000_000_000
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

    # store test information in a dictionary
    test_record = {
        "material": material_name,
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length,
        "stress": stress,
        "strain": strain,
        "youngs_modulus": youngs_modulus,
        "safety_result": safety_result
    }

    # store the test record in the calculation history list
    calculation_history.append(test_record)

    # add material to the set
    materials_used.add(material_name)

    # Display results
    print("\n=== Results ===")
    print(f"Material: {material_name}")
    print(f"Stress: {stress:,.2f} {units[3]}")
    print(f"Strain: {strain:.6f}")
    print(f"Yield Strength: {yield_strength:,.2f} Pa")
    print(f"Young's Modulus: {youngs_modulus:,.2f} Pa")
    print(f"Factor of Safety: {factor_of_safety:.2f}")
    print(f"Safety Result: {safety_result}")

    print(f"\nCalculation saved.")
    print(f"Total calculations: {len(calculation_history)}")

    # ask if user wants another calculation
    while True:
        again = input(
            "\nDo you want to perform another calculation? (y/n): "
        ).strip().lower()

        if again == "y":
            break
        elif again == "n":
            print("\nProgram ended. Thank you!")
            break
        else:
            print("Kindly enter if y or n.")

    if again == "n":
        break


# session summary
print("\n=== Session Summary ===")

if len(calculation_history) == 0:
    print("No calculations were recorded.")

else:
    stress_values = []
    strain_values = []

    for record in calculation_history:
        stress_values.append(record["stress"])
        strain_values.append(record["strain"])

    average_stress = sum(stress_values) / len(stress_values)
    average_strain = sum(strain_values) / len(strain_values)

    highest_stress = max(stress_values)
    lowest_stress = min(stress_values)

    print(f"Total tests: {len(calculation_history)}")
    print(f"Materials used: {', '.join(sorted(materials_used))}")
    print(f"Average Stress: {average_stress:,.2f} Pa")
    print(f"Average Strain: {average_strain:.6f}")
    print(f"Highest Stress: {highest_stress:,.2f} Pa")
    print(f"Lowest Stress: {lowest_stress:,.2f} Pa")

print("\nProgram ended. Thank you!")
