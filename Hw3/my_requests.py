ex_1 = """
SELECT 
    FirstName,
    LastName
FROM 
    Customers
WHERE 
    City = 'Prague'
"""

ex_2 = """
SELECT 
    FirstName, 
    LastName
FROM 
    Customers
WHERE 
    FirstName LIKE 'M%' AND FirstName LIKE '%ch%'
"""

ex_3 = """
SELECT 
    Name, 
    CAST(Bytes AS REAL) / 1048576 AS Size_MB -- 1048576 bytes in 1 MB
FROM 
    Tracks
"""

ex_4 = """
SELECT 
    LastName, 
    FirstName
FROM 
    Employees
WHERE 
    STRFTIME('%Y', HireDate) = '2002' AND City = 'Calgary'
"""

ex_5 = """
SELECT 
    LastName, 
    FirstName
FROM 
    Employees
WHERE 
    HireDate - BirthDate >= 40
"""

ex_6 = """
SELECT 
    FirstName, 
    LastName
FROM 
    Customers
WHERE 
    Country = 'USA' AND Fax IS NULL
"""

ex_7 = """
SELECT
    ShipCity
FROM
    sales
WHERE
    ShipCountry = "Canada" AND STRFTIME('%m', SalesDate) IN ('08', '09')
"""

ex_8 = """
SELECT
    Email 
FROM
    Customers
WHERE
    Email LIKE '%@gmail.com'
"""

ex_9 = """
SELECT
    LastName, FirstName
FROM
    Employees
WHERE
    HireDate <= date("now", "-18 year")
"""

ex_10 = """
SELECT
    DISTINCT Title
FROM
    Employees
ORDER BY Title ASC
"""

ex_11 = """
SELECT
    LastName, FirstName, strftime("%Y", date("now")) - Age AS BirthYear
FROM
    customers
ORDER BY
    LastName, FirstName, BirthYear
"""

ex_12 = """
SELECT
    CAST(MIN(Milliseconds) as REAL) / 1000 as seconds
FROM
    tracks
"""

ex_13 = """
SELECT
    Name, CAST(MIN(Milliseconds) as REAL) / 1000 as seconds
FROM
    tracks
WHERE
    milliseconds = (
    SELECT
        min(milliseconds)
    FROM
        tracks
    )
"""

ex_14 = """
SELECT
    Country, AVG(Age) AS AverageAge
FROM
    Customers
GROUP BY Country;
"""

ex_15 = """
SELECT
    LastName
FROM
    Employees
WHERE
    STRFTIME('%m', HireDate) = '10';
"""

ex_16 = """
SELECT
    LastName
FROM
    Employees
ORDER BY HireDate ASC
LIMIT 1;
"""