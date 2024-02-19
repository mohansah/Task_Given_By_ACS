SELECT T1.NumOrders, T1.CustomerID, T2.CustomerName, T1.ShipperID, T3.ShipperName, T1.Month, T1.Year
FROM (
    SELECT 
        YEAR(OrderDate) AS Year,
        MONTH(OrderDate) AS Month,
        CustomerID,
        ShipperID,
        COUNT(OrderID) AS NumOrders
    FROM 
        Orders
    GROUP BY 
        YEAR(OrderDate),
        MONTH(OrderDate),
        CustomerID,
        ShipperID
) AS T1
LEFT JOIN Customers AS T2 ON T1.CustomerID = T2.CustomerID
LEFT JOIN Shippers AS T3 ON T1.ShipperID = T3.ShipperID;