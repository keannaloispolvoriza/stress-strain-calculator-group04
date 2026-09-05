import json
import csv
from material import Material, Metal
from properties import MaterialProperties
material = Metal

REQUIRED_SAFETY_FACTOR = 1.5

def create_material_database():
    """Create and return the built-in material database."""

    steel = Metal(
        "Steel",
        MaterialProperties(
            density=7850,
            yield_strength=250,
            typical_youngs_modulus=200
        ),
        is_ferrous=True
    )

    aluminum = Metal(
        "Aluminum",
        MaterialProperties(
            density=2700,
            yield_strength=95,
            typical_youngs_modulus=69
        )
    )

    titanium = Metal(
        "Titanium",
        MaterialProperties(
            density=4500,
            yield_strength=880,
            typical_youngs_modulus=114
        )
    )

    return {
        "1": steel,
        "2": aluminum,
        "3": titanium
    }

MATERIALS = create_material_database()


def get_material(database, choice):
    """Return a selected material from the database."""
    return database.get(choice)
    if material is None:
        raise KeyError(f"No material found for choice '{choice}'")
    return material    

def create_custom_material():
    """Create a custom material from user input."""

    name = input("Enter material name: ").strip()

    if not name:
        raise ValueError("Material name cannot be empty.")

    while True:
        try:
            density = float(
                input("Enter density (kg/m³): ")
            )

            if density <= 0:
                print("Density must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            yield_strength_mpa = float(
                input("Enter yield strength (MPa): ")
            )

            if yield_strength_mpa <= 0:
                print("Yield strength must be greater than 0.")
                continue

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
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    properties = MaterialProperties(
        density=density,
        yield_strength=yield_strength_mpa * 1_000_000,
        typical_youngs_modulus=youngs_modulus_gpa * 1_000_000_000
    )

    return Material(name, properties)
    
def save_results_to_json(results, filename): 
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

def export_results_to_csv(results, filename):
    if not results:
        raise ValueError("No results to export")
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
