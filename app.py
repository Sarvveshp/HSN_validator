from flask import Flask, request, render_template
from hsn_validator import HSNCodeLookupTool

app = Flask(__name__)
tool = HSNCodeLookupTool("HSN_Master_Data.xlsx")

memory_log = []

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        codes = request.form["codes"]
        codes_list = [code.strip() for code in codes.split(",") if code.strip()]
        results = [tool.validate(code) for code in codes_list]
        for result in results:
            memory_log.append(result)
    return render_template("index.html", results=results)

@app.route("/memory")
def memory():
    return render_template("memory.html", memory=memory_log)

if __name__ == "__main__":
    app.run(debug=True)
