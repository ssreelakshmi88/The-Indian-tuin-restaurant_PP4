# Indian Tuin restaurant

The webpage of “Indian Tuin” restaurant was developed to introduce customers to the rich and exquisite Indian cuisines. 
The project was developed based on the principles of UX design and the agile development methodology. The webpage has been created using HTML, CSS, Javascript, Python and Django framework.


![responsive page view](https://user-images.githubusercontent.com/97182442/198889121-4c2ab0c2-41e3-47a0-bdd1-b36a267202ed.jpg)


## **Table of content** 

  - [UX Design](#ux-design)
    - [User stories](#user-stories)
    - Admin features (#admin-features)
    - Structure(#structure)
  - Design (design)
  - [Features](#features)
    - [Implemented features](#implemented-features)
    - [Features left to implement](#features-left-to-implement)
  - [Technologies Used](#technology-used)
    - [Languages](#languages)
    - [Database](#database)
    - [Libraries, frameworks and other technologies](#libraries-frameworks-and-other-technologies)
  - [Code structure](#code-structure)
  - [Data validation](#data-validation)
  - [Testing](#testing)
    - Testing User stories (#testing-user-stories)
    - Further testing (#further-testing)  
  - [Deployment](#deployment)
    - Forking the github repository (#forking-the-github-repository)
   - [Credits](#credits)
     - [Code](#code)
     - [Content](#content)
     - [Media](#media)
     - [Acknowledgments](#acknowledgments)


## UX (User Experience)

#### User stories

- **First Time Visitor Goals**


  i.	As a first time visitor, I want to understand how to navigate and find information.
  
  
  ii.	I want to have easy access to the menu including prices.
 
  iii.	To access customer testimonials in dedicated section. In addition, I want to have access to social media page of the restaurant.
 
  iv.	Important information such as directions and opening timing of the restaurant should be easy to access at a click of a button.
 
  v.	Finally, I want to make reservations and contact the restaurant, if necessary.
 
- **Returning Visitor Goals**


   i.	As a returning visitor, I want share my experience through dedicated blog within the site. Furthermore, I should be able to comment on customer testimonials.
   
   
   ii.	I want to convey my concerns and/or suggestions to the management.
   
   iii.	As a returning visitor, I want to subscribe to restaurant’s newsletter for updates and interesting events.
   
- **Frequent Visitor Goals**


   i.	As a frequent visitor, I want to check if there any new blog posts.
 
   ii.	As a frequent user, I can also send messages to the admin asking for new menu.
   
   iii.	As a frequent user, I can like the posts so that the author can know that I enjoyed the content.
   
   iv.	As a frequent user, I can like the posts so that the author can know that I enjoyed the content.
   
   v.	As a frequent user, I can like the posts so that the author can know that I enjoyed the content.


## Design

#### Colour Scheme

   The main colors used for the web page designing are red, white and black.
 
 
####  Typography

   The Montserrat font is the main font used for the whole website with Sans Serif as the fallback font. Montserrat makes the webpage attractive and clean.
   
#### Images

   The images were taken from pexels.com
   
   
## Wireframes

 This can be used as a layout of the various pages. The wireframe images can be found at [wireframes](./wireframes.md).
 
## Features
  Responsive on all device sizes.
  
  
## Technologies Used

###    Languages Used

   - Python, HTML, CSS, JavaScript


###    Database

   - PostgreSQL
 
 
 ###    Libraries frameworks and other technologies
 
1.	**Bootstrap 4.4.1**: This is used for responsiveness and styling of the website.
2.	**Google fonts**: Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
3.	**JQuery:** jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
4.	**Git:** Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5.	**GitHub:** GitHub is used to store the projects code after being pushed from Git.
6.	**Balsamiq**: Balsamiq is used to create wireframes


## Testing


The W3C Markup Validator, W3C CSS Validator Services, Jshint and PEP8, Pylint validator were used to validate every page of the project to ensure there were no syntax errors in the project.


## Deployment
Deploying the project using Heroku:
i.	Login to Heroku and Create a New App

ii.	Give the App a name, it must be unique, and select a region closest to you

iii.	Click on 'Create App', this will take you to a page where you can deploy your project.

iv.	Click on the 'Resources' tab and search for 'Heroku Postgres' as this is the add-on you will use for the deployed database.

v.	Click on the 'Settings' tab at the top of the page. The following step must be completed before deployment.

vi.	Scroll down to 'Config Vars' and click 'Reveal Config Vars'. Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py as a root level file. The env.py files is where the projects secret environment variables are stored. This file is then added to a .gitignore file so it isn't stored publicly within the projects repository.

vii.	Next, the secret key needs to be created within the projects env.py file on GitPod and then added to the Config Vars on Heroku. Once added, go to the settings.py file on GitPod.

viii.	Within the settings.py file you need to import the libraries:


        import os
        import dj_database_url
        from django.contrib.messages import constants as messages
        if os.path.isfile('env.py'):
        import env

i.	Then onnect the project to whitenoise, which is where the static files will be stored. You can find a full explanation of how to install whitenoise here
ii.	Then on Heroku add to the Config Vars, DISABLE_COLLECTSTATIC = 1, as a temporary measure to enable deployment without any static files, this will be removed when it is time to deploy the full project.
iii.	Next we need to tell Django where to store the media and static files. Towards the bottom of settings.py file we can add:



          STATIC_URL = '/static/'
          STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
          STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
          MEDIA_URL = '/media/'
          

i.	At the top of settings.py, under BASE_DIR (the base directory), add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS': [].

ii.	Now we have to add our Heroku Host Name into allowed hosts in settings.py file:

       ALLOWED_HOSTS = ['YOUR-APP-NAME-HERE', 'localhost']

i.	Finally, to complete the first deployment set up of the skeleton app, create a Procfile so that Heroku knows how to run the project. Within this file add the following: web: gunicorn APP-NAME.wsgi Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.

ii.	Now, go to the 'Deploy' Tab on Heroku. Find the 'Deployment Method' section and choose GitHub. Connect to your GitHub account and find the repo you want to deploy.

iii.	Scroll down to the Automatic and Manual Deploys sections. Click 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed the code.

iv.	Once the project is finished deploying, click 'Open App' to see the newly deployed project.

v.	Before deploying the final draft of your project you must:

vi. Remove staticcollect=1 from congifvars within Heroku

vii. Ensure DEBUG is set to false in settings.py file.


## Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...
1.	Log in to GitHub and locate the GitHub Repository
2.	At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3.	You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1.	Log in to GitHub and locate the GitHub Repository
2.	Under the repository name, click "Clone or download".
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4.	Open Git Bash
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied in Step 3.
https://github.com/ssreelakshmi88/The-Indian-tuin-restaurant_PP4.git

7.	Press Enter. Your local clone will be created.



