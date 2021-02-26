#### [Back to README](README.md)

## **Testing**
### [**Table of Contents**](#table-of-contents)

- [User Stories](#user-stories)
- [Manual Testing](#manual-testing)
- [Responsiveness](#responsiveness)
- [Automated Testing](#automated-testing)
- [Bugs and Issues](#bugs-and-issues)
    - [Resolved](#resolved)
    - [Existing](#existing)

---

## **User Stories**
Each _user story_ was tested to ensure site meets user expectations.

*"As a user, I want to immediately understand the purpose of the site"*
- The home page clearly explains the purpose of the site.

*"As a user, I want to create my own reviews."*
- A user can chose to use the _Add Review_ form on their profile page or click the _Add Review_ link in the Navbar to add their own review.
- The fields required to add a review are clearly identified

*"As a user, I want to be able to rate the book I am reviewing."*
- The star rating input on the add reivew forms allows user to give a star rating to their review
- If no stars are chosen, the field is filled with _'No Stars Given'_.

*"As a user, I want to easily access my own content."*
- All content created by the user is easily accessible through their personalised profile page
under clearly identified tabs.

*"As a user, I want to edit reviews I have created."*
- Users can edit their own reviews through the _'Edit'_ button on the review in the _'My Reviews'_ tab on their profile page

*"As a user, I want to control my own content."* 
- On their personalised profile page users can 
    - Add a new review 
    - Edit or delete existing reviews 
    - Remove reviews they have add to their _'Favourites'_ tab
    - Delete their account

*"As a user, I want to be able to delete reviews I have created."* 
- On their personalised profile page, under the _'My Reviews'_ tab
    - The _'Delete'_ button on their own reviews allows them to delete the review completely

*"As a user, I want to be able to delete my account."* 
-  On their personalised profile page, under the _'Delete Account'_ tab 
    - The _'Delete Account'_ button allows a user to completely delete their account

*"As a user, I want to be able to browse reviews created by other users."*
- All reviews in the database are displayed on the reviews page

*"As a user, I want to be to save reviews created by other users that I like."*
- The save review heart allows users to save reviews created by other users to their own profile
- The review can be removed by clicking the broken heart button on the review in the _'Favourites'_ tab on their profile

*"As a user, I want to be directed to a site where I can buy a book."*
- The buy button redirects the user to a site where the book can be purchased

*"As a user, I want to be able to search for a book, author or genre."*
- The search bar on the profile and reviews page allows users to search through all existing reviews
- On small devices _'Search'_ can be accessed through to search link or the search icon on the reviews page

*"As a user, I want a site that is visually appealing."*
- Each page has a beautiful book related background image
- The elegant typography and colour scheme enhance the aesthetic

*"As a user, I want a site that is easy to navigate."* 
- Links are clearly defined in the navbar with additional options to navigate to different pages throughout the site
- Buttons and icons are easily identifiable
- Consistency across the site is achieved with the navbar and footer remaining fixed across all pages

*"As a user, I want a site that is intuitive."*
- The links are ordered in an intuitive manner
- All content is located where it would be expected to be found.
- By directing users to their personalised profile page on registration/login it shows them exactly what they can expect to find regardless if they have content or not
- The profile also allows them to navigate to where ever they need to go to find or create content

#### [**Table of Contents**](#table-of-contents)

--- 

## **Manual Testing**
 Each element was tested both locally and on the live site to ensure it was working correctly.  
 Testing on functionality was carried out throughout the build using 
 [DevTools](https://developers.google.com/web/tools/chrome-devtools) to ensure everything worked as it should and to identify
 issues/bugs.

#### **Navbar/Sidenav**
 - Navbar is fixed to top of the viewport when scrolling down
 - Each link was clicked to ensure it directed user to correct page
 - Nav brand logo clicked to ensure it returns user to index.html
 - Logged out user only has access to relevant links - 'Home', 'Login', 'Sign up'
 - Logged in user who **_is not 'admin'_** has access to - _'Home', 'My Profile', 'Reviews', 'Add Review', 'Search' 
 (on Small devices only), 'Log Out'_
 - Logged in user who **_is 'admin'_** has access to - _Home', 'My Profile', 'Reviews', 'Add Review', 'Search' 
 (on small devices only), 'Manange Users, 'Log Out'_
 - _'Log Out'_ link
    - logs user out of their account
    - flash message informs user they have been logged out
    - redirects user to _'Log In'_ page
 - Hamburger icon is visible on small devices

#### **Footer**
- Is fixed at bottom of page regardless of content
- Is visible on all pages at all device sizes

#### **index.html**
 - **_Log In_** Link 
    - directs user to _'Log In'_ page
 - **_Sign Up_** Link
    - directs user to _'Sign Up'_ page
 - **_Log In_** Button
    - changes colour on hover
    - directs user to _'Log In'_ page
 - **_Sign Up_** Button
    - changes colour on hover
    - directs user to _'Sign Up'_ page

#### **register.html**
- **_Form Validation_** 
    - All fields must be completed to submit form  
    - If _username_ already exists, flash message informs the user and form is reloaded
    - If _email_ is already registered, flash message informs user and form is reloaded
    - Minlength, maxlength and pattern attributes added to firstname, lastname and username inputs
    - _'Sign Up'_ Button 
        - Changes colour on hover
        - On button click:
            - If form is filled out correctly, submits user information to the users collection
            in the database 
            - Flash message informs user their registration was successful and loads user profile page
            - If form is not filled out correctly, user is informed to fill out missing field
    -  _'Log In'_ Link - redirects to Log In page
    
#### **login.html**
- **_Form Validation_** 
    - All fields must be completed to submit form 
    - If _username and/or password_ are entered incorrectly flash message informs user and form is reloaded
    - _'Log In'_ Button 
        - Changes colour on hover
        - On button click:
            - If form is not filled out correctly, user is informed to fill out missing field
         - If form is filled out correctly, users profile page is loaded
    - _'Sign Up'_ Link - redirects user to register.html

#### **profile.html**
- **_Seach Bar_**
    - Users can perform search on all reviews by _'Title', 'Author' or 'Genre'_
    - At least 3 characters must be enterd for search to be valid
    - On click of the _'search'_ button, results are displayed on reviews.html
    - _'Search'_ button changes colour on hover
    - Search bar is not visible on small devices
- **_Profile Title_** 
    - Displays the users name
    - Not visible on smalle devices
- **_Tabs_**
    - The active tab button is highlighted
    - **_'My Favourites'_**
        - The _'My Favourites'_ tab opens automatically on page load.
        - _'Find Books'_ button - redirects user to reviews.html
        - Any reviews that have been saved by the user are displayed in this tab along with all information related to that review
        - _'Broken heart'_ icon: 
            - Grows on hover
            - When clicked, removes that review from the users _'My Favourites'_ tab and from the 'favourites' field in the users collection in the database
        - If a review saved to favourites is deleted by the owner of that review it is prevented from being displayed in 
        the 'My Favourites' tab 
        - _'Buy'_ button 
            - Changes colour on hover
            - Redirects user to a site where they can buy the book 
        - If the user has no books saved to their favourites, tab contains a heading stating 'You have no books saved'
        and a _'Find Books'_ button which redirects user to reviews.html
    - **_My Reviews_**
        - Any reviews that have been created by the user are displayed in this tab along with all information related to that review
        - _'Delete'_ button: 
            - Changes colour on hover
            - Triggers a modal to confirm review delete.
        - _'Delete Modal'_: 
            - Changes colour on hover
            - Asks user to confirm they want to delete the review
            - States the name of the book they are trying to delete
        - _'Delete'_modal button:
            - Changes colour on hover 
            - Deletes the review from the database, 
            - Flash message informs user review has been deleted 
            - Reloads profile page
        - _'Cancel'_ Modal button 
            - Changes colour on hover
            - Closes the modal
        - _'Edit'_ button 
            - Changes colour on hover
            - Redirects user to _Edit Review_ form 
        - If the user has not books created any reviews, tab contains a heading stating 'You have no reviews'
        and a _'Add Review'_ button which redirects user to add_review.html
    - **_Add Review_**
        - Contains a form for user to add review
        - _Form Validation_ 
            - All fields except _buy link_ and _cover image link_ must be completed to submit form 
                - There are default values set up for these fields if the user leaves them blank 
            - _star ratings_ 
                - Stars change colour when hovered over
                - User can chose how many stars to give a review
                - If no stars are selected, then '_No Stars Given_' is displayed
            - _'Add Review'_ button 
                - Changes colour on hover
                - If form is not filled out correctly, user is informed to fill out missing field
                - If form is filled out correctly, review is added to the database 
                    - profile is reloaded
                    - Review is added to _'My Reviews'_ tab and to reviews.html
    - **_Delete Account_** 
        - Allows user to delete their account
        - _'Delete Account'_ button:
            - Changes colour on hover 
            - Triggers modal asking users to confirm they want to delete their account
        - _'Delete'_modal button
            - Changes colour on hover 
            - Deletes the user from the database 
            - Flash message informs user their account has been deleted 
            - Loads index.html
        - _'Cancel'_ modal button - closes the modal
- **_Scroll Up Button_**
    - Appears when the user scrolls 20px down the page
    - Changes colour on hover
    - Scrolls back to top of the page when clicked

#### **reviews.html** 
- **_Seach Bar_**
    - Users can perform search on all reviews by _'Title', 'Author' or 'Genre'_
    - At least 3 characters must be enterd for search to be valid
    - On click of the _'search'_ button, results are displayed
    - If there are no matching results, user informed 'No Results Found' and 'clear results button is displayed
    - **_Clear Results_** button clears the current search and reloads reviews.html
    - _'Search'_ button changes colour on hover
    - _Clear results_ button 
        - Font awesome icon for '_redo_'
        - On hover:
            - Button changes colour
            - Tooltip appears with _'clear results'_ text 
- **_Reviews_** 
    - All reviews in the database are displayed, including: 
        - All info entered by the creator of the review 
        - Username of user that created the review
        - Date review was created
    - _'Save Review Heart'_ icon
        - Only visible to user if they **_did not_** create the review
        - Pulses when hovered over
        - When clicked:
            - Adds review to 'My Favourites' in the users profile
            - Adds review to the favourites field in the users collection
            - Flash message informs user that the review has been 'saved to their favourites'
            - If review has already been saved by that user, informs the user that the 'review has already been saved'
    - _'Buy'_ button - redirects user to a site they can buy the book
    - If logged in as **_admin_**
        - _'Delete'_ button is visible on all reviews
            - _'Delete'_ button: 
                - Changes colour on hover
                - Triggers a modal to confirm review delete
        - _'Delete Modal'_:
            - Changes colour on hover
            - Asks user to confirm they want to delete the review
            - States the title of the book to be deleted
        - _'Delete'_modal button:
            - Changes colour on hover 
            - Deletes the review from the database
            - Flash message informs user review has been deleted 
            - Reloads reviews.html page
        - _'Edit'_ Button is visible on all reviews
            - Allows **admin** to edit any review created by any user
- **_Scroll Up Button_**
    - Appears when the user scrolls 20px down the page
    - Changes colour on hover
    - Scrolls back to top of the page when clicked 
- **_On Small Devices_**
    - **_Search Bar_** is not accessible on small devices 
    - _'Search'_ icon - returns user to search_mobile.html to perform search
        - Results from searches performed from search_mobile.html are rendered on reviews.html
    - _'Clear'_ icon 
        - Clears search results
        - Reloads reviews.html
        - On hover:
            - Button changes colour
            - Tooltip appears with _'clear results'_ text

#### **add_review.html**
- **_Add Review_**
    - Contains a form for user to add review
    - Allows user to add a review without having to navigate to profile page
    - _Form Validation_ 
        - All fields except _buy link_ and _cover image link_ must be completed to submit form 
            - There are default values set up for these fields if the user leaves them blank 
        - _star ratings_ 
            - Stars change colour when hovered over
            - User can chose how many stars to give a review
            - If no stars are selected, then '_No Stars Given_' is displayed
        - _'Add Review'_ button: 
            - Changes colour on hover
            - If form is not filled out correctly, user is informed to fill out missing field
            - If form is filled out correctly, review is added to the database 
                - profile.html is loaded
                - Review is added to _'My Reviews'_ tab and to reviews.html

#### **edit_review.html**
- **_Edit Review_**
    - Contains a form for user to edit their own review
    - Is popluated with the original infomation added by the user
    - _Form Validation_ 
        - All fields except _buy link_ and _cover image link_ must be completed to submit form 
            - There are default values set up for these fields if the user leaves them blank 
        - _star ratings_
            - Original rating is not displayed on the form
            - User must add rating again 
            - Stars change colour when hovered over
            - User can chose how many stars to give a review
            - If no stars are selected, then '_No Stars Given_' is displayed
        - _'Save'_ button 
            - Changes colour on hover
            - If form is not filled out correctly, user is informed to fill out missing field
            - If form is filled out correctly, review is updated in the database 
                - Users profile is loaded
        - _'Cancel'_ button 
            - Changes colour on hover
            - No changes to the form are saved
            - Users profile is loaded

#### **search_mobile.html**
- Only available on small devices
- **_Seach Bar_**
    - Users can perform search on all reviews by _'Title', 'Author' or 'Genre'_
    - At least 3 characters must be enterd for search to be valid
    - On click of the _'search'_ button, results are displayed on reviews.html
    - _'Search'_ button changes colour on hover

#### **manage_users.html**
- Only accessible to the **_admin_** user
- Displays all users in the database, including:
    - Database Id
    - Firstname
    - Lastname
    - Username 
    - Email Address 
- _'Delete Account'_ button: 
    - Changes colour on hover
    - Triggers a modal to confirm account delete
- _'Delete Account'_ Modal: 
    - Asks user to confirm they want to delete this account
- _'Delete Account'_modal button:
    - Changes colour on hover 
    - Deletes the account from the database, 
    - Flash message informs user review has been deleted 
    - Reloads page

#### [**Table of Contents**](#table-of-contents)

--- 

## **Responsive Design**
The app was developed using the _Mobile First_ philosophy.

Responsive design was tested throughout the build using [DevTools](https://developers.google.com/web/tools/chrome-devtools)
and [Am I Responsive](http://ami.responsivedesign.is/).

[Materialize CSS](https://materializecss.com/) grid was used for the structure to ensure responsiveness
at all breakpoints. [Materialize CSS](https://materializecss.com/) classes, 
including `margin`, `padding`, `center-align` `hide` were used to adjust HTML structure for various device sizes.
In addition media queries were used to tweak font-sizes, margins, padding and alignment.

#### **Browsers**
- Chrome 
- Edge
- Firefox
- Safari

#### **Screen Sizes**
Using [DevTools](https://developers.google.com/web/tools/chrome-devtools) profiles:
- Moto G4
- Galaxy S5
- Pixel 2/ 2XL
- iPhone 5/SE
- iPhone 6/7/8 
- iPhone 6/7/8 Plus 
- iPhone X 
- iPad / Pro 
- Surface Duo
- Galaxy

Using [DevTools](https://developers.google.com/web/tools/chrome-devtools) responsive profiles:
- Mobile S - 320px
- Mobile M - 375px
- Mobile L - 425px
- Tablet - 768px
- Laptop - 1024px

 It was also tested physically on various devices including:
 - Hauwei P20 Pro
 - Galaxy A6
 - HP Pavilion Laptop 

#### [**Table of Contents**](#table-of-contents)

---

## **Automated Testing**
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) - to validate HTML
    - All errors thrown were related to jinja templating
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) - to vaildate CSS Code
    - no errors found
- [JShint](https://jshint.com/) - to validate Javascript code
    - no errors found
- [PEP8 Online](http://pep8online.com/) 
    - no errors found
- [Python Checker](https://www.pythonchecker.com/) - no errors found
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) - no overflow detected
- [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) - generated the below reports:

**index.html**
- **Desktop**
    - Performance: 86
    - Accessiblity: 100
    - Best Practices: 100
    - SEO: 100
- **Mobile**
    - Performance: 65 - due to background image size
    - Accessiblity: 100
    - Best Practices: 100
    - SEO: 100

**login.html**
- **Desktop**
    - Performance: 96
    - Accessiblity: 100
    - Best Practices: 93
    - SEO: 100
- **Mobile**
    - Performance: 71 - due to background image size
    - Accessiblity: 96
    - Best Practices: 93
    - SEO: 100

**reviews.html**
- **Desktop**
    - Performance: 87
    - Accessiblity: 86
    - Best Practices: 93
    - SEO: 100
- **Mobile**
    - Performance: 55 - due to background image/images size
    - Accessiblity: 96
    - Best Practices: 93
    - SEO: 100

**add_review.html**
- **Desktop**
    - Performance: 90
    - Accessiblity: 100
    - Best Practices: 100
    - SEO: 100
- **Mobile**
    - Performance: 68 - due to background image 
    - Accessiblity: 96
    - Best Practices: 100
    - SEO: 100

**edit_review.html**
- **Desktop**
    - Performance: 94
    - Accessiblity: 100
    - Best Practices: 100
    - SEO: 100
- **Mobile**
    - Performance: 67 - due to background image 
    - Accessiblity: 96
    - Best Practices: 100
    - SEO: 100

**register.html**
- **Desktop**
    - Performance: 91
    - Accessiblity: 100
    - Best Practices: 93
    - SEO: 100
- **Mobile**
    - Performance: 69 - due to background image 
    - Accessiblity: 96
    - Best Practices: 93
    - SEO: 100

**manage_users.html**
- **Desktop**
    - Performance: 98
    - Accessiblity: 100
    - Best Practices: 93
    - SEO: 100
- **Mobile**
    - Performance: 86 
    - Accessiblity: 95
    - Best Practices: 93
    - SEO: 100

**search_mobile.html**
- **Mobile**
    - Performance: 67 - due to background image 
    - Accessiblity: 96
    - Best Practices: 93
    - SEO: 100

- Lighthouse was unable to generate a report for profile.html
- I was unable to compress the background images further to improve performance


#### [**Table of Contents**](#table-of-contents)
---

## **Bugs and Issues**

### **Resolved**

**_issue_**:
- Sidenav links not clickable

**_fix_**:
- Materialize has a built class of `.sidenav-overlay` which was covering the sidenav links
- Changed the `z-index` of `.sidenav-overlay` to 1

**_issue_**:
- Profile not rendering

**_fix_**:
- Add `username=session['user']` to profile `href` in navlinks
````
<li><a href="{{ url_for('profile', username=session['user']) }}">My Profile</a></li>
````

**_issue_**:
- Heart checkboxs on review in reviews.html couldn't be clicked independantly of each other.

**_fix_**:
- Added `{{loop.index}}` to `id`, `label` and `name` to the input and label of `heart-checkbox` div.
````
<div class="heart-checkbox">
    <input type="checkbox" id="save{{loop.index}}" name="save{{loop.index}}" onchange="this.form.submit()" />
        <label for="save{{loop.index}}" class="hvr-pulse">
            Save Review!
        </label>
</div>
````
**_issue_**:
- Clicking on heart checkbox on review did not submit the form

**_fix_**:
- Added `onchange="this.form.submit()` to the checkbox input
````
<input type="checkbox" id="save{{loop.index}}" name="save{{loop.index}}" onchange="this.form.submit()" />
````

**_issue_**:
- User was able to save the same review to their favourites multiple times

**_fix_**:
- Added an `if` statement to `add_favourite` function
````
    if ObjectId(review_id) in favourites:
        flash("Review Already Saved")
````

**_issue_**: 
- Star rating not being picked up on _edit_review_ form submit

**_fix_**:
- Added `"rating": request.form.get("star") or default_rating` to `update{}` dictionary in _edit_reivew_ function

**_issue_**:
- Scripts for scrollBtn on reviews.html and tabs on profile.html not executing.
- Scripts were in conflict with each other when switching between the pages.

**_fix_**:
- Seperated the scripts for each page into their own `.js` file

**_issue_**:
- `delete_profile`function throwing `user not defined` error when trying to delete user account

**_fix_**:
- Defined user in profile view 
````
 user = mongo.db.users.find_one({"username": session["user"]})
````
**_issue_**:
- `default_img ` variable set in add/edit review forms for when a user doesn't add 
a link was not being pulled onto reviews displayed on the profile page   

**_fix_**:
- Added a `/` to the start of the file path
`default_img = ("/static/images/no_cover.png")`

**_issue_**:
- If user didn't select a _star rating_ on add/edit review forms, the word 'none' was displaying instead

**_fix_**:
- Created a default variable `default_rating` to display if no stars were selected by the user
` default_rating = "No Stars Awarded"`

**_issue_**:
- `{% else %}` clause (if user has created no reviews) of `{% if reviews|length > 0 %} ` was
not rendering `{% else %}` clause code
````
 {% else %}
<h3>You have no reviews </h3>
    <a href="{{ url_for('add_review') }}" type="submit" class="btn btn-small center-align">
        Add Review 
    </a>
````
**_fix_**:
- Changed the `my_reviews` variable in the profile view to a list 
 ````
 my_reviews = list(mongo.db.reviews.find(
            {"created_by": session["user"]}).sort("title", 1))
````
**_issue_**:
- `setTimeOut()` function not running on `flash messages`
- `cannot set style of undefined` error in the console

**_fix_**:
- Added a `for loop` to iterate through the list of flash messages and set `display:none`
to each one

**_issue_**:
- ScrollBtn not scrolling up when clicked

**_fix_**:
- Changed `onclick` event to `event listener`
````
    document.getElementById("scrollToTop").addEventListener("click", scrollUp);
````
**_issue_**:
- Users reviews not being deleted when they deleted their account

**_fix_**:
- Changed `mongo.db.reviews.remove({"created_by": session['user']})` in the delete_profile function to
`mongo.db.reviews.delete_many({"created_by": session['user']})`

**_issue_**:
- Favourite reviews not displaying in 'My favourites' tab on profile page

**_fix_**:
- Looped through the `user_favourites` object and appended the review to `fav_review[]` 
- Moved code from `get_favourites` function into `profile` function
````
    user_favourites = user["favourites"]
    fav_review = []
    for fav in user_favourites:
        review = mongo.db.reviews.find_one({"_id": ObjectId(fav)})
        if review is not None:
            fav_review.append(review)
````

**_issue_**:
- When deleting a review or account from the modals delete button the first document in the list was being 
deleted instead of the selected account/review

**_fix_**:
- Specified document to be deleted in the modal `id` and `data-target`
- For delete review modals the below code was added:
````
    <button data-target="{{'confirm_delete'+review.title}}" class="btn-small modal-trigger">Delete</button>
    <div id="{{'confirm_delete'+review.title}}" class="modal">
````
- For the delete account modals the the below code was added:
````
    <button data-target="{{'admin_profile_delete'+user.username}}" class="btn-small delete-btn right modal-trigger">
        Delete Account
    </button>  
    <div id="{{'admin_profile_delete'+user.username}}" class="modal">
````    
**_issue_**:
- Deleted reviews were not being removed from the 'My Favourties' tab on the profile page of other users

**_fix_**:
- Added an `if` statement to profile function to only display reviews that exist to the profile page
````
  for fav in user_favourites:
    review = mongo.db.reviews.find_one({"_id": ObjectId(fav)})
    if review is not None:
        fav_review.append(review)
````
### **Existing**

- Although _favourites_ are not being displayed when the review has been deleted they still exist in the favourites[] field in the users collection in the database

- When _admin_ user deletes a users account that users reviews are not being deleted


#### [**Table of Contents**](#table-of-contents)
---
#### [Back to README.md](README.md)