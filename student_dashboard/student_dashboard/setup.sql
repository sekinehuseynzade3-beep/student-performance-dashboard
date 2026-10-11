-- UniversityDB üçün cədvəl, nümunə data və Stored Procedure (Task 1)
USE UniversityDB;
GO

IF OBJECT_ID('dbo.Students', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Students (
        StudentID INT IDENTITY(1,1) PRIMARY KEY,
        Name      NVARCHAR(100) NOT NULL,
        Score     INT NOT NULL CHECK (Score BETWEEN 0 AND 100)
    );

    INSERT INTO dbo.Students (Name, Score) VALUES
        (N'Ali', 85), (N'Leyla', 72), (N'Murad', 48),
        (N'Aysel', 91), (N'Kamran', 63);
END
GO

CREATE OR ALTER PROCEDURE dbo.GetStudentResult
    @StudentName NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        Name,
        Score,
        CASE
            WHEN Score >= 90 THEN 'A'
            WHEN Score >= 80 THEN 'B'
            WHEN Score >= 70 THEN 'C'
            WHEN Score >= 60 THEN 'D'
            ELSE 'F'
        END AS Grade
    FROM dbo.Students
    WHERE Name = @StudentName;
END
GO

-- Test: EXEC dbo.GetStudentResult @StudentName = N'Ali';
