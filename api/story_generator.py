from PIL import Image
from io import BytesIO
import base64
from helpers.story_generator import create_story_text_response, configure_gemini
from models.types import StoryTextResponse


vision_model = configure_gemini()


def generate_story_text(prompt: str, image: bytes, width: int, height: int, img_type: str) -> StoryTextResponse:
    try:
        img_base64 = image.split(",")[1]
    except:
        img_base64 = image
    decoded_image = base64.b64decode(img_base64)

    # Create a PIL Image from bytes
    try:
        pil_image = Image.frombytes(
            'RGB', (width, height), decoded_image, 'raw', 'RGB')
    except:
        print("except")
        pil_image = Image.open(BytesIO(decoded_image))

    buffer_image = BytesIO()
    pil_image.save(buffer_image, format=img_type)
    image = Image.open(buffer_image)
    # image.show()

    response = vision_model.generate_content(
        [prompt, image], stream=True)
    response.resolve()

    return create_story_text_response(response.text)
