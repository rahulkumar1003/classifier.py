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
