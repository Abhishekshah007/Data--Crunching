# Data--Crunching

Documentation


Problem:

          We have obtained raw database from one of the popular site on the internet with large
          user base.Now we need to process that data and determine passwords of all users. The only issue
          is we don’t have high end machines to process this data so we have to go with low end
          machines to perform this task.
          

Objective:

           we need to create tool/script/program which crunches data from these
           different TSV files and aggregates them to output file.


Approch:

           Here is my approach to solving this program: First, I check all the data for a common value or column, 
           and I discovered that two files share the same column name, and a third has a common value but no heading, 
           so I edit the .tsv file because adding just the column name makes my code half as long, and also try to remove 
           files which are not useful after getting output so that it not use more power and memory


Language and Libraries:

           Python
              - Pandas
              - CSV
              - OS




Method and Solution:

           I used Python and Pandas, as well as an attempt to use R, but R does not provide an optimised solution, so I used the 
           PANDAS library to read .tsv files and merge them with a common column, and I used an inner join to save memory by 
           ignoring rows with missing values. Following that, I used OS Lib to remove unnecessary files and clear the cache if it existed. 

Result:
           Id, username, email, hashed_password, plaintext_password, ip

