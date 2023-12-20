from models.types import StoryImageResponse


def create_story_image_response(story_image: bytes) -> StoryImageResponse:
    return StoryImageResponse(story_image)
