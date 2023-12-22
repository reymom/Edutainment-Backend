import requests
from helpers.question_generator import get_questionnaire


tet = """Question: What should Sir Lancelot do next?
Answer: Continue his quest.
Color: bg-blue-500
Answer: Return to Camelot.
Color: bg-purple-500
Answer: Seek out other magical artifacts.
Color: bg-red-500
Answer: Retire from knighthood.
Color: bg-green-500"""

q = get_questionnaire(tet)
print(q)
