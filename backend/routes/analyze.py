from flask import Blueprint, jsonify, request

from analyser.heuristic import heuristic_score
from analyser.llm_detector import llm_score
from analyser.url_detector import extract_urls
from analyser.url_risk import url_risk_score
from analyser.scoring import combine_scores

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze_email():
    data = request.json
    email_text = data.get("email")

    #1: extract urls:
    urls = extract_urls(email_text)

    #2 heuristic detections:
    h_score, h_keywords = heuristic_score(email_text)

    #3 url risk:
    u_score, u_issues = url_risk_score(urls)

    #4 llm reasoning:
    llm_s, explanation = llm_score(email_text, urls)

    #5 final score:
    final_score = combine_scores(h_score, u_score, llm_s)

    return jsonify({
        "final score": final_score,
        "heuristic_score": h_score, 
        "url_score": u_score,
        "llm score": llm_s,
        "urls found": urls,
        "keywords_detected": h_keywords,
        "url_issues": u_issues,
        "llm_analysis": explanation
    })

    