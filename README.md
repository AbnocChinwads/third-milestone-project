# Third Milestone Project

For this project I chose to build a web app that allows people to add details about games to a webpage, and to leave reviews on any games added.
The basic premise of this app is to allow people to share their views on either their favourite or least favourite games.

## UX

The intended users of this website would be anyone who enjoys playing video games.
They would visit this website and have the ability to add specific details about any video game, and then be able to add a review by visiting that games page.

    * As a casual gamer, I want to check out what other people are saying about games, and to see if it sounds like I would enjoy them.
    
    * As someone who doesn't earn a high amount, I want the ability to check out what other people think of a game before I spend my hard earned money on it.

## Features

#### Existing Features
    
* Title – This tells the user the name of the web service.

* Table on main page - This lists all of the games in the database; using their name, genre, and age rating.

* Pagination - These sets of links allow the user to show the next set of games in the database.

* Dark mode – This switch is located in the top left of the webpage, and can be used if the user wants a less harsh viewport, it switches the background colour to baltic sea, the text colour to goldenrod, and the link hover colour to a plum.
  The dark mode switch will persist through page loads as it makes use of a localStorage variable.

* Header – This contains the dark mode switch and page links, which allows users to achieve navigation to the home page, the add game form, and to the contact email.

* Footer – This contains social media links to Facebook, Instagram and Twitter.

#### Features Left to Implement

* The addition of a login system, so that users can only edit or remove their own reviews.

* Add a filter function to the table to only show games of a certain genre or age rating.

* Add a contact page that displays contact information for snail mail and phone as well as email, and to differentiate between business and personal contact requests.

## Technologies Used

* HTML 5 (https://www.w3schools.com/html/html5_intro.asp)
The project uses HTML 5 to create the webpage.

* CSS 3 (https://www.w3schools.com/css/)
The project uses CSS 3 to customise the look of the website

* Bootstrap v4.5.0 (https://getbootstrap.com/)
The project uses Bootstrap to simplify CSS processes

* Font Awesome v5.13.0 (https://fontawesome.com/)
The project uses Font Awesome to provide images for social media links and alongside the header links

* jQuery (https://jquery.com/)
The project uses jQuery for the dark mode switch and deletion of the flash messages

* Flask (https://flask.palletsprojects.com/en/1.1.x/quickstart/)
The project uses Flask to connect the frontend and backend processes using python

* Flask-Paginate (https://pythonhosted.org/Flask-paginate/)
The project uses Flask-paginate to create the pagination in the table on the main page

* Python 3.x (https://www.python.org/doc/)
The project uses Python, in conjunction with Flask framework and the imported modules to create a backend connection for the frontend.

* PyMongo (https://api.mongodb.com/python/current/tutorial.html)
PyMongo is used to create a connection to the MongoDB collections used in the project

* MongoDB (https://www.mongodb.com/)
MongoDB was the chosen database system to store the information used in this project

## Testing

As a casual gamer myself, I distributed a live link to my web game to friends, so that I could have a group of testers alert me to any issues or work arounds to my design. I would receive regular feedback through messages on Whatsapp and Facebook, that would alert me to various issues with the latest live version.

The dark mode switch came from a side project in which I was trying to create a persistent dark mode switch, it required some googling and reading of documentation on localStorage to get the code to work. But as it does function as intended I decided to include it in this project, to add something that is becoming more and more the standard in the development world.

The initial design relied on just connecting the backend to a very simplistic frontend, the design of the landing page has changed very little as user feedback was that the simple design made it easy to find specific games.

With each stage of development I utilised google chromes developer tools to see how my website would function on varying screen sizes. On smaller screen sizes the main header was too large and spilled over the other elements.

4K resolution brought the new issue of the font size being too small to read. This required the addition of media queries to increase all of the text sizes.

There was an issue on mobile screen sizes, where users reported the heading sat too close to the dark mode switch and overflowed to it, this was fixed by decreasing the h1 font size to 2rem as standard.

## Deployment

Having written the code in Gitpod, it was quite easy to deploy it on GitHub, I did this by using the git commands to add (git add), and then commit (git commit -m) my files to my Gitpod session, and then used the git push command to push the changes through to my master branch.
As GitHub does not run python the live version of this project was deployed on Heroku. This was easily done by linking the commits via heroku git:remote -a, and then using the command git push heroku master. It did require the use of a requirements.txt and Procfile to run properly.

The deployed version is different to the development version as initially it was going to have a contact page and display all the games for review in one table, through user feedback it was found that a contact page was unneccessary as there was only an email to contact. Initially when adding and editing information, the user was just taken to the main page but given no indication that it was successful, this was fixed through the use of flash messages which appear at the top of the main page after a succesful addition or edit.

If you want to run my code locally, choose the IDE you’re most comfortable with, if that is Gitpod then you'll need to add an env.py file that includes an `os.environ["MONGO_URI"]` and `os.environ["SECRET_KEY"]`. Then type into the terminal ‘python3 app.py’ to open a port that will run the site in your web browser. For other IDEs you will have to check their help files as to how to do this.

## Credits

#### Content

* The dark mode switch code came from online searching and reading through the use of localStorage (https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

* Flash messages came from online searching and reading up on Flask utils (https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).

* Pagination, as mentioned above, came from reading the Flask-Paginate documentation (https://pythonhosted.org/Flask-paginate/).

#### Media

* The media in this project where added by me is referenced by the "By Source, Fair Use" link below the image.

#### Acknowledgements

* I received inspiration for using Flask-Paginate and flash messages from google searches and stackoverflow queries on how to best paginate and display messages when using the Flask framework.

* I used stackoverflow to find the solution to how best to close the flash messages (https://stackoverflow.com/questions/19704477/adding-close-button-in-div-to-close-the-box).