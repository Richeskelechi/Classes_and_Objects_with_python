class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        return(Bob.name)

    def change_age(self, new_age):
        self.age = new_age
        return(Bob.age)

    def add_track(self, added_track):
        self.tracks.append(added_track)
        return(Bob.tracks)

    def get_score(self):
        return(self.score)


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)
# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
