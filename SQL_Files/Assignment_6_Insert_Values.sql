INSERT INTO `Department` (Department_Name)
VALUES
('Computer Science and Engineering'),('Mechanical Engineering'),('Electrical Engineering'),('Civil Engineering'),('MEMS Engineering');

INSERT INTO `Course` (Course_ID,Course_Name,Department_Name)
VALUES
('CS1','ASD','Computer Science and Engineering'),
('ME1','ADASD','Mechanical Engineering'),
('CS2','AEGD','Computer Science and Engineering'),
('EE1','AWR','Electrical Engineering'),
('MEMS1','AQWE','MEMS Engineering'),
('CE1','ASQWE','Civil Engineering'),
('EE2','AASD','Electrical Engineering');

INSERT INTO `Faculty` (Faculty_ID,Faculty_Name,Department_Name)
VALUES
('FACS1','ETT','Computer Science and Engineering'),
('FAME1','QWE','Mechanical Engineering'),
('FACS2','AOOQ','Computer Science and Engineering'),
('FAEE1','XCV','Electrical Engineering'),
('FAMEMS1','HT','MEMS Engineering'),
('FACE1','ASTHRE','Civil Engineering'),
('FAEE2','RTHRTH','Electrical Engineering'),
('FACS3','EASDAT','Computer Science and Engineering'),
('FAME2','ASADS','Mechanical Engineering'),
('FACS4','AADSAD','Computer Science and Engineering'),
('FAEE3','ASDSAADS','Electrical Engineering'),
('FAMEMS2','ASDASD','MEMS Engineering'),
('FACE2','AADADS','Civil Engineering'),
('FAEE4','ASDADSADS','Electrical Engineering');



INSERT INTO `Course_Has_Faculty` (Course_ID,Faculty_ID,Year,Semester,Students)
VALUES
('CE1','FACE1',2014,'Autumn',55),
('CS1','FACS1',2012,'Spring',45),
('ME1','FAME1',2011,'Autumn',11),
('CS2','FACS2',2015,'Spring',22),
('CE1','FACE1',2016,'Spring',46),
('CS1','FACS1',2011,'Autumn',35),
('CS1','FACS2',2014,'Spring',58),
('MEMS1','FAMEMS1',2017,'Autumn',39),
('CE1','FACE1',2015,'Spring',41),
('CE1','FACE1',2011,'Autumn',22),
('CE1','FACE1',2012,'Spring',31),
('MEMS1','FAMEMS1',2013,'Autumn',75),
('EE2','FAEE2',2011,'Spring',56),
('CS1','FACS1',2013,'Spring',65),
('MEMS1','FAMEMS1',2014,'Autumn',80),
('EE1','FAEE2',2016,'Autumn',13),
('MEMS1','FAMEMS1',2015,'Spring',44),
('EE2','FAEE4',2019,'Autumn',44),

('EE2','FAEE3',2013,'Spring',50),
('EE2','FAEE3',2013,'Autumn',55);


INSERT INTO `TimeTable` (Course_ID,Start_Time,End_Time,Year,Weekda,Room_No,Semester)
VALUES
('CS2','08:00:00','10:00:00',2015,'Monday','L103','Spring'),
('CS2','08:00:00','10:00:00',2015,'Tuesday','L103','Spring'),
('CS2','08:00:00','10:00:00',2015,'Wednesday','L103','Spring'),
('EE2','10:00:00','11:50:00',2011,'Wednesday','L102','Spring'),
('EE2','10:00:00','11:50:00',2011,'Thursday','L102','Spring'),
('CE1','09:00:00','09:50:00',2011,'Thursday','L111','Autumn'),
('CE1','09:00:00','09:50:00',2011,'Friday','L111','Autumn'),
('CE1','09:00:00','09:50:00',2011,'Saturday','L111','Autumn'),
('MEMS1','07:00:00','09:00:00',2015,'Thursday','POD101','Spring'),
('MEMS1','06:00:00','08:00:00',2015,'Friday','POD102','Spring'),
('MEMS1','08:00:00','10:00:00',2015,'Saturday','POD103','Spring'),

('EE2','11:24:00','12:36:00',2013,'Saturday','KOD111','Spring'),
('EE2','11:24:00','12:36:00',2013,'Sunday','KOD111','Spring'),
('EE2','11:24:00','12:36:00',2013,'Saturday','KOD111','Autumn'),
('EE2','11:24:00','12:36:00',2013,'Sunday','KOD111','Autumn');







