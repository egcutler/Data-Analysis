-- Declare a variable to hold the search value
DECLARE @SearchValue NVARCHAR(MAX) = 'YourValue'; -- Replace 'YourValue' with the value you're looking for
--DECLARE @SubStr NVARCHAR(MAX) = 'SubStr'; -- Replace 'SubStr' with the substring you're looking for in column names
--DECLARE @TableSubStr NVARCHAR(MAX) = 'SubStr'; -- Replace 'SubStr' with the substring you're looking for in table names

-- Declare variables to hold the names of the current table and column, and the dynamic SQL command
DECLARE @TableName NVARCHAR(MAX), @ColumnName NVARCHAR(MAX), @Sql NVARCHAR(MAX);

-- Declare a table variable to store the results
DECLARE @Results TABLE (TableName NVARCHAR(MAX), ColumnName NVARCHAR(MAX));

-- Initialize a cursor to iterate over columns in all tables that contain the specified substring in their names
DECLARE TableCursor CURSOR FOR 
    SELECT TABLE_SCHEMA + '.' + TABLE_NAME, COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    --WHERE COLUMN_NAME LIKE '%' + @SubStr + '%'; -- Filter columns by the specified substring
    --WHERE TABLE_NAME LIKE '%' + @TableSubStr + '%'; -- Filter tables by the specified substring
    --WHERE DATA_TYPE IN ('char', 'varchar', 'nchar', 'nvarchar')
    --AND (CHARACTER_MAXIMUM_LENGTH = 5 OR CHARACTER_MAXIMUM_LENGTH IS NULL);

-- Open the cursor
OPEN TableCursor;

-- Fetch the first row from the cursor
FETCH NEXT FROM TableCursor INTO @TableName, @ColumnName;

-- Loop through each column in each table
WHILE @@FETCH_STATUS = 0
BEGIN
    -- Construct a dynamic SQL to check if the current column contains the search value
    SET @Sql = N'SELECT TOP 1 ''' + @TableName + ''' AS TableName, ''' + @ColumnName + ''' AS ColumnName 
                 FROM ' + @TableName + ' 
                 WHERE CAST(' + @ColumnName + ' AS NVARCHAR(MAX)) = @SearchValue';

    -- Execute the dynamic SQL inside a TRY block to handle potential errors
    BEGIN TRY
        INSERT INTO @Results (TableName, ColumnName)
        EXEC sp_executesql @Sql, N'@SearchValue NVARCHAR(MAX)', @SearchValue;
    END TRY
    BEGIN CATCH
        -- Error handling: This block can be used to handle errors or incompatible column types
    END CATCH

    -- Fetch the next row from the cursor
    FETCH NEXT FROM TableCursor INTO @TableName, @ColumnName;
END

-- Close and deallocate the cursor
CLOSE TableCursor;
DEALLOCATE TableCursor;

-- Select and display all rows from the results table
SELECT * FROM @Results;
