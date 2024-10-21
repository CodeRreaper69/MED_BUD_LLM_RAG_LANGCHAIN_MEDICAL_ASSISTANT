import streamlit as st
from PIL import Image

# Custom CSS with medical theme
custom_css = """
<style>
/* Main theme colors */
:root {
    --primary-blue: #4a90e2; /* Softer blue for a professional look */
    --secondary-blue: #7ab1f2; /* Complementary lighter blue */
    --alert-red: #e74c3c;
    --success-green: #2ecc71;
    --neutral-gray: #f7f9fc; /* Lighter gray for a cleaner background */
    --dark-gray: #3c3c3c; /* Darker gray for contrast */
    --doctor-white: #ffffff;
}

/* Main container */
.main-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

/* Custom styling for the main header */
.medical-header {
    background: var(--neutral-gray);
    border-bottom: 3px solid var(--primary-blue);
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.medical-header h1 {
    color: var(--primary-blue);
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Sidebar customization */
.css-1d391kg {
    background-color: var(--neutral-gray);
    border-right: 2px solid var(--secondary-blue);
    padding: 2rem;
    color: var(--dark-gray);
}

.css-1d391kg h2 {
    color: var(--primary-blue);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* File uploader styling */
.upload-container {
    border: 2px dashed var(--primary-blue);
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.3s ease;
    background-color: rgba(127, 146, 255, 0.05);
}

.upload-container:hover {
    border-color: var(--secondary-blue);
    background-color: rgba(74, 144, 226, 0.1);
}

/* Warning Card */
.warning-card {
    background-color: #FFF1F1;
    border: 1px solid #DC2626;
    border-left: 4px solid #DC2626;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 8px;
}

.medical-warning h4 {
    color: var(--alert-red);
    margin-bottom: 1rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Button styling */
.medical-button {
    background-color: var(--primary-blue);
    color: white;
    border: none;
    padding: 0.75rem 2.5rem;
    border-radius: 25px;
    font-weight: 600;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    transition: all 0.3s ease;
    text-align: center;
    display: inline-block;
    margin: 1rem 0;
}

.medical-button:hover {
    background-color: var(--secondary-blue);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Model selection styling */
.model-selection {
    background-color: var(--neutral-gray);
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.model-selection label {
    font-weight: 500;
    color: var(--primary-blue);
}

/* Health feature cards */
.feature-card {
    background-color: white;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-left: 4px solid var(--primary-blue);
}

.feature-card h3 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--primary-blue);
}

.feature-card p, .feature-card ul {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--dark-gray);
}

/* Responsive design */
@media (max-width: 768px) {
    .medical-header {
        padding: 1rem;
    }
    
    .medical-header h1 {
        font-size: 2rem;
    }
    
    .medical-button {
        width: 100%;
    }
}
</style>
"""

# Page configuration
st.set_page_config(
    page_title="AI-Powered Medical Chatbot - Medi Bud",
    page_icon="⚕",
    layout="wide",
)

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="medical-header"><h2>Medi Bud</h2></div>', unsafe_allow_html=True)
    st.markdown("### Your AI Health Companion")
    
    # Model Selection
    st.markdown('<div class="model-selection">', unsafe_allow_html=True)
    llm_option = st.radio(
        "Choose LLM Model Variant:",
        ("GPT-4o-mini", "Gemini", "Use your OpenAI API key")
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # File Upload
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown("📄 Upload Medical Documents")
    uploaded_file = st.file_uploader(
        "Attach your medical files (PDF, JPG, PNG)", 
        type=["pdf", "jpg", "png"]
    )
    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")
    st.markdown('</div>', unsafe_allow_html=True)

# Main Content
st.markdown('<div class="medical-header">', unsafe_allow_html=True)
st.image("logo-no-background.png", width=700)
st.markdown('</div>', unsafe_allow_html=True)

# Welcome Message
st.markdown("""
<div class="feature-card">
    <h3>👋 Welcome to Medi Bud!</h3>
    <p>Your AI-powered healthcare assistant designed to offer:</p>
    <ul>
        <li>Preliminary medical consultations</li>
        <li>Health-related guidance</li>
        <li>Medical information and explanations</li>
        <li>Symptom assessment assistance</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Caution Section
st.markdown("""
<div class="medical-warning">
    <h4>⚠ Important Medical Disclaimer:</h4>
    <ul>
        <li>This AI chatbot provides preliminary guidance only and is not a substitute for professional medical advice.</li>
        <li>Always consult qualified healthcare providers for medical conditions.</li>
        <li>In case of emergency, contact your local emergency services immediately.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="feature-card">
    <h3>🏥 Key Features</h3>
    <ul>
        <li>24/7 availability for health-related queries</li>
        <li>Secure document upload for context-aware consultations</li>
        <li>Multiple AI model options for diverse healthcare needs</li>
        <li>Clear, accessible medical information</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Start Conversation Section
st.markdown("""
<div class="feature-card">
    <h3>🩺 Ready to Start Your Consultation?</h3>
    <p>Click below to begin your conversation with Medi Bud.</p>
</div>
""", unsafe_allow_html=True)

# Initiate Conversation Button
if st.button("Start Consultation", key="start_consultation"):
    st.session_state["conversation_initiated"] = True
    st.session_state["llm_model"] = llm_option
    if uploaded_file:
        st.session_state["uploaded_file"] = uploaded_file
    st.experimental_rerun()
    st.experimental_redirect("Conversation.py")

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; color: #666;">
    <p>Medi Bud - Your Trusted AI Health Assistant</p>
    <p style="font-size: 0.8rem;">Version 1.0.0 | © 2024 Medi Bud. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)    