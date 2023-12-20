from helpers.gemini import create_story_text_response, create_questionnaire_response
from models.types import StoryTextResponse, QuestionnaireResponse


def generate_story_text(image_url: str, prompt: str) -> StoryTextResponse:
    # Implement logic to call Gemini Vision model and generate story text
    # Replace this with your actual code
    story_text = "Once upon a time..."
    return create_story_text_response(story_text)


def generate_questionnaire(story_text: str) -> QuestionnaireResponse:
    # Implement logic to call Gemini Vision model and generate a questionnaire
    # Replace this with your actual code
    questionnaire = ["Funny", "Adventure", "Mystery"]
    return create_questionnaire_response(questionnaire)
