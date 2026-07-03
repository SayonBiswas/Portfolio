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
    "blurb": (
        "Passionate about technology, data, and problem-solving with a strong foundation "
        "in Python, AI/ML, and data analysis. Curious by nature, always eager to learn, "
        "and motivated by discovering innovative solutions in technology."
    ),
    "photo": "profile_photo.jpeg",  # add your photo URL here
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
        "period": "2024\u20132028",
        "text": "Focused on software engineering, data structures, and backend development. CGPA: 8.29. Actively working on real-world projects and internships alongside coursework.",
        "accent": "cyan",
    },
    {
        "degree": "BS in Data Science",
        "school": "Indian Institute of Technology, Madras (Online)",
        "period": "2024\u2013Present",
        "text": "Building expertise in data analysis, machine learning, and statistical methods. CGPA: 6.43. Applying data science principles to real-world problems and projects.",
        "accent": "violet",
    },
    {
        "degree": "Class 10 & 12",
        "school": "Valley View School, Jamshedpur",
        "period": "2009\u20132024",
        "text": "Class 12: 64.8% | Class 10: 82%. Built a strong foundation in Mathematics and Sciences leading to a career in technology.",
        "accent": "cyan",
    },
]

EXPERIENCE = [
    {
        "role": "Python Application Development Summer Intern",
        "org": "Syllogistek Systems Private Ltd.",
        "period": "Jun 2025 \u2013 Jul 2025",
        "bullets": [
            "Developed and deployed robust REST API endpoints using Python for the Silicon Campus Hub backend infrastructure",
            "Implemented API functionalities to manage campus announcements, enabling seamless data creation, retrieval, and updates",
            "Built comprehensive API logic for a Lost & Found module, allowing users to securely post and view lost or found items",
            "Designed structured JSON-based request and response formats to ensure consistent and scalable data exchange",
            "Connected API endpoints with backend database logic to ensure reliable data handling and system integrity",
        ],
    },
]

PROJECTS = [
    {
        "title": "IWT Examination Web Application",
        "description": "A comprehensive backend web application featuring a functional dashboard, secure user authentication, and a dynamic examination system with a relational database.",
        "tech": ["JSP", "PostgreSQL", "SQL"],
        "github": "https://github.com/SayonBiswas/IWT",
        "live": "https://examhub-q9ez.onrender.com",
        "image": "examhub.png",
    },
    {
        "title": "Silicon Campus Hub",
        "description": "Centralized codebase for the Python summer internship project. Collaborated on REST API integration, ensuring smooth version control and team code management.",
        "tech": ["Python", "REST APIs", "GitHub"],
        "github": "https://github.com/SayonBiswas/Summer-Internship-Python-Group-18",
    },
    {
        "title": "Student Management Website",
        "description": "A full-featured student management web application for managing student records, with a clean interface and robust backend functionality.",
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": "https://github.com/SayonBiswas/Student_Management_Website",
        "live": "https://student-management-website-iirr.onrender.com",
        "image": "student_management.png",
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

ACHIEVEMENTS = [
    {
        "title": "Electronic Arts – Software Engineering Job Simulation",
        "text": "Completed the EA Software Engineering Job Simulation, gaining hands-on exposure to real-world software engineering workflows and practices.",
        "icon": "award",
    },
    {
        "title": "Deloitte Australia – Data Analytics Job Simulation",
        "text": "Completed Deloitte Australia's Data Analytics Job Simulation, applying data analysis techniques to realistic business scenarios.",
        "icon": "trophy",
    },
    {
        "title": "Python Programming and Application Certification",
        "text": "Earned a certification in Python Programming and Application, validating core Python skills and practical development knowledge.",
        "icon": "award",
    },
]

CONTACT = {
    "email": "sayonbiswas31@gmail.com",
    "phone": "+91 9234705784",
    "phone_href": "tel:+919234705784",
}

FOOTER = {
    "name": "Sayon Biswas",
    "tagline": "Python Developer & Aspiring Data Scientist",
    "copyright": "\u00a9 2025 Sayon Biswas. All rights reserved. Built with Python.",
}