import streamlit as st
import time # Used to simulate AI response time
import json # Used for structuring quiz data

# --- Configuration and Styling ---

# Set wide layout and page title
st.set_page_config(
    page_title="AI Learning & Quiz Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to mimic a modern, Tailwind-like dashboard look
# This includes shadows, rounded corners, and a clean primary color.
def load_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        html, body, [class*="stApp"] {
            font-family: 'Inter', sans-serif;
        }
        
        /* Main background color */
        .stApp {
            background-color: #f7f9fc;
        }

        /* Customize main Streamlit components (like buttons/select boxes) */
        .stButton>button {
            border-radius: 8px;
            border: 1px solid #4a90e2;
            background-color: #4a90e2;
            color: white;
            padding: 10px 20px;
            font-weight: 600;
            transition: all 0.2s ease;
        }
        .stButton>button:hover {
            background-color: #3b7ac8;
            border-color: #3b7ac8;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        /* Custom Card Styles for Dashboard feel */
        .dashboard-card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.08);
            margin-bottom: 20px;
            height: 100%; /* Ensure columns fill height */
        }
        
        .card-header {
            font-size: 1.25rem;
            font-weight: 700;
            color: #333;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
        }
        
        /* Style for the answer result */
        .correct-answer {
            color: green;
            font-weight: bold;
        }
        .incorrect-answer {
            color: red;
            font-weight: bold;
        }
        
        /* Responsive column styling (Streamlit columns already handle some of this) */
        /* Custom alert/feedback boxes */
        .feedback-box {
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-weight: 500;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .warning {
            background-color: #fff3cd;
            color: #856404;
            border: 1px solid #ffeeba;
        }

        </style>
        """, unsafe_allow_html=True)

# Load CSS
load_css()

# --- Quiz Data Structure ---
QUIZ_DATA = {
    "q1": {
        "question": "What is the primary function of a Convolutional Neural Network (CNN)?",
        "options": ["Processing Sequential Data", "Image Recognition", "Generating Text", "Database Management"],
        "answer": "Image Recognition",
        "explanation": "CNNs are specifically designed to process pixel data, making them highly effective for computer vision tasks like image recognition and object detection."
    },
    "q2": {
        "question": "Which Python library is most commonly used for numerical computing and array manipulation in AI/ML?",
        "options": ["Pandas", "Matplotlib", "NumPy", "Scikit-learn"],
        "answer": "NumPy",
        "explanation": "NumPy (Numerical Python) is the foundational library for scientific computing in Python, providing efficient array and matrix operations essential for all ML algorithms."
    },
    "q3": {
        "question": "What problem does the Vanishing Gradient address in deep learning?",
        "options": ["Overfitting in CNNs", "Gradients becoming too large during backpropagation", "Gradients becoming too small, hindering training", "Poor memory management"],
        "answer": "Gradients becoming too small, hindering training",
        "explanation": "The Vanishing Gradient problem occurs when the gradient values shrink as they propagate backward through layers, slowing down or stopping the learning process in initial layers."
    }
}

# --- State Initialization ---
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'user_answers' not in st.session_state:
    # Initialize answers with None
    st.session_state.user_answers = {q_id: None for q_id in QUIZ_DATA}

# --- Core Functions ---

def submit_quiz():
    """Handles the quiz submission and sets the state."""
    # Collect all current radio button values
    for q_id in QUIZ_DATA:
        # We assume the key for the input is the question ID
        st.session_state.user_answers[q_id] = st.session_state.get(f'radio_{q_id}', None)
    
    st.session_state.quiz_submitted = True
    st.toast("Quiz Submitted! Check your results below.", icon="🎉")

def reset_quiz():
    """Resets the quiz state and form values."""
    st.session_state.quiz_submitted = False
    st.session_state.user_answers = {q_id: None for q_id in QUIZ_DATA}
    st.toast("Quiz reset. You can try again!", icon="🔄")


@st.cache_data
def generate_ai_response(prompt):
    """
    Placeholder for an actual LLM API call.
    In a real application, you would replace this with:
    1. A call to the Gemini API (as outlined in the instructions)
    2. Or another LLM service (OpenAI, Anthropic, etc.)
    
    The @st.cache_data ensures the response is cached unless the prompt changes.
    """
    if not prompt:
        return "Please enter a question about AI/ML to get an answer."

    # Simulate network delay and LLM processing
    time.sleep(1.5) 
    
    # Simple simulated response based on keywords
    prompt_lower = prompt.lower()
    if "python" in prompt_lower or "library" in prompt_lower:
        response = "Python is the dominant language for AI/ML. Key libraries include *NumPy* for numerical operations, *Pandas* for data handling, and frameworks like *TensorFlow* and *PyTorch* for deep learning model building."
    elif "neural network" in prompt_lower or "nn" in prompt_lower:
        response = "A Neural Network (NN) is a series of algorithms that tries to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates. They consist of input, hidden, and output layers."
    else:
        response = f"That's an excellent question! The field of AI is vast. For your query regarding '{prompt}', the core concept involves optimizing algorithms like Gradient Descent across large datasets to minimize an error function (loss). Would you like a deeper dive into a specific algorithm?"
        
    # In a real app, you would add citations/grounding metadata here if using the Google Search tool.
    return response


# --- UI Layout ---

st.title("🧠 AI Learning Dashboard")
st.markdown("Dive into the world of Artificial Intelligence with interactive quizzes and an instant learning assistant.")

# Use columns for a responsive, two-panel dashboard layout
col1, col2 = st.columns(2)

# =======================================================
# COLUMN 1: AI Knowledge Quiz
# =======================================================
with col1:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">🚀 AI Knowledge Quiz</div>', unsafe_allow_html=True)
    
    correct_count = 0
    
    # Create the quiz form
    with st.form("ai_quiz_form"):
        for q_id, data in QUIZ_DATA.items():
            # Display question and radio options
            user_selection = st.radio(
                f"{data['question']}",
                data['options'],
                key=f'radio_{q_id}',
                # Disable the options if the quiz is submitted
                disabled=st.session_state.quiz_submitted,
            )
            
            # Store the current selection (important for grading)
            st.session_state.user_answers[q_id] = user_selection
            
            # Display results after submission
            if st.session_state.quiz_submitted:
                if st.session_state.user_answers.get(q_id) == data['answer']:
                    correct_count += 1
                    st.markdown(f'<p class="correct-answer">✅ Correct! </p>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<p class="incorrect-answer">❌ Incorrect. The correct answer is: *{data["answer"]}*</p>', unsafe_allow_html=True)
                
                # Always show the detailed explanation
                with st.expander(f"Explanation for Q{q_id[-1]}"):
                    st.info(data['explanation'])
            
            st.markdown("---") # Separator between questions
        
        # Form submission buttons in two internal columns
        col_submit, col_reset = st.columns(2)
        
        with col_submit:
            st.form_submit_button("Submit Quiz", on_click=submit_quiz, disabled=st.session_state.quiz_submitted)
        with col_reset:
            st.form_submit_button("Reset Quiz", on_click=reset_quiz, disabled=not st.session_state.quiz_submitted)

    # Final Score Display
    if st.session_state.quiz_submitted:
        total_questions = len(QUIZ_DATA)
        score = f"{correct_count}/{total_questions}"
        percentage = (correct_count / total_questions) * 100
        
        if percentage == 100:
            feedback_class = "success"
            message = "Flawless! You have a deep understanding of these AI concepts. Keep learning!"
        elif percentage >= 66:
            feedback_class = "warning"
            message = "Great Job! You have a solid grasp of the material. Review the explanations to perfect your knowledge."
        else:
            feedback_class = "warning"
            message = "Good start! Keep practicing and reviewing the concepts. The AI assistant can help clarify things!"
            
        st.markdown(f"""
            <div class='feedback-box {feedback_class}'>
                *Your Score: {score} ({percentage:.0f}%)*
                <br>{message}
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =======================================================
# COLUMN 2: AI Learning Assistant
# =======================================================
with col2:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">🤖 AI Learning Assistant</div>', unsafe_allow_html=True)
    st.info("Ask any question about AI, Machine Learning, or Deep Learning concepts.")
    
    # Input area for the prompt
    prompt = st.text_area(
        "Enter your learning query:", 
        height=100, 
        placeholder="e.g., Explain the difference between supervised and unsupervised learning.",
        key="assistant_prompt"
    )

    # Button to generate the response
    if st.button("Get AI Explanation"):
        if prompt:
            # Use the spinner to show loading while the 'AI' thinks
            with st.spinner('Generating insightful explanation...'):
                response_text = generate_ai_response(prompt)
                
            # Store and display the response
            st.session_state.last_response = response_text
            st.subheader("AI Assistant Response:")
            st.markdown(response_text)
            
            # Note about grounding metadata (important for real LLM use)
            st.caption("(Note: In a real-world application, this is where grounding citations and links would appear if the AI used web search to answer the query.)")
        else:
            st.warning("Please enter a prompt before asking for an explanation.")

    # Show the last response if it exists and the button wasn't clicked again with an empty prompt
    elif 'last_response' in st.session_state and st.session_state.last_response:
        st.subheader("AI Assistant Response:")
        st.markdown(st.session_state.last_response)
        
    st.markdown('</div>', unsafe_allow_html=True)

# =======================================================
# Sidebar & Footer
# =======================================================

with st.sidebar:
    st.header("App Navigation")
    st.markdown("This Streamlit application demonstrates a simple two-module AI learning environment.")
    st.markdown("""
    *Features:*
    - *Interactive Quiz:* Test your knowledge on core AI concepts.
    - *AI Assistant:* Get instant explanations for complex topics.
    - *Responsive Design:* Utilizes Streamlit's layout for adaptability.
    - *Custom Styling:* Injected CSS for a modern, dashboard feel.
    """)
    st.markdown("---")
    st.markdown("Built with Python & Streamlit.")