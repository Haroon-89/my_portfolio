from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Your information - EDIT THIS!
MY_INFO = {
    'name': 'Haroon Iqbal',
    'title': 'AI/ML Engineer & Full Stack Developer',
    'about': "B.Tech CSE student who is passionate about Artificial Intelligence and Machine Learning. I love exploring how AI can be used to solve meaningful problems, especially in the healthcare field. I enjoy learning new tools and putting them into real web applications so people can actually use what I build. I am currently improving my skills in deep learning, computer vision and full-stack development using Python, Java, Flask, and SQL. I like working on practical projects and always try to create something that has real value. My long-term goal is to become an AI/ML Engineer and work on innovative technologies that can make life easier for people.",
    'location': 'Bhubaneswar, Odisha, India',
    
    # Contact Links
    'email': 'harooniqbal829@gmail.com',
    'phone': '+917889615224',
    'github': 'https://github.com/Haroon-89',
    'linkedin': 'https://linkedin.com/in/haroon-iqbal-drabu',
    'whatsapp': '+917889615224',
    
    # Profile Image
    'profile_pic': 'psp.png',
    
    # Skills
    'skills': [
        'Python', 'TensorFlow', 'Keras', 'PyTorch',
        'Flask', 'Streamlit', 'Machine Learning',
        'Deep Learning', 'Computer Vision', 'Data Analysis',
        'Pandas', 'NumPy', 'SQL', 'Git', 'Java', 'JDBC', 'MySQL'
    ],
    
    # Resume Files
    'resumes': [
        {'name': 'Europass CV', 'file': 'europass_cv.pdf', 'icon': 'fa-file-pdf'},
        {'name': 'Simple CV', 'file': 'simple_cv.pdf', 'icon': 'fa-file-pdf'}
    ],
    
    # Educational Certificates
    'education_docs': [
        {'name': '10th Marksheet', 'file': '10th_marksheet.pdf', 'year': '2019'},
        {'name': '12th Marksheet', 'file': '12th_marksheet.pdf', 'year': '2021'},
        {'name': 'B.Tech CGPA Card', 'file': 'graduation_cgpa.pdf', 'year': 'Current'}
    ],
    
    # Course Certificates
    'certificates': [
        {'name': 'IBM Data Science', 'file': 'DS.pdf', 'issuer': 'Coursera'},
        {'name': 'IBM Cybersecurity', 'file': 'IBM Cybersecurity.pdf', 'issuer': 'Coursera'},
        {'name': 'Palo Alto Cybersecurity', 'file': 'Palo Alto.pdf', 'issuer': 'Coursera'}
    ],
    
    # Awards & Achievements
    'awards': [
        {
            'name': 'B.Tech Scholarship Winner',
            'description': 'Received merit-based scholarship for academic excellence from AICTE',
            'file': 'allotment_letter.pdf',
            'year': '2023'
        }
    ],
    
    # ALL Your Projects
    'projects': [
        {
            'title': 'Diabetic Retinopathy Detection System',
            'description': 'AI-powered web application for automated detection of Diabetic Retinopathy from retinal fundus images using EfficientNetB3 deep learning architecture.',
            'image': 'diabetic.png',
            'tech': ['Python', 'TensorFlow', 'Streamlit', 'Deep Learning'],
            'features': [
                '96.97% model accuracy',
                'Batch processing support',
                'Real-time predictions',
                'Downloadable reports'
            ],
            'demo': 'https://diabetic-retinopathy-detection-89.streamlit.app/',
            'github': 'https://github.com/Haroon-89/diabetic-retinopathy-detection'
        },
        {
            'title': 'Startup Funding Analysis Dashboard',
            'description': 'Interactive Streamlit dashboard providing detailed insights into Indian startup funding trends with comprehensive data visualization and analytics.',
            'image': 'startup.png',
            'tech': ['Python', 'Streamlit', 'Pandas', 'Matplotlib', 'Seaborn'],
            'features': [
                'MoM funding trends',
                'Sector-wise analysis',
                'Investor insights',
                'Interactive visualizations'
            ],
            'demo': 'https://finance-data-analysis-deewukgm5kzrprcyum5gsn.streamlit.app/',
            'github': 'https://github.com/Haroon-89/startup-funding-analysis'
        },
        {
            'title': 'Book Recommendation System',
            'description': 'A web application using content and collaborative-based filtering to provide personalized book recommendations and showcase the top 50 most popular books.',
            'image': 'book_recommendation.png',
            'tech': ['Python', 'Flask', 'Pandas', 'NumPy', 'Bootstrap'],
            'features': [
                'Content & Collaborative Filtering',
                'Top 50 Popular Books Display',
                'Book Search & Recommendation Feature',
                'Simple, Responsive Web Interface'
            ],
            'demo': 'https://book-recommendation-system-wxru.onrender.com/',
            'github': 'https://github.com/Haroon-89/Book-Recommendation-System'
        },
        {
            'title': 'IPL Stats Web App',
            'description': 'A Flask-based web application with a modular API backend for detailed exploration of Indian Premier League (IPL) cricket statistics, including team records, head-to-head, and player performance.',
            'image': 'ipl.png',
            'tech': ['Python', 'Flask', 'Pandas', 'NumPy', 'Jinja2'],
            'features': [
                'Modular API Backend (Flask)',
                'Team Records & Head-to-Head Matchups',
                'Detailed Batting and Bowling Player Stats',
                'Responsive UI with Dropdown Selectors'
            ],
            'demo': 'http://localhost:8000/',
            'github': 'https://github.com/Haroon-89/IPL-Api-Web-Services'
        },
        {
            'title': 'Railway Reservation System (CLI)',
            'description': 'A Command-Line Interface (CLI) based Railway Reservation and Ticketing System built in Java, featuring separate Admin and User roles for managing trains, booking tickets, and viewing/cancelling reservations.',
            'image': 'railway.png',
            'tech': ['Java', 'JDBC', 'MySQL', 'CLI'],
            'features': [
                'Dual-Role Access (Admin/User)',
                'Admin: Add, View, and Cancel Trains',
                'User: Signup, Login, Book, View, and Cancel Tickets',
                'Data Persistence via MySQL/JDBC'
            ],
            'demo': 'N/A (CLI Project)',
            'github': 'https://github.com/Haroon-89/Railway_Reservation_System_Project'
        },
        {
            'title': 'SIH 2024: Museum Chatbot Ticketing System',
            'description': 'Official solution for SIH-1648 (Ministry of Culture): A full-stack, multilingual chatbot-based ticketing system for museums, integrating payment, advanced analytics, and supporting all booking types to eliminate manual errors and long queues.',
            'image': 'museum.png',
            'tech': ['Next.js', 'TypeScript', 'Chatbot/AI', 'Payment Gateway', 'Vercel'],
            'features': [
                'Multilingual Chatbot Booking',
                'Integrated Payment Gateway',
                'Automated Ticket & Show Booking',
                'Data Analytics for Decision Making',
                'Efficient High-Volume Handling'
            ],
            'demo': 'https://heritage-app-gamma.vercel.app/',
            'github': 'https://github.com/Haroon-89/Heritage-app'
        },
        {
            'title': 'Data Visualization of India (Streamlit)',
            'description': 'An interactive Streamlit dashboard for visualizing demographic data across Indian states and districts using Plotly geographic scatter plots, allowing for parameter-based bubble sizing and coloring.',
            'image': 'india.png',
            'tech': ['Python', 'Streamlit', 'Pandas', 'Plotly', 'Data Visualization'],
            'features': [
                'Interactive Geographic Scatter Plots',
                'State and Parameter Selection',
                'Bubble Size and Color Mapping (Primary/Secondary Parameters)',
                'District Name Tooltips on Hover'
            ],
            'demo': '',
            'github': 'https://github.com/Haroon-89/DataMap-India'
        },
        {
            'title': 'SpaceX Falcon 9 Landing Prediction (ML)',
            'description': 'An end-to-end Data Science capstone project predicting the Falcon 9 first stage landing success using historical data collected via API/web scraping, wrangled, analyzed with SQL, and modeled with Scikit-learn (Best Model: Logistic Regression, 83% accuracy).',
            'image': 'falcon.png',
            'tech': ['Python', 'Scikit-learn', 'Pandas', 'SQLAlchemy', 'BeautifulSoup', 'Matplotlib'],
            'features': [
                'End-to-End Data Science Pipeline',
                'Data Collection via API & Web Scraping',
                'EDA and Insight Generation with SQL/Visualization',
                'Machine Learning Model Comparison (Logistic Regression, SVM, KNN, Tree)',
                'Key Finding: Success rate rises sharply post-2015'
            ],
            'demo': 'N/A (Jupyter Notebooks)',
            'github': 'https://github.com/Haroon-89/SpaceX-Landing-Predictor'
        },
        {
            'title': 'NLPApp: Desktop NLP Application',
            'description': 'A Python desktop application with a Tkinter GUI for performing key Natural Language Processing (NLP) tasks, including Sentiment Analysis, Named Entity Recognition (NER), and Emotion Detection, leveraging the paralleldots API.',
            'image': 'nlp.png',
            'tech': ['Python', 'Tkinter', 'NLP', 'API Integration', 'JSON'],
            'features': [
                'Graphical User Interface (GUI) built with Tkinter',
                'Secure User Authentication (Login/Signup)',
                'Sentiment Analysis (Positive, Negative, Neutral)',
                'Named Entity Recognition (NER)',
                'Emotion Detection'
            ],
            'demo': 'N/A (Desktop App)',
            'github': 'https://github.com/Haroon-89/NLPApp'
        }
    ]
}

@app.route('/')
def home():
    return render_template('home.html', info=MY_INFO)

@app.route('/projects')
def projects():
    return render_template('projects.html', info=MY_INFO)

@app.route('/credentials')
def credentials():
    return render_template('credentials.html', info=MY_INFO)

# Route to download documents
@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    directory = os.path.join(app.static_folder, 'documents', folder)
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)