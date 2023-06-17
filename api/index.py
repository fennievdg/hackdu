from flask import Flask, request
import pandas as pd
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route("/api/form", methods=["POST"])
def handle_form_submission():
    data = request.get_json()  # Access the JSON payload sent from the frontend
    report = data.get('report')

    system_prompt = 'You are a sophisticated AI assistant for physicians, equipped with up-to-date knowledge from the guidelines by the American Medical Association on how to analyze blood test results. You are tasked with providing preliminary types of anemia diagnoses based on lab reports with patients' blood values. Only output what is abnormal, an accurate list of a differential diagnosis based on lab values, and what you recommend the doctor in terms of next steps, prioritizing treatments with dosage medication and diet advice.'
    user_prompt = report

    completion = openai.Completion.create(
        engine="davinci",
        prompt=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
    )

    print(completion)

    response = completion.choices[0].text.strip()

    # Example: Print the received form data
    return {"response": response}

if __name__ == "__main__":
    app.run()