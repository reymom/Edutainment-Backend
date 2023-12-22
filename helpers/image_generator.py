from models.types import StoryImageResponse


def create_story_image_response(story_image: bytes) -> StoryImageResponse:
    return StoryImageResponse(story_image)


def init_image_generation_model():
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    return pipe


def get_img_prompts(story):
    image_prompts_list = []
    for paragraph_num in range(1, 4):
        paragraph_key = f"Paragraph {paragraph_num}"
        if paragraph_key in story:
            paragraph_data = story[paragraph_key]
            if "Image Prompt" in paragraph_data:
                image_prompt_paragraph = paragraph_data["Image Prompt"]
                image_prompts_list.append(image_prompt_paragraph)
    return image_prompts_list
