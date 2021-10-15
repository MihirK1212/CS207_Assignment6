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
    session['dept_name_fac'] = dept_name
    if request.method=='POST':
        course=request.form['course']
        s_time=request.form['s_time']
        l_time = request.form['l_time']
        print(course)
        print(s_time)
        print(l_time)

        if int(s_time)==0:
            s_time=2009
        if int(l_time)==0:
            l_time=2021

        if course!='All':
            query = '''
                    SELECT cf.Faculty_ID,f.Faculty_Name,cf.Year,cf.Semester
                    FROM Course_Has_Faculty cf
                    JOIN Faculty f on cf.Faculty_ID = f.Faculty_ID
                    JOIN Course c on cf.Course_ID = c.Course_ID
                    WHERE cf.Year>=%s AND cf.Year<=%s AND c.course_Name='%s' ''' % (int(s_time), int(l_time),course)
        else:
            print("kuch nahi")
            query = '''SELECT cf.Faculty_ID,f.Faculty_Name,cf.Year,cf.Semester
                    FROM Course_Has_Faculty cf
                    JOIN Faculty f on cf.Faculty_ID = f.Faculty_ID
                    JOIN Course c on cf.Course_ID = c.Course_ID and c.Department_Name = '%s'
                    WHERE cf.Year>=%s AND cf.Year<=%s ''' % (session['dept_name_fac'],int(s_time), int(l_time))
        cur = myconn.cursor()
        cur.execute(query)
        courseDetails = cur.fetchall()
        print(courseDetails)
        return render_template('search_faculty.html',check=True,faculty=courseDetails,query_details=[course,s_time,l_time],d_name=session['dept_name_fac'])

    if session['dept_name_fac'] == 'none':
        return render_template('search_faculty.html',check=False,query_details=['','',''],d_name=session['dept_name_fac'])
    else:
        dept = session['dept_name_fac']
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
        return render_template('search_faculty.html',check=True,query_details=['','',''],d_name=session['dept_name_fac'])

@app.route('/search_course/<string:dept_name>', methods = ['GET', 'POST'])
def search_course(dept_name):
    session['dept_name_course'] = dept_name
    if request.method == 'POST':
        faculty = request.form.get('faculty')
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')

        if start_year == 'None':
            start_year=2011
        else:
            start_year=int(start_year)

        if end_year == 'None':
            end_year=2020
        else:
            end_year=int(end_year)

        if faculty == 'None':
            cur = myconn.cursor()
            query = "SELECT * FROM course WHERE Department_Name='%s' " % (session['dept_name_course'])
            cur.execute(query)
            course = cur.fetchall()
            course = list(set(course))
        else:
            cur1 = myconn.cursor()
            query1 = "SELECT course.Course_ID, course.Course_Name FROM course INNER JOIN course_has_faculty ON course.Course_ID = course_has_faculty.Course_ID AND course.Department_Name = '%s' AND course_has_faculty.faculty_ID = '%s' AND course_has_faculty.Year>='%s' AND course_has_faculty.Year<='%s' " % (session['dept_name_course'], faculty, start_year, end_year)
            cur1.execute(query1)
            course = cur1.fetchall()
            course = list(set(course))
        return render_template('search_course.html', check=True, course=course,d_name=session['dept_name_course'])

    if session['dept_name_course']=='none':
        return render_template('search_course.html',check=False,course=None,d_name=session['dept_name_course'])

    else:
        dept = session['dept_name_course']
        cur = myconn.cursor()
        query = "SELECT * FROM course WHERE Department_Name='%s' " % (dept)
        cur.execute(query)
        course = cur.fetchall()
        query1 = "SELECT faculty.Faculty_Name, faculty.Faculty_ID FROM faculty INNER JOIN course_has_faculty ON faculty.Faculty_ID = course_has_faculty.Faculty_ID AND faculty.Department_Name = '%s' " %(dept)
        cur1 = myconn.cursor()
        cur1.execute(query1)
        faculty = cur1.fetchall()
        session['faculty'] = list(set(faculty))
        session['dept'] = dept
        return render_template('search_course.html', check=True, course=course,d_name=session['dept_name_course'])
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
