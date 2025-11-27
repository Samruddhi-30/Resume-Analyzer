import re

def extract_keywords(text):
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                  'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                  'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 
                  'should', 'could', 'may', 'might', 'must', 'can', 'this', 'that',
                  'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'}
    
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    
    keyword_freq = {}
    for word in keywords:
        keyword_freq[word] = keyword_freq.get(word, 0) + 1
    
    sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_keywords[:30]]  


def extract_skills(text):

    skills_database = [
        'python', 'java', 'javascript', 'c++', 'sql', 'r', 'html', 'css',
        'react', 'angular', 'vue', 'node', 'django', 'flask', 'spring',
        'machine learning', 'deep learning', 'data analysis', 'statistics',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'linux',
        'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
        'tableau', 'power bi', 'excel', 'powerpoint', 'jira', 'agile',
        'scrum', 'ci/cd', 'jenkins', 'selenium', 'api', 'rest', 'graphql',
        'mongodb', 'postgresql', 'mysql', 'redis', 'elasticsearch' , 'spark',
        'hadoop', 'nosql', 'microservices', 'devops', 'cybersecurity','machine learning',
        'artificial intelligence', 'data science', 'big data', 'blockchain', 'ui/ux design',
        'full stack development', 'mobile development', 'ios', 'android','flutter','react native' ,'rea'
        'swift', 'kotlin'
    ]
    
    text_lower = text.lower()
    found_skills = []
    
    for skill in skills_database:
        if skill in text_lower:
            found_skills.append(skill)
    
    return list(set(found_skills)) 