CREATE TABLE [business table] (
[ID_Record] int,
[Account] int, 
[Branch] varchar(100), 
[External ID] varchar(100), 
[Business Status] varchar(100),
[Company Name] varchar(100), 
[Account Type] varchar(100), 
[Creation Date] varchar(100), 
[Modified Date] varchar(100),
[Closed Date] varchar(100),
[Business TAG] varchar(100),
[Security Category] int
)


-- Declare a variable to hold the search value
DECLARE @SearchValue NVARCHAR(MAX) = 'YourValue'; -- Replace 'YourValue' with the value you're looking for

-- Declare variables to hold the names of the current table and column, and the dynamic SQL command
DECLARE @TableName NVARCHAR(MAX), @ColumnName NVARCHAR(MAX), @Sql NVARCHAR(MAX);

-- Declare a table variable to store the results
DECLARE @Results TABLE (TableName NVARCHAR(MAX), ColumnName NVARCHAR(MAX));

-- Initialize a cursor to iterate over all columns in all tables, but only those with a max string length of 5
DECLARE TableCursor CURSOR FOR 
    SELECT TABLE_SCHEMA + '.' + TABLE_NAME, COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE DATA_TYPE IN ('char', 'varchar', 'nchar', 'nvarchar')
    AND (CHARACTER_MAXIMUM_LENGTH = 5 OR CHARACTER_MAXIMUM_LENGTH IS NULL);

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
