"""
All portfolio content lives here as plain Python data.
Edit these values to update your site - no HTML/CSS editing needed
for text/content changes. Re-run build.py after editing.
"""

SITE = {
    "title": "Portfolio | Sayon Biswas",
    "description": "Python Developer & Aspiring Data Scientist. Explore my projects, skills, and experience.",
}

NAV_LINKS = [
    {"name": "About", "id": "about"},
    {"name": "Education", "id": "education"},
    {"name": "Experience", "id": "experience"},
    {"name": "Projects", "id": "projects"},
    {"name": "Skills", "id": "skills"},
    {"name": "Achievements", "id": "achievements"},
    {"name": "Contact", "id": "contact"},
]

SOCIALS = [
    {"name": "github",   "url": "https://github.com/SayonBiswas"},
    {"name": "linkedin", "url": "https://www.linkedin.com/in/sayonbiswas08"},
    {"name": "mail",     "url": "mailto:sayonbiswas31@gmail.com"},
]

HERO = {
    "first_name": "Sayon",
    "last_name": "Biswas",
    "role": "Python Developer & Backend Engineer",
    "subrole": "Aspiring Data Scientist",
    "blurb": "Passionate about technology, data, and problem-solving. I build thoughtful backend systems and explore the stories hidden inside data.",
    "photo": "profile_photo.jpeg",  # add your photo URL here
    "location": "Jamshedpur, India",
    "year": "2026",
}

ABOUT_TAGLINE = {
    "line1": "Curious by nature.",
    "line2": "Builder by choice.",
}

ABOUT = {
    "paragraphs": [
        "I'm Sayon Biswas, a Python developer and aspiring Data Scientist from Jamshedpur, Jharkhand. "
        "With a strong foundation in Python, AI/ML, and data analysis, I enjoy exploring new ideas and "
        "applying my skills to understand and solve complex challenges.",
        "Currently pursuing my B.Tech in Computer Software Engineering at Silicon Institute of Technology, "
        "Bhubaneswar (2024\u20132028) and simultaneously pursuing a BS in Data Science from IIT Madras (Online, 2024\u2013Present).",
    ],
    "cards": [
        {
            "title": "Key Focus",
            "text": "Building robust backend systems and REST APIs using Python, while exploring data-driven insights through AI and ML.",
        },
        {
            "title": "Approach",
            "text": "Valuing collaboration, continuous learning, and sharing knowledge with others to drive impactful project outcomes.",
        },
    ],
}

EDUCATION = [
    {
        "degree": "B.Tech in Computer Software Engineering",
        "school": "Silicon Institute of Technology (SIT), Bhubaneswar",
        "period": "2024—2028",
        "text": "Focused on software engineering, data structures, and backend development. CGPA: 8.29. Actively working on real-world projects and internships alongside coursework.",
        "accent": "cyan",
    },
    {
        "degree": "BS in Data Science",
        "school": "Indian Institute of Technology, Madras (Online)",
        "period": "2024—Present",
        "text": "Building expertise in data analysis, machine learning, and statistical methods. CGPA: 6.43. Applying data science principles to real-world problems and projects.",
        "accent": "violet",
    },
    {
        "degree": "Class 10 & 12",
        "school": "Valley View School, Jamshedpur",
        "period": "2009—2024",
        "text": "Class 12: 64.8% | Class 10: 82%. Built a strong foundation in Mathematics and Sciences leading to a career in technology.",
        "accent": "cyan",
    },
]

EXPERIENCE = [
    {
        "role": "Python Application Development Summer Intern",
        "org": "Syllogistek Systems Private Ltd.",
        "period": "Jun 2025—Jul 2025",
        "github": "https://github.com/SayonBiswas/Summer-Internship-Python-Group-18",
        "tech": ["Python", "REST APIs", "JSON", "GitHub"],
        "bullets": [
            "Worked on the Silicon Campus Hub project — a centralized campus management platform built by Group 18",
            "Developed and deployed robust REST API endpoints using Python for the Silicon Campus Hub backend infrastructure",
            "Implemented API functionalities to manage campus announcements, enabling seamless data creation, retrieval, and updates",
            "Built comprehensive API logic for a Lost & Found module, allowing users to securely post and view lost or found items",
            "Designed structured JSON-based request and response formats to ensure consistent and scalable data exchange",
            "Connected API endpoints with backend database logic to ensure reliable data handling and system integrity",
        ],
    },
]

