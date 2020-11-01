from teachinglearning import student as student
from teachinglearning import teacher as teacher

class generate_result():
    def generate_result(self,s,t):
        attendance = s.get_attendance()
        m = t.marks
        result = t.calculate_total_marks()/len(m)
        print("Student Attendance:",attendance,"%")
        print("Result:",result)

s1 = student.Student()
t1 = teacher.Teacher()
s1.set_attendance(85)
t1.set_marks(s1,[82,75,98,100])
result = generate_result()
result.generate_result(s1,t1)