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

##OUTPUT:
**Valiation page**
![image](https://github.com/user-attachments/assets/77f3d1da-ef6b-4df8-8950-38c15d882556)

**Validation log**
![image](https://github.com/user-attachments/assets/543a2243-7fb4-4dc8-a3d4-5d425f7619a4)

## 📄 License
This project is licensed under the MIT License.
