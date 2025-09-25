# Question Classifier

A simple Python script that can classify questions as **factual**, **opinion**, or **math** and give a basic response. For math questions, it can even try to solve simple calculations.

---

## How It Works

1. You type a question.  
2. The script figures out if it’s a factual, opinion-based, or math question.  
3. It then gives a response:
   - **Factual:** Suggests an answer based on information or data.  
   - **Opinion:** Acknowledges it’s subjective.  
   - **Math:** Tries to calculate the result.  

---

## How to Run

1. Make sure you have Python 3.7+ installed.  
2. Install the required package:

```bash
pip install sympy

Run the script:

python question_classifier.py


Type your question when prompted and see the response.

Example Usage

Math question:

12 + 8


Output:

I recognized it as math. The result is: 20


Factual question:

Who is the CEO of Google?


Output:

This looks like a factual question. You’d usually answer it with data or a knowledge source.


Opinion question:

What do you think about AI?


Output:

This seems like an opinion-based question. Different people may have different answers.

Future Improvements

Integrate with AI/LLM APIs for smarter responses.

Turn it into a web API using FastAPI or Flask.

Improve math solving for more complex expressions.




