from configration import llm
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain




MCQ_TEMPLATE_ARB = """

        النص: 
        {text}
        وظيفتك كصانع أسئلة اختيار من متعدد هي انشاء اختبار يتكون من 
        {number}
        أسئلة، عن 
        {subject}
        و مستوى الاسئلة 
        {tone}.
        تأكد من أن الأسئلة غير متكررة وأن جميع الأسئلة تتوافق مع النص. تأكد من تضمين 
        {number} 
        أسئلة اختيار من متعدد.
        و اريد النتائج مثل هذا الشكل
        {response_json}
        

    """


MCQ_TEMPLATE_ENG = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the question are not repeated and check all the questions to be conforming the text as well.
Ensure to make {number} MCQs
### I want the output in this format {response_json}

"""

quiz_generation_prompt_arabic = PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=MCQ_TEMPLATE_ARB
)


quiz_generation_prompt_english = PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=MCQ_TEMPLATE_ENG
)

##########################################################################################



REVIEW_TEMPLATE_ARB = """
أنت خبير في قواعد اللغة العربية والكتابة.
بالنظر الى اختبار اختيار من متعدد لطلاب عن 
{subject}
نحتاج الى تقيم مدى تعقيد الاسئلة وتقديم تحليل كامل للاختبار. استخدم 50 كلمة كحد اقصى لتعقيد الاسئلة.
اذا لم يكن الاختبار متوافقا مع القدرات المعرفية والتحليلية للطلاب، فقم بتحديث سؤال الاختبار الذي يحتاج الى التغير، وتغير اللهجه بحيث يتناسب تماما مع الطلاب.

## اسئلة اختيار من متعدد
{quiz}


## مراجعة وتدقيق من قبل خبير في اللغة العربية للاختبار السابق


"""


REVIEW_TEMPLATE_ENG = """
You are an expert english grammarican and writer. Given a Multiple Choice Quiz for {subject} students.\
you need to evaluate the complexity of the question and given a complete analysis of the quiz. Only use at max 50 words for complexities
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz question which needs to be changed and change the tone such that it perfectly fits the students 
Quiz_MCQ:
{quiz}

Check from an expert English Writer of the above quiz:

"""

quiz_evaluation_prompt_arabic = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=REVIEW_TEMPLATE_ARB
)



quiz_evaluation_prompt_english = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=REVIEW_TEMPLATE_ENG
)

####################################################################################


quiz_chain_arabic = LLMChain(llm=llm, prompt=quiz_generation_prompt_arabic, output_key="quiz", verbose=True)
quiz_chain_english = LLMChain(llm=llm, prompt=quiz_generation_prompt_english, output_key="quiz", verbose=True)


####################################################################################


review_chain_arabic = LLMChain(llm=llm, prompt=quiz_evaluation_prompt_arabic, output_key="review", verbose=True)
review_chain_english = LLMChain(llm=llm, prompt=quiz_evaluation_prompt_english, output_key="review", verbose=True)



####################################################################################


generate_evaluation_chain_arabic = SequentialChain(
    chains=[quiz_chain_arabic, review_chain_arabic],
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    output_variables=["quiz", "review"],
    verbose=True
)  


generate_evaluation_chain_english = SequentialChain(
    chains=[quiz_chain_english, review_chain_english],
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    output_variables=["quiz", "review"],
    verbose=True
)  