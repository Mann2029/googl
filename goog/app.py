import os
import random
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
# To work with PDFs, you need PyMuPDF
# Install it using: pip install PyMuPDF
import fitz  # PyMuPDF

# --- Configuration ---
# Creates a folder named 'uploads' in the same directory as this script.
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
# This is crucial! It allows your HTML files to make requests to this Python server.
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the uploads folder if it doesn't exist.
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- PDF Scoring Placeholder Functions ---

def convert_pdf_to_image(file_path):
    """
    Uses PyMuPDF to open the PDF. In a real app, this would
    return image data for computer vision processing.
    """
    try:
        pdf_document = fitz.open(file_path)
        if len(pdf_document) > 0:
            print(f"Successfully opened and verified '{file_path}'.")
            pdf_document.close()
            return True
        else:
            pdf_document.close()
            return False
    except Exception as e:
        print(f"Error processing PDF file: {e}")
        return False

def analyze_image_for_marks():
    """
    Placeholder: This is where the core computer vision logic (e.g., OpenCV) would go.
    For this demo, we just return a random score.
    """
    print("--- Simulating analysis of marked bubbles ---")
    num_questions = 50
    correct_answers = random.randint(30, num_questions)
    return correct_answers, num_questions

def scan_marks_from_pdf(file_path):
    """
    Orchestrates the simulated OMR (Optical Mark Recognition) process.
    It now raises an exception if PDF processing fails.
    """
    print(f"--- Starting mark scanning for: {file_path} ---")
    
    if not convert_pdf_to_image(file_path):
        raise ValueError("Failed to process the PDF file. It might be corrupt or empty.")

    final_score, max_score = analyze_image_for_marks()

    filename = os.path.basename(file_path)
    if 'midterm' in filename.lower():
        test_name = "Math Mid-term"
    elif 'quiz' in filename.lower():
        test_name = "Science Quiz"
    else:
        test_name = "General Assessment"
        
    return {
        "test_name": f"{test_name} ({random.randint(100,999)})",
        "score": final_score,
        "max_score": max_score,
    }

# --- Timetable Generation Functions ---

def generate_mock_timetable():
    """
    Simulates an intelligent timetable generation process.
    In a real-world scenario, this would involve complex constraint satisfaction algorithms.
    """
    print("--- Simulating AI timetable generation ---")
    subjects = ["Math", "Science", "History", "English", "Art", "P.E."]
    teachers = ["Mr. Smith", "Ms. Jones", "Mr. Chen", "Mrs. Davis", "Ms. Lee"]
    rooms = ["101", "102", "201", "202", "Gym", "Art Studio"]
    time_slots = ["09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "13:00 - 14:00", "14:00 - 15:00"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    timetable = {day: [] for day in days}
    class_count = 0

    for day in days:
        for time in time_slots:
            # Simulate scheduling for 10 different classes/grades simultaneously
            for _ in range(10): 
                subject = random.choice(subjects)
                teacher = random.choice(teachers)
                room = random.choice(rooms)
                timetable[day].append({
                    "time": time,
                    "subject": subject,
                    "teacher": teacher,
                    "room": room
                })
                class_count += 1

    stats = {
        "classesScheduled": class_count,
        "conflictsResolved": 12 
    }
    
    return {
        "timetable": timetable,
        "stats": stats
    }

# --- AI Student Dashboard Generation ---

def generate_student_dashboard_data():
    """
    Simulates a sophisticated AI analysis to generate a student's dashboard.
    In a real app, this would query a database for the student's actual performance.
    """
    print("--- Simulating AI analysis for student dashboard ---")
    
    learning_paces = ["Below Average", "Average", "Above Average", "Fast"]
    subjects = ["Mathematics", "Science", "English", "History"]
    
    # Simulate overall stats
    completion_rate = random.randint(60, 95)
    strong_topics_count = random.randint(5, 15)
    
    # AI logic for determining review topics
    review_topics_count = 0
    if completion_rate < 75:
        review_topics_count = random.randint(4, 6)
    else:
        review_topics_count = random.randint(1, 3)

    # Simulate detailed learning profile
    profile = {
        "learningPace": random.choice(learning_paces),
        "retentionRate": random.randint(70, 98),
        "focusTime": f"{random.randint(25, 55)}m"
    }
    
    # Simulate a personalized schedule
    schedule = [
        { "time": "9:00 AM - Mathematics", "topic": "Quadratic Equations", "difficulty": "Medium", "status": "Completed" },
        { "time": "10:30 AM - Biology", "topic": "Photosynthesis", "difficulty": "Easy", "status": "In Progress" },
        { "time": "2:00 PM - History", "topic": "World War II", "difficulty": "Hard", "status": "Pending" }
    ]
    random.shuffle(schedule) # Mix up the order for variety

    # Simulate AI feedback
    feedback = [
        { 
            "type": "positive", 
            "title": f"Great Progress in {random.choice(subjects)}!", 
            "description": f"You've mastered {random.choice(['core concepts', 'advanced topics'])} {random.randint(15, 30)}% faster than average. Keep it up!"
        },
        { 
            "type": "review", 
            "title": "Review Recommended: Organic Chemistry", 
            "description": "Your last quiz showed some gaps. We've added 3 flashcards to help reinforce concepts."
        }
    ]

    # Simulate progress in different subjects
    progress = [
        {"subject": "Mathematics", "value": random.randint(70, 95)},
        {"subject": "Science", "value": random.randint(65, 85)},
        {"subject": "English", "value": random.randint(80, 98)},
        {"subject": "History", "value": random.randint(50, 75)}
    ]
    
    # Simulate identified strengths and gaps
    strengths = ["Algebra", "Literature Analysis", "Critical Thinking", "Problem Solving"]
    gaps = ["Organic Chemistry", "Grammar", "Ancient History", "Data Structures"]

    return {
        "stats": {
            "learningPace": profile["learningPace"],
            "completionRate": completion_rate,
            "strongTopics": strong_topics_count,
            "topicsToReview": review_topics_count
        },
        "profile": profile,
        "schedule": schedule,
        "feedback": feedback,
        "progress": progress,
        "skills": {
            "strengths": random.sample(strengths, k=3),
            "gaps": random.sample(gaps, k=3)
        },
        "recommendation": f"Based on your learning pattern, I recommend focusing on {random.randint(2,4)} short study sessions ({random.randint(20, 30)} minutes) with 5-minute breaks."
    }

# --- API Endpoints ---

@app.route('/upload_and_score', methods=['POST'])
def upload_file():
    """Handles the file upload for OMR scoring."""
    if 'answerSheet' not in request.files:
        return jsonify({"success": False, "message": "No file part in the request"}), 400
    
    file = request.files['answerSheet']
    
    if file.filename == '':
        return jsonify({"success": False, "message": "No file selected for uploading"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"success": False, "message": "Allowed file type is PDF (.pdf) only"}), 400

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        scoring_result = scan_marks_from_pdf(filepath)
        
        # os.remove(filepath) # Optional: clean up file after processing
        
        return jsonify({
            "success": True,
            "data": scoring_result 
        }), 200
        
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/generate_timetable', methods=['POST'])
def generate_timetable_endpoint():
    """Handles the request to generate a new school timetable."""
    try:
        timetable_data = generate_mock_timetable()
        return jsonify({
            "success": True,
            "message": "Timetable generated successfully!",
            "data": timetable_data
        }), 200
    except Exception as e:
        print(f"An error occurred during timetable generation: {e}")
        return jsonify({"success": False, "message": "Could not generate timetable."}), 500

@app.route('/get_student_dashboard', methods=['GET'])
def get_student_dashboard():
    """Endpoint to provide the AI-generated student dashboard data."""
    try:
        dashboard_data = generate_student_dashboard_data()
        return jsonify({
            "success": True,
            "data": dashboard_data
        }), 200
    except Exception as e:
        print(f"An error occurred during dashboard generation: {e}")
        return jsonify({"success": False, "message": "Could not generate dashboard data."}), 500


if __name__ == '__main__':
    # debug=True automatically reloads the server when you save changes.
    app.run(debug=True, port=5000)