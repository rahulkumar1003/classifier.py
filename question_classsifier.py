from sympy import sympify

def classify_question(user_question: str) -> str:
    """
    Classify the question into one of three categories:
    - opinion: asks about feelings, beliefs, or personal views
    - math: contains mathematical expressions or keywords
    - factual: everything else (default)
    """
    text = user_question.lower()

    # Opinion cues
    if any(word in text for word in ["think", "feel", "opinion", "believe"]):
        return "opinion"

    # Math cues
    if any(sign in text for sign in ["+", "-", "*", "/", "solve", "calculate"]):
        return "math"

    return "factual"


def generate_response(user_question: str) -> str:
    """
    Generate a simple response based on the classified type.
    """
    category = classify_question(user_question)

    if category == "factual":
        return "This looks like a factual question. You’d usually answer it with information or data."
    
    elif category == "opinion":
        return "This seems like an opinion-based question. Different people may have different answers."
    
    elif category == "math":
        try:
            result = sympify(user_question).evalf()
            return f"I recognized it as math. The result is: {result}"
        except:
            return "I identified it as math, but couldn’t calculate it."
    
    else:
        return "Hmm, I couldn’t classify that one."


if __name__ == "__main__":
    question = input("Ask me a question: ")
    print(generate_response(question))
