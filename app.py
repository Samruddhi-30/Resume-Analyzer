import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf, clean_text, extract_email, extract_phone
from utils.keyword_extractor import extract_keywords, extract_skills
from utils.matcher import calculate_match_score, find_missing_skills, find_matched_skills
from utils.suggestions import generate_suggestions

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 18px;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    .skill-box {
        background-color: #e8f4f8;
        padding: 10px;
        border-radius: 5px;
        margin: 5px;
        display: inline-block;
    }
    .missing-skill {
        background-color: #ffe8e8;
        padding: 10px;
        border-radius: 5px;
        margin: 5px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Resume Analyzer for Job Seekers</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload your resume and job description to get an ATS compatibility score</div>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=['pdf','docx'], accept_multiple_files=False)
    
    if uploaded_file:
        st.success("Resume uploaded successfully!")

with col2:
    st.subheader("Enter Job Description here...")
    job_description = st.text_area(
        "Paste the job description here",
        height=200,
        placeholder="Paste the complete job description including requirements, skills, and qualifications..."
    )

analyze_button = st.button("Analyze Resume", use_container_width=True, type="primary")

if analyze_button:
    if uploaded_file is None:
        st.error("⚠️ Please upload your resume first!")
    elif not job_description.strip():
        st.error("⚠️ Please paste a job description!")
    else:
        with st.spinner("🔄 Analyzing your resume..."):
            
            resume_text = extract_text_from_pdf(uploaded_file)
            resume_text_clean = clean_text(resume_text)

            job_text_clean = clean_text(job_description)
            
            resume_keywords = extract_keywords(resume_text_clean)
            job_keywords = extract_keywords(job_text_clean)
            
            resume_skills = extract_skills(resume_text_clean)
            job_skills = extract_skills(job_text_clean)
            
            keyword_score = calculate_match_score(resume_keywords, job_keywords)
            skill_score = calculate_match_score(resume_skills, job_skills)
            
            overall_score = (keyword_score * 0.4) + (skill_score * 0.6)
            
            missing_skills = find_missing_skills(resume_skills, job_skills)
            matched_skills = find_matched_skills(resume_skills, job_skills)
        
        st.success("Analysis Complete!")

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Overall Match Score",
                value=f"{overall_score:.1f}%",
                delta="Good" if overall_score >= 70 else "Needs Improvement"
            )
        
        with col2:
            st.metric(
                label="Keyword Match",
                value=f"{keyword_score:.1f}%"
            )
        
        with col3:
            st.metric(
                label="Skills Match",
                value=f"{skill_score:.1f}%"
            )
        
        # Progress bar
        st.markdown("###ATS Compatibility")
        st.progress(overall_score / 100)
        
        if overall_score >= 80:
            st.success("Excellent! Your resume is highly compatible with this job!!!.")
        elif overall_score >= 60:
            st.warning("Good match, but there's room for improvement.")
        else:
            st.error("Your resume needs significant improvements to match this job.")
        

        st.markdown("### Matched Skills")
        if matched_skills:
            skills_html = "".join([f'<span class="skill-box">✓ {skill}</span>' for skill in matched_skills])
            st.markdown(skills_html, unsafe_allow_html=True)
        else:
            st.info("No technical skills matched. Consider adding relevant skills to your resume.")
        
        st.markdown("")
        
        # Show missing skills
        st.markdown("###Missing Skills")
        if missing_skills:
            missing_html = "".join([f'<span class="missing-skill">✗ {skill}</span>' for skill in missing_skills])
            st.markdown(missing_html, unsafe_allow_html=True)
            
            st.markdown("")
            st.info(" **Tip:** Add these skills to your resume if you have experience with them!")
        else:
            st.success("Great! You have all the required technical skills.")
        
        
        # Suggestions section (calling function from utils)
        st.markdown("###  Improvement Suggestions")
        suggestions = generate_suggestions(overall_score, skill_score, missing_skills)
        
        for suggestion in suggestions:
            st.markdown(suggestion)
        
        st.markdown("---")
        
        # Contact info extraction (bonus)
        with st.expander("Extracted Contact Information"):
            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Email:** {email}")
            with col2:
                st.write(f"**Phone:** {phone}")

# Footer
# st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>Helps understand job compatibility simpler</p>
    </div>
""", unsafe_allow_html=True)