# Indian Tuin restaurant

The webpage of “Indian Tuin” restaurant introduce our clients to the rich and exquisite Indian cuisines and delicacies. The project encompasses the principles of UX design and agile development methodology and designed using HTML, CSS, Javascript, Python and Django framework.

[View live project here](https://indian-tuin.herokuapp.com/)



![responsive page view](https://user-images.githubusercontent.com/97182442/198889121-4c2ab0c2-41e3-47a0-bdd1-b36a267202ed.jpg)



## **Table of Contents** 

  - [UX Design](#ux-design)
    - [User stories](#user-stories)
  - [Design](#design)
  - [Features](#features)
    - [Implemented features](#implemented-features)
    - [Features left to implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Database](#database)
    - [Libraries, frameworks and other technologies](#libraries-frameworks-and-other-technologies)
  - [Testing](#testing)
    - [Testing User stories](#testing-user-stories)
    - [Further testing](#further-testing)  
  - [Deployment](#deployment)
    - [Forking the github repository](#forking-the-github-repository)
   - [Credits](#credits)
     - [Code](#code)
     - [Content](#content)
     - [Media](#media)
     - [Acknowledgements](#acknowledgements)


## UX Design

### User stories

- **First Time Visitor Goals**

    i. I want to navigate and find information about the restaurant.

    ii. I want to have easy access to the menu including prices.

    iii. I want to have access to social media page of the restaurant including user reviews.

    iv. Details such as directions and opening timing of the restaurant should be easy to access at a click of a button.

     v. Finally, I want to make reservations and contact the restaurant, if necessary.

    vi. I can register and create a profile.


- **Returning Visitor Goals**

   i. Update my profile and cancel my account.
  
   ii. I would like to make changes to a reservation.
  
   iii. I would like to be greeted with interesting blogs
  
   iv. I want to give feedback and contact the restaurant with suggestions.
   
- **Frequent Visitor Goals**
    
    i. As a frequent visitor, I want to check if there any new blog posts.

   ii. I can also ask questions and send messages or feedback to the admin.
   
   iii.I can like/dislike posts so that the author can know that I agree/disagree with the content.
   
   iv. I want to visit social media for updates and interesting events, like food festivals.
   
### Admin Features

1. As a Site Admin I can create draft posts so that I can finish writing the content later
2. As a Site Admin I can make, edit and remove comments so that I can manage the interactions of the blog community.
3. As a Site Admin I can view accounts of members so that I can know how many users are registered.
4. As a Site Admin I can view the number of reservations so that I can know how many customers are expected.
5. As a Site Admin I can approve comments so that I can filter out any unwanted comments.
6. As a Site Admin I can create, edit, view and delete posts so that I can manage my blog content.
7. As a Site User/Admin I can view the number of likes so that I can know which topics are in vogue.
8. As a Site Admin I can create, edit, view and delete items in the menu so that I can always manage the menu contents.

9. As a Site Admin I can display key information so that users can know the location and opening timings of the restaurant.

### Structure

#### Entity Relationship Diagram
In this diagram, the Users entity stores information about website users, including their names, email addresses and passwords. The Menu Items entity stores information about the menu items available at the restaurant, including their names, descriptions, and prices.

The Reservation entity stores information about reservations made by users, including the reservation date, time, and number of guests. The Contact entity stores information about users who submit messages through the website contact form.

In this diagram, there is a one-to-many relationship between the Users entity and both the Reservation and Blog Post entities, indicating that a user can make multiple reservations and read multiple blog posts. There is also a one-to-many relationship between the Blog Post entity and the Blog Comment entity, indicating that a single blog post can have multiple comments.

The relationship between the User entity and the Contact entity in the ERD diagram for a restaurant website can be described as a one-to-many relationship because:
- One user can submit many messages through the website's contact form.

- Each message submitted through the contact form is associated with one user.


![ERD DIAGRAM_NEW](https://user-images.githubusercontent.com/97182442/223586223-33ebf8f3-dec8-4645-bd26-76ff38d3adfa.jpg)


## Design

#### Colour Scheme

The main colors used for the web page designing are red, white and black.


#### Typography

The Montserrat font is the main font used for the whole website with Sans Serif as the fallback font. Montserrat makes the webpage attractive and clean.

#### Imagery

The images were taken from pexels.com

#### Wireframes

This can be used as a layout of the various pages. The wireframe images can be found at [wireframes](./wireframes.md).


## Features

This website is made for educational purposes and hence there is scope for improvement and further features need to be added.

Following features have been implemented.

### Implemented features

- **User registration**

  New visitors can register to create a personal account. Users will be intimidated upon successful registration. Certain privileges will be open to registered users such as;
  
  ![Screen shot-sign in message](https://user-images.githubusercontent.com/97182442/198905753-fc633748-0a68-47ea-9ad0-bb6b398861f8.jpg)
  
  
  ![screenshot_logged out](https://user-images.githubusercontent.com/97182442/198905771-76690247-b3fc-4ef3-a4ea-d84c38d9acfe.jpg)



     i. Registered users can cancel and/or make changes to an existing reservation. 
	 
	 ii. They can post/edit their comments. 
	 
	 iii. They can create personalized profile.
	 
	 iv. They will be able to comment on other user experience/reviews.


![user registration](https://user-images.githubusercontent.com/97182442/198904448-267a0e9d-9897-4efb-a0b6-2932e6790563.jpg)


![User profile page](https://user-images.githubusercontent.com/97182442/198904470-818ea9b2-dede-4698-a185-357a2563b948.jpg)


- **Admin profile**

  An admin profile has been built for staff members or admin. The admin profile has the following rights:
  
  i. Modify menu page.
  
  ii. Approve user comments.
  
  iii. Can modify blogs from frontend.
  
  
  ![admin profile](https://user-images.githubusercontent.com/97182442/198904513-1b494081-c632-4902-a223-b263b9389681.jpg)

  
- **Menu**

    i. There are 6 cuisines listed per menu page with a brief description. Cost of each item is displayed.

    ii.Only the admin or staff members can modify menu items.
    
    
    ![menu page_6 per page](https://user-images.githubusercontent.com/97182442/198904562-f0d1d86c-c651-4c58-9d46-8829f4061d3a.jpg)
    
    


- **Blog posts**

   i. A blog section highlighting interesting recipes has been created to enrich user experience. Only staff members or admin have the permission to edit and delete the blog posts.
   
   ![blog recipe with edit and delete](https://user-images.githubusercontent.com/97182442/198904701-f8f38d14-66fa-4d90-a603-1cb4a64a3722.jpg)
   
   ii. All users can view blog posts and comments made by registered users.
   
   iii. Only registered users can make/edit comment, like or dislike posts.
   
   iv. User comments have to approved by the admin before being displayed.
   
   
   
   ![recipe blog](https://user-images.githubusercontent.com/97182442/198904601-028f4d12-a256-4cff-a986-65b03f497542.jpg)
   
   

![blog recipe with edit and delete](https://user-images.githubusercontent.com/97182442/198904701-f8f38d14-66fa-4d90-a603-1cb4a64a3722.jpg)



![comment_blog post](https://user-images.githubusercontent.com/97182442/198904740-b28d6172-dc95-46e2-8e9c-31a98a9b63dd.jpg)


- **Reservation**

    Reservations can be made by users without registration. However, only registered users can update and/or cancel reservations. User will be notified in case of multiple reservation for a slot.
    
    
![reservation page](https://user-images.githubusercontent.com/97182442/224512102-9c3ada77-20d8-4b22-864b-f5b42504df3e.jpg)


Unregistered users receive a separate success page indicating about their booking. Those users have to contact the restaurant in order to cancel
or update their booking.

![Booking_success page](https://user-images.githubusercontent.com/97182442/224512109-8bc861a6-979b-4872-8960-1bc2906b9b91.jpg)



- **Contact page**

     Contact page is designed to enable users to connect to the admin. Visitors can ask questions or can give feedback to the admin through the contact page.


![contact page_screenshot](https://user-images.githubusercontent.com/97182442/224512124-bc1f3b5d-8756-4079-994e-73758d58a576.jpg)


- **The Footer**

     The footer section includes links to the relevant social media sites for the restaurant. The links will open a new tab to allow easy navigation for the user. The footer is valuable platform both for the establishment and the user as it enables a healthy discussion in the social circle.



![footer](https://user-images.githubusercontent.com/97182442/198904973-306ad650-5fbf-4195-ba42-bac7eeef666f.jpg)


### Features left to implement

- **Search field**

    A search field in blog post page and menu page to search for recipes and menu items.


- **Tag Cloud/Tags**

    Each blog post and menu will be having fields related to dish types and categories.


- **Expanding the menu page**

    Menu page consisting of sub navigation links for categories: Starters, Main and Dessert, Drinks.
    

- **Separate dashboard for admin or staff members**

     Separate page for admin where they can access everything like
reservations, details of users.


- **Reservation email confirmation**

     When users create booking, they will get a confirmation email.
     

- **Creation of blog posts from front end**

     Admin and staff can create blog posts from front end.


## Technologies Used

### Languages

   •	Python, HTML, CSS, JavaScript
   
### Database

•	PostgreSQL

### Libraries frameworks and other technologies

1. **Bootstrap**: This is used for responsiveness and styling of the website.

2.	**Google fonts**: Google fonts were used to import the 'Titillium Web'font into the style.css file which is used on all pages throughout the project.

3.	**JQuery**: jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.

4.	**Git**: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

5.	**GitHub**: GitHub is used to store the projects code after being pushed from Git.

6.	**Balsamiq**: Balsamiq is used to create wireframes

7.	**Fontawesome**: Icons were taken from font awesome icons

8.	**Smartdraw**: Entity relationship was created using Smartdraw.

9.	**Cloudinary**: This is used for storing photos.

10. **Crispy Forms**: To create forms for reservation, contact page and editing pages.

11. **Summernote**: This is a JavaScript library that helps you create WYSIWYG editors online.

12.	**Django-allauth**: This is an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication.

13.   **Favicon Generator**: This is used for favicon generation.


**Agile methodology**

Agile methodology has been used to plan and design this website/project. User stories were documented and implemented and mapped them to the project within Agile tool.

![agile_progress_screenshot](https://user-images.githubusercontent.com/97182442/198904988-08748ac5-adb3-405e-bba7-79a7f82124f0.jpg)



![agile_completed](https://user-images.githubusercontent.com/97182442/198905022-d2f75375-f18d-41b8-921c-56c120cc5d85.jpg)



## Testing

### Testing User stories 

**First time visitor goals**

  - I want to navigate and find information about the restaurant, menu, social media links and user reviews.
  
       i. The webpage offers a clean and well defined layout for easy access to information via an intuitive navigation bar.
  
       ii. Users can easily access the menu items and the corresponding prices.
       
       
       ![Screenshot navigation bar](https://user-images.githubusercontent.com/97182442/198905069-a749a30e-73ba-41f8-b9d7-171f5dc14001.jpg)

  
      iii. In the menu page, users can see of list of menu items with photos and prices.
      
      
    ![menu page_screenshot](https://user-images.githubusercontent.com/97182442/198905084-2589ff85-5995-4f0b-8f27-2de191a3241d.jpg)
      
      
![menu page_6 per page](https://user-images.githubusercontent.com/97182442/198905550-48d5ab10-a649-492f-99bc-e8f66cbad1ba.jpg)

	  
- Details such as directions and opening timing of the restaurant should be easy to access at a click of a button.

    i. The contact page gives information about the location of the restaurant.
    
    
    ![Screenshot address and location](https://user-images.githubusercontent.com/97182442/198905093-e02e5ca6-9a1c-494e-9715-a60b5cbdd1be.jpg)

    

    ii. In reservation page, users can find the opening times of the restaurant. 
    
    ![Opening-time image](https://user-images.githubusercontent.com/97182442/224512565-4bf6258b-0e12-43c4-88c1-7cd8ac954276.jpg)

   

- Finally, I want to make reservations and contact the restaurant, if necessary.

    i. The reservation page allows a new user to make booking.
    
    
![reservation page](https://user-images.githubusercontent.com/97182442/224512686-21b187b5-dc75-418a-abc1-6bb829783027.jpg)


    ii. User can contact the admin via the contact page.
    
    
   
![contact page_screenshot](https://user-images.githubusercontent.com/97182442/224512702-3645e38a-eca2-4ddc-bf73-91ac550b833c.jpg)

 
- I can register and create a profile.

     i. User can create personalized profile via the “Register” button.

![user registration](https://user-images.githubusercontent.com/97182442/198905171-5231f5b2-bd9e-47ed-bae4-cbb720cdf1bd.jpg)


     ii. Registered users can make modifications and delete their profile.
     
     
 ![edit and delete in user profile](https://user-images.githubusercontent.com/97182442/224512718-3cef89b9-496f-43c2-991f-cee9469660b5.jpg)
 



**Returning visitor goals**

- I would like to make changes to a reservation.

   i. A registered user can login to make changes to an existing reservation.
   
   
   
   ![user reservation screenshot](https://user-images.githubusercontent.com/97182442/198905265-e5380661-3586-4b24-b137-7f4a40cb5707.jpg)

   
   ii. Through personal profile, users can view the number of bookings they have made.
   
   
   
   ![Number of reservations](https://user-images.githubusercontent.com/97182442/224512754-9a6c216b-0519-4162-91e2-d8a4541a4d66.jpg)



   ![user  with number of reservations](https://user-images.githubusercontent.com/97182442/224512760-8e82417e-4dbd-40a4-94ab-935518bb1d57.jpg)


- I would like to be greeted with interesting blogs.


![Blog page_screenshot](https://user-images.githubusercontent.com/97182442/198905300-e0859e5d-a305-4c93-a59e-97c3f150adc7.jpg)


 i. Blog pages allow users to scroll through interesting recipes. Each page contains two recipes per page and users can easily pass through pages through pagination links provided below the page.
 
 
 ![blog posts with 2 recipes](https://user-images.githubusercontent.com/97182442/198905404-acfdceaa-af0c-45a8-b10e-655ea99e1f5e.jpg)
 
 
 ![blog posts with pagination](https://user-images.githubusercontent.com/97182442/198905410-4b48f794-3a7a-476b-bb5d-e5c8c4b1660e.jpg)


 ii. Registered users can make comments and like/dislike posts which is displayed beneath each recipe.
 
 
 ![Screenshot blog posts](https://user-images.githubusercontent.com/97182442/198905496-6842ae28-f64e-4820-81b2-4d174967d4b5.jpg)

 
 iii. Comments will be displayed after approval by admin.
 
 
 ![comment_blog post](https://user-images.githubusercontent.com/97182442/198905508-075db082-aca4-42eb-8439-20ae67151bb8.jpg)
 
 
 

 ![Comments section](https://user-images.githubusercontent.com/97182442/198905506-9ba40633-0a98-43a6-aec9-c6200d538372.jpg)

 
 
 iv. Registered users can update and delete their comments according to their wish.
 
 
 ![Delete comment page](https://user-images.githubusercontent.com/97182442/198905525-c193091b-d66c-4575-a318-f6a9e0febc53.jpg)

 
- I want to give feedback and contact the restaurant with suggestions.
 
     i. In the contact page, users can give feedbacks and suggestions.
     
     
     ![contact page_screenshot](https://user-images.githubusercontent.com/97182442/224512790-36509915-b5e3-48a8-813f-30e4121f274b.jpg)

   

**Frequent Visitor Goals**

- As a frequent visitor, I want to check if there any new blog posts.

   i. A returning visitor should be able to easily navigate the blog posts through dedicated link.
   
   ii. Registered user can comment and/or like/dislike other user posts.
   
   
- I can also ask questions and send messages or feedback to the admin.

   i. Contact page enables user to send feedback to the admin.


- I can like/dislike posts so that the author can know that I agree/disagree with the content.

     i. Only registered users can comment or like/dislike posts made by other users.


- I want to visit social media for updates and interesting events, like food festivals.

   i. Links to social media page of the restaurant can be accessed at the footer of the page.

### Further testing

The W3C Markup Validator, W3C CSS Validator Services, Pylint validator and Unittests were used to validate every page of the project to ensure there were no syntax errors in the project.

The results of these tests are found here:

**Python test results:** [python test results](./tests_python.md).

**HTML and CSS test results:** [html and css test results](./tests_html&css.md).


#### Other tests

1. The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, Safari browsers.

2. The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 11 and iPhone 12 .

3. Sufficient testing has been done to ensure that all pages were linking correctly.

4. Friends were asked to review the site and documentation to point out any bugs and/or user experience issues.


#### Known Bugs

The contact page is not responsive in all devices.

The website is not responsive in all devices. In some devices, the submit buttons were pushed to different sides. Also, the position of logo changes in some devices.


## Deployment

Deploying the project using Heroku: 
1.  Login to Heroku and Create a New App

![heroku-login](https://user-images.githubusercontent.com/97182442/224512832-7008acd5-5039-4951-822b-db99ee78f503.jpg)

2.  Give the App a name, it must be unique, and select a region

2.  Give the App a name, it must be unique, and select a region.
3. Click on 'Create App', this will take you to a page where you can deploy your project.
4. Click on the 'Resources' tab and search for 'Heroku Postgres' as this is the add-on you will use for the deployed database.
5. Click on the 'Settings' tab at the top of the page. The following step must be completed before deployment.


![Settings tab](https://user-images.githubusercontent.com/97182442/224512940-6689b0b1-ca2c-4cb9-9102-7e1cd7093971.jpg)

6. Scroll down to 'Config Vars' and click 'Reveal Config Vars'. Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py as a root level file. The env.py files is where the projects secret environment variables are stored. This file is then added to a .gitignore file so it isn't stored publicly within the projects repository.


![Reveal config vars](https://user-images.githubusercontent.com/97182442/224512948-1a31d9f6-744b-41b7-a854-606e5a16206d.jpg)


![env py](https://user-images.githubusercontent.com/97182442/224512987-f4fbd022-2fbe-47d3-9065-57995e9f2ab3.jpg)

7. Below your Config Vars in your app settings, click **Add build pack**.

![Select build pack](https://user-images.githubusercontent.com/97182442/224512993-c9bc3a60-9b7b-4a81-90ad-fc7f1167e3b1.jpg)

8. Select **Python** from the list of build packs. Click **Save Changes**

9. Select **Deploy** from the tabs at the top of the app page.

![Select deploy](https://user-images.githubusercontent.com/97182442/224513010-a37e69d2-30ab-4d60-a661-6ce9339ec044.jpg)

10. Select **Connect to GitHub** from the deployment methods.

![Select repository](https://user-images.githubusercontent.com/97182442/224513019-d246e32b-7cdd-4d95-865a-24d9243708be.jpg)

11. Search for the repository to connect to by name. 

12. Click **Connect**. Your app should now be connected to your GitHub account.

13. Select Enable Automatic Deploys for automatic deployments.

- If you would like to deploy manually, select Deploy Branch. If you manually deploy, you will need to re-deploy each time the repository is updated.


![Manual deploy](https://user-images.githubusercontent.com/97182442/224513024-99948287-bc57-4183-84c0-0f996ac6bc61.jpg)


![Automatic deploy](https://user-images.githubusercontent.com/97182442/224513031-47c5303f-710d-45d4-b321-7ffdda2f7494.jpg)

14. Click **View** to view the deployed site.



### Elephant SQL
Heroku ended their free tier hosting at the end of November 2022. Students registered with the GitHub Student Developer Pack can apply for the Heroku credits. The Heroku credits allows transfer the projects from free dynos to Eco dynos to ensure that they continue to work. Unfortunately, the student offer does not include the Postgres add-on being used to host my Postgres database. Code Insitute, therefore, have recommended students migrate their databases to a new provider. In this case, it's ElephantSQL, as they are free. The DATABASE_URL value now points to the elephantSQL database in my Heroku Config Vars.

As the database provided by Django is only accessible within Gitpod and is not suitable for a production environment. The deployed project on Heroku will not be able to access it. So, you need to create a new database that can be accessed by Heroku. The following steps will create a new PostgreSQL database instance for use within the project.

#### Create & attach the Elephant SQL database

1. Log in to ElephantSQL to access your dashboard.
![login_elephant sql](https://user-images.githubusercontent.com/97182442/224513112-9b3c93a6-7106-4f77-b387-ea1d0a016bd2.jpg)

2. Click **Create New Instance** at the top right of the page.

3. Set up your **plan**
- Give your plan a Name (the name of the project)
- Select the Tiny Turtle (Free) plan
- You can leave the Tags field blank

![select plan and name](https://user-images.githubusercontent.com/97182442/224513123-b62c9240-6f39-4e0c-b307-55a9f1133993.jpg)

4. Click **Select Region**.

5. Click **Review**.

6. Check your details and then click Create instance.

7. In the **ElephantSQL dashboard**, **database instance name** will be visible

8. Copy the database URL from the URL section.

![cpoy database url](https://user-images.githubusercontent.com/97182442/224513135-be71d401-327a-4534-b8d2-450406e98772.jpg)


9. In Heroku app, add DATABASE_URL as the KEY and paste the URL and  ElephantSQL database will be connected to your Heroku app.

![database url copied to heroku](https://user-images.githubusercontent.com/97182442/224513143-311e5287-116f-4189-b370-e721ea6599c5.jpg)

#### In Gitpod workspace
1. Next, the secret key needs to be created within the projects env.py file on GitPod and then added to the Config Vars on Heroku. Once added, go to the settings.py file on GitPod.
2. Within the settings.py file you need to import the libraries:

           import os
           import dj_database_url
           from django.contrib.messages import constants as messages
           if os.path.isfile('env.py'):
           import env

3. Next we need to tell Django where to store the media and static files. Towards the bottom of settings.py file we can add:

                   STATIC_URL = '/static/'
                  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
                  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
                  MEDIA_URL = '/media/'

4. At the top of settings.py, under BASE_DIR (the base directory), add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS': [].

5. Now we have to add our Heroku Host Name into allowed hosts in settings.py file:
   ALLOWED_HOSTS = ['YOUR-APP-NAME-HERE', 'localhost']
   
6. Finally, to complete the first deployment set up of the skeleton app, create a Procfile so that Heroku knows how to run the project. Within this file add the following: web: gunicorn APP-NAME.wsgi Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.

7.Before deploying the final draft of your project you must:

   . Remove “**DISABLE staticcollect=1** from congifvars within Heroku
   
   . Ensure DEBUG is set to **False** in settings.py file.
   
   
## Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

   1. Log in to GitHub and locate the GitHub Repository
   
   2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
   
   3. You should now have a copy of the original repository in your GitHub account.
   
   
####  Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository.

2. Under the repository name, click "Clone or download".

3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.

4. Open Git Bash

5. Change the current working directory to the location where you want the cloned directory to be made.

6. Type git clone, and then paste the URL you copied in Step 3:

https://github.com/ssreelakshmi88/The-Indian-tuin-restaurant_PP4.git

7. Press Enter. Your local clone will be created.


## Credits

### Code

- Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

- Date picker widget has been taken from stackoverflow.

- Most of the code used in this project was taken from [Code Institutes](https://codeinstitute.net/) Django lessons.

- [DioCar84/A-Taste-of-Lisbon](https://github.com/DioCar84/A-Taste-of-Lisbon.git) for README, setup code and guidance.

- [MikeR94/CI-Project-Portfolio-4](https://github.com/MikeR94/CI-Project-Portfolio-4.git )for setting up README.

- Code institute READMe template was referred to create README template for this project.

- [chris-townsend/PP4-Kitchen_Tales](https://github.com/chris-townsend/PP4-Kitchen_Tales.git) Elephant SQL section from README

- Stack Overflow.

### Content

The recipes and menu were taken from various sources,

https://ministryofcurry.com/


### Media

- All images were taken from pexels.com

- The image of opening times of restaurant(found in reservation page) was created from https://edit.org/edit/cat/0/65#

- The profile image in user profile has been taken from [ThisPersonDoesNotExist](https://thispersondoesnotexist.com/). This website creates randomly generated faces.

### Acknowledgements

- My mentor, Narender Singh for his support and continuous feedback.

- Tutor support at Code Institute for their support.


