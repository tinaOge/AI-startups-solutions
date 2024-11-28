# app/routes.py
from flask import Flask, request, jsonify
from app.query_interface.bert_model import get_kpi_answer
from app.query_interface.suggest_viz import suggest_visualization
from app.investor_matching.matching_logic import match_investors

app = Flask(__name__)

@app.route('/query_kpi', methods=['POST'])
def query_kpi():
    data = request.json
    context = data['context']
    question = data['question']
    answer = get_kpi_answer(context, question)
    visualization = suggest_visualization(question)
    return jsonify({"answer": answer, "visualizations": visualization})

@app.route('/match_investors', methods=['POST'])
def match_investors_api():
    data = request.json
    startup_id = data['startup_id']
    matched_investors = match_investors(startup_id)
    return jsonify({"matched_investors": matched_investors})

if __name__ == "__main__":
    app.run(debug=True)

