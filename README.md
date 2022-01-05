<h1 align="center">Best of Music</h1>

<h1>About:</h1>
This is the website for Best of Music. A community that will allow users to upload their favourite artist/albums and rate them accordingly. Users have the ability to see which albums are more recently uploaded and the highest rated albums. Users will also be able to rate the music that is uploaded and edit their own ratings or reviews as they see fit. Best of music is designed to be responsive on all screen sizes and work across multiple devices. Ensuring it is easy for new and existing users to sign up, login, and upload their favourite albums and rate existing ones. 



## Contents
-  ###  [UX User Experience](#User-Experience-(UX))
    -   [User Stories](#User-stories)
    -   [Site Owner Goals](#Site-Owner-Goals)

-  ###  [Website Design](#Design-Choices) 
    -   [Typography](#Typography)
    -   [Colours](#Colour-Scheme)
    -   [Imagery](#Imagery)
    -   [Wireframes](#Wireframes)

-  ###  [Technologies](#Technologies-Used)
    -   [Languages](#Languages-Used)
    -   [Database](#Database-Used)
    -   [Libraries](#frameworks-Libraries-&-Programs-Used)

-  ###  [Features](#Features)  
    -   [Site Navigation](#Site-Navigation)
    -   [Current Features](#Current-Features)

-  ###  [Testing](TESTING.md)

-  ###  [Deployment](#GitHub-Pages)
    -   [GitHub Pages](#GitHub-Pages)

-  ###  [Credits](#Code)
    -   [Code](#Code)
    -   [Content](#Content)
    -   [Media](#Media)

    ## User Experience (UX)

### User stories

-   ### As a First Time User

    - I want to be able to quickly understand the websites purpose.
    - I want to easily navigate the site and see what content is available.
    - I want to be able to quickly join so I can rate music.
    - I would like the ability to read reviews of the music uploaded.
    - I want to be able to see ratings of all the music uploaded.


-   ### As a Returning User

    - I want to be able to easily login.
    - I want to still be able to see uploaded albums.
    - I would like the ability to upload music.
    - I would like the ability to read reviews of the music uploaded.
    - I would like to be able to edit my own ratings or reviews if I change my mind.


-   ### Frequent User

    - I want to be able to upload music.
    - I want to be able to see my uploaded music or reviews easily. 
    - I would like to rate music as much as I want.
    - I want the ability to rate albums as I see them in their rankings.
    - I would like the ability to read reviews of the music uploaded by different users.
    - I want to have the option to edit my reviews.
    - I would like the ability delete my reviews.


-   ### Site Owner Goals

    -  Create a music community sharing the most liked or even disliked albums so that the user and even owner can show relive nostalgic music or find new music.


## Design Choices 

-   ### Colour Scheme


## Typography

-  ### Fonts


##  Imagery


## Wireframes

-   ### Desktop view


## Features

###  Site Navigation

-  ### User site map

<img align="center" src="./static/images/site-map.png">  

-   ### Current Features

    - All dynamics of CRUD functionality have been implemented in this site for registered users who are logged in.


    | Function      | Location       | 
    | ------------- | -------------  | 
    | Create        | Upload albums  |
    |               | Upload Artist  |
    |               | Write Review   |
    |               | Rate Albums    |
    | Read          | Read Reviews   | 
    |               | All Reviews    |
    | Update        | Edit Review    |
    |               | Update Rating  | 
    | Delete        | Reviews& Ratings| 


    ###  Header  [see here](/static/images/navbar-header.png)

-   ### Navigation bar

    - Upon entering the website, users will be greeted with a clean and easy to read navigation bar indicating where to go(home/rankings/login/register)

    - If they go to the registration link it will allow the user to sign up for a new account and will direct them to their new profile.

    - Jinja if statements were used to ensure only certain navigation links are visible to registered users. Unregistered users will not have access to upload or rate.


### Mobile [see here](/static/images/mobile.jpg)

-   ### Navigation bar

    - For mobile and tablet view there is a hamburger icon which will collapses once clicked on to display the navbar menu.


###  Log In  [see here](/static/images/log-in-img.png)

-  ### User Log In 

    - Frequent users can log in to accsess additional links to leave reviews on all the latest books.

###  Register  [see here](/static/images/register.png)
 
-  ### Sign Up Page 

    -  New visitors are able to register their details by providing an email address, user name and password to create an account.


###  Profile  [see here](/static/images/welcome.png)  

-   ### User Profile  

    - Registered users have access to their profile page that presents a welcome message when logged in.

-   ### User Reviews

    - User reviews are saved to the profile page, including book names, and the dates they were made. Users have the option to edit and delete their reviews.

###  Review books  [see here](/static/images/review.png)

-  ### Add Reviews 

    - Users can add reviews by clicking on the book cover image or pressing the 'write a review' button below. Users are then taken to a page where they can fill out a form that will prompt them to enter a heading and written review. 

###  Read Reviews  [see here](/static/images/my-reviews.jpg)

-  ### Book Reviews 

    - Users can read all reviews made by registered users. 

### Edit Page  [see here](/static/images/edit-reviews.jpg)

-  ### Edit Reviews

   - Users are able to edit and update their reviews using the submit button located at the bottom of the review form.

### Log Out  [see here](/static/images/log-in.jpg)

-  ### Users Logged Out

    - When a user logs out of their account a flash message is displayed that reads "You have been logged out" to inform the user they have logged out.

### Account Settings  [see here](/static/images/account-settings.jpg)

-  ### User Account 

    - All users have the option to delete their own accounts where necessary.

### App banner  [see here](/static/images/app-download.png)

-  ### App Store 

    - At the bottom of every page users will find links to download the Book Hub app.

### Footer  [see here](/static/images/app-download.png)

-  ### Links 

    - The footer contains links to social media.

    - Copyright information can be found here.    


    ###  Features

-  ### Future Features

    - To add an online payment system that allows users to buy books directly from the website.

    - To give users the option to add star ratings.

    - To allow users to add friends to their profile.

## Database Layout

-  ### Collections

    | Title         | Field          | Data Type |
    | ------------- | -------------  | --------- |
    | albums        | _id            | ObjectId  |
    |               | album_name     | string    |
    |               | artist_id      | string    |
    |               | image_url      | string    |
    |               | created_by     | string    |
    

    | Title         | Field          | Data Type |
    | ------------- | -------------  | --------- |
    | artists       | _id            | ObjectId  |
    |               | artist_name    | string    |


    | Title         | Field          | Data Type |
    | ------------- | -------------  | --------- |
    | ratings       | _id            | ObjectId  |
    |               | album_id       | ObjectId  |
    |               | rating         | string    |
    |               | review         | string    |
    |               | created_by     | string    |


    | Title         | Field          | Data Type |
    | ------------- | -------------  | --------- |
    | users         | _id            | ObjectId  |
    |               | username       | string    |
    |               | email_address  | string    |
    |               | password       | string    |
   
    
## Technologies Used

### Languages Used

-   ### [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   Used as the main markup lanuage for the website content.
-   ### [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   Used to add styling to the website.
-   ### [Python3](https://en.wikipedia.org/wiki/Python)
    -   Used to run the site and speak to the mongodb database.
-   ### [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   Used to validate the materialize inputs.

### Database Used

-   ### [MongoDB Atlas](https://cloud.mongodb.com/)
    -   Used to store structured user and book review data.

### Frameworks & Libraries

-  ### [JQuery](https://jquery.com/)
    -  Used for the initialisation of Materialize CSS components
-  ### [Materialize:](https://getbootstrap.com/docs/5.0/getting-started/download/) 
    -  Used to design a mobile-first responsive website along with custom components
-  ### [Flask](https://en.wikipedia.org/wiki/Flask)
    -  Used as a lightweight WSGI web application framework
-  ### [PyMongo](https://docs.mongodb.com/drivers/pymongo/)
    -  A Python distribution containing tools for working with MongoD
-  ### [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    -  Flask-PyMongo bridges Flask and PyMono
-  ### [Werkzeug](https://de.wikipedia.org/wiki/Werkzeug)
    -  A comprehensive WSGI web application library
-  ### [itsDangerous](https://itsdangerous.palletsprojects.com/en/2.0.x/)
    -  Allows data to be sent and received safely using python and secret keys
-  ### [DNSPython](https://pypi.org/project/dnspython/)
    -  A DNS toolkit for Python
-  ### [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
    -  Jinja2 is a full-featured template engine for python    
-  ### [Click](https://click.palletsprojects.com/en/8.0.x/)
    -  A Python package for creating beautiful command line interfaces 


### Programs Used

-  ### [Heroku](https://id.heroku.com/)
    -  Used to deploy, manage, and scale modern apps
-  ### [Gitpod](https://www.gitpod.io/)
    -  An online IDE linked to the GitHub repository used to write my code.    
-  ### [Git](https://git-scm.com/)
    -  Git was used for version control by utilizing the Gitpod terminal to commit to Git and Puch to GitHub
-  ### [GitHub](https://github.com/)
    -  GitHub is used to store project codes after being pushed from the Gitpod    terminal
-  ### [JSHint](https://jshint.com/) 
    -  Used to detect errors in the JavaScript files 
-  ### [Google Fonts](https://fonts.google.com/)
    -  Google fonts were used to import 'Yeseva One' for the main website logo
-  ### [Font Awesome](https://fontawesome.com/) 
    -  Font Awesome were used on all social icons of the website.
-  ### [Affinity Designer](https://affinity.serif.com/en-gb/designer/)
    -  Affinity Designer was used to create the hero background image for the website
-  ### [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process

## Testing

-  ### All testing can be found [here](TESTING.md) 

## Deployment

### The project was developed using [Gitpod](https://www.gitpod.io/) and pushed to [GitHub](https://github.com/) then deployed on
Heroku using the following steps...    
 
1. Create requirements.txt file using command pip3 freeze --local > requirements.txt
2. Create a Procfile with the terminal command echo web: python app.py > Procfile and at this point checking the Procfile to make sure there is no stray line as this can cause issues when deploying to Heroku.
3. The new requirements file and Procfile committed to GitHub.
4. New app created in Heroku by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to location.
5. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
6. Search for GitHub repo and connect.
7. In the dashboard click "Settings" -> "Reveal Config Vars"
8. Set config vars:

- ## Table

    | Key           | Location        | 
    | ------------- | -------------   | 
    | PORT          | 5000            | 
    | IP            | 0.0.0.0         |
    | SECRET_KEY    | USER_SECRET_KEY |
    | MONGO_URI     | USER_MONGO_URI  | 
    | MONGO_DBNAME  | book_hub        |
 
  
## GitHub Pages

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
   Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
 5. Change the current working directory to the location where you want the cloned directory to be made.
 6. Type `git clone`, and then paste the URL you copied in Step 3.

```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

        7. Press Enter. Your local clone will be created.

```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `CI-Clone`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
```
---

## Credits

-   ### Code

    - The Code Institute material was the main source of information used to create this project.

    - Materialize CSS Library used throughout the project mainly to make site responsive using the Grid System [https://materializecss.com/](https://materializecss.com/)

-   ### Content

    -  All content was written by the developer.

    -  Psychological properties of colours text in the README.md was found - [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

    - w3schools was used as a general source of knowledge.

    - Materialize for creating a responsive website.

-   ### Media

    -  Hero Image was created by the developer using affinity designer to crop and edit photo on to background [Affinity Designer](https://affinity.serif.com/en-gb/designer/)

    - All Images on the site were sourced from [Amazon.co.uk](https://www.amazon.co.uk/)

  
-   ### Acknowledgements

    - Code Institute for their support and providing all of the necessary material.