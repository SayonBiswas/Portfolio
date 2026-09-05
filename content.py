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

    {
        "role": "AWS Data Engineering & DevOps Industrial Trainee",
        "org": "Ingenious-TechWorld (ITW) · Silicon University, Odisha",
        "period": "May 2026—Jun 2026",
        "github": "https://github.com/SayonBiswas/AWS-Project-Details",
        "tech": ["AWS", "Data Engineering", "DevOps", "Cloud Infrastructure"],
        "bullets": [
            "Completed an intensive industrial training program on AWS Data Engineering & DevOps by Ingenious-TechWorld",
            "Gained hands-on exposure to cloud-based data pipelines, infrastructure management, and DevOps practices on AWS",
            "Earned a Certificate of Appreciation from ITW and Silicon University for successful programme completion",
        ],
    },
]

PROJECTS_COMPLETED = [
    {
        "title": "ExamHub",
        "number": "01",  # change to match your numbering
        "status": "completed",  # "completed" | "ongoing"
        "image": "examhub1.png",  # e.g. "examhub_preview.png" — place in static/
        "case_study_image": "examhub2.png",  # Image for detailed case study page
        "difficulty": "advanced",  # "basic" | "medium" | "advanced"
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
        "status": "completed",
        "image": "student_management_1.png",
        "case_study_image": "student_management_2.png",
        "difficulty": "medium",
        "description": (
            "A full-featured student management system built with FastAPI and PostgreSQL, "
            "featuring JWT authentication, role-based access control, ML-based score prediction, "
            "sentiment analysis on feedback, and PDF marksheet export — deployed on AWS Elastic Beanstalk."
        ),
        "tech": ["Python", "FastAPI", "PostgreSQL", "Jinja2", "JWT", "bcrypt", "scikit-learn", "TextBlob", "WeasyPrint",
                 "SlowAPI"],

        "details": (
            "Built for schools and educational institutions to manage student records, marks, "
            "feedback, analytics, and lost & found reports. The system supports three roles — "
            "Admin, Teacher, and Student — each with scoped permissions enforced on every route. "
            "ML features include score prediction based on current performance and TextBlob "
            "sentiment analysis on feedback, categorising it as praise, concern, or improvement. "
            "Student marksheets are exportable as PDFs via WeasyPrint."
        ),

        "stats": [
            {"value": "3", "label": "User Roles"},
            {"value": "7", "label": "Modules"},
            {"value": "5+", "label": "Security Layers"},
            {"value": "PDF", "label": "Marksheet Export"},
        ],

        "feature_cards": [
            {
                "icon": "🔐",
                "title": "JWT Auth & Role-Based Access",
                "description": (
                    "Secure login and registration with bcrypt password hashing and JWT "
                    "stored in HttpOnly cookies. Three roles — Admin, Teacher, Student — "
                    "with granular permissions enforced on every route."
                ),
            },
            {
                "icon": "👨‍🎓",
                "title": "Student & Marks Management",
                "description": (
                    "Full CRUD for student records with dynamic subject support. "
                    "Teachers can add, update, and remove subject-wise marks per student. "
                    "A database VIEW auto-computes total, average, and percentage."
                ),
            },
            {
                "icon": "📊",
                "title": "ML Analytics Dashboard",
                "description": (
                    "Rule-based score predictor (scikit-learn ready) forecasts a student's "
                    "future percentage from current performance. Class-wise performance "
                    "summaries give teachers an at-a-glance overview."
                ),
            },
            {
                "icon": "💬",
                "title": "Feedback & Sentiment Analysis",
                "description": (
                    "Teachers and students submit feedback which is analysed by TextBlob "
                    "and automatically categorised as praise, concern, or improvement. "
                    "All ML outputs are stored for future model training."
                ),
            },
            {
                "icon": "📄",
                "title": "PDF Marksheet Export",
                "description": (
                    "Any user can download an individual student's marksheet as a PDF "
                    "via WeasyPrint — including student info, subject-wise marks, total, "
                    "average, percentage, and pass/fail result."
                ),
            },
            {
                "icon": "🧳",
                "title": "Lost & Found Module",
                "description": (
                    "Students and teachers can report lost or found items. Admins and "
                    "teachers can mark items as resolved. Full CRUD with role-scoped "
                    "delete permissions."
                ),
            },
        ],

        "architecture": [
            {
                "label": "Client",
                "boxes": [
                    {"text": "Jinja2 Templates", "style": "dim"},
                    {"text": "HTML5 + CSS3", "style": "dim"},
                ],
                "arrow_after": True,
            },
            {
                "label": "API",
                "boxes": [
                    {"text": "FastAPI + uvicorn", "style": "cyan"},
                    {"text": "JWT (HttpOnly cookies)", "style": "cyan"},
                    {"text": "RBAC on every route", "style": "cyan"},
                    {"text": "SlowAPI Rate Limiting", "style": "cyan"},
                ],
                "arrow_after": True,
            },
            {
                "label": "ML / Export",
                "boxes": [
                    {"text": "Score Predictor (scikit-learn)", "style": "lime"},
                    {"text": "Sentiment Analysis (TextBlob)", "style": "lime"},
                    {"text": "PDF Export (WeasyPrint)", "style": "lime"},
                ],
                "arrow_after": True,
            },
            {
                "label": "Data",
                "boxes": [
                    {"text": "PostgreSQL", "style": "orange"},
                    {"text": "asyncpg + databases", "style": "orange"},
                    {"text": "student_results VIEW", "style": "dim"},
                ],
                "arrow_after": True,
            },
            {
                "label": "Deploy",
                "boxes": [
                    {"text": "AWS Elastic Beanstalk", "style": "lime"},
                ],
                "arrow_after": False,
            },
        ],

        "arch_description": (
            "Jinja2-rendered pages talk to FastAPI routers. Every request passes through "
            "JWT auth middleware and SlowAPI rate limiting before hitting the route handler. "
            "ML modules run in-process; WeasyPrint generates PDFs server-side on demand."
        ),

        "security_description": (
            "Security was built in at every layer — from password storage to cookie policy."
        ),

        "security": [
            {
                "icon": "🔑",
                "title": "bcrypt Password Hashing",
                "description": "All passwords are hashed with bcrypt before storage. Plain-text passwords never touch the database.",
            },
            {
                "icon": "🍪",
                "title": "JWT in HttpOnly Cookies",
                "description": (
                    "Auth tokens are stored as <code>HttpOnly</code> cookies — inaccessible to JavaScript. "
                    "<code>SameSite</code> cookie policy is applied to prevent CSRF attacks."
                ),
            },
            {
                "icon": "👥",
                "title": "Role-Based Access Control",
                "description": "Admin, Teacher, and Student roles each have scoped permissions enforced on every route — not just the UI.",
            },
            {
                "icon": "🚦",
                "title": "Per-Route IP Rate Limiting",
                "description": (
                    "SlowAPI enforces rate limits per IP on all routes — "
                    "5/min on login, 3/min on register, 10/min on deletes — "
                    "preventing brute force and abuse."
                ),
            },
        ],

        "challenges_intro": "Real problems solved while building a multi-module system with auth, ML, and PDF export.",

        "challenges": [
            {
                "accent": "cyan",
                "label": "🔐 Auth",
                "title": "Implementing HttpOnly JWT Cookies",
                "problem": (
                    "Storing JWT in localStorage exposes it to XSS attacks. "
                    "The challenge was setting up a secure cookie-based auth flow "
                    "that works with server-side Jinja2 rendering."
                ),
                "solution": (
                    "Used <code>python-jose</code> to generate JWTs and FastAPI's "
                    "<code>Response.set_cookie()</code> with <code>httponly=True</code> "
                    "and <code>samesite='lax'</code>. Auth middleware reads the cookie "
                    "on every request."
                ),
            },
            {
                "accent": "lime",
                "label": "📊 ML",
                "title": "Integrating ML Into a Web App",
                "problem": (
                    "Wiring a scikit-learn predictor and TextBlob sentiment analyser "
                    "into async FastAPI routes without blocking the event loop or "
                    "slowing down page loads."
                ),
                "solution": (
                    "Ran ML inference in <code>run_in_executor</code> to offload "
                    "CPU-bound work from the async event loop. Results are stored "
                    "in the database immediately for future reuse."
                ),
            },
            {
                "accent": "orange",
                "label": "📄 Export",
                "title": "Server-Side PDF Generation",
                "problem": (
                    "Generating a correctly formatted PDF marksheet server-side — "
                    "with tables, styling, and dynamic data — without a headless "
                    "browser dependency."
                ),
                "solution": (
                    "Used WeasyPrint to render a dedicated <code>marksheet_pdf.html</code> "
                    "Jinja2 template to PDF in-process. CSS handles all print formatting; "
                    "the file streams directly to the browser as a download."
                ),
            },
        ],

        "tech_stack": [
            {"icon": "🐍", "name": "Python", "role": "Language"},
            {"icon": "⚡", "name": "FastAPI", "role": "API Framework"},
            {"icon": "🐘", "name": "PostgreSQL", "role": "Database"},
            {"icon": "🔌", "name": "asyncpg + databases", "role": "Async DB Driver"},
            {"icon": "🔑", "name": "JWT + bcrypt", "role": "Authentication"},
            {"icon": "🧩", "name": "Jinja2", "role": "Server-Side Templating"},
            {"icon": "📈", "name": "scikit-learn", "role": "Score Prediction"},
            {"icon": "💬", "name": "TextBlob", "role": "Sentiment Analysis"},
            {"icon": "📄", "name": "WeasyPrint", "role": "PDF Export"},
            {"icon": "🚦", "name": "SlowAPI", "role": "Rate Limiting"},
            {"icon": "☁️", "name": "AWS Elastic Beanstalk", "role": "Deployment"},
        ],

        "tech_stack_description": (
            "A production-minded Python stack — async FastAPI with JWT auth, "
            "two ML modules, server-side PDF generation, and IP-based rate limiting, "
            "all deployed on AWS."
        ),

        "github": "https://github.com/SayonBiswas/Student_Management_Website",
        "live": "http://studentmanagement-env.eba-uup6bgvc.ap-south-2.elasticbeanstalk.com",
    },

    {
        "number": "03",
        "title": "AI Risk Manager",
        "status": "completed",
        "image": "ai-risk-manager-1.png",
        "case_study_image": "ai-risk-manager-2.png",
        "difficulty": "advanced",
        "description": (
            "A full-stack payment risk platform built for the Razorpay Buildathon. "
            "Analyses transactions in real-time using XGBoost fraud detection, LightGBM return "
            "risk scoring, and Gemini AI-generated chargeback evidence — served via FastAPI with "
            "a React dashboard."
        ),
        "tech": ["Python", "FastAPI", "XGBoost", "LightGBM", "Gemini AI", "PostgreSQL", "Redis", "React", "Docker"],

        "details": (
            "Built solo for Razorpay Buildathon Track 02. The platform scores every transaction "
            "across three risk dimensions: fraud (XGBoost, ROC-AUC ~0.94), return risk (LightGBM, "
            "ROC-AUC ~0.91), and chargeback risk (IsoForest + LR ensemble). High-risk transactions "
            "are blocked or flagged instantly with a Gemini-generated plain-English explanation. "
            "Chargebacks trigger a full AI-drafted dispute evidence package. Deployed backend on "
            "Render, frontend on Vercel."
        ),

        "stats": [
            {"value": "~0.94", "label": "Fraud ROC-AUC"},
            {"value": "3", "label": "ML Models"},
            {"value": "6", "label": "Security Layers"},
            {"value": "<150ms", "label": "API Latency"},
        ],

        "feature_cards": [
            {
                "icon": "🔍",
                "title": "Real-Time Fraud Detection",
                "description": (
                    "XGBoost classifier scores every transaction 0–100. "
                    "Scores above 0.80 are blocked instantly; above 0.50 are flagged "
                    "with a Gemini AI plain-English reason."
                ),
            },
            {
                "icon": "↩️",
                "title": "Return Risk Scoring",
                "description": (
                    "LightGBM model predicts the probability of a return for each "
                    "transaction, bands it LOW/MEDIUM/HIGH, and recommends merchant "
                    "actions to reduce exposure."
                ),
            },
            {
                "icon": "⚖️",
                "title": "AI Chargeback Response",
                "description": (
                    "When a chargeback is filed, Gemini AI auto-drafts a complete "
                    "dispute evidence package — summary, document checklist, and "
                    "recommended bank response — in seconds."
                ),
            },
            {
                "icon": "🔑",
                "title": "JWT + API Key Auth",
                "description": (
                    "Dashboard routes use JWT Bearer tokens; ML endpoints use "
                    "SHA-256 hashed API keys via X-API-Key header. Both auth "
                    "paths share a unified middleware layer."
                ),
            },
            {
                "icon": "🚦",
                "title": "Rate Limiting & Caching",
                "description": (
                    "Redis sliding-window rate limiter (100 req/min per API key) "
                    "and LLM response caching. App degrades gracefully when Redis "
                    "is unavailable — fully functional without it."
                ),
            },
            {
                "icon": "📊",
                "title": "React Analytics Dashboard",
                "description": (
                    "React 18 + Vite frontend with Recharts visualisations. "
                    "Pages for fraud detection, return scoring, chargeback response, "
                    "and API key management — all wired to the FastAPI backend."
                ),
            },
        ],

        "architecture": [
            {
                "label": "Client",
                "boxes": [
                    {"text": "React 18 + Vite", "style": "dim"},
                    {"text": "Recharts Dashboard", "style": "dim"},
                ],
                "arrow_after": True,
            },
            {
                "label": "API",
                "boxes": [
                    {"text": "FastAPI + uvicorn", "style": "cyan"},
                    {"text": "JWT / API Key Auth", "style": "cyan"},
                    {"text": "Rate Limiter (Redis)", "style": "cyan"},
                    {"text": "Audit Logger", "style": "cyan"},
                ],
                "arrow_after": True,
            },
            {
                "label": "ML / AI",
                "boxes": [
                    {"text": "XGBoost (Fraud)", "style": "lime"},
                    {"text": "LightGBM (Returns)", "style": "lime"},
                    {"text": "IsoForest+LR (Chargeback)", "style": "lime"},
                    {"text": "Gemini 2.0 Flash (LLM)", "style": "lime"},
                ],
                "arrow_after": True,
            },
            {
                "label": "Data",
                "boxes": [
                    {"text": "PostgreSQL / Neon", "style": "orange"},
                    {"text": "Redis 7", "style": "orange"},
                ],
                "arrow_after": False,
            },
        ],

        "arch_description": (
            "React frontend talks to FastAPI over HTTPS. Every request passes through "
            "auth middleware and rate limiting before hitting the ML service layer. "
            "Three .joblib models run in-process; Gemini is called async for LLM tasks."
        ),

        "challenges_intro": "Real engineering problems solved during the Razorpay Buildathon.",

        "challenges": [
            {
                "accent": "cyan",
                "label": "⚡ ML Integration",
                "title": "Pydantic strict=True Rejecting All JSON",
                "problem": (
                    "Pydantic v2 with strict=True caused 422 validation errors on every "
                    "request because JSON coercion for Decimal and date fields was disabled."
                ),
                "solution": (
                    "Switched to <code>strict=False</code> with explicit field validators "
                    "for edge cases. All inputs now coerce cleanly without losing type safety."
                ),
            },
            {
                "accent": "lime",
                "label": "🔌 Infrastructure",
                "title": "Redis Crash Blocking App Startup",
                "problem": (
                    "If Redis wasn't running, the app threw a connection error at startup "
                    "and refused to start — breaking local dev and cold deploys."
                ),
                "solution": (
                    "Wrapped Redis init in try/except and set <code>app.state.redis = None</code> "
                    "on failure. Rate limiting and caching disable gracefully; all ML endpoints "
                    "remain fully functional."
                ),
            },
            {
                "accent": "orange",
                "label": "🤖 LLM",
                "title": "Gemini Model Deprecated Mid-Build",
                "problem": (
                    "The originally used <code>gemini-1.5-flash</code> model was deprecated "
                    "by Google in June 2026, causing all LLM calls to fail mid-buildathon."
                ),
                "solution": (
                    "Updated <code>GEMINI_MODEL</code> config to <code>gemini-2.0-flash</code>. "
                    "All chargeback and fraud explanation endpoints resumed working immediately."
                ),
            },
            {
                "accent": "fg2",
                "label": "🔒 Auth",
                "title": "401 Interceptor Logging Out on Every API Error",
                "problem": (
                    "The axios 401 interceptor on the frontend was redirecting to login on "
                    "any API error, not just auth failures — logging users out unexpectedly."
                ),
                "solution": (
                    "Scoped the redirect to only fire on <code>/auth/</code> endpoint "
                    "401 responses. All other API errors are now handled inline without "
                    "disrupting the session."
                ),
            },
        ],

        "tech_stack": [
            {"icon": "⚡", "name": "FastAPI", "role": "API Framework"},
            {"icon": "🐍", "name": "Python 3.12", "role": "Language"},
            {"icon": "🤖", "name": "XGBoost", "role": "Fraud Detection ML"},
            {"icon": "🌿", "name": "LightGBM", "role": "Return Risk ML"},
            {"icon": "🧠", "name": "Gemini 2.0 Flash", "role": "LLM Reasoning"},
            {"icon": "🐘", "name": "PostgreSQL / Neon", "role": "Primary Database"},
            {"icon": "⚙️", "name": "Redis 7", "role": "Cache & Rate Limiting"},
            {"icon": "⚛️", "name": "React 18 + Vite", "role": "Frontend"},
            {"icon": "📊", "name": "Recharts", "role": "Data Visualisation"},
            {"icon": "🔑", "name": "JWT + bcrypt", "role": "Authentication"},
            {"icon": "🐳", "name": "Docker", "role": "Containerisation"},
            {"icon": "☁️", "name": "Render + Vercel", "role": "Deployment"},
        ],

        "tech_stack_description": (
            "A modern Python ML stack paired with a React frontend — "
            "FastAPI for async performance, three specialised ML models, "
            "and Gemini for human-readable AI explanations."
        ),

        "github": "https://github.com/SayonBiswas/Ai-Risk-Manager",
        "live": "https://ai-risk-manager-sand.vercel.app",
    },
]

