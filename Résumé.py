from pathlib import Path

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Digital CV | Shayan Darabi", page_icon=":wave:")    
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume Shayan Darabi.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shayan Darabi"
PAGE_ICON = ":wave:"
NAME = "Shayan Darabi"
DESCRIPTION = """
Enthusiastic and analytical data scientist with a strong foundation in statistical modeling, Python programming, and data analysis. I am seeking to leverage my skills and expertise to contribute to a dynamic team and tackle complex business challenges through data-driven insights.
"""
EMAIL = "darabishayan0@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/darabi-shayan/",
    "GitHub": "https://github.com/ShayanDarabi",
}


# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")

pqprc_url = 'https://pqprc.ac.ir/'
dr_saghaei_linkedin = 'https://www.linkedin.com/in/abbas-saghaei-01135044/'
st.write(
    f"""
✔️ Data Analyst at [Parsian Quality and Productivity Research Center]({pqprc_url}) - *Internship*:
    """
)
st.markdown("<span style='color:green'>Jun 2023 - Aug 2023 . Tehran, Tehran Province, Iran - Remote</span>",
             unsafe_allow_html=True)
st.write(f"""
- Exploring the realm of data analysis and working as a machine learning researcher in the field of Remaining Useful Life (RUL) prediction for rollers in the hot and cold rolling process under the supervision of [Dr. Abbas Saghaei]({dr_saghaei_linkedin}).
- Cleaning and aggregating complex datasets using Python packages like Pandas and Numpy to ensure data quality and integrity.
- Utilizing Matplotlib and Seaborn to create insightful data visualizations like depicting P control charts. Developing informative dashboards and doing EDA by using Pandas Profiling to provide actionable insights.
- Learning and exploring the implementation of metaheuristics optimization techniques in Python to solve complex optimization problems like VRP.
""")

st.write('\n')
st.write("""
✔️ Teaching Assistant in Programming Fundamentals (C++) Course at K. N. Toosi University:
""")
st.markdown("<span style='color:green'>Oct 2022 - Jan 2023 · 4 mos Tehran Province, Iran</span>",
             unsafe_allow_html=True)

st.write("""
- Provided individual and group support to students, offering guidance and clarifications on programming concepts, syntax, and problem-solving techniques.
- Assisted in developing and updating course materials, assignments, and programming exercises.
- Administered and graded assignments, quizzes, and exams.
- Assisted students with technical issues, debugging errors, and resolving programming-related challenges.

"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")

st.write("""
📚 ML and Statistical Modeling: Logistic Regression, Linear Regression, Decision Trees, etc.
""")

st.write(
    """
🐍 Python (Scikit-learn, Pandas, Numpy)
""")
st.write(
    """
❔ SQL
    """
)
st.write("""
📊 Data Visualization: Matplotlib, Seaborn
""")

st.write("""
📐 Mathematics: Statistics, Linear Algebra
""")

st.write("""
🔰 Familiarity With Version Control Systems Like Git
"""
)
st.write(
    """
🙌 Teamwork
""")
st.write("""
📖 Self-learning
""")
st.write("""
🔑 Problem-solving
    """
)
st.write("""
🏃‍♂️ Active Learning
""")
#--Licenses & certifications

st.write('\n')
st.subheader("Licenses & certifications")

machine_learning_course = 'https://www.coursera.org/account/accomplishments/certificate/ENYQR9YR3S8M'
st.write(f"""
🏆 [Machine Learning]({machine_learning_course})
""")

Supervised_course = 'https://www.coursera.org/account/accomplishments/certificate/4PW9GMB764JT'
st.write(f"""
🏆 [Supervised Machine Learning: Regression and Classification]({Supervised_course})
""")

neural_course = 'https://www.coursera.org/account/accomplishments/certificate/BPGK6DVN9MGF' 
st.write(f"""
🏆 [Neural Networks and Deep Learning]({neural_course})
""")

advanced_course = 'https://www.coursera.org/account/accomplishments/certificate/PM9NPVSSXCS2'
st.write(f"""
🏆 [Advanced Learning Algorithms]({advanced_course})
""")

Python_course = 'https://quera.org/certificate/fKoLCtfq/'
st.write(
    f"""
🏆 [Advanced Python Programming and Object-Oriented  Thinking Course]({Python_course})
""")

understanding_course = 'https://www.coursera.org/account/accomplishments/certificate/UR9CPFQKDWU9'
st.write(f"""
🏆 [Understanding and Visualizing Data with Python]({understanding_course})
""")
excel_course = 'https://www.coursera.org/account/accomplishments/specialization/certificate/AQWTP4R4RJJW'
st.write(f"""
🏆 [Excel Skills for Business Specialization]({excel_course})
""")

data_analysis_course = 'https://freecodecamp.org/certification/ShayanDarabi/data-analysis-with-python-v7'
st.write(f"""
🏆 [Data Analysis with Python]({data_analysis_course})
""")

html_course = 'https://www.coursera.org/account/accomplishments/certificate/ZTTPBRKUSHHL'
st.write(f"""
🏆 [Introduction to HTML5]({html_course})
""")

st.write(f"""
🏆 Microsoft SQL Server Development for Everyone
    """
)
