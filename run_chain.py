import re
import json
from mcq import generate_evaluation_chain_arabic, generate_evaluation_chain_english
from utilities import generate_exam, display_mcq



def run(DOCS, NUMBER, SUBJECT, TONE):

    if re.match("[a-zA-Z0-9]", SUBJECT):
        with open (r'D:\Python\Gen AI\Zinc\response_english.json', 'r') as file:
                RESPONSE_JOSN = json.load(file) 
        response = generate_evaluation_chain_english(
                        {
                        "text": DOCS,
                        "number": NUMBER,
                        "subject": SUBJECT,
                        "tone": TONE,
                        "response_json": json.dumps(RESPONSE_JOSN)
                        }
                    )
        display_mcq(json.loads(response['quiz']))
    else:
        with open (r'D:\Python\Gen AI\Zinc\response_arabic.json', 'r') as file:
                    RESPONSE_JOSN = json.load(file)
        response = generate_evaluation_chain_arabic(
                        {
                        "text": DOCS,
                        "number": NUMBER,
                        "subject": SUBJECT,
                        "tone": TONE,
                        "response_json": json.dumps(RESPONSE_JOSN)
                        }
                    )
        display_mcq(json.loads(response['quiz']))