import json

possessed_skills = ['invisibility', 'levitation', 'healing']
desired_skills = ['teleportation', 'programming', 'rainofmoney']


class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__)
