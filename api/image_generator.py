from helpers.image_generator import create_story_image_response, init_image_generation_model, get_img_prompts
from models.types import StoryImageResponse


def generate_image(story: dict) -> StoryImageResponse:
    negative_prompt = "nude, naked"
    image_prompts = get_img_prompts(story)
    pipe = init_image_generation_model()
    images = []
    for i, prompt in enumerate(image_prompts):
        image = pipe(prompt, negative_prompt=negative_prompt).images[0]
        image.save(f'picture_{i+1}.jpg')
        images.append(image)
        story[f"Paragraph {i + 1}"]["Image"] = f'picture_{i+1}.jpg'

    image_bytes = b'\x89PNG\r\n\x1a\n\x00\x00...'
    return create_story_image_response(image_bytes)
