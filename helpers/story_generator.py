from typing import List
from models.types import StoryTextResponse

import google.generativeai as genai


def configure_gemini():
    print("configure_gemini")
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        }
    ]

    return genai.GenerativeModel(
        model_name="gemini-pro-vision",
        generation_config=generation_config,
        safety_settings=safety_settings)


def create_story_text_response(story_text: str) -> StoryTextResponse:
    return StoryTextResponse(story_text=story_text)
