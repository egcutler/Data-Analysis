BULK INSERT [Business Data Flag]
FROM '/root/workspace/github.com/egcutler/Data-Analysis/Recon_Invalid_Data_Flags/Data_Archive/Business Data Flag.csv'
WITH
(
    FIELDTERMINATOR = ',',  -- or the appropriate field delimiter
    ROWTERMINATOR = '\n',   -- or the appropriate row delimiter
    FIRSTROW = 2            -- if your CSV file contains headers
);


