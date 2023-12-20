import PIL.Image
import base64
from helpers.gemini import create_story_text_response, create_questionnaire_response, configure_gemini
from models.types import StoryTextResponse, QuestionnaireResponse


vision_model = configure_gemini()


def generate_story_text(image: bytes, prompt: str) -> StoryTextResponse:
    decoded_image = base64.b64decode(image)
    # image = PIL.Image.open(image)
    # new_size = (200, 200)
    # image = image.resize(new_size)

    response = vision_model.generate_content(
        [prompt] + decoded_image, stream=True)
    response.resolve()

    return create_story_text_response(response.text)


def generate_questionnaire(story_text: str) -> QuestionnaireResponse:
    # Implement logic to call Gemini Vision model and generate a questionnaire
    # Replace this with your actual code
    questionnaire = ["Funny", "Adventure", "Mystery"]
    return create_questionnaire_response(questionnaire)
