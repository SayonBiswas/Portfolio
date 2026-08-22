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
        "title": "ExamHub",
        "number": "01",  # change to match your numbering
        "status": "completed",  # "completed" | "ongoing"
        "image": "examhub.png",  # e.g. "examhub_preview.png" — place in static/
        "description": (
            "An online exam management system built with Java + JSP + PostgreSQL, "
            "featuring AI-powered question generation via Google Gemini, async job "
            "processing, and a hardened security layer — all containerised with Docker."
        ),
        "tech": ["Java 21", "JSP", "Tomcat 9", "PostgreSQL", "Gemini AI", "Docker", "Maven", "BCrypt"],

        # ── Extended case study fields (used by project.html.j2) ──

        "details": (
            "Built as an IWT lab project with Suranjeet Behera. The system handles "
            "student registration, role-based dashboards, AI-generated question sets by "
            "topic, timed exams, result analytics, PDF report merging, and a full admin "
            "control panel — all served from a single Tomcat 9 servlet container."
        ),

        "stats": [
            {"value": "5+", "label": "Security Layers"},
            {"value": "15s", "label": "AI Response (async)"},
            {"value": "100%", "label": "Prepared Statements"},
            {"value": "3", "label": "User Roles"},
        ],

        "feature_cards": [
            {
                "icon": "🤖",
                "title": "AI Question Generation",
                "description": (
                    "Google Gemini generates topic-specific MCQs on demand. "
                    "An async JobStore runs generation off the HTTP thread; "
                    "the browser polls for completion every 2 seconds."
                ),
            },
            {
                "icon": "📋",
                "title": "Role-Based Dashboards",
                "description": (
                    "Three roles — Student, Teacher, Admin — each with a dedicated "
                    "dashboard. Admins see live analytics, manage users, and "
                    "download merged PDF reports via Apache PDFBox."
                ),
            },
            {
                "icon": "⏱️",
                "title": "Timed Exam Engine",
                "description": (
                    "Exams run with a server-enforced timer. Flushed HTTP response "
                    "buffering streams the loading skeleton instantly; questions "
                    "appear without a blank-screen wait."
                ),
            },
            {
                "icon": "🔒",
                "title": "Hardened Security",
                "description": (
                    "BCrypt password hashing, CSRF tokens, rate limiting (5 failures "
                    "→ 15-min lockout), HTTP security headers, HttpOnly+Secure cookies, "
                    "and 100% parameterised SQL queries."
                ),
            },
            {
                "icon": "📑",
                "title": "PDF Report Merging",
                "description": (
                    "Apache PDFBox merges individual result pages into a single "
                    "downloadable report. Admins can export results for any exam "
                    "or date range with one click."
                ),
            },
            {
                "icon": "🐳",
                "title": "Containerised Deployment",
                "description": (
                    "Docker Compose orchestrates the Tomcat app server and "
                    "PostgreSQL database. A single `docker-compose up` spins "
                    "the full stack locally or on any cloud VM."
                ),
            },
        ],

        "architecture": [
            {
                "label": "Client",
                "boxes": [
                    {"text": "Browser / JSP Pages", "style": "dim"},
                    {"text": "Vanilla JS + Fetch", "style": "dim"},
                ],
                "arrow_after": True,
            },
            {
                "label": "Servlet",
                "boxes": [
                    {"text": "Tomcat 9", "style": "cyan"},
                    {"text": "Servlets", "style": "cyan"},
                    {"text": "Filters (Auth / Rate Limit / Security Headers)", "style": "cyan"},
                ],
                "arrow_after": True,
            },
            {
                "label": "Services",
                "boxes": [
                    {"text": "JobStore (ExecutorService)", "style": "lime"},
                    {"text": "QuestionCache", "style": "lime"},
                    {"text": "AIUtils → Gemini API", "style": "lime"},
                    {"text": "PDFBox Merger", "style": "lime"},
                ],
                "arrow_after": True,
            },
            {
                "label": "Data",
                "boxes": [
                    {"text": "PostgreSQL", "style": "orange"},
                    {"text": "PreparedStatements only", "style": "dim"},
                ],
                "arrow_after": False,
            },
        ],

        "arch_description": (
            "A classic layered servlet architecture: JSP views talk to servlets, "
            "which delegate to service classes. A custom async job queue decouples "
            "slow AI calls from HTTP threads. All DB access goes through prepared statements."
        ),

        "security": [
            {
                "icon": "🔑",
                "title": "BCrypt Password Hashing",
                "description": (
                    "All passwords are hashed with <code>jbcrypt</code> before storage. "
                    "Plain-text passwords never touch the database."
                ),
            },
            {
                "icon": "🛡️",
                "title": "CSRF Protection",
                "description": (
                    "Every state-changing form includes a server-generated CSRF token "
                    "stored in the session. The <code>CsrfFilter</code> rejects any "
                    "POST missing a matching token."
                ),
            },
            {
                "icon": "🚦",
                "title": "Rate Limiting",
                "description": (
                    "The <code>RateLimitFilter</code> tracks failed login/register attempts "
                    "by IP. After 5 failures, the IP is locked out for 15 minutes with "
                    "an HTTP 429. Counters reset automatically."
                ),
            },
            {
                "icon": "📋",
                "title": "HTTP Security Headers",
                "description": (
                    "Every response includes <code>Content-Security-Policy</code>, "
                    "<code>X-Frame-Options: DENY</code>, <code>X-Content-Type-Options: nosniff</code>, "
                    "<code>HSTS</code>, <code>Referrer-Policy</code>, and <code>Permissions-Policy</code>."
                ),
            },
            {
                "icon": "🍪",
                "title": "Secure Session Cookies",
                "description": (
                    "Session cookies are set as <code>HttpOnly</code>, <code>Secure</code>, "
                    "and <code>SameSite=Strict</code>. Sessions are fully regenerated on "
                    "login to prevent session fixation."
                ),
            },
            {
                "icon": "💉",
                "title": "SQL Injection Prevention",
                "description": (
                    "All queries use <code>PreparedStatement</code> with parameterised values. "
                    "No string concatenation in SQL. Dynamic IN clauses use placeholder arrays."
                ),
            },
        ],

        "security_description": (
            "Security was treated as a first-class requirement, not an afterthought. "
            "Six independent defence layers cover authentication, transport, and data integrity."
        ),

        "challenges_intro": (
            "Four real engineering problems that pushed beyond typical lab-project scope."
        ),

        "challenges": [
            {
                "accent": "cyan",
                "label": "⚡ Performance",
                "title": "AI Latency Blocking HTTP Threads",
                "problem": (
                    "Gemini API calls take 15–60 seconds. Running them synchronously "
                    "on a Tomcat thread would exhaust the thread pool under moderate load."
                ),
                "solution": (
                    "Built a custom async job queue (<code>JobStore</code>) using "
                    "<code>ExecutorService</code> and <code>ConcurrentHashMap</code>. "
                    "The HTTP thread starts a job and redirects in milliseconds; "
                    "the browser polls <code>jobStatus.jsp</code> every 2 s."
                ),
            },
            {
                "accent": "lime",
                "label": "🗄️ Data Consistency",
                "title": "Stale Questions After AI Regeneration",
                "problem": (
                    "The question cache stores sets by topic. When AI regenerates "
                    "questions, the cache keeps serving the old set even after fresh "
                    "rows are inserted."
                ),
                "solution": (
                    "Added <code>QuestionCache.invalidate()</code>, called by "
                    "<code>AIUtils.prepareTopicForAI()</code> before clearing old "
                    "questions. The next exam load fetches fresh data and repopulates."
                ),
            },
            {
                "accent": "orange",
                "label": "🖥️ UX / Rendering",
                "title": "Blank Screen During Database Queries",
                "problem": (
                    "Tomcat's default JSP buffering meant users saw a completely "
                    "blank page for the entire duration of the DB query on exam.jsp."
                ),
                "solution": (
                    "Called <code>response.setBufferSize(0)</code> and flushed after "
                    "writing the loading overlay. The spinner renders instantly; "
                    "a JS <code>window.onload</code> swap then hides the skeleton."
                ),
            },
            {
                "accent": "fg2",
                "label": "🔒 Code Structure",
                "title": "JSP Scriptlet Scope Bug in Admin Dashboard",
                "problem": (
                    "The <code>renderHtmlTable()</code> helper was declared inside a "
                    "<code>&lt;%!</code> block where the implicit <code>out</code> "
                    "object isn't available — causing a runtime error."
                ),
                "solution": (
                    "Refactored to build HTML into a <code>StringBuilder</code> and "
                    "return a String. The calling scriptlet renders via "
                    "<code>out.print()</code>, cleanly separating method logic from "
                    "JSP output handling."
                ),
            },
        ],

        "tech_stack": [
            {"icon": "☕", "name": "Java 21", "role": "Language"},
            {"icon": "🐱", "name": "Tomcat 9", "role": "Servlet Container"},
            {"icon": "📄", "name": "JSP / Servlets", "role": "Presentation Layer"},
            {"icon": "🐘", "name": "PostgreSQL", "role": "Primary Database"},
            {"icon": "📦", "name": "Maven", "role": "Build Tool"},
            {"icon": "🤖", "name": "Google Gemini AI", "role": "Question Generation"},
            {"icon": "🔑", "name": "BCrypt (jbcrypt)", "role": "Password Hashing"},
            {"icon": "📑", "name": "Apache PDFBox", "role": "PDF Merging"},
            {"icon": "🐳", "name": "Docker", "role": "Containerisation"},
            {"icon": "🎨", "name": "CSS Custom Properties", "role": "Design System"},
            {"icon": "⚡", "name": "Vanilla JS / Fetch", "role": "Client Interactions"},
            {"icon": "🎉", "name": "canvas-confetti", "role": "Result Celebration"},
        ],

        "tech_stack_description": (
            "A deliberate mix of classic enterprise Java with modern AI APIs "
            "and containerised deployment."
        ),

        "github": "https://github.com/SayonBiswas/IWT",
        "live": "https://examhub-q9ez.onrender.com",
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