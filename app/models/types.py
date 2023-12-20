from typing import List


class StoryTextResponse:
    def __init__(self, story_text: str):
        self.story_text = story_text


class QuestionnaireResponse:
    def __init__(self, questionnaire: List[str]):
        self.questionnaire = questionnaire


class StoryImageResponse:
    def __init__(self, story_image: bytes):
        self.story_image = story_image
