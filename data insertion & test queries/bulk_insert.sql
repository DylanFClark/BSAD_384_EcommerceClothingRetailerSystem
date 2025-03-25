
BULK INSERT supplier  
FROM 'file.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);

BULK INSERT supplier_rep  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);

BULK INSERT product  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);

BULK INSERT customer  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);



BULK INSERT review  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);

BULK INSERT item  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);

BULK INSERT cart  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);

BULK INSERT cart_item  
FROM 'file_location.csv' 
WITH (  
    FIELDTERMINATOR = ',',  
    ROWTERMINATOR = '\n',  
    FIRSTROW = 2  
);