PROJECTS_COMPLETED = [
    {
        "number": "01",
        "title": "IWT Examination Web Application",
        "description": "A comprehensive backend web application featuring a functional dashboard, secure user authentication, and a dynamic examination system with a relational database.",
        "details": "Built during my internship at Syllogistek Systems, this application demonstrates full-stack development skills with JSP, PostgreSQL, and REST API integration. The system handles user authentication, exam creation, student management, and result processing with a clean, intuitive interface.",
        "features": [
            "Secure user authentication and session management",
            "Dynamic examination creation and scheduling",
            "Real-time result processing and grading system",
            "Admin dashboard for comprehensive system management",
            "Responsive design for mobile and desktop access"
        ],
        "tech": ["JSP", "PostgreSQL", "SQL"],
        "github": "https://github.com/SayonBiswas/IWT",
        "live": "https://examhub-q9ez.onrender.com",
        "image": "examhub.png",
    },
    {
        "number": "02",
        "title": "Student Management Website",
        "description": "A full-featured student management web application for managing student records with a clean interface and robust backend functionality.",
        "details": "This student management system provides educational institutions with a comprehensive tool for managing student data, academic records, and administrative tasks. The application features a user-friendly interface with efficient CRUD operations and data visualization capabilities.",
        "features": [
            "Complete student record management (CRUD operations)",
            "Academic performance tracking and reporting",
            "Search and filter functionality for quick data access",
            "Responsive design for administrative use",
            "Data export capabilities for record keeping"
        ],
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": "https://github.com/SayonBiswas/Student_Management_Website",
        "live": "http://studentmanagement-env.eba-uup6bgvc.ap-south-2.elasticbeanstalk.com",
        "image": "student_management.png",
    },
    {
        "number": "03",
        "title": "Personal Portfolio Website",
        "description": "A fully static portfolio website built entirely with Python and Jinja2 — no JavaScript. Features dark/light theme toggle via CSS-only checkbox hack, hosted on Render.",
        "details": "This portfolio website represents my approach to clean, efficient web development without relying on JavaScript frameworks. Built using Python for template rendering and CSS for all interactivity, it demonstrates fundamental web development principles and modern CSS techniques.",
        "features": [
            "CSS-only dark/light theme toggle using checkbox hack",
            "Fully responsive design with mobile-first approach",
            "Optimized performance with no JavaScript dependencies",
            "Clean, maintainable code structure with Jinja2 templates",
            "SEO-friendly with semantic HTML structure"
        ],
        "tech": ["Python", "Jinja2", "CSS", "Render"],
        "github": "https://github.com/SayonBiswas/Portfolio",
        "live": "https://portfolio-u2go.onrender.com",
        "image": "portfolio.png",
    },
]

PROJECTS_ONGOING = [
    {
        "number": "04",
        "title": "IPL Website",
        "description": "An ongoing IPL cricket website project featuring team and player information, match details, and tournament statistics.",
        "details": "Currently in development, this IPL cricket website aims to provide comprehensive coverage of IPL tournaments with team statistics, player profiles, match schedules, and live score updates. The project focuses on creating an engaging user experience for cricket fans.",
        "features": [
            "Team profiles with detailed statistics and history",
            "Player information and performance metrics",
            "Match schedules and live score integration",
            "Tournament standings and playoff scenarios",
            "Interactive data visualization for statistics"
        ],
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": "https://github.com/SayonBiswas/IPL_Website",
        "live": "",
        "image": "",
    },
]

SKILLS = [
    {
        "category": "Programming & Technologies",
        "skills": ["Python", "Java Server Pages (JSP)", "PostgreSQL", "Git", "RESTful APIs", "JSON"],
    },
    {
        "category": "Concepts & Domains",
        "skills": ["Software Development", "Backend Web Development", "Artificial Intelligence", "Machine Learning"],
    },
    {
        "category": "Soft Skills",
        "skills": ["Team Collaboration", "Problem Solving", "Continuous Learning", "Adaptability"],
    },
]

SKILLS_FLAT = [
    "Python",
    "Java Server Pages (JSP)",
    "PostgreSQL",
    "Git",
    "RESTful APIs",
    "JSON",
    "Software Development",
    "Backend Web Development",
    "Artificial Intelligence",
    "Machine Learning",
    "Team Collaboration",
    "Problem Solving",
    "Continuous Learning",
    "Adaptability",
]

ACHIEVEMENTS = [
    {
        "title": "CodeVerse – Certificate of Participation",
        "text": "Participated in CodeVerse, held as part of NIRMAN 5.0 organized by the Silicon Innovation and Promotion Cell (SIPC) at Silicon University, Odisha, from 28th–30th November 2025 and went upto the 3rd/final round of the competition.",
        "icon": "trophy",
        "image": "CodeVerse.jpeg",
    },
]

CERTIFICATIONS = [
    {
        "title": "Electronic Arts – Software Engineering Job Simulation",
        "text": "Completed the EA Software Engineering Job Simulation, gaining hands-on exposure to real-world software engineering workflows.",
        "icon": "award",
        "image": "EA.jpeg",
    },
    {
        "title": "Deloitte Australia – Data Analytics Job Simulation",
        "text": "Completed Deloitte Australia's Data Analytics Job Simulation, applying data analysis techniques to realistic business scenarios.",
        "icon": "trophy",
        "image": "Delloite.jpeg",
    },
    {
        "title": "Python Programming and Application",
        "text": "Earned a certification in Python Programming and Application, validating core Python skills and practical development knowledge.",
        "icon": "award",
        "image": "Python.jpeg",
    },
]

CONTACT = {
    "email": "sayonbiswas31@gmail.com",
    "phone": "+91 9234705784",
    "phone_href": "tel:+919234705784",
    "note": "Feel free to reach out — I'm always excited to connect and discuss new opportunities!",
    "resume": "Sayon_Biswas_Resume.pdf",  # Add your resume file name here
}

FOOTER = {
    "name": "Sayon Biswas",
    "tagline": "Python Developer & Aspiring Data Scientist",
    "copyright": "© 2026 Sayon Biswas. Built with precision.",
    "tagline_line1": "Let's make",
    "tagline_line2": "something useful.",
}