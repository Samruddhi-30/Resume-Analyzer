def generate_suggestions(overall_score, skill_score, missing_skills):
    """Generate improvement suggestions based on analysis"""
    suggestions = []
    
    if overall_score < 70:
        suggestions.append("🔸 Add more keywords from the job description naturally throughout your resume")
    
    if len(missing_skills) > 0:
        suggestions.append(f"🔸 Highlight your experience with: {', '.join(missing_skills[:3])}")
    
    if skill_score < 50:
        suggestions.append("🔸 Add a dedicated 'Technical Skills' section to your resume")
    
    suggestions.append("🔸 Use action verbs like 'Developed', 'Implemented', 'Managed', 'Led'")
    suggestions.append("🔸 Quantify your achievements with numbers and metrics")
    suggestions.append("🔸 Tailor your resume summary to match the job description")
    
    return suggestions