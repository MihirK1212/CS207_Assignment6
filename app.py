from re import A
# import cur as cur
from flask import Flask, render_template, request,session
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)
app.secret_key = 'Amit Kumar Makkad'
# myconn = mysql.connector.connect(host="localhost", user="root", passwd="amit@186", database="faculty_course",
#                                  buffered=True)

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "200001044mysql",database="course_management", buffered=True)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')


@app.route('/getSummary',methods=['GET','POST'])
def summary_page():
    if request.method=='POST':
        queryDetails = request.form
        semester = queryDetails['semester']
        year = queryDetails['year']
        print(year,semester)
        query = '''
        SELECT cf.Course_ID,c.Course_Name,c.Department_Name,cf.Faculty_ID,f.Faculty_Name,tt.Weekday,tt.Start_Time,
               tt.End_Time,tt.Semester,tt.Room_No,tt.Year
        FROM Course_Has_Faculty cf 
        JOIN TimeTable tt on cf.Course_ID = tt.Course_ID  AND cf.Year = tt.Year AND cf.Semester = tt.Semester
        JOIN Faculty f on cf.Faculty_ID = f.Faculty_ID
        JOIN Course c on cf.Course_ID = c.Course_ID
        WHERE cf.Year=%s AND cf.Semester='%s' '''  %(int(year),semester)

        cur = myconn.cursor()
        cur.execute(query)
        courseDetails = cur.fetchall()
        print(courseDetails)
        return render_template('summary.html',courseDetails=courseDetails)
    return render_template('summary.html',courseDetails='')

@app.route('/search_faculty/<string:dept_name>',methods =['GET', 'POST'])
def search_faculty(dept_name):
    session['dept_name'] = dept_name
    if request.method=='POST':
        course=request.form['course']
        s_time=request.form['s_time']
        l_time = request.form['l_time']
        s_sem = request.form['s_sem']
        l_sem = request.form['l_sem']
        if l_time!='':
            print(1)
            query = '''
                    SELECT cf.Faculty_ID,f.Faculty_Name,cf.Year,cf.Semester
                    FROM Course_Has_Faculty cf
                    JOIN Faculty f on cf.Faculty_ID = f.Faculty_ID
                    JOIN Course c on cf.Course_ID = c.Course_ID
                    WHERE cf.Year>='%s' AND cf.Year<='%s' AND c.course_Name='%s' ''' % (s_time, l_time,course)

        elif s_time!='':
            print(2)
            query = '''
                    SELECT cf.Faculty_ID,f.Faculty_Name,cf.Year,cf.Semester
                    FROM Course_Has_Faculty cf
                    JOIN Faculty f on cf.Faculty_ID = f.Faculty_ID
                    JOIN Course c on cf.Course_ID = c.Course_ID
                    WHERE cf.Year='%s' AND cf.Semester='%s'AND c.course_Name='%s' ''' % (s_time, s_sem,course)
        else:
            print(3)
            query = '''
                    SELECT cf.Faculty_ID,f.Faculty_Name,cf.Year,cf.Semester
                    FROM Course_Has_Faculty cf
                    JOIN Faculty f on cf.Faculty_ID = f.Faculty_ID
                    JOIN Course c on cf.Course_ID = c.Course_ID
                    WHERE c.course_Name='%s' ''' % (course)

        cur = myconn.cursor()
        cur.execute(query)
        courseDetails = cur.fetchall()
        return render_template('search_faculty.html',check=True,faculty=courseDetails,query_details=[course,s_time,l_time,s_sem,l_sem],d_name=session['dept_name'])

    if session['dept_name'] == 'none':
        return render_template('search_faculty.html',check=False,query_details=['','','','',''],d_name=session['dept_name'])
    else:
        dept = session['dept_name']
        cur = myconn.cursor()
        query = '''SELECT Faculty_ID,Faculty_Name FROM Faculty WHERE department_name='%s' ''' % (dept)

        cur = myconn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        q = '''SELECT * FROM Course WHERE department_name='%s' ''' % (dept)
        cur = myconn.cursor()
        cur.execute(q)
        d = cur.fetchall()
        session['dept']=d
        return render_template('search_faculty.html',check=True,query_details=['','','','',''],d_name=session['dept_name'])




if __name__ == '__main__':
    app.run(debug=True, port=8000)
