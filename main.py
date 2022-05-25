# Here I created A class called students
class Student:
    # [assignment] Skeleton class. Add your code here
    # I have an __init__ function that specifies the constructor of the class
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    # A function to change the name of the student 
    def change_name(self, new_name):
        self.name = new_name
        return(Bob.name)

    # A function to change the age of a student
    def change_age(self, new_age):
        self.age = new_age
        return(Bob.age)

    # A function to add track to an existing list of tracks 
    def add_track(self, added_track):
        self.tracks.append(added_track)
        return(Bob.tracks)

    # A function to get the score of a student
    def get_score(self):
        return(self.score)

# Here I am creating an Instance of the class together with the properties 
Bob = Student("Bob", 26, ["FE", "BE"], 20.90)
# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
