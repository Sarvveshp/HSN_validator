from flask import Flask, request, render_template
from hsn_validator import HSNCodeLookupTool

app = Flask(__name__)
tool = HSNCodeLookupTool("HSN_Master_Data.xlsx")

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        codes = request.form["codes"]
        codes_list = [code.strip() for code in codes.split(",")]
        results = [tool.validate(code) for code in codes_list]
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)