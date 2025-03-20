import sqlite3

def create_tables():
    conn = sqlite3.connect("student_database.db")
    cursor = conn.cursor()

    # Create Students Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT,
            DateOfBirth DATE,
            Gender TEXT,
            Address TEXT,
            PhoneNumber TEXT,
            Email TEXT,
            EnrollmentDate DATE,
            DepartmentID INTEGER,
            FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
        )
    """)
    
    # Create Departments Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            DepartmentID INTEGER PRIMARY KEY,
            DepartmentName TEXT,
            DepartmentHead TEXT
        )
    """)
    
    # Create Courses Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY,
            CourseName TEXT,
            CourseCode TEXT,
            Credits INTEGER,
            DepartmentID INTEGER,
            FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
        )
    """)
    
    # Create Enrollments Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollments (
            EnrollmentID INTEGER PRIMARY KEY,
            StudentID INTEGER,
            CourseID INTEGER,
            EnrollmentDate DATE,
            Grade TEXT,
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        )
    """)
    
    # Create Grades Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Grades (
            GradeID INTEGER PRIMARY KEY,
            StudentID INTEGER,
            CourseID INTEGER,
            AssignmentName TEXT,
            Grade TEXT,
            GradeDate DATE,
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        )
    """)
    
    # Create Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Attendance (
            AttendanceID INTEGER PRIMARY KEY,
            StudentID INTEGER,
            CourseID INTEGER,
            AttendanceDate DATE,
            Status TEXT,
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        )
    """)
    
    # Create Contacts Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contacts (
            ContactID INTEGER PRIMARY KEY,
            StudentID INTEGER,
            ContactName TEXT,
            Relationship TEXT,
            PhoneNumber TEXT,
            Email TEXT,
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
        )
    """)

    

    
    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect("student_database.db")
    cursor = conn.cursor()

    # Insert Departments
    departments = [
        (1, 'Computer Science', 'Dr. Arvind Sharma'),
        (2, 'Mechanical Engineering', 'Dr. Ramesh Iyer'),
        (3, 'Electrical Engineering', 'Dr. Anjali Verma'),
        (4, 'Civil Engineering', 'Dr. Suresh Patil'),
        (5, 'Mathematics', 'Dr. Kavita Desai')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Departments VALUES (?, ?, ?)", departments)

    # Insert Students
    students = [
        (1, 'Amit', 'Kumar', '2001-01-15', 'Male', 'Mumbai', '9876543210', 'amit.kumar@example.com', '2022-08-01', 1),
        (2, 'Priya', 'Sharma', '2002-04-10', 'Female', 'Delhi', '9876543211', 'priya.sharma@example.com', '2022-08-01', 2),
        (3, 'Rahul', 'Verma', '2001-07-21', 'Male', 'Chennai', '9876543212', 'rahul.verma@example.com', '2022-08-01', 3),
        (4, 'Neha', 'Patel', '2002-09-30', 'Female', 'Kolkata', '9876543213', 'neha.patel@example.com', '2022-08-01', 4),
        (5, 'Vikas', 'Singh', '2001-12-15', 'Male', 'Bangalore', '9876543214', 'vikas.singh@example.com', '2022-08-01', 5),
        (6, 'Ritu', 'Joshi', '2002-02-25', 'Female', 'Hyderabad', '9876543215', 'ritu.joshi@example.com', '2022-08-01', 1),
        (7, 'Sanjay', 'Nair', '2001-05-18', 'Male', 'Pune', '9876543216', 'sanjay.nair@example.com', '2022-08-01', 2),
        (8, 'Kavita', 'Desai', '2002-06-11', 'Female', 'Ahmedabad', '9876543217', 'kavita.desai@example.com', '2022-08-01', 3),
        (9, 'Arjun', 'Mehta', '2001-08-27', 'Male', 'Jaipur', '9876543218', 'arjun.mehta@example.com', '2022-08-01', 4),
        (10, 'Ananya', 'Rao', '2002-03-14', 'Female', 'Lucknow', '9876543219', 'ananya.rao@example.com', '2022-08-01', 5)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", students)

    cursor.executemany("INSERT INTO Courses (CourseName, CourseCode, Credits, DepartmentID) VALUES (?, ?, ?, ?)", [
        ('Data Structures', 'CS101', 4, 1),
        ('Machine Learning', 'CS102', 4, 1),
        ('Engineering Mathematics', 'MATH101', 3, 2),
        ('Physics', 'PHY101', 3, 3),
        ('Artificial Intelligence', 'CS103', 4, 1)
    ])
    # Insert 10 records into the Enrollments table with explicit EnrollmentID values
    cursor.executemany("""
    INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate, Grade) 
    VALUES (?, ?, ?, ?, ?)
""", [
    (1, 1, 1, '2024-09-01', 'A'),
    (2, 1, 3, '2024-09-01', 'B+'),
    (3, 2, 2, '2024-09-02', 'A-'),
    (4, 2, 4, '2024-09-02', 'B'),
    (5, 3, 1, '2024-09-03', 'C+'),
    (6, 3, 5, '2024-09-03', 'A'),
    (7, 4, 3, '2024-09-04', 'B-'),
    (8, 4, 5, '2024-09-04', 'A-'),
    (9, 5, 2, '2024-09-05', 'B+'),
    (10, 5, 4, '2024-09-05', 'A')
])
    # Insert 10 records into the Grades table
    cursor.executemany("""
    INSERT INTO Grades (GradeID, StudentID, CourseID, AssignmentName, Grade, GradeDate) 
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 1, 1, 'Midterm Exam', 'A', '2024-10-15'),
    (2, 1, 3, 'Final Project', 'B+', '2024-11-20'),
    (3, 2, 2, 'Quiz 1', 'A-', '2024-09-25'),
    (4, 2, 4, 'Lab Report', 'B', '2024-10-05'),
    (5, 3, 1, 'Homework 3', 'C+', '2024-10-10'),
    (6, 3, 5, 'Term Paper', 'A', '2024-11-15'),
    (7, 4, 3, 'Group Presentation', 'B-', '2024-10-22'),
    (8, 4, 5, 'Final Exam', 'A-', '2024-12-01'),
    (9, 5, 2, 'Programming Assignment', 'B+', '2024-10-18'),
    (10, 5, 4, 'Research Paper', 'A', '2024-11-25')
])

# Insert 10 records into the Attendance table with only 'Present' or 'Absent' status
    cursor.executemany("""
    INSERT INTO Attendance (AttendanceID, StudentID, CourseID, AttendanceDate, Status) 
    VALUES (?, ?, ?, ?, ?)
""", [
    (1, 1, 1, '2024-09-05', 'Present'),
    (2, 1, 3, '2024-09-06', 'Present'),
    (3, 2, 2, '2024-09-05', 'Absent'),
    (4, 2, 4, '2024-09-07', 'Present'),
    (5, 3, 1, '2024-09-08', 'Present'),
    (6, 3, 5, '2024-09-09', 'Absent'),
    (7, 4, 3, '2024-09-10', 'Present'),
    (8, 4, 5, '2024-09-11', 'Present'),
    (9, 5, 2, '2024-09-12', 'Absent'),
    (10, 5, 4, '2024-09-13', 'Present')
])

# Insert 10 records into the Contacts table with Indian names and 10-digit Indian phone numbers
    cursor.executemany("""
    INSERT INTO Contacts (ContactID, StudentID, ContactName, Relationship, PhoneNumber, Email) 
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 1, 'Rajesh Sharma', 'Father', '9876543210', 'rajesh.sharma@email.com'),
    (2, 1, 'Priya Sharma', 'Mother', '9876543211', 'priya.sharma@email.com'),
    (3, 2, 'Vikram Patel', 'Father', '8765432109', 'vikram.patel@email.com'),
    (4, 2, 'Meena Patel', 'Mother', '8765432108', 'meena.patel@email.com'),
    (5, 3, 'Suresh Verma', 'Guardian', '7654321098', 'suresh.verma@email.com'),
    (6, 3, 'Anita Verma', 'Guardian', '7654321097', 'anita.verma@email.com'),
    (7, 4, 'Amit Kumar', 'Father', '9654321087', 'amit.kumar@email.com'),
    (8, 4, 'Sunita Kumar', 'Mother', '9654321086', 'sunita.kumar@email.com'),
    (9, 5, 'Ramesh Singh', 'Father', '8543210976', 'ramesh.singh@email.com'),
    (10, 5, 'Lata Singh', 'Mother', '8543210975', 'lata.singh@email.com')
])


# Commit the changes
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    print("Student database created successfully with sample data.")
