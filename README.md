# CGPA Calculator

A simple web application to calculate SGPA and CGPA for students based on their subjects, marks, and credit hours.

## Website is Live: http://rasikhali.pythonanywhere.com/

## Features

- Calculate SGPA and CGPA based on the subjects, marks, and credit hours.
- Dynamically add or remove subjects.
- Display results in a tabular format with individual grades for each subject.
- Provide detailed SGPA and CGPA results.

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/RasikhAli/CGPA-Calculator.git
    cd CGPA-Calculator
    ```

2. Create a virtual environment and activate it (Optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## File Structure
  ```
  CGPA-Calculator/
  │
  ├── app.py # Main Flask application
  ├── calculations.py # GPA calculation logic
  ├── templates/
  │ └── index.html # HTML template for the application
  ├── requirements.txt # List of dependencies
  └── README.md # Project documentation
  ```


## Project Overview

### `app.py`
The main Flask application that handles routing and form submissions. It includes:
- An index route to render the homepage.
- A calculate route to process the form data and return the GPA calculations.

### `calculations.py`
Contains the logic for calculating SGPA and CGPA based on the input subjects, marks, and credit hours.

### `templates/index.html`
The HTML template that provides the user interface for the application, allowing users to input their subjects, marks, and credit hours.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.
