CREATE TABLE IF NOT EXISTS `Department` (
  `Department_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Department_Name`));

CREATE TABLE IF NOT EXISTS `Course` (
  `Course_ID` VARCHAR(45) NOT NULL,
  `Course_Name` VARCHAR(45) NULL DEFAULT NULL,
  `Department_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Course_ID`), 
  FOREIGN KEY (`Department_Name`) REFERENCES `Department` (`Department_Name`) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS `Faculty` (
  `Faculty_ID` VARCHAR(45) NOT NULL,
  `Faculty_Name` VARCHAR(45) NOT NULL,
  `Department_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Faculty_ID`),
  FOREIGN KEY (`Department_Name`) REFERENCES `Department` (`Department_Name`) ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS `Course_Has_Faculty` (
  `Course_ID` VARCHAR(45) NOT NULL,
  `Faculty_ID` VARCHAR(45) NOT NULL,
  `Year` INT,
  `Semester` VARCHAR(45),
  `Students` INT,
  PRIMARY KEY (`Course_ID`, `Faculty_ID`,`Year`,`Semester`),
  KEY(`Course_ID`),
   KEY(`Year`),
   KEY(`Semester`),
   KEY(`Course_ID`,`Year`,`Semester`),
  FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`) ON DELETE CASCADE,
 FOREIGN KEY (`Faculty_ID`) REFERENCES `Faculty` (`Faculty_ID`) ON DELETE CASCADE);
    
    
CREATE TABLE IF NOT EXISTS `TimeTable` (
  `Time_ID` INT AUTO_INCREMENT,
  `Course_ID` VARCHAR(45) NOT NULL,
  `Start_Time` TIME,
  `End_Time` TIME,
  `Year` INT ,
  `Weekda` VARCHAR(45) ,
  `Room_No` VARCHAR(45) ,
  `Semester` VARCHAR(45) ,
  KEY (`Time_ID`),
  PRIMARY KEY(`Course_ID`,`Start_Time`,`End_Time`,`Year`,`Weekda`,`Room_No`,`Semester`),
 FOREIGN KEY (`Course_ID`,`Year`,`Semester`) REFERENCES `Course_Has_Faculty` (`Course_ID`,`Year`,`Semester`) ON DELETE CASCADE
);
