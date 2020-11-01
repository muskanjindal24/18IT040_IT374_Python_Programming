class Teacher():
    def get_marks(self,s):
        print("Marks:",s.m)

    def set_marks(self,s,m):
        self.marks = list(m)
        s.marks(m)

    def calculate_total_marks(self):
        return sum(self.marks)