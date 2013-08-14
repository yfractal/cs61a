-- !!!!!!!!!! http://www.tutorialspoint.com/sqlite/sqlite_order_by.htm

-- Q1
select title from Movie where director = 'Steven Spielberg'

-- Question 2
-- Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order.

select distinct year from Rating,Movie 
where Rating.mID = Movie.mID and 
 (stars = 4 or stars = 5 )
 order by year 


 -- Question 3
 -- Find the titles of all movies that have no ratings. 

 -- 1,select all the movies have rating
 -- 2,expect from all movies
select title from Movie 
except
select title from Movie , Rating where Movie.mID = Rating.mID;

-- Question 4
-- Some reviewers didn't provide a date with their rating. 
-- Find the names of all reviewers who have ratings with a NULL value for the date. 
select name from Rating,Reviewer where Rating.rID = Reviewer.rID and Rating.ratingDate  is null
order by year 

-- Question 5
-- Write a query to return the ratings data in a more readable format:
 -- reviewer name, movie title, stars, and ratingDate. 
 -- Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 
select name,title,stars ,ratingDate from Movie,Reviewer,Rating where Movie.mID = Rating.mID and Rating.rID = Reviewer.rID
order by name,title,stars ASC;

-- Question 6
-- For all cases where the same reviewer rated the same movie twice 

-- and gave it a higher rating the second time, 
-- return the reviewer's name and the title of the movie. 


 -- Movie ( mID, title, year, director )
 -- English: There is a movie with ID number mID, a title, a release year, and a director.

 -- Reviewer ( rID, name )
 -- English: The reviewer with ID number rID has a certain name.

 -- Rating ( rID, mID, stars, ratingDate )
 -- English: The reviewer rID gave the movie mID a number of stars rating (1-5) on a certain ratingDate. 

