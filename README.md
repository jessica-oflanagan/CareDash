# CareDash
CareDash Assignment
-------------------README------------------

This was my take on the CareDash coding assignment.

For the web design, I chose to implement using HTML, CSS, and some JavaScript.  
I am happy with the final product of these, but I think that there are a few
directions that I would take it, given the time.

   - ensuring that all divs and buttons don't move with window resizing

   - adding a second form for a login

   - adding a third form for users to post reviews


I think that these three things would take it to the next level, but
I had a lot of fun putting the page together and I really enjoy the final
product!


I unfortunately did not finish the API to interact with the MySQL database.
As of right now, my understanding is the the HTML is not triggering itself to 
go to the python function to process the form, and that is where I got 
stuck.  I did, however, connect the database, create some columns
for data, and use SQLAlchemy to match the columns in the online
database.  Here's what I would do next if I had more time and 
midterms had not (sadly) gotten in the way:

- restructure my HTML to make sure the filling out the form triggers the 
  python function 'process'

- add a database for 'reviews', and nest that in the other database

- create another function for posting a review and have it 
  attach to a parent data member.  
