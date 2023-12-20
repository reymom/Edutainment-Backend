from typing import List

from models.types import StoryTextResponse, QuestionnaireResponse


def create_story_text_response(story_text: str) -> StoryTextResponse:
    return StoryTextResponse(story_text)


def create_questionnaire_response(questionnaire: List[str]) -> QuestionnaireResponse:
    return QuestionnaireResponse(questionnaire)
