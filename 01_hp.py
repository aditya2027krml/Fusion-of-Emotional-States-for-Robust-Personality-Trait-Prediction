import streamlit as st

st.set_page_config(page_title="Multimodal Emotion Recognition", page_icon="🧠", layout="wide")

# Custom CSS for page and colorful sidebar
custom_css = """
<style>
/* Page background gradient */
.stApp {
    background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    color: #333;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Container styling */
.container {
    max-width: 850px;
    margin: auto;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}

/* Headings */
h1 {
    font-weight: 700;
    font-size: 3rem;
    margin-bottom: 0.5rem;
    text-align: center;
    color: #4a90e2;
    text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
}

h2 {
    color: #5a5a5a;
    font-weight: 600;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

/* Paragraph */
p {
    font-size: 1.15rem;
    line-height: 1.6;
    text-align: justify;
    color: #555;
}

/* Image container with smaller image */
.image-container {
    text-align: center;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

.image-container img {
    width: 60%;
    border-radius: 15px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

/* Sidebar background and text colors */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ff7e5f 0%, #feb47b 100%);
    color: white;
}

[data-testid="stSidebar"] .css-1d391kg {
    color: white;
    font-weight: 600;
}

[data-testid="stSidebar"] .css-1v0mbdj {
    color: white;
}

/* Sidebar header style */
[data-testid="stSidebar"] h2 {
    color: #ffe066;
    font-weight: 700;
    margin-bottom: 1rem;
}

/* Scrollbar styling for sidebar */
[data-testid="stSidebar"] ::-webkit-scrollbar {
    width: 8px;
}

[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background-color: #ff3b2f;
    border-radius: 10px;
}

/* Responsive adjustments */
@media (max-width: 600px) {
    h1 {
        font-size: 2.2rem;
    }
    p {
        font-size: 1rem;
    }
    .image-container img {
        width: 80%;
    }
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# HTML content for the home page
home_html = """
<div class="container">
    <h1>Multimodal Emotion Recognition</h1>
    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1517841905240-4729888e0c0e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDF8fGVtb3Rpb258ZW58MHx8fHwxNjY0MjY0MjY0&ixlib=rb-4.0.3&q=80&w=800" 
             alt="Emotion Recognition"/>
    </div>
    <h2>About This Project</h2>
    <p>
        Welcome to the Multimodal Emotion Recognition app! This project harnesses the power of <strong>text</strong>, <strong>audio</strong>, and <strong>video</strong> data to detect human emotions accurately.
        Leveraging advanced deep learning models such as BERT for text analysis, CNN-LSTM for audio processing, and ResNet50 embeddings for video, this system offers a comprehensive platform for emotion classification.
    </p>
    <p>
        Use the sidebar to explore individual modalities or their combinations. Whether you're a researcher, developer, or enthusiast, this app provides interactive insights into affective computing and human-computer interaction.
    </p>
</div>
"""

st.markdown(home_html, unsafe_allow_html=True)
