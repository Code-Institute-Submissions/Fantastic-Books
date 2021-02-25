
<img src="https.github.com/aineon/fantastic-books/blob/master/README_images/site_mock_up.jpg?raw=true">
<img src="mock_up.png>

## [**Table of Contents**](#table-of-contents)

- [UX](#ux)
    - [Overview](#overview)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Design Process](#design-process)
        * [Colour Palette](#colour-palette)
        * [Background Images](#background-images)
        * [Typography](#typography)
        * [Development Process](#development-process)
        * [Wireframes](#wireframes)

- [Database Model](#database-model)

- [Features](#features)
    - [CRUD Functionality](#crud-functionality)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)

- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Frameworks](libraries-and-frameworks)
    - [Project Management](project-management)
    - [Tools](#tools)
    - [Resources](#resources)

- [Testing](#testing)

- [Bugs and Solutions](#bugs-and-solutions)
    - [Resolved Bugs](#resolved-bugs)
    - [Still Existing](#still-existing)

- [Deployment](#deployment)
    - [Locally](#locally)
    - [To Heroku](#to-heroku)

- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

[Disclaimer](#disclaimer)

---

## **UX** 
### **Overview**
A Book Review App that allows registered users to create, read, edit and delete their own content. 
Browse reviews left by other users. Save reviews made by other users. Access their own content and and reviews they've saved from their personalised profile.

### **Project Goals**
The aim of this project was to create a visually appealing, 
interactive Book Review App.  

- As an owner my goals were: 
    - to create a community of book lovers
    - to encourage users to create their own content
    - to encourage users to supply as much information in the review as possible
    - to encourage users to explore other users content
    - to help users find new books to read
    - to offer a link for users to buy books
    - to allow users to curate their own profile 

### **User Stories**
*"As a user, I want to immediately understand the purpose of the site"*
*"As a user, I want to create my own reviews."*
*"As a user, I want to be able to rate the book I am reviewing."* 
*"As a user, I want to easily access my own content."* 
*"As a user, I want to edit reviews I have created."*
*"As a user, I want to control my own content."*  
*"As a user, I want to be able to delete reviews I have created."*  
*"As a user, I want to be able to delete my account."*  
*"As a user, I want to be able to browse reviews created by other users."*
*"As a user, I want to be to save reviews created by other users that I like."*  
*"As a user, I want to be directed to a site where I can buy a book."* 
*"As a user, I want to be able to search for a book, author or genre."*
*"As a user, I want a site that is visually appealing."*  
*"As a user, I want a site that is easy to navigate."* 
*"As a user, I want a site that is intuitive."*  

### **Design Process**
- I wanted to design an app that envoked the feeling a reading a good book and escaping into the world that book creates.
- I wanted the app to be intuitive and easy to navigate  
- I kept the amount of elements on each page to a minimum as I wanted to achieve an uncluttered
and clean aesthetic.  
- I used [Materialize CSS](https://materializecss.com/) grid for the layout throughout the site.  
- I used various [Materialize CSS](https://materializecss.com/) classes to enhance and structure different elements.
- I wanted the app to be responsive on all commonly used devices.

#### Colour Palette
- I wanted the colour scheme to be elegant and complement the background images while still be easily readable.  
   
   PUT COLOUR PALETTE HERE

##### **Primary Colour Palette**
I chose #420420, #5a052c and #fafaed as my main colour scheme. I felt these colours worked well together and were in
keeping with the overall aesthetic of the app.

     PUT IMAGE HERE
- **#42042**
    - Site wide:
        - brand logo
        - nav links
        - sidenav trigger icon
        - sidenav links
        - footer background colour
        - all button backgrounds
    - Home Page: 
        - Welcome title, subtitle and text
    - Profile Page:  
        - tab buttons
        - search button
    - Mobile Search Page:
        - title text
    
- **#5a052c**
    - Site wide:
        - body text
        - sidenav title
        - form labels/inputs 

- **#fafaed**
    - Site wide:
        - nav background
        - sidenav background
        - footer text
        - page headings
        - button text
        - flash message background

GRADIENT HERE 
   
##### **Secondary Colour Palette**
I chose these colours as I felt they worked well with the primary colour scheme and highlighted
certain elements.

PUT IMAGE HERE

- **#952055**
    - hover colour for all buttons
    - dividers
    - links
    - active inputs/labels


#### **Backgrounds Gradient** 

#### **Background Images**
I chose book related imagery that I felt envoked the magic of reading your favourite book
and discovering new books. THe feeling you get when your're in a beautiful library or bookshop.

#### **Typography**
- I wanted a handwriting style font for the brand logo, titles and headings.
- I chose [Tangerine](https://fonts.google.com/specimen/Tangerine?query=tanger&preview.text_type=custom) as I felt
it had an elegant feel, was inkeeping with the overall aesthetic while still maintaining readability.
- For the body text I chose [Roboto](https://fonts.google.com/specimen/Roboto?query=robo&preview.text_type=custom) as it complemented the [Tangerine](https://fonts.google.com/specimen/Tangerine?query=tanger&preview.text_type=custom)
font, had good readability and was listed as a popular pairing for [Tangerine](https://fonts.google.com/specimen/Tangerine?query=tanger&preview.text_type=custom).

 #### **Development Process**
 Once I decided to build a book review app, I broke the development process down into stages to help me manage the project.
 - Research existing book review sites 
 - Choose background images
 - Decide on general colour scheme
 - Decide on what and how many links I was going to have and the content of each of those links
 - Create the base.html with common elements, links and scripts
 - Design the basic layout of each page, decide on which background image would be used for each page and write the basic functionality to render each page.
 - Develop login/logout/register functionality
 - Develop CRUD logic and functionality
 - Layout and style for CRUD functionality - Reviews/forms
 - Add logic and functionality for additional features.
 - Adjust layout and styling

 #### **Wireframes**
- I used [Balsamiq](https://balsamiq.com/wireframes/) to create the wireframes for my project.
- I create 3 sets of wireframes for Desktop, Tablet and Mobile.
- To view the wireframes please click the links below:

**Desktop**  
  

**Tablet**  
 

 **Mobile**

## **Database Model**
 DB SCHEMA HERE

##### [Back to Table of Contents](#table-of-contents)
---

## **Features**
### **CRUD Functionality**

#### **Users Can:**
- Add their own reviews
- Edit their own reviews
- Delete their own reviews
- Read all reviews 
- Delete their own account

#### **Admin Can:**
- Add their own reviews
- Edit their own reviews
- Delete their own reviews
- Read all reviews
- Delete their own account
- Delete reviews created by any user
- Delete any user account

### **Existing Features** 
#### **Site wide**
 - **_Navbar/Sidenav_** - to allow easy navigation across the app, identifies app name
 - **_Footer_** - contains copyright information 
 #### **Index.html**
 - **_Welcome Title_** - identifies the name and type of app
 - **_Welcome Text_** - information about the app
 - **_Log In_** button/link - directs user to login page  
 - **_Sign Up_** button/link - directs user to sign up page  
 #### **Profile.html**  - A personalised page for each user
 - **_Search bar_** - allows users to search for a book/review by title, author or genre and renders results on reviews.html  
 - **_My Favourites Tab_** - displays any reviews a user has added to their favourites
 - **_Remove Review_** Icon - allows users to remove a review from their favourites tab and from the favourites field in the users collection in the database
 - **_Buy_** Button - Redirects user to a site where the book can be purchased
 - **_Find Books_** button - directs user to the reviews page
 - **_My Reviews Tab_** - displays reviews created by that user
 - **_Delete_** Button - triggers a modal asking user to confirm they want to delete that review 
 - **_Modal Delete_** Button - deletes the review, removing it from the database - flash message confirms delete
 - **_Modal Cancel_** Button - closes the modal with no action being taken
 - **_Edit_** Button - redirects user to 'Edit Review' form
 - **_Add Review Tab_** - a form that allows users to create a review
 - **_Add Review_** Button - adds review to the reviews collection in the database. renders it on the 'My Reviews' tab and on Reviews.html - 
 flash message confirms review has been added, redirects user to reviews.html
 - **_Delete Account Tab_** - contains delete account button
 - **_Delete Account_** Button - triggers modal asking user to confirm they want to delete their account. 
 - **_Modal Delete_** Button 
 - Deletes users account from the database
 - Flash message confirms delete
 - Redirects to index.html
#### **Reviews.html** - Displays all reviews created by all users
 - **_Search bar_** - allows users to search for a book/review by title, author or genre and renders results 
 - **_Save Review_** 
 - Not visible to review creator 
 - Allows other users to save that review to 'My Favourites' tab on thier profile 
 - Confirmed by flash message that review has been 'added to favourites' 
 - If review is already saved, flash message informs user.
 - **_Buy_** Button - Redirects user to a site where the book can be purchased  
 - **_Scroll Up_** Button - returns user to the top of the page
#### **Add Review.html** - Allows users to add reviews without navigating to profile page 
 - Contains form to add review
 - **_Add Review_** Button 
 - Adds review to the database 
 - Confirmed by flash message
 - Redirects user to reviews.html
#### **Edit Review.html**
 - Only accessible through Edit button on users own reviews. 
 - Allows users to edit the selected review. 
 - Updates the review in the database
#### **Register.html**
 - Allows users to sign up to the site by supplying required information Adds user information to the users collection in the database
 - **_Link to login.html_** - redirects user to login.html 
#### **Login.html** 
 - Users must sign in with username and password to access the site
 - **_Link to Register.html_** - redirects user to register.html 
#### **Log Out** Nav Link 
 - Logs user out of their account 
 - Confirms logout with flash message 
 - Redirects to login page 

### **Future Features**
- Implement Google Books API access so users can automatically populate book info fields
- Add logic so users can comment on other users reviews
- Add logic so users can upvote or downvote other users reviews

##### [Back to Table of Contents](#table-of-contents)
---

## **Technologies Used**
### **Languages**
- **HTML** - used to create the structure of the application
- **CSS** - used to position and style the application 
- **JavaScript** - used to for interactivity
- **Python** - used to handle backend
- **Jinja** - Python templating language

### **Libraries and Frameworks**
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
- [Materialize CSS](https://materializecss.com/) 
- [Google Fonts](https://fonts.google.com/) 
- [Font Awesome](https://fontawesome.com/) 
- [jQuery](https://code.jquery.com/) 
- [hover.css](https://ianlunn.github.io/Hover/) 

### **Project Management**
- [Git](https://git-scm.com/) 
- [Gitpod](https://gitpod.io/) 
- [Github](https://github.com/) 
- [Heroku](https://signup.heroku.com)
- [MongoDB](https://www.mongodb.com/)

### **Tools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) 
- [Balsamiq](https://balsamiq.com/wireframes/)
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)
- [Favicon](https://favicon.io/favicon-converter/) 
- [Autoprefixer](https://autoprefixer.github.io/) 
- [Compress PNG](https://compresspng.com/)
- [jpg2png](https://jpg2png.com/)


### **Resources**
- [cdnjs](https://cdnjs.com/)
- [w3schools](https://www.w3schools.com/) 
- [Stack Overflow](https://stackoverflow.com/)
- Task Manager Mini Project - [Code Institute](https://codeinstitute.net/) Data Centric Dev Module


##### [Back to Table of Contents](#table-of-contents)
---

## **Testing**
Full testing documentation can be found [here](Fantastic_Books/TESTING.md).

##### [Back to Table of Contents](#table-of-contents)
  ---

## **Deployment**
This project was developed using Gitpod IDE. The live version of this site is hosted using [Heroku](https://signup.heroku.com/)
To deploy this project follow the below steps.

### **Requirements to run this app**
- **Python3** 
- **PIP** package installation
- **MongoDB**
    - All content created by users of the site is stored in a **MongoDB** database
    - The following collections should be created:
        - **Users**
        - **Reviews**
- A document in the **users** collection should contain the following fields:

| **Key**       | **Value**     | **Type**
|-------------  | :----------:  | -------:
| firstname     |  unassigned   | String
| lastname      |               | String
| username      |               | String  
| email         |               | String
| password      |               | String
| favourites    |               | Array
| date_created  |               | String

- A document in the **reviews** collection should contain the following fields:

| **Key**       | **Value**     | **Type**
|-------------- |:------------: |--------:
title           |               |     String
author          |               |     String
genre           |               |     String
published       |               |     String
cover           |               |     String
buy             |               |     String
synopsis        |               |     String
review          |               |     String
created_by      |               |     String
rating          |               |     String
date_created    |               |     String


### **Locally**
To run this project locally, follow the below steps:
To clone this project from Github:
- Click the [Fantastic Books Repository Link](https://github.com/aineon/Fantastic-Books)
- From the repository click the **Code** button
- In the **_Clone with HTTPs_** section, copy the clone URL for the repository
- In your local IDE open **_Git Bash_**
- Change the current working directory to the location where you want the cloned directory to be made
- Type `git clone` and then paste the URL you copied from the repository
```console
git clone https://github.com/aineon/Fantastic-Books.git
```
- Press Enter. Your local clone will be created
- To remove the origin link from your IDE type `git remote rm origin`

- Alternatively you can download the **ZIP folder** of this project by clicking the **Code** button *(as you did in step 2)*
and selecting **_Download ZIP_**
- It can then be unpacked into your desired location
- Open the **index.html** file to run the project locally

- Create a file called **env.py**. **_All your app's environmental variables should be stored here_**
- The **env.py** file should contain the following information:
````import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<app secret key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>.1jegb.mongodb.net/<database_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database_name>")
````
- Check that the **env.py** file is listed in the **.gitignore** file
- if it is not add it to the **.gitignore** file
    - This prevents your environmental variables being publicly accessed.

- The app can now be run locally:
    - in the terminal type:
    ````
    python3 app.py
    ````

### **To Heroku**
To deploy the app using [Heroku](https://signup.heroku.com/) from its [GitHub Repository](https://github.com/aineon/Fantastic-Books),
follow the steps below:
- From the IDE terminal create the following files:
    - requirements.txt 
    - Procfile
- Use the below commands to create the files:
````
pip3 freeze --local > requirements.txt
echo web: python3 app.py > Procfile
````
- Push these files to Github
- Sign up/login to [Heroku](https://signup.heroku.com/)
- Click the **New** dropdown menu
- Select **Create new app**
- Enter a unique name for the App
- Choose your region
- Click **create app** button
- The **Deploy** tab will open
- Select Github as the **Deployment Method**
- Enter your Github details and the repository name
- Click **search**
- When the correct repository has been found, click connect
- Go to the **Settings** tab
- Under **Config Vars** select **Reveal Config Vars**
- Enter the following **key/value** pairs. **_Ensure they match the key/value pairs contained in your env.py file_**

|**Key**        |**Value**
|-----------    |-----------  
| IP            | `0.0.0.0`
| PORT          | `5000`
| SECRET_KEY    | `<app secxret key>`
| MONGO_URI     | `"mongodb+srv://<username>:<password>@my<cluster_name>.1jegb.mongodb.net/<database_name>?retryWrites=true&w=majority")`
| MONGO_DBNAME  | `<database name>`          


- Go back to the **Deploy** tab
- Under **Automatic Deploys** select **Enable Automatic Deploys**
- Under **Manual Deploys** select **master** 
- Click **Deploy Branch**
- When the app has finished building, click **Open app** button on the top right of the page.