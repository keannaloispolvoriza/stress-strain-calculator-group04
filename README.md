# Stress and Strain Analysis System
## Group 4

| **Member**                 | **Assigned Task**                           | **GitHub Username**      |
| -------------------------- | ------------------------------------------- | ------------------------ |
| Keanna Lois Polvoriza      | Task 1 – Basic Stress and Strain Calculator | @keannaloispolvoriza     |
| Arianne Denise Sumalinog   | Task 2 – Control Structures and Validation  | @ariannesumalinog        |
| Princess Kassy Mercado     | Task 3 – Data Structures and Test History   | @pkkmercado              |
| Olivia Patricia Jovita Baña| Task 4 – Functions and Modular Programming  | @olivia-bana             |
| Rianne Rose Mendoza        | Task 5 – Object-Oriented Programming        | @riannerosemendoza-droid |

Task 6 – Final Modular Application and Integration was completed collaboratively by all five members.

## Project Description
The Stress and Strain Analysis System is a Python-based application developed to calculate and analyze the mechanical behavior of different materials.
The program allows users to select predefined materials such as Steel, Aluminum, and Titanium, or create a custom material. Users can enter applied force, cross-sectional area, original length, and change in length to calculate stress, strain, Young's modulus, and factor of safety.
The application was developed progressively across six tasks. Each task introduced additional Python programming concepts, beginning with basic calculations and progressing to control structures, data structures, functions, object-oriented programming, and modular integration.
Git and GitHub were used throughout the development process to track individual contributions and collaboratively integrate the final application.

## Project Features
The Stress and Strain Analysis System provides the following major features:
1. Material Selection – Users can select from predefined materials such as Steel, Aluminum, and Titanium or create a custom material with its own properties.
2. Stress and Strain Analysis – The system calculates stress, strain, and Young's modulus based on the user's input.
3. Safety Evaluation – The program calculates the factor of safety and determines whether the material is safe or unsafe.
4. Input Validation – Invalid inputs, such as non-numeric, negative, or zero values, are handled to prevent calculation errors.
5. Multiple Test Calculations – Users can perform multiple stress-strain tests within a single session.
6. Test History – The system stores the results of each test performed during the current session.
7. Session Summary – At the end of the session, the program displays a summary including the total tests, materials used, average stress and strain, and the highest and lowest stress results.
8. Data Export – Test results can be stored using JSON and CSV functionality.

## Installation and Requirements
The project requires:
1. Python 3.11.13
2. Git
3. GitHub account for collaborative development
The application uses Python's standard library.
No third-party packages are required for the current implementation.

## How to Run the Program
Clone the repository:
git clone <repository-url>

Navigate to the project directory:
cd stress-strain-calculator-group04-14

Run the program:
python main.py

If the Python files are located inside a project folder, navigate to that folder first and run:
python main.py

## Repository Structure

The application is organized into separate modules based on their responsibilities:
stress-strain-calculator-group04-14/
│
├── material.py
├── properties.py
├── tests.py
├── utils.py
├── database.py
├── main.py
└── README.md

1. material.py
Contains the material class hierarchy and material-related behavior.
2. properties.py
Contains material property information and dataclasses used by the application.
3. tests.py
Contains the classes and functionality used to represent and analyze stress-strain tests.
4. utils.py
Contains reusable calculation functions, including stress, strain, and Young's modulus calculations.
5. database.py
Contains the predefined material database, custom material creation, safety factor configuration, and data management functions.
6. main.py
Serves as the main entry point of the application. It coordinates material selection, user input, calculations, test creation, result display, and session summaries.
7. README.md
Contains documentation about the project, its features, structure, installation, usage, testing, and group contributions.

## Testing Requirements
Sample Test Cases:

Test 1 – Steel
Required test input:
Material: Steel
Force: 50,000 N
Area: 0.01 m²
Original Length: 10 m
Change in Length: 0.005 m

Expected:
Stress = 5,000,000 Pa
Strain = 0.0005

Test 2 – Aluminum
Required test input:
Material: Aluminum
Force: 10,000 N
Area: 0.002 m²
Original Length: 1 m
Change in Length: 0.0015 m

Expected:
Stress = 5,000,000 Pa
Strain = 0.0015

Additional Tests
The application was also tested with:
Steel
Aluminum
Titanium
Custom materials
Multiple calculations in one session
Invalid material choices
Non-numeric input
Negative values
Custom material validation
Session summaries
Program termination
