import streamlit as st
from langchain.load import dumps, loads





def get_unique_union(documents: list[list]):
    """
    This function takes a list of lists of Documents and returns a list of unique Documents that are the union of all the Documents in the input list.

    Parameters:
    documents (list[list]): A list of lists of Documents

    Returns:
    list[Document]: A list of unique Documents that are the union of all the Documents in the input list
    """
    # Flatten list of lists, and convert each Document to string
    flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
    # Get unique documents
    unique_docs = list(set(flattened_docs))
    # Return
    return [loads(doc) for doc in unique_docs]





def display_mcq(questions):
    """
    Display multiple-choice questions with options and correct answers.

    Parameters:
        questions (dict): Dictionary containing multiple-choice questions. Each question should be represented as a dictionary
            with keys 'mcq' (the question), 'option' (dictionary of options), and 'correct' (the correct answer).
    """
    correct_answers = {}  # Dictionary to store correct answers

    # Display each question, options, and store correct answers
    for question_number, question_data in questions.items():
        st.write(f"**Question {question_number}:** {question_data['mcq']}")
        st.write("Options:")
        for option, choice in question_data['option'].items():
            st.write(f"- {option}: {choice}")
        correct_answers[question_number] = question_data['correct']  # Store correct answer
        st.write("")  # Add a newline for readability
    
    # Display correct answers after all questions are displayed
    st.write("Correct Answers:")
    for question_number, correct_answer in correct_answers.items():
        st.write(f"Question {question_number}: {correct_answer}")













def generate_exam(mcq_data):
    # Check if mcq_data is not None
    
        # Initialize score
    score = 0

        # Loop through each question
    for q_id, question in mcq_data.items():
            # Display question
        st.subheader(f"Question {q_id}: {question['mcq']}")

            # Radio button for options
        user_answer = st.radio("Select your answer:", list(question['option'].values()), index=None)
        c = question['correct']
        for key, value in question['option'].items():
            if key == c:
                if value == user_answer:
                    score += 1

    if st.button("Score"):
        st.subheader(f"Your final score is {(score / len(mcq_data)) * 100:.2f}%")