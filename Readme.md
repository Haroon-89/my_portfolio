# Haroon Iqbal - Portfolio Website

A modern, dark-themed portfolio website built with Flask showcasing my projects, skills, and credentials.

**Live Demo:** [Your Deployed URL Here]

## Features

- Dark theme design with blue accents
- Responsive layout for all devices
- Animated typing effect for job titles
- Project showcase with live demos
- Downloadable resume and certificates
- Educational documents section
- Awards and achievements display
- One-click contact via Email, WhatsApp, LinkedIn, and GitHub

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap 5, Custom CSS
- **Icons:** Font Awesome 6
- **Deployment:** [Platform Name]

## Project Structure
my-portfolio/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   ├── base.html              # Base template with navbar & footer
│   ├── home.html              # Homepage with hero section
│   ├── projects.html          # Projects showcase page
│   └── credentials.html       # Resume, certificates, awards
└── static/
    ├── css/
    │   └── style.css          # Dark theme styles
    ├── images/
    │   ├── psp.png            # Profile picture
    │   ├── diabetic.png       # Project screenshots
    │   ├── startup.png
    │   ├── book_recommendation.png
    │   ├── ipl.png
    │   ├── railway.png
    │   ├── museum.png
    │   ├── india.png
    │   ├── falcon.png
    │   └── nlp.png
    └── documents/
        ├── resumes/
        │   ├── europass_cv.pdf
        │   └── simple_cv.pdf
        ├── certificates/
        │   ├── 10th_marksheet.pdf
        │   ├── 12th_marksheet.pdf
        │   ├── graduation_cgpa.pdf
        │   └── [course_certificates].pdf
        └── awards/
            └── scholarship_letter.pdf

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/Haroon-89/portfolio-website.git
cd portfolio-website
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Add Your Documents

Place your files in the following folders:

**Images** (`static/images/`):
- Profile picture: `psp.png`
- Project screenshots: `[project_name].png`

**Documents** (`static/documents/`):
- `resumes/` - Your CV files
- `certificates/` - Marksheets and course certificates
- `awards/` - Award letters and achievements

### Step 5: Run the Application
```bash
python app.py
```

Visit: `http://localhost:5000`

## Configuration

Edit `app.py` to customize your information:
```python
MY_INFO = {
    'name': 'Your Name',
    'email': 'your.email@example.com',
    'phone': '+91XXXXXXXXXX',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'whatsapp': '+91XXXXXXXXXX',
    # ... add your details
}
```

## Pages

### Home (`/`)
- Hero section with profile picture
- Animated job title rotation
- Skills showcase
- Featured projects

### Projects (`/projects`)
- All 9 projects with detailed information
- Live demo links
- GitHub repository links
- Technology stack for each project

### Credentials (`/credentials`)
- Downloadable resumes (Europass & Simple CV)
- Educational documents (10th, 12th, B.Tech)
- Course certificates
- Awards and achievements

## Projects Included

1. **Diabetic Retinopathy Detection System** - AI/ML Healthcare
2. **Startup Funding Analysis Dashboard** - Data Analytics
3. **Book Recommendation System** - Machine Learning
4. **IPL Stats Web App** - Data Visualization
5. **Railway Reservation System** - Java/MySQL
6. **Museum Chatbot Ticketing System** - SIH 2024 Winner
7. **Data Visualization of India** - Streamlit Dashboard
8. **SpaceX Falcon 9 Landing Prediction** - Data Science
9. **NLPApp** - Natural Language Processing

## Deployment

### Deploy to Render

1. Create `render.yaml`:
```yaml
services:
  - type: web
    name: portfolio
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

2. Add `gunicorn` to `requirements.txt`
3. Push to GitHub and connect to Render

### Deploy to PythonAnywhere

1. Upload files to PythonAnywhere
2. Create virtual environment
3. Install dependencies
4. Configure WSGI file
5. Reload web app

## Features Breakdown

### Dark Theme
- Professional dark color scheme
- Blue accent colors (#0d6efd)
- Smooth hover effects with glow
- Custom dark scrollbar

### Animations
- Typing/rotating job titles
- Card hover lift effects
- Smooth transitions
- Fade-in effects

### Responsive Design
- Mobile-first approach
- Breakpoints for tablets and desktops
- Optimized images
- Touch-friendly buttons

### Contact Integration
- Direct email links
- WhatsApp click-to-chat
- LinkedIn profile
- GitHub repositories

## Customization

### Change Colors

Edit CSS variables in `static/css/style.css`:
```css
:root {
    --bg-primary: #0a0a0a;      /* Main background */
    --bg-secondary: #1a1a1a;    /* Section backgrounds */
    --bg-card: #2d2d2d;         /* Card backgrounds */
    --text-primary: #ffffff;     /* Main text */
    --accent-color: #0d6efd;    /* Blue accent */
}
```

### Add More Projects

Add to the `projects` list in `app.py`:
```python
{
    'title': 'Project Name',
    'description': 'Project description',
    'image': 'project_image.png',
    'tech': ['Tech1', 'Tech2'],
    'features': ['Feature 1', 'Feature 2'],
    'demo': 'https://demo-link.com',
    'github': 'https://github.com/repo'
}
```

### Update Skills

Modify the `skills` list in `app.py`:
```python
'skills': [
    'Skill 1', 'Skill 2', 'Skill 3'
]
```

## Technologies Used

- **Flask** - Python web framework
- **Bootstrap 5** - Responsive CSS framework
- **Font Awesome** - Icon library
- **JavaScript** - Dynamic animations
- **HTML5/CSS3** - Modern web standards

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Performance

- Optimized images
- Minimal JavaScript
- Fast page loads
- Efficient CSS
- CDN for libraries

## Security

- No sensitive data in code
- Environment variables for secrets
- Secure file downloads
- HTTPS recommended for deployment

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Contact

**Haroon Iqbal**
- Email: harooniqbal829@gmail.com
- LinkedIn: [linkedin.com/in/haroon-iqbal-drabu](https://linkedin.com/in/haroon-iqbal-drabu)
- GitHub: [github.com/Haroon-89](https://github.com/Haroon-89)
- WhatsApp: +917889615224

## Acknowledgments

- Bootstrap team for the CSS framework
- Font Awesome for icons
- Flask community for documentation
- All open-source contributors

## Future Enhancements

- [ ] Blog section
- [ ] Admin panel for easy updates
- [ ] Dark/Light theme toggle
- [ ] Multi-language support
- [ ] Contact form with backend
- [ ] Analytics integration
- [ ] SEO optimization
- [ ] Progressive Web App (PWA)

---

**Made with ❤️ by Haroon Iqbal**

If you like this project, please give it a star!