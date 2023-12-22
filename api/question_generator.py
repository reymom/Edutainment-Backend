from helpers.question_generator import create_questionnaire_response, QuestionnaireResponse, init_text_model, get_questionnaire

text_model = init_text_model()


def generate_questionnaire_object(story_text: str) -> QuestionnaireResponse:
    prompt = f"""For the following story, create a questionnaire to ask what continuation of the story the user want:
{story_text}
Create one short question and four answers with one or two words maximum following the exact format:
Question: Your question related to a story.
Answer: The first possible answer.
Color: The tailwind color style class for the first answer's button, such as bg-blue-500. Change blue for your option.
Answer: The second possible answer.
Color: The tailwind color style class for the second answer's button, such as bg-purple-500. Change purple for your option.
Answer: The third possible answer.
Color: The tailwind color style class for the third answer's button, such as bg-red-500. Change red for your option.
Answer: The fourth possible answer.
Color: The tailwind color style class for the fourth answer's button, such as bg-green-500. Change green for your option.
"""
    response = text_model.generate_content(prompt)
    print("response.text = ", response.text)
    questionnaire = get_questionnaire(response.text)
    print("questionnaire = ", questionnaire)
    return create_questionnaire_response(questionnaire)
