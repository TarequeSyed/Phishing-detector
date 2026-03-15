from flask import Blueprint, jsonify, request
from models.scan import Scan
from database import db

from analyser.heuristic import heuristic_score
from analyser.llm_detector import llm_score
from analyser.url_detector import extract_urls
from analyser.url_risk import url_risk_score
from analyser.scoring import combine_scores


analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/analyze", methods=["POST"])
def analyze_email():

    data = request.get_json()
    email_text = data["email"]

    # 1. Extract URLs
    urls = extract_urls(email_text)

    # 2. Heuristic detection
    h_score, h_keywords = heuristic_score(email_text)

    # 3. URL risk analysis
    u_score, u_issues = url_risk_score(urls)

    # 4. LLM reasoning
    llm_s, explanation = llm_score(email_text, urls)

    # 5. Final combined score
    final_score = combine_scores(h_score, u_score, llm_s)

    # 6. Save scan to database
    scan = Scan(
    email_text=email_text,
    heuristic_score=h_score,
    url_score=u_score,
    llm_score=llm_s,
    final_score=final_score,
    urls_found=",".join(urls),
    llm_analysis=explanation
)

    db.session.add(scan)
    db.session.commit()

    # 7. Return API response
    return jsonify({
        "final_score": final_score,
        "heuristic_score": h_score,
        "url_score": u_score,
        "llm_score": llm_s,
        "urls_found": urls,
        "keywords_detected": h_keywords,
        "url_issues": u_issues,
        "llm_analysis": explanation
    })