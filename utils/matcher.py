def calculate_match_score(resume_keywords, job_keywords):
    resume_set = set(resume_keywords)
    job_set = set(job_keywords)
    
    if len(job_set) == 0:
        return 0
    
    matches = resume_set.intersection(job_set)
    
    score = (len(matches) / len(job_set)) * 100
    
    return round(score, 2)

def find_missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))

def find_matched_skills(resume_skills, job_skills):
    return list(set(job_skills).intersection(set(resume_skills)))