from flask import Flask, request
import pandas as pd
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('API_URL')

@app.route("/api/form", methods=["POST"])
def handle_form_submission():
    data = request.get_json()  # Access the JSON payload sent from the frontend
    report = data.get('report')

    system_prompt = 'You are a sophisticated AI assistant for physicians, equipped with up-to-date knowledge from the guidelines by the American Medical Association on how to analyze blood test results. You are tasked with providing preliminary type of anemia diagnoses based on lab reports with patients blood values. Only output what is abnormal, an accurate list of a differential diagnosis based on lab values, and what you recommend the doctor which next clear steps to take prioritizing treatments with dosage medication and diet advices.'
    user_prompt = report

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    print(completion)

    response = completion.choices[0].message.content

    # Example: Print the received form data
    return {"response": response}

if __name__ == "__main__":
    app.run()