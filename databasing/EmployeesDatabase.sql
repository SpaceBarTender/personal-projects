CREATE TABLE EmployeeDenormalized (
	EEID VARCHAR(15),
	Full_Name VARCHAR(100),
    Job_Title VARCHAR(100),
    Department VARCHAR(100),
    Business_Unit VARCHAR(100),
    Gender ENUM('Male', 'Female'),
    Ethinicity ENUM('Asian', 'Black', 'Caucasian', 'Latino'),
    Age INT,
    Hire_Date DATE,
    Annual_Salary VARCHAR(50),
    Bonus VARCHAR(20),
    Country ENUM('Brazil','China','United States'),
    City ENUM('Austin','Beijing','Chengdu','Chicago','Chongqing','Columbus','Manaus','Miami','Phoenix','Rio De Janerio','Sao Paulo','Seattle','Shanghai'),
    Exit_Date DATE
    );



    
    