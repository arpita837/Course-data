import matplotlib.pyplot as plt
from data import course_marks

# Calculating average marks by course
course_avg_marks = {}
course_counts = {}

for record in course_marks:
    course_name = record['course_name']
    marks = record['marks']
    
    if course_name in course_avg_marks:
        course_avg_marks[course_name] += marks
        course_counts[course_name] += 1
    else:
        course_avg_marks[course_name] = marks
        course_counts[course_name] = 1

for course_name in course_avg_marks:
    course_avg_marks[course_name] /= course_counts[course_name]

# Creating a bar plot
plt.bar(course_avg_marks.keys(), course_avg_marks.values())
plt.xlabel('Courses')
plt.ylabel('Average Marks')
plt.title('Average Marks by Course')
plt.xticks(rotation=45, ha='right')
plt.show()
