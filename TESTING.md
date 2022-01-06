# Testing

## Navigation 


| <p align="center">Feature</p>    | <p align="center">Expected</p> | <p align="center">Testing </p> | <p align="center">Results </p> | Pass/Fail  |
| -------------------------------- | -----------------------------  | ------------------------       | ---------------------------    | :--------: |
| Nav links     | Clicking Home will redirect <br>  users to the Home page  | Click Home   | navigates to Home page   | Pass          
|               | Clicking Rankings takes users <br>to the Album Ranking page | Click Ranking     | navigates to the ranking page   | Pass   |
|               | Clicking Profile takes users <br> to their profile page   | Click Profile   | navigates to the  profile page    | Pass       |
|               | Clicking Log Out <br> logs out the user     | Click Log Out   | User is logged out and taken <br> back to the log in page    | Pass
| Social Media <br> Links   | Redirect to Facebook <br> in a new tap    | Click Facebook Icon  | Facebook page opens in new tap | Pass       |
|               | Redirects to Twitter <br> in new tap   | Click Twitter  Icon   | Twitter page opens <br> in new tap  | Pass       |
|                 | Redirects to Instagram <br> in new tap     | Click Instagram Icon  | Instagram page opens <br> in new tab     | Pass     |


## Buttons 

| <p align="center">Feature</p>  | <p align="center">Expected</p> | <p align="center">Testing</p>    | <p align="center">Results </p>  | Pass/Fail  |
| ------------------------------ | -----------------------------  | -------------------------------- | ------------------------------  | :--------: |
| Info       | Clicking the Info button will <br> open up more info on rankings modal  | Click Info   | navigates to the album modal   | Pass       |
| Upload An Album| Clicking the Submit <br> button will add an album   | Click submit   | submits data to the <br> mongodb  | Pass    |
| Upload An Artist| Clicking the Submit <br> button will add an artist  | Click submit   | submits data to the <br> mongodb  | Pass    |
| Rate     | Clicking the ratte <br> button will submit a rate/review <br> to db    | Click rate | Sends data to db     | Pass       |


## Log In 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| ------------------------------   | -----------------------------     | ------------------------------     | ----------------------------   | :--------: |
| Log In         | Enter the correct user, password, <br> email address will direct users <br> to their profile page with name  <br> displayed and a welcome flash <br> message    | Log in with correct <br> username/password/ <br> email address | Directs users to their profile page <br> with their name displayed and <br> a welcome message  | Pass       |
|                | Incorrect username/password/ <br> email address | Error showing "incorrect <br> username/password" | Flash message <br> displaying error | Pass|



## Registration

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Register   | Username and Password must <br> have a minimum length <br> of 4 characters | Attempt to enter username <br> and password with less than <br> 5 characters | red error displays  | Pass |
|          | Username and Password must <br> have a maximum length <br> of 10 characters | Attempt to enter username <br> and password with more <br> than 15 characters | Form restrcits the user from <br> using more than 10 characters | Pass |
|          | Users can not register <br> with an existing username | Attempt to register with <br> an existing username | error flash message <br> "Username already exists" | Pass |
| Users can not register <br> with an email | Attempt to register with <br> an existing username | error flash message <br> "Email Already In Use" | Pass |


## Upload Album 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Upload a <br> new album | New reviews are albums are saved to the rankings page | Fill in the form  and  click <br> submit | Flash message "Album <br>Successfully Added" informs user <br> the upload was successful. <br> New albums are added to the <br>  rankings page depending on rating number | Pass |      

## Upload Artist 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Uplooad a <br> new artist | New artists are saved  to the <br> upload page | Fill in the form  and  click <br> submit | Flash message "Artist <br>Successfully Added" informs user <br> the uplooad was successful. <br> New artists are added to the <br>  Choose an artist dropdown | Pass |  

## Edit/Delete Review Page 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Edit function                    | Only users who are <br> logged in can edit <br> their uploaded | Log in as a regular user, <br> navigate to profile <br> click the Edit <br> button underneath the <br> album desired, <br> on edit page, edit your rating or review <br>  click submit | Flash message displays <br> "Rating Successfully Updated" | Pass
| Delete function |  Only users who are <br> logged in can delete <br> their reviews/ratings | Log in as a regular user, <br> navigate to profile <br> click the Delete button <br> underneath the album desired, <br>  click the delete<br> button again when prompted. <br> | Flash message displays "Rating/Review Successfully Deleted" | Pass         



## Testing User Stories from User Experience (UX)

| <p align="center">User Stories</p>    | <p align="center">Expectation</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------       | -----------------------------       | -------------------------------    | ------------------------------ | :--------: |
|  First Time <br> User | I want to be able to quickly understand the websites purpose. | On entering the site <br> users are greeted with <br> the music image <br> and some informative text | "Sign Up <br> & START RATING <br> Today" with Top rate Albums below | Pass |
|          | "I want to easily navigate the site and see what content is available. | On entering the site <br> users can scroll down <br> to find albums. | Recent and highly rated albums can be found towards the bottom of <br> the home page | Pass |
|          | "I want the site to be <br> responsive on all devices"| Navigate to site on laptop, <br> tablet and mobile, move <br> around the site to test for <br> responsiveness | Site responsive on all <br> devices | Pass |
|          | "I want to be able to quickly join so I can rate music. | On entering the site <br> users can see <br> a card asking them to register | Visitors will find the register button on the navigation bar. | Pass |
|          | "I would like the ability to read reviews of the music uploaded." | Users can see the top 3 ratetd albums and rankings in the nav bar | Pass |
|          | "I want to be able to see ratings of all the music uploaded."
 | Ratings are posted next to the album on the index and rankings pages | Pass |

|  As a <br> Returning <br> User | "I want to be able to easily login." | Users can find the login button and enter their details | Enter the desired details | Pass |
|        | "I want to still be able to see uploaded albums." | Navigate to the rankings <br> page, click on pagination for left to right, more albums will appear | All the highest rated albums <br> can be found. <br> | Pass|
|         | "I would like the ability to upload music." | Users can find in the <br> nav bar the UPLOAD button. | users have a variety <br> of info to enter ot upload their album | Pass |
|         | "I would like the ability to read reviews of the music uploaded." | Users can find in the <br> info of each album on the ranking page. | Uers have a variety <br> of info to read about their album | Pass |
|         | " would like to be able to edit my own ratings or reviews if I change my mind." | Users can find in their <br> profile the Edit/delete buttons. | Users Can choose <br> to delete or edit their reviews/ratings | Pass |



| As a Frequent <br> User | "I want to be able to upload new artists." | User can upload new artists, <br> click the 'Upload' navbar button, then click the <br> 'Upload New Artist' button <br> And enter the info | A Flash message will <br> displays to the user <br> "Artist <br>Successfully  Added" | Pass | 
|       | "I want to be able to see my uploaded albums or reviews easily.  | Navigate to profile | users can find a <br> their uploaded data to edit  | Pass
|          | "I would like to rate different albums." | On the ranking page <br> users can pick which album <br> they would like to rate | At the bottom of each <br> modal on ranking a user can rate if they haven't done so yet | Pass |
|          | "I would like the ability to read reviews of the music uploaded by different users." | In Rankings <br>Different reviews are in the modals by each user who has rated that album. | In Rankings Modal each users rating/review will be posted in the reviews box | Pass |
|         | "I want to have the option <br> of deleting my reviews" | Navigate to the profile <br> page find a review press delete | Flash message will display <br> "Review Successfully <br> Deleted" | Pass |
|         | "I want to have the option <br> of editing my reviews"  | Navigate to the profile <br> page find an album to edit press <br>the edit button, you will <br> be directed to edit_rating <br>and then edit your rating | Flash message will display <br> "Rating/Review Successfully <br> Updated" | Pass |

## Validator

## HTML Validator

HTML validated on [https://validator.w3.org/](https://validator.w3.org/)

- The W3C Markup Validator was used to validate all HTML pages to ensure there were no major errors.

-   ### [HTML](/static/images/jigsaw.w3.org.png) 

-  ### Home Page
-  ### Log In Page
-  ### Register Page
-  ### Rankings Page
-  ### Profile Page
-  ### Edit Rating Page
-  ### Upload Page
-  ### Upload New Artist Page
 
 
## CSS Jigsaw

CSS3 Validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

-   ### [CSS](/static/images/css.png) 

## PEP8

Python was checked to PEP8 compliance and passed with no errors [http://pep8online.com/](http://pep8online.com/)
-   ### [PEP8](/static/images/pep8.png) 
   
## JSHint

JSHint was used to validate JavaScript with no issues. [https://jshint.com/](https://jshint.com/)
 

## Debugging

-   ### Firefox Inspect Tools

    -  Firefox Inspect was used for inspection of HTML, and CSS. It helped to diagnose problems, and debug issues right in the browers.

-   ### Further Testing

    -   All pages on the site were tested to be fully responsive on all devices

    -   The Website was tested on Firefox, Ecosia, Google Chrome, and Safari browsers.

    -   The website was viewed on a variety of devices such as 
        - Desktop 
        - Laptop 
        - Motorola G4 
        - Galaxy S5/7
        - Pixel 2
        - iPhone 6/7/8/Plus 
        - iPhone X, 
        - iPhone 10
        - iPhone XR
        - iPad2
        - ipad/Pro.

    -   A large amount of testing was done to ensure that all pages were linking correctly.

    -   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

-   ### Bugs Found and not fixed

    -   Users can duplicate artists if they lowercase or uppercase certain characters.

    -   The Image URL validator checks for to ensure there is a  .jpg, .gif, .png but not if it is a proper image.
