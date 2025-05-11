import pandas as pd

class HSNCodeLookupTool:
    def __init__(self, excel_path):
        self.df = pd.read_excel(excel_path)
        self.df.columns = self.df.columns.str.strip()
        self.df['HSNCode'] = self.df['HSNCode'].astype(str).str.strip()

    def validate(self, code):
        code = str(code).strip()
        if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
            return {"code": code, "valid": False, "reason": "Invalid format"}

        match = self.df[self.df['HSNCode'] == code]
        if not match.empty:
            return {"code": code, "valid": True, "description": match['Description'].values[0]}

        return {"code": code, "valid": False, "reason": "Code not found"}
