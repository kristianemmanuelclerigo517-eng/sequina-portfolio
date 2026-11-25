
import streamlit as st
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Mariviev B. Sequiña | Portfolio",
    page_icon="🏐",
    layout="wide"
)

# IMAGE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

def show_image(filename, caption=None, width=None):
    image_path = IMAGE_DIR / filename

    if image_path.is_file():
        if width:
            st.image(str(image_path), caption=caption, width=width)
        else:
            st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.info(f"Add {filename} to your images folder to display it.")

# CUSTOM DESIGN
st.markdown("""
<style>
.stApp {
    background-color: #f7f4ed;
    color: #202d3b !important;
}

[data-testid="stHeader"] {
    background-color: #f7f4ed;
}

.stApp p,
.stApp li,
.stApp label,
[data-testid="stMarkdownContainer"] p {
    color: #344353 !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #18334b !important;
}

[data-testid="stSidebar"] {
    background-color: #18334b;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #ffffff !important;
}

.stButton button {
    background-color: #e87559;
    color: white !important;
    border: none;
    border-radius: 8px;
}

hr {
    border-color: #e5d9c9;
}

.highlight {
    background-color: #e9e1d3;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #e87559;
    margin: 10px 0;
}

.small-heading {
    color: #e87559 !important;
    font-weight: bold;
    letter-spacing: 2px;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION
st.sidebar.markdown("# MB")
st.sidebar.caption("PERSONAL PORTFOLIO")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "EXPLORE",
    [
        "Home",
        "Personal Information",
        "Education",
        "Hobbies",
        "Interests",
        "STEM & Engineering"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("MARIVIEV B. SEQUIÑA")
st.sidebar.caption("© 2026")

# HOME
if page == "Home":

    st.markdown(
        '<p class="small-heading">WELCOME TO MY PORTFOLIO</p>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.7, 1], gap="large")

    with left:
        st.title("Mariviev B. Sequiña")
        st.subheader("A little creativity, passion, and determination.")

        st.write("""
        Hello! I'm Mariviev B. Sequiña. Welcome to my personal
        portfolio, where I share my background, hobbies, interests,
        and the activities that make me who I am.
        """)

        st.markdown("""
        <div class="highlight">
        <b>MY PERSONALITY</b><br>
        Creative, active, and always willing to learn and experience
        new things.
        </div>
        """, unsafe_allow_html=True)

    with right:
        show_image("profile.jpg", width=240)

    st.markdown("---")
    st.header("What I Enjoy")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("💃 Dancing")
        st.write("Expressing myself through movement and rhythm.")

    with col2:
        st.subheader("🎤 Singing")
        st.write("Enjoying music and expressing emotions through songs.")

    with col3:
        st.subheader("🏐 Volleyball")
        st.write("Staying active and learning the value of teamwork.")

# PERSONAL INFORMATION
elif page == "Personal Information":

    st.markdown(
        '<p class="small-heading">GET TO KNOW ME</p>',
        unsafe_allow_html=True
    )

    st.title("Personal Information")

    st.write("**Full Name:** Mariviev B. Sequiña")

    st.markdown("---")
    st.header("My Values")

    st.write("""
    I value creativity, teamwork, discipline, and personal growth.
    I enjoy activities that allow me to express myself, improve my
    abilities, and build meaningful connections with others.
    """)

# EDUCATION
elif page == "Education":

    st.markdown(
        '<p class="small-heading">MY ACADEMIC JOURNEY</p>',
        unsafe_allow_html=True
    )

    st.title("Educational Attainment")

    st.markdown("### 01 — Senior High School")

    st.write("**School:** Bislig City National High School")
    st.write("**Strand:** Science, Technology, Engineering, and Mathematics (STEM)")

    st.markdown("---")

    st.markdown("### 02 — College")

    st.write("**School:** North Eastern Mindanao State University (NEMSU)")
    st.write("**Level:** College")

    st.write("""
    My educational journey allows me to gain knowledge, develop
    important skills, and prepare myself for future opportunities.
    """)

    show_image("engineering.jpg", "Learning through science, technology, and innovation")

# HOBBIES
elif page == "Hobbies":

    st.markdown(
        '<p class="small-heading">THE THINGS I LOVE DOING</p>',
        unsafe_allow_html=True
    )

    st.title("My Hobbies")

    st.subheader("💃 01. Dancing")

    st.write("""
    Dancing is one of the activities I enjoy because it allows me
    to express myself through movement, rhythm, and creativity.
    """)

    st.markdown("---")

    st.subheader("🎤 02. Singing")

    st.write("""
    I enjoy singing because music gives me a way to express my
    emotions, appreciate different songs, and enjoy my free time.
    """)

    st.markdown("---")

    st.subheader("🏐 03. Playing Volleyball")

    st.write("""
    Playing volleyball keeps me active and helps me develop
    teamwork, discipline, communication, and sportsmanship.
    """)

    show_image("hobbies.jpg")

# INTERESTS
elif page == "Interests":

    st.markdown(
        '<p class="small-heading">WHAT INSPIRES ME</p>',
        unsafe_allow_html=True
    )

    st.title("My Interests")

    st.subheader("🎶 Music and Performing Arts")

    st.write("""
    I appreciate music and performing arts because they provide
    opportunities to express creativity, build confidence, and
    enjoy meaningful experiences.
    """)

    st.markdown("---")

    st.subheader("🏐 Sports and Physical Activities")

    st.write("""
    I am interested in sports and physical activities because
    they encourage an active lifestyle, teamwork, discipline,
    and determination.
    """)

    show_image("interest.jpg")

# STEM AND ENGINEERING
elif page == "STEM & Engineering":

    st.markdown(
        '<p class="small-heading">SCIENCE • TECHNOLOGY • INNOVATION</p>',
        unsafe_allow_html=True
    )

    st.title("STEM & Engineering")

    show_image("engineering.jpg")

    st.write("""
    As a STEM student, I am introduced to different concepts
    involving science, technology, engineering, and mathematics.
    These fields help me understand how things work and how
    knowledge can be used to solve real-world problems.
    """)

    st.markdown("---")

    st.subheader("⚙️ Understanding Engineering")

    st.write("""
    Engineering combines creativity, mathematics, and
    problem-solving to design and improve machines,
    structures, and technologies.

    It plays an important role in developing solutions
    that make everyday life easier, safer, and more efficient.
    """)

    st.markdown("---")

    st.subheader("🔬 Skills I Want to Develop")

    st.write("""
    - Critical and logical thinking
    - Problem-solving
    - Creativity and innovation
    - Teamwork and communication
    - Scientific and mathematical understanding
    """)

    st.markdown("---")

    st.subheader("My Goal")

    st.write("""
    I want to continue learning, improving my abilities,
    and exploring opportunities that will help me grow
    academically and personally.
    """)

# FOOTER
st.markdown("---")
st.caption("MARIVIEV B. SEQUIÑA | PERSONAL PORTFOLIO • 2026")
