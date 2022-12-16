
# Last Minute F1

![Last Minute F1 ](/media/homepage_background_cropped.jpg 'Shows responsive views of site')

[View the live project here](https://lastminutef1.herokuapp.com/ "Link to deployed site - Last Minute F1")

## Table of contents
1. [Introduction](#Introduction)
2. [Business](#Biz)
    1. [Business Model](#business-model)
    2. [Marketing Mix](#marketing-mix)
3. [UX](#UX)
    1. [User Stories](#user-stories)
    2. [Development Planes](#development-planes)
    3. [Design](#design)
4. [Features](#features)
    1. [Design Features](#design-features) 
    2. [Existing Features](#existing-features)
    3. [Features to Implement in the future](#features-to-implement-in-the-future)
5. [Issues and Bugs](#bssues-and-bugs)
6. [Technologies Used](#technologies-used)
     1. [Main Languages Used](#main-languages-used)
     2. [Additional Languages Used](#additional-languages-used)
     3. [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used)
7. [Testing](#testing)
     1. [Testing.md](TESTING.md)
8. [Deployment](#deployment)
     1. [Deploying on Heroku](#deploying-on-heroku)
9. [Credits](#credits)
     1. [Content](#content)
     2. [Media](#media)
     3. [Code](#code)
10. [Acknowledgements](#acknowledgements)
***

## Introduction

This is the 5th and final Portfolio Project needed to complete the FSSD program with Code Institute.

I took the opportunity, during this project, to build towards my vision of a business and have used my learnings during the FSSD program to create the foundation of a working MVP for v1.
In order to get this project off the ground I had to manually build the categories & tickets json files as there were no databases available on Kaggle.com.

Throughout the project I was using Agile methodologies to plan my project and building iteratively. Once I had made the decision to start, I followed the Django Boutique Ado tutorial from my Code Institute course, adapated it to my needs, and was able to build the foundation of my vision for this business.

Portfolio Project 5 requires students to build a Full Stack website based on business logics using CRUD with Stripe payment functionalities. On top of that, we must create a business around it / narrative and use digital marketing skills to showcase the opportunities.

My project is a ticketing website to buy exclusive Grandstand, Paddock and Team Paddock tickets to attend the 2023 Formula 1 races. Users can search, browse, learn about, add to cart & buy tickets which will be delivered to them via email. Users that are logged in will be able to save time while purchasing as their purchase information will be saved.

[Back to top ⇧](#top)

## Biz
### Business Model
#### business-model

An ecommerce business selling Formula 1 Paddock, Team Paddock, and grandstand tickets can follow a number of different business models, depending on the specific needs and goals of the business. The model I wish to follow is the Direct-to-consumer model as I am currently acting as a broker.

Direct-to-consumer (D2C) model: In this model, the ecommerce business sells tickets directly to consumers through its website or other online channels. The business may purchase tickets from the official Formula 1 organizers or from ticket brokers, and then mark them up for resale to consumers.

### Marketing Mix
#### marketing-mix

1. Product: The product in this case would be the Formula 1 Paddock, Team Paddock, and grandstand tickets. These should be clearly described and presented on the ecommerce website, including details such as location, seating options, and any additional perks or amenities that are included.

2. Price: The price of the tickets should be competitive and in line with similar offerings in the market. It may be helpful to offer different pricing options or packages to appeal to a variety of customers.

3. Place: The ecommerce website should be the primary place where customers can purchase tickets. It should be easy to navigate and user-friendly, with a secure checkout process to ensure customer confidence.

4. Promotion: Digital marketing strategies such as email marketing (mailchimp), social media marketing (instagram, facebook), and online advertising can be used to promote the tickets and drive traffic to the ecommerce website. It may also be helpful to offer special promotions or discounts to encourage purchases.

5. People: The customer service team should be knowledgeable and able to assist customers with any questions or concerns they may have. It may also be helpful to have knowledgeable sales staff available to help customers choose the best tickets for their needs.

6. Process: The ticket purchasing process should be streamlined and easy to follow. This includes clear instructions and an efficient checkout process.

7. Physical evidence: Providing physical evidence of the tickets, such as a confirmation email or ticket stub, can help to build customer trust and confidence in the ecommerce business.


[Back to top ⇧](#top)

## UX 

### User Stories
#### User-Stories:
1. As a **logged out user**, I want to **easily purchase tickets** to my favorite races through the ecommerce site, **so that** I can secure my spot at the event.

2. As a **logged out user**, I want to be able to **access exclusive tickets** and paddock club tickets, **so that** I can save money on my purchases.

3. As a *logged out user**, I want to be able to **easily navigate the ecommerce site and find information** about the different ticket and paddock club options available, **so that** I can make an informed decision about my purchase.

4. As a **logged out user**, I want to be able to **purchase team paddock club tickets** that give me access to the team's paddock area, **so that** I can get a behind-the-scenes look at the team's operations.

5. As a **logged in user**, I want to be able to **see my purchase history**, **so that** I can review past purchases

6. As a **logged in user**, I want to be able to **save my billing information**, **so that** the next time I buy a ticket I don't have to fill those fields out again.

[Back to top ⇧](#top)

#### Site Admin:
1. As a **admin user**, I want to be able to **add** tickets, **so that** I can add tickets should new opportunities arise.

2. As a **admin user**, I want to be able to **edit** tickets, **so that** I can modify information pending on changes in the season or cost changes.

3. As a **admin user**, I want to be able to **delete** tickets, **so that** I can remove tickets if they are no longer available or have wrong information.

4. As a **admin user**, I want to be able to **have access to an admin panel** to manage customer accounts and orders, **so that** I can efficiently handle any questions or issues that may arise.

[Back to top ⇧](#top)

### Development Planes
To create a comprehensive and appealing website, I inspired myself off of formula1.com as well as various f1 related ticketing sites like tickets.formula1.com and gptickets.com. I did research websites to discover what features and functionality that would be interesting to add. This information created the above user stories and is developed further below.

[Back to top ⇧](#top)

#### Strategy
Broken into three categories, the website will attempt to focus on the following target audiences:
- **Roles:**
     - User
     - Admin

- **Demographic:**
     - F1 fans
     - F1 newbies
     - High Networth Individuals
     - Sports aficionados
     - Family & Friends of drivers/teams

- **Psychographics:**
     - Personality & Attitudes:
          - Sporty
	     - Wealthy
          - Travelers
          - Party lovers
          - Love exclusivity

     - Values:
        - Interested in seeing the races 
        - Interested in partying in new cities & countries
        - Love experiencing exclusivity
     - Lifestyles:
        - Globetrotters
        - Bon-vivant

The website needs to enable the **user** to:
- browse the tickets.
- add tickets to cart.
- buy the tickets.
- receive an email with ticket information.
- register and log in to save order history and user info.

The website needs to enable the **admin** to:
- add, edit and delete tickets
- charge the users and deliver tickets


[Back to top ⇧](#top)

#### Scope
A scope was defined to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
         - a comprehensive list of available tickets for all races in 2023.
	    - a description of each race and their dates
	    - an understanding of what paddock club is
         - a way to purchase these tickets

- **Functionality Requirements**
     - The user will be able to:
         - Easily navigate the site to find the information they want.
	    - Be able to add tickets they wish to buy to their cart.
         - Select the days they would like to attend per ticket
         - Be able to purchase tickets and receive a confirmation email.

[Back to top ⇧](#top)


#### Skeleton 
Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ 'Balsamiq Website').

Home Page:
![Home Page Wireframe](/media/readme/home.png 'Home Page - Wireframe')

Ticket Page:
![Ticket Page Wireframe](/media/readme/ticket_page.png 'Ticket Page - Wireframe')

Ticket Detail:
![ticket detail Wireframe](/media/readme/ticket_detail.png 'Ticket Detail - Wireframe')


[Back to top ⇧](#top)

### Design

#### Colour Scheme
I chose to use the same color palette as formula 1 as the colors are vibrant, exciting and consistant throughout every business in the industry. Black and white have been used for the typography and red has been used for buttons and banners.  I wanted the website to look fresh and convey an exciting feel.

The off-white background allows the colours and the tickets to pop out a bit.

[Back to top ⇧](#top)

#### Logo
The lastminutef1 is basic and uses a specific font-family: Titillium Web.  I liked it because it is simple and emphasizes on 'F1'

[Back to top ⇧](#top)

#### Typography

The font chosen for the logo was Titillium Web as it is bold and crisp.  The font has also been used throughout the website for sub-headings, to add some differentiation from the main font of the site. All instances of Titillium Web have also been styled black or red to make them stand out against the white background of the site.

The main font of the website is Titillium Web, which has been used for large headings, as well as all other text.  Titillium Web is the font used on Formula 1.com and it ensures that the most important information on the site is readable.

The font was chosen from [Google Fonts](https://fonts.google.com/ 'Google Fonts website')

[Back to top ⇧](#top)

#### Imagery
To match the colour scheme chosen, I chose an image of the Abu Dhabi Race from Pexels.com to be the hero image on the index page. Abu Dhabi is the last race of every season and is recognizable by F1 fans. 

On each ticket in the ticket.html file, you will find a 'country image' to help users quickly recognize the country of the race as well as a 'image' of the circuit for that race. These two types of images were chosen to help each user browse more effectively.

All of the ticket images are from [Formula1](https://www.formula1.com/ 'Formula1 website').

[Back to top ⇧](#top)

## Features

### Design Features
Each page of the website features a consistent responsive navigational system:

- The **Header** contains a conventionally placed logo in the top left of the page (whereby clicking this will redirect users back to the home page) and a search bar also centered on the browser and on the right you will see a user icon as well as a cart icon. On smaller screens, the navigation bar condenses into a dropdown with navigation options.  I chose to make the dropdown horizontal so that it didn't take up too much real estate on the screen.

- The navigation sits centered below the search bar and has 5 nav-links: 'tickets', 'paddock club', 'schedule', 'more F1 news' & 'what is paddock' - Respectively, these links enable users to browser and filter tickets according to various variables, see the 2023 race schedule, go to F1.com & learn more about what paddock access is.

- The **Footer** contains a mail chimp newsletter subscription form as well as 4 links to external social media links
 
[Back to top ⇧](#top)

### Existing Features
- **Header Logo** - Appearing on every page for brand recognition. Clicking the logo will return the users to the home page, as expected.
- **Search Bar** - Appearing on every page for a consistently easy and intuitive navigation system.
- **Navigation** - The navigation sits centered below the search bar and has 5 nav-links: 'tickets', 'paddock club', 'schedule', 'more F1 news' & 'what is paddock' - Respectively, these links enable users to browser and filter tickets according to various variables, see the 2023 race schedule, go to F1.com & learn more about what paddock access is.
- **Social Icons** - Appearing on every page, the icons are appropriate representations of the Social Media platforms, found in the footer.
- **Tickets** - Appearing on the tickets page and search results, giving a brief overview of the ticket, the cost, the description, the dates, the availability, showing the image, servings, difficulty, prep and cook time, and the number of likes on the ticket.
- **Ticket Form** - Appearing on the add a ticket page and edit ticket page, the form allows the user to add or edit a ticket, including adding an image to display on the ticket page and ticket card.
- **Home Page** - A home page that makes it clear to the user what the objective of the site is
- **Information (Schedule) Page** - A Schedule page that showcases a table with each 2023 F1 grand prix, the destination and dates
- **What is Paddock** - An information page so that users who do not know what Paddock access is, can find this information and learn about it.
- **Sign In Page** - A page designed to allow the user to log in using previously created user details; a username and a password.
- **Sign Up Page** - A page designed to allow the user to create a user profile using a username, optional email address and a password that needs to be repeated to ensure it is correct.
- **Sign Out Page** - A page designed to confirm the user wishes to log out of their account. If the user clicks the sign out button, they are then redirected to the home page.

### Features to Implement in the future
- **Highligh Seating on circuit image**
     - **Feature** - This feature would let the user know where they would be seated on the circuit dynamically letting them assess if the view would be something that they would like
     - **Reason for not featuring in this release** - tickets.formula1.com has somewhat of a similar feature and I have not had the chance to experiment with this technology yet - which will require me to do a lot more learning.
- **Grandstand seat booking**
     - **Feature** - This feature would dynamically let the user book their seats like people who book the cinemas - being able to select an assigned seat in the grand stands
     - **Reason for not featuring in this release** - Due to data being owned by F1, seating data is unavailable to general public.
 **Stock Management**
- **Feature** - This feature would dynamically manage ticket stock (would also need to be implemented when we add tickets) so that the Admin can know how many tickets are left and that the User can know of product availability
- **Reason for not featuring in this release** - I started watching stock management videos on Youtube but adding this would have required me to spend 2x as much time to develop this project.
-  **Display date of race on each ticket card**
     - **Feature** - This feature would dynamically display the date of the race for each ticket in the ticket.html view
     - **Reason for not featuring in this release** - Ran out of time on the project.
 **Blog section**
- **Feature** - This feature would be a simple blog section where the Admin could share blog posts (or use an RSS feed)
- **Reason for not featuring in this release** - Only thought of this idea as I was typing the README...

[Back to top ⇧](#top)

## Issues and Bugs 

**Bug** - Working with added values in the models for tickets to enable users to select different options in their tickets was buggy at first due to data being strings and containing special characters.
- ***Solution***: Once I figured out the root cause of the problem I was able to convert everything to strings using special character formatting.

**Bug** - Deployment was full of bugs as Heroku Stack 22 was making the deployment fail as well as a few typos 'DISABLE_COLLLECTSTATIC' & 'os.environ.gget()' that took me a while to find. I wasn't able to access Heroku via CLI due to have MFA and at first there seemed to be very limited information / steps described online
- ***Solution***: Once I realized that I could simple use the API key from Heroku as my password via CLI - I was able to set:stack 20 and then saw where the other issues to deployment were coming from -> typos.

**Bug** - I was having rendering issues on mobile on the cart while users were checking out as the - + were not layout out in a good way
- ***Solution***: I refactored the code and broke down the cart into 4 different html filed (image, product info, price, checkout button), which enabled me to have more control within the CSS.

**Bug** - As a user I was able to access my order history, but when I clicked on the ticket number,  I would get to the checkout success page - which would have the confirmation - but not contain any information from the actual order
- ***Solution***: I had to review the user journey and check the URLs as well as the forms that were being called. Turned out there was an indentation error on the form.save().


**Issue** - Still some styling issues on mobile, especially with the footer and the mailchimp subscription.

**Issue** - I have left errors flagged by Flake8 which call out long lines. 

[Back to top ⇧](#top)

## Technologies Used
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

### Additional Languages Used
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
     - Used to implement the Summernote feature that allowed the user to add styling to the ticket in the form.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")
     - Used to implement Django functionality, including building models, forms and views for the app.

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [AWS](https://s3.amazon.com/ "Link to AWS page")
     - AWS was used as free cloud storage for images uploaded to the site through the ticket forms.
- [ElephantSQL](https://elephantsql.com/ "Link to ElephantSQL page")
     - Elephant SQL was used as free platform to host and store my databases
- [Heroku](https://www.heroku.com "Link to Heroku page")
     - Heroku was used to deploy my project
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit ticket forms, allowing more than one field to occupy a line on the form.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Poppins" and "Dancing Script" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.

[Back to top ⇧](#top)

## Testing

Testing information can be found in a separate [testing file](TESTING.md "Link to testing file").

## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was commited to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - Add all relevant keys (STRIPE, SECRET_KEY, API, AWS...) into Config Vars
    - In your GitPod workspace, create ensure all config variables are in settings.py
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the settings.py.
    - In settings.py add the following sections:
        - STATICFILES_DIRS
        - MEDIA_URL 
        - MEDIA_ROOT 
        - AWS_S3_OBJECT_PARAMETERS 
        - AWS_STORAGE_BUCKET_NAME 
        - AWS_S3_REGION_NAME 
        - AWS_ACCESS_KEY_ID 
        - AWS_SECRET_ACCESS_KEY_ID 
        - AWS_S3_CUSTOM_DOMAIN 
        - STATICFILES_STORAGE
        - STATICFILES_LOCATION 
        - DEFAULT_FILE_STORAGE
        - MEDIAFILES_LOCATION 
        - STATIC_URL 
        - MEDIA_URL
        - DEFAULT_AUTO_FIELD 
        - STRIPE_CURRENCY
        - STRIPE_PUBLIC_KEY 
        - STRIPE_SECRET_KEY 
        - STRIPE_WH_SECRET
        - DEFAULT_FROM_EMAIL
        - EMAIL_BACKEND 
        - EMAIL_USE_TLS
        - EMAIL_PORT
        - EMAIL_HOST
        - EMAIL_HOST_USER
        - EMAIL_HOST_PASSWORD
        - DEFAULT_FROM_EMAIL
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in AWS and Deploy to Heroku:
    - Create 2 directories in the bucket; media, static .
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Log in to Heroku using the terminal heroku login -i.
    - Then run the following command: **heroku git:remote -a your_app_name_here** and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
    - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.


[Back to top ⇧](#top)

## Credits 

### Content
- All circuit images were taken from [Formula1.com](https://www.formula1.com/ "Link Formula 1 website")'.

- The descriptions of the races were taken from Formula 1.com as well.

### Media
- The country icons and the hero image on 'home' have been sourced from [Pexels](https://pexels.com/).

### Code 
References used:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Formula1](https://www.formula1.com/ "Link to Formula1 page")
- [Django Docs](https://docs.djangoproject.com/en/3.2/ "Link to Django's Docs for Version 3.2")
- [Boutique Ado](https://boutique-ado-a.herokuapp.com/ "Link to Boutique Ado")
- [Nooz Site](https://nooz-site.herokuapp.com "Link to Nooz website")
- [Cripsy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to Crispy Forms documentation")

### Other
- [Visio](https://www.microsoft.com/en-gb/microsoft-365/visio/flowchart-software "Link to Visio on Microsoft's website")
     - Visio was used for the diagrams in this Readme document.

[Back to top ⇧](#lastminutef1)

## Acknowledgements

- I would like to my friends and colleagues who all tried the features for me on the finished product to see what could be improved (e.g: what is paddock?)
- I would like to thank all of the tutors that helped me (Oisin, John, Gemma) as every time I had issues, they were headaches - they are all great!
- Thanks also to Kieron/Code Institute's student relations who in spite of all the things that happened to me personally in 2022, were able to give me the space I needed to finish the program. 

[Back to top ⇧](#top)

***