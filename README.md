# Motivational Chatbot 💬

A **motivational chatbot** built with Python (Flask), HTML, CSS, and JavaScript. The chatbot helps users by providing supportive messages, guidance, and motivational quotes or stories based on the problem they share. It’s designed to recognize common issues such as stress, confidence, or time management, and offer empathetic and encouraging responses.

---

## ✅ **Overall Concept**

This chatbot is created to support users emotionally and mentally by offering motivation in times of difficulty. It listens to the user's input, identifies the underlying problem, and responds with relevant motivational advice. If repeated inputs are detected, it shares inspiring stories to keep the user encouraged.

The chatbot is suitable for:

✔ Students struggling with studies  
✔ Professionals facing stress or burnout  
✔ Anyone needing emotional support and encouragement  

---

## 📂 **Project Structure**
```
motivating-chatbot/
│
├── backend/ # Flask backend API
│ ├── app.py # Main server logic
│ ├── config.py # Configuration settings (optional)
│ ├── chatbot/ # Chatbot modules
│ │ ├── init.py
│ │ ├── value_mapping.py # Mapping problems to motivational values
│ │ └── response_builder.py # Generate responses and quotes
│ └── utils/ # Helper functions and logging
│ ├── logger.py
│ └── helpers.py
│
├── frontend/ # User interface
│ ├── index.html # Main chat page
│ ├── styles.css # Styling for the chatbot
│ └── chatbot.js # Handles user interactions
│
├── data/ # Static data files
│ ├── problems.json # Problem keywords mapping
│ └── values.json # Motivational values and content
│
├── tests/ # Automated or manual test cases
│ ├── test_nlp_model.py
│ ├── test_response_builder.py
│ └── test_value_mapping.py
│
├── .gitignore # Ignore unnecessary files like virtual env
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── .env # Environment variables (ignored in Git)
```
---

## ✅ **Features**

✔ Recognizes user’s problem from input  
✔ Offers empathetic and motivational responses  
✔ Avoids repetition by tracking previous replies  
✔ Shares motivational stories if repeated inputs occur  
✔ Simple and clean user interface  
✔ Responsive layout for better interaction  

---

## ✅ **Technology Stack**

- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** HTML, CSS, JavaScript
- **Data Handling:** JSON files for problem mapping and motivational content
- **Environment:** Python virtual environment (`venv` or similar)
- **Version Control:** Git & GitHub  

---

## ✅ **Test Cases**

**1. Greeting Test**  
**Input:** "hello"  
**Expected Output:**  
Bot responds with a welcome message and asks for the user’s problem.

---

**2. Recognize Stress Problem**  
**Input:** "I am stressed"  
**Expected Output:**  
Bot responds with motivational advice related to stress and a supporting quote.

---

**3. Avoid Repetition**  
**Input:** Repeating "I am stressed" multiple times  
**Expected Output:**  
Bot provides a motivational story to inspire and avoid repeating responses.

---

**4. Recognize Confidence Problem**  
**Input:** "I lack confidence"  
**Expected Output:**  
Bot responds with advice from the ‘confidence’ category and a quote.

---

**5. Unknown Problem**  
**Input:** "I feel strange today"  
**Expected Output:**  
Bot responds with a general message encouraging the user.

---

**6. Multiple Issues**  
**Input:** "I need discipline and trust"  
**Expected Output:**  
Bot provides responses from both categories and a motivational quote.

---

## ✅ **How to Run**

1. Clone the repository.
2. Set up a Python virtual environment and install dependencies:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate   # On Windows
   pip install -r requirements.txt
3.Create a .env file and add any required environment variables like API keys.

4.Run the backend:
```
python backend\app.py
```
5.Open frontend/index.html in your browser.

## ✅ Future Improvements

1. Add machine learning for better problem recognition
2. Store user history for personalized responses
3. Improve UI with animations and chatbot avatars
4. Add sentiment analysis for deeper support

## 📫 Contact

Feel free to contribute, open issues, or ask questions!

Happy coding and stay motivated! 🚀✨


