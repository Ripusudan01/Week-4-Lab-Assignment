from flask import Flask, render_template, request
import matplotlib.pyplot as plt, csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():
    if request.method == 'GET':
        return render_template("index.html")
    with open('DATA/data.csv', newline='') as file:
        reader = csv.reader(file) 
        
        if request.method == 'POST':
            student_course = []
            total_me = 0
            course_mark = []

            selected_id = request.form.get('ID')
            value_id = request.form.get('id_value')

            if selected_id == 'student_id':
                for row in reader:
                    if value_id in row[0]:
                        total_me += int(row[2].strip())  
                        student_course.append(row)  

            
                if student_course == []:
                    return render_template('wrong.html')
                else:
                    return render_template('details_1.html', total=total_me, student_course=student_course)
            elif selected_id == 'course_id':
                for row in reader:
                    if value_id in row[1]:
                        course_mark.append(int(row[2].strip()))
                if course_mark == []:
                    return render_template('wrong.html')
                else:
                    average_mark = sum(course_mark)/len(course_mark)
                    maximum_mark = max(course_mark)
                    x = course_mark
                    plt.clf()
                    plt.hist(x)
                    plt.savefig("static/hist.png")
                    return render_template('details_2.html',average_mark = average_mark, maximum_mark = maximum_mark)

                


app.run(debug=True)