# HSN Validator

A Python-based web application for validating HSN (Harmonized System of Nomenclature) codes using an Excel dataset.

## 🚀 Features

- Validates HSN codes using a master Excel file
- Flask-based web interface for easy interaction
- Modular structure with separate logic (`hsn_validator.py`)
- Simple UI using templates folder (HTML)

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- HTML
- Excel (.xlsx)

## 📁 Project Structure
.
├── app.py # Main Flask app
├── hsn_validator.py # Core HSN validation logic
├── HSN_Master_Data.xlsx # HSN master data file
├── requirements.txt # List of Python packages
└── templates/ # HTML templates


## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sarvveshp/HSN_validator.git
   cd HSN_validator

2. **(Optional) Create a virtual environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt

4. **Run the Flask app**:
    ```bash
    python app.py

5. **Access the application**:
    Open your browser and go to `http://127.0.0.1:5000/`

## 📄 License
This project is licensed under the MIT License.
