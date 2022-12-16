
# Last Minute F1 - Testing 

[Main README.md file](/README.md)

[View live project](https://lastminutef1.herokuapp.com/)

[View GitHub repository](https://github.com/mpysys/lastminutef1)

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
4. [User Testing](#User-Testing)


***

## Testing User Stories

#### User Stories:
1. As a **logged out user**, I want to **easily purchase tickets** to my favorite races through the ecommerce site, **so that** I can secure my spot at the event.

2. As a **logged out user**, I want to be able to **access exclusive tickets** and paddock club tickets, **so that** I can save money on my purchases.

3. As a *logged out user**, I want to be able to **easily navigate the ecommerce site and find information** about the different ticket and paddock club options available, **so that** I can make an informed decision about my purchase.

4. As a **logged out user**, I want to be able to **purchase team paddock club tickets** that give me access to the team's paddock area, **so that** I can get a behind-the-scenes look at the team's operations.

5. As a **logged in user**, I want to be able to **see my purchase history**, **so that** I can review past purchases

6. As a **logged in user**, I want to be able to **save my billing information**, **so that** the next time I buy a ticket I don't have to fill those fields out again.

8. As a **admin user**, I want to be able to **add** tickets, **so that** I can add tickets should new opportunities arise.

8. As a **admin user**, I want to be able to **edit** tickets, **so that** I can modify information pending on changes in the season or cost changes.

9. As a **admin user**, I want to be able to **delete** tickets, **so that** I can remove tickets if they are no longer available or have wrong information.

10. As a **admin user**, I want to be able to **have access to an admin panel** to manage customer accounts and orders, **so that** I can efficiently handle any questions or issues that may arise.

[Back to top ⇧](#top)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Test that website works from different devices (pc/mac/ios/android)

- Test logged in versus logged out features

- Test registration features & account creation

- Test add, edit, delete tickets from ticket_detail and from the ticket management area

- Test that Logo redirects to home screen.

- Test that Nav Links work.

- Test that Footer Links work & mail chimp subscription

- Test Search 

- Test 404.html

- Test that Social Links work and open in a new page.

### Home Page
Manual testing was conducted on the following elements of the [Home Page](https://lastminutef1.herokuapp.com/):
     
- Test that navigation is responsive

- Test user profile create, login & update within profile

- Test Search 

### Ticket Detail Page
Manual testing was conducted on the following elements of the [Ticket Detail Page](https://lastminutef1.herokuapp.com/tickets/ & https://lastminutef1.herokuapp.com/tickets/1):

- Test that article can be accessed by users.

- Test that article can only be edited/deleted by Admin.

- Test that a success message appears when something has been added to cart.
     
- Test that tickets can be added to cart
     
- Test that the quantity of tickets can be added and substracted

- Test that the user can select tickets according to the day packages available per race.

### Add Ticket Page
Manual testing was conducted on the following elements of the [Ticket Add Page](https://lastminutef1.herokuapp.com/add_ticket/):

- Test that Admin can add a ticket and input all the related fields (sku, race & country, description, image for country & image for circuit...)

- Test that Admin can upload and remove images to the countryimg and image fields (one is for the country flag, one is for the image of the circuit)
     
- Test that Admin can submit the new ticket and that it saves to the data base

- Test that Users can search for the newly added ticket

- Test that Users cannot access this URL or feature

### Edit/Delete Ticket Page
Manual testing was conducted on the following elements of the [Ticket Add Page](https://lastminutef1.herokuapp.com/tickets/1/edit_ticket/ & https://lastminutef1.herokuapp.com/tickets/1/delete/):

- Test that Admin can edit a ticket and all the related fields (sku, race & country, description, image for country & image for circuit...)

- Test that Admin can delete an existing ticket
     
- Test that Admin can edit the new ticket and that it saves to the data base with the updated information.

- Test that Users can search for the edited ticket

- Test that Users cannot access this URL or feature
     
### Sign in/Sign Out/Sign Up Pages
Manual testing was conducted on the following elements of the [Login Page](https://lastminutef1.herokuapp.com/profile/login/), [Sign Out Page](https://lastminutef1.herokuapp.com/profile/logout/) and [Register Page](https://lastminutef1.herokuapp.com/profile/register/):

- Users can register, log in and logout.

### Pages are Responsive
- Manual testing was conducted for responsiveness on large, medium and small screens.

[Back to top ⇧](#top)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python` code used.

**Results:**

- HTML Pages - Code Validation

HTML validation - all pages clear.

- CSS stylesheet - Code Validation

CSS tested clear.

- Python Files - Code Validation

**Files tested**

cart - urls.py
cart - views.py
checkout - urls.py
checkout - models.py
checkout - views.py
lastminutef1 - urls.py
lastminutef1 - settings.py
tickets - urls.py
tickets - forms.py
tickets - models.py
tickets - views.py
profiles - urls.py
profiles - forms.py
profiles - models.py
profiles - views.py



All files tested clear.

### Browser Validation
- Chrome
- Edge
- Opera
- Firefox

## User testing 
My group of friends were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience. 

[Back to top ⇧](#top)

***

Future updates 

