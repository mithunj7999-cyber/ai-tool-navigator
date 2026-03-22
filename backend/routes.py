# backend/routes.py

from flask import render_template, request, jsonify
from category_detector import detect_category
from section_suggestions import get_dynamic_sections
from prompt_generator import generate_prompts


def register_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/results")
    def results():
        return render_template("results.html")

    @app.route("/get_sections", methods=["POST"])
    def get_sections():
        data     = request.get_json() or {}
        topic    = data.get("topic", "").strip()
        category = detect_category(topic)
        sections = get_dynamic_sections(topic, category)
        return jsonify({"sections": sections, "category": category})

    @app.route("/generate", methods=["POST"])
    def generate():
        data     = request.get_json() or {}
        topic    = data.get("topic", "").strip()
        selected = data.get("selected_sections", [])

        if not topic:
            return jsonify({"error": "Please enter a topic."}), 400

        category = detect_category(topic)
        try:
            return jsonify(generate_prompts(topic, category, selected))
        except Exception as e:
            return jsonify({"error": f"Gemini API error: {str(e)}"}), 500
