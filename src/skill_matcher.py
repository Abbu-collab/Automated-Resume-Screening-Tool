def extract_skills(text, required_skills):

    matched_skills = []

    for skill in required_skills:

        if skill.lower() in text.lower():

            matched_skills.append(skill)

    return matched_skills