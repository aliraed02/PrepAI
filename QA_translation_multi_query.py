from langchain.prompts import PromptTemplate




def MultiQueryTemplateEN():

        TEMPLATE = """
        You are an AI language model assistant. Your task is to generate five 
        different versions of the given user question to retrieve relevant documents from a vector 
        database. By generating multiple perspectives on the user question, your goal is to help
        the user overcome some of the limitations of the distance-based similarity search. 
        Provide these alternative questions separated by newlines. Original question: {question}
                
        """
        return TEMPLATE

def MultiQueryTemplateAR():
        TEMPLATE = """
        أنت مساعد نموذج لغة الذكاء الاصطناعي. مهمتك هي إنشاء خمس نسخ مختلفة من سؤال المستخدم المعطى لاسترداد المستندات ذات الصلة من قاعدة بيانات المتجه.
        من خلال إنشاء وجهات نظر متعددة حول سؤال المستخدم ،
        فإن هدفك هو مساعدة المستخدم على التغلب على بعض قيود البحث عن التشابه القائم على المسافة.
        قدم هذه الأسئلة البديلة مفصولة بعلامات أسطر جديدة. 
        : السؤال الأصلي

        {question}

        """
        return TEMPLATE


##############################################################


promptMultiQueryEN = PromptTemplate(
        input_variables=['question'],
        template=MultiQueryTemplateEN()
)

promptMultiQueryAR = PromptTemplate(
        input_variables=['question'],
        template=MultiQueryTemplateAR()
)

###############################################################



def AnswerTemplateEN():

        TEMPLATE = """
        Answer the following question based on this context:

        {context}

        Question: {question}

        """
        return TEMPLATE




def AnswerTemplateAR():

        TEMPLATE = """
        اجب على السؤال التالي بناءً على هذا السياق:

        {context}

        السؤال: 
        {question}

        """
        return TEMPLATE

#################################################################

promptAnswerEN = PromptTemplate(
        input_variables=['context', 'question'],
        template=AnswerTemplateEN()
)


promptAnswerAR = PromptTemplate(
        input_variables=['context', 'question'],
        template=AnswerTemplateAR()
)


