dic = {} # - Empty Dictionaru
about_me = {
    "myName": "Moattar",
    "job" : "As a Junior Developer",
    "education": {
        "highSchool": "Arizona State University",
        "university": "University of Arizona"
    },
    "skills": ["Python", "JavaScript", "HTML", "CSS", "React"],
    "hobbies": ["Reading", "Coding", "Photography"],
    "friends": "No Friends",
    "family": ["Mom", "Dad", "Sisters"]
}

print(about_me)
print(type(about_me))
print(f"My Name: {about_me['myName']}")
print(f"My Job: {about_me['job']}")
print(f"My Education: {about_me['education']}")
print(f"My Skills: {about_me['skills']}")
print(f"My Hobbies: {about_me['hobbies']}")
about_me["friends"] = "Mahi"
print(f"My Friends: {about_me['friends']}")
print(f"My Family: {about_me['family']}")

