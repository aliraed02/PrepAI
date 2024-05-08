from configration import llm
from utilities import get_unique_union
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from QA_translation_multi_query import promptMultiQueryEN, promptMultiQueryAR, promptAnswerEN, promptAnswerAR





class QuestionAnsweringSystemEN:
    """
    A question answering system that retrieves relevant context and uses a language model to generate an answer.

    Parameters:
        retriever (Retriever): The retriever object responsible for retrieving relevant context from a data source.
        question (str): The question to be answered by the system.

    Attributes:
        retriever (Retriever): The retriever object used for retrieving context.
        question (str): The question to be answered.
    """

    def __init__(self, retriever, question):
        """
        Initializes the question answering system with a retriever object and the question to be answered.

        Args:
            retriever (Retriever): The retriever object responsible for retrieving relevant context from a data source.
            question (str): The question to be answered by the system.
        """

        self.retriever = retriever
        self.question = question

    def generate_multi_query_chain(self):
        """
        Generates a chain of prompts for the language model based on the input question (placeholder).

        This function is currently a placeholder and needs to be implemented based on your chosen prompting strategy.
        The goal is to create informative prompts that can guide the language model towards generating a good answer.

        Possible prompting techniques include:
            * Reformulating the question
            * Breaking down the question into sub-questions
            * Providing additional context or instructions

        Returns:
            Callable: A chain of callables representing the multi-query prompt for the language model.
        """

        # Replace this with the actual implementation for generating the multi-query chain
        return (
            promptMultiQueryEN  # Placeholder for the actual promptMultiQuery function
            | llm
            | StrOutputParser()
            | (lambda x: x.split('\n'))
        )

    def retrieval_chain(self):
        """
        Generates a chain to retrieve relevant context for answering the question.

        1. Calls generate_multi_query_chain (placeholder) to get the prompts.
        2. Uses the retriever object's map function to retrieve context based on the prompts.
        3. Applies get_unique_union to remove duplicate retrieved passages.

        Returns:
            Callable: A chain that retrieves and processes relevant context.
        """

        return (
            self.generate_multi_query_chain()
            | self.retriever.map()
            | get_unique_union
        )

    def answer_question(self):
        """
        Answers the given question by retrieving relevant context, formulating a final question based on context,
        and using the language model to generate the answer.

        1. Calls retrieval_chain to get the retrieved context.
        2. Creates a dictionary with the context and the original question.
        3. Uses promptAnswer (placeholder) to formulate the final question based on the retrieved context.
        4. Uses geminiLlm (language model) to generate the answer based on the final question.
        5. Parses the answer string using StrOutputParser.

        Returns:
            str: The generated answer to the question.
        """

        return (
            {'context': self.retrieval_chain(), 'question': RunnablePassthrough()}
            | promptAnswerEN  # Placeholder for the actual promptAnswer function
            | llm
            | StrOutputParser()
        ).invoke({'question': self.question})







class QuestionAnsweringSystemAR:
    """
    A question answering system that retrieves relevant context and uses a language model to generate an answer.

    Parameters:
        retriever (Retriever): The retriever object responsible for retrieving relevant context from a data source.
        question (str): The question to be answered by the system.

    Attributes:
        retriever (Retriever): The retriever object used for retrieving context.
        question (str): The question to be answered.
    """

    def __init__(self, retriever, question):
        """
        Initializes the question answering system with a retriever object and the question to be answered.

        Args:
            retriever (Retriever): The retriever object responsible for retrieving relevant context from a data source.
            question (str): The question to be answered by the system.
        """

        self.retriever = retriever
        self.question = question

    def generate_multi_query_chain(self):
        """
        Generates a chain of prompts for the language model based on the input question (placeholder).

        This function is currently a placeholder and needs to be implemented based on your chosen prompting strategy.
        The goal is to create informative prompts that can guide the language model towards generating a good answer.

        Possible prompting techniques include:
            * Reformulating the question
            * Breaking down the question into sub-questions
            * Providing additional context or instructions

        Returns:
            Callable: A chain of callables representing the multi-query prompt for the language model.
        """

        # Replace this with the actual implementation for generating the multi-query chain
        return (
            promptMultiQueryAR  # Placeholder for the actual promptMultiQuery function
            | llm
            | StrOutputParser()
            | (lambda x: x.split('\n'))
        )

    def retrieval_chain(self):
        """
        Generates a chain to retrieve relevant context for answering the question.

        1. Calls generate_multi_query_chain (placeholder) to get the prompts.
        2. Uses the retriever object's map function to retrieve context based on the prompts.
        3. Applies get_unique_union to remove duplicate retrieved passages.

        Returns:
            Callable: A chain that retrieves and processes relevant context.
        """

        return (
            self.generate_multi_query_chain()
            | self.retriever.map()
            | get_unique_union
        )

    def answer_question(self):
        """
        Answers the given question by retrieving relevant context, formulating a final question based on context,
        and using the language model to generate the answer.

        1. Calls retrieval_chain to get the retrieved context.
        2. Creates a dictionary with the context and the original question.
        3. Uses promptAnswer (placeholder) to formulate the final question based on the retrieved context.
        4. Uses geminiLlm (language model) to generate the answer based on the final question.
        5. Parses the answer string using StrOutputParser.

        Returns:
            str: The generated answer to the question.
        """

        return (
            {'context': self.retrieval_chain(), 'question': RunnablePassthrough()}
            | promptAnswerAR  # Placeholder for the actual promptAnswer function
            | llm
            | StrOutputParser()
        ).invoke({'question': self.question})



