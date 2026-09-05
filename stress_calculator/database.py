import json
import csv
from datetime import datetime
from pathlib import Path
from material import Material, Metal
from properties import MaterialProperties
material = Metal


REQUIRED_SAFETY_FACTOR = 1.5

RESULTS_FOLDER = Path("results")
RESULTS_FOLDER.mkdir(exist_ok=True)

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

def convert_test_to_dict(test):
    """Convert a StressStrainTest object into a dictionary."""

    return {
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "material": test.material.name,
        "force": test.force,
        "area": test.area,
        "original_length": test.original_length,
        "change_in_length": test.change_in_length,
        "stress": test.stress,
        "strain": test.strain,
        "youngs_modulus": test.youngs_modulus,
        "factor_of_safety": test.factor_of_safety()
    }


def save_results_to_json(results, filename="results.json"):
    """Save test results to a JSON file."""

    data = []

    for test in results:
        data.append(convert_test_to_dict(test))

    filepath = RESULTS_FOLDER / filename

    with open(filepath, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    return filepath


def load_results_from_json(filename="results.json"):
    """Load test results from a JSON file."""

    filepath = RESULTS_FOLDER / filename

    if not filepath.exists():
        raise FileNotFoundError(
            f"No file found: {filepath}"
        )

    with open(filepath, "r") as file:
        return json.load(file)


def export_results_to_csv(results, filename="results.csv"):
    """Export test results to a CSV file."""

    if not results:
        raise ValueError(
            "No results to export."
        )

    data = []

    for test in results:
        data.append(convert_test_to_dict(test))

    filepath = RESULTS_FOLDER / filename

    with open(
        filepath,
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=data[0].keys()
        )

        writer.writeheader()
        writer.writerows(data)

    return filepath
