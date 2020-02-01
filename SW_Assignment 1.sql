
/*How many airplanes have listed speeds?  What is the 
minimum listed speed and the maximum listed speed?*/

Select tailnum,manufacturer,model,speed from planes where speed is not null;

-- There are 23 planes with listed speeds the minimum spee is 90 the maximum speed is 432

/*What is the total distance flown by all of the planes in 
January 2013?  W
hat is the total distance flown by all of 
the planes in January 2013 where the tailnum is 
missing?*/

Select SUM(distance) from flights where month = 1 and year = 2013;
Select SUM(distance) from flights where month = 1 and year = 2013 and tailnum = null;

-- The total distance for planes flown in January 2013 is 27,188,805 miles. There are no missing tailnums in flights

/* What is the total distance flown for all planes on July 5, 
2013 grouped by aircraft manufacturer?  Write this 
statement first using an INNER JOIN, then using 
a LEFT 
OUTER JOIN
.  How do your results compare?*/

SELECT SUM(distance), p.manufacturer
From flights f
Inner Join planes p
ON f.tailnum = p.tailnum
Where f.month = 7 and f.day = 5 and f.year = 2013
Group by manufacturer;

-- My results show the sum of the distance for each manufacturer

SELECT SUM(distance), p.manufacturer
From flights f
Left Outer Join planes p
ON f.tailnum = p.tailnum
Where f.month = 7 and f.day = 5 and f.year = 2013
Group by manufacturer;

-- My results dont show much difference, only a re-order of the chart and a new null manufacturer

-- What Carrier's plane traveled the farthest distance?

SELECT f.tailnum, distance,a.carrier
From flights f
Inner Join planes p on p.tailnum = f.tailnum
Inner Join airlines a on a.carrier = f.carrier;
-- Carrier HA, tailnum N380HA, traveled 4,983 miles (farthest distance)