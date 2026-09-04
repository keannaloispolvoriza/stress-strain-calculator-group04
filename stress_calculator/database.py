from properties import MaterialProperties
from material import Metal


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


def get_material(database, choice):
    """Return a selected material from the database."""
    return database.get(choice)


import json 
def save_results(results, filename): 
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

import csv
def export_results(results, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )
        writer.writeheader()
        writer.writerows(results)
    
    
