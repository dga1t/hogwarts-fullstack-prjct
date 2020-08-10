
class Validator:
    def __init__(self, students_dict):
        self.students_dict = students_dict

    # abstract method that the other validator files override
    @staticmethod
    def validate():
        """abstract method for validator children classes"""
        pass