PROJECTS_ONGOING = [
    {
        "number": "04",
        "title": "IPL Website",
        "difficulty": "basic",  # "basic" | "medium" | "advanced"
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
        "image": "ipl-website.png",
    },
    {
        "number": "05",
        "title": "CodeReview",
        "difficulty": "medium",  # "basic" | "medium" | "advanced"
        "description": "A code review platform for analyzing and improving code quality through automated analysis and collaborative feedback.",
        "details": "Details to be added soon.",
        "features": [
            "Automated code analysis",
            "Collaborative review features",
            "Code quality metrics"
        ],
        "tech": ["TBD"],
        "github": "",
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
        "title": "Bharatiya Antariksh Hackathon 2026 – ISRO",
        "text": "Participated in the Bharatiya Antariksh Hackathon 2026, hosted by ISRO and powered by Hack2skill. Team submitted an idea addressing real-world space challenges. Reached Round 1 PPT screening phase as part of this national innovation initiative focused on aerospace technology applications.",
        "icon": "trophy",
        "image": "BAH-ISRO.jpg",
        "link": "BAH-ISRO.jpg",
    },
    {
        "title": "CodeVerse – Certificate of Participation",
        "text": "Participated in CodeVerse, held as part of NIRMAN 5.0 organized by the Silicon Innovation and Promotion Cell (SIPC) at Silicon University, Odisha, from 28th–30th November 2025 and went upto the 3rd/final round of the competition.",
        "icon": "trophy",
        "image": "CodeVerse.jpeg",
        "link": "CodeVerse.jpeg",
    },
    {
        "title": "Adobe University Hackathon – Certificate of Participation",
        "text": "Participated in the Adobe University Hackathon organised by Adobe via Unstop, representing Silicon Institute of Technology (SIT), Bhubaneswar, Odisha. Dated 9th August 2026.",
        "icon": "trophy",
        "image": "adobe-hackathon.jpg",
        "link": "adobe-hackathon.jpg",
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
    {
        "title": "AWS Data Engineering & DevOps – Industrial Training",
        "text": "Completed an industrial training programme on AWS Data Engineering & DevOps by Ingenious-TechWorld (ITW), in association with Silicon University, Odisha. Awarded a Certificate of Appreciation (May–June 2026).",
        "icon": "award",
        "image": "24BCSE96_Sayon_Biswas.jpg",
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