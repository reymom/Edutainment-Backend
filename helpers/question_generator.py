from typing import List
from models.types import QuestionnaireResponse

import google.generativeai as genai


def init_text_model():
    generation_config = {
        "temperature": 0.9, "top_p": 1,
        "top_k": 1, "max_output_tokens": 2048
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        }
    ]

    text_model = genai.GenerativeModel(
        model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)

    return text_model


def get_questionnaire(input_string) -> dict:
    lines = input_string.split('\n')

    # Extracting the question
    question_line = lines[0].split(':')
    question = question_line[1].strip()

    # Extracting answers and colors
    options = []
    for i in range(1, len(lines)-1, 2):
        print(" i = ", i)
        answer_line = lines[i].split(':')
        color_line = lines[i+1].split(':')

        option = {'option': answer_line[1].strip(
        ), 'color': color_line[1].strip()}
        options.append(option)

    # Creating the dictionary
    questionnaire = {'question': question, 'options': options}

    return questionnaire


def create_questionnaire_response(questionnaire: List[str]) -> QuestionnaireResponse:
    return QuestionnaireResponse(questionnaire)
