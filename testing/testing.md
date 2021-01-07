## Testing

### Manual Testing

Manual testing was used to test navigation, responsiveness on different screen sizes, database operations (Create, Read, Update and Delete) and application functions.

### Responsiveness

#### Desired Result

All information from each page on the app should be viewable on all screen sizes from small mobile phone, to tablet sized devices up to very large monitor screens.

#### Steps Taken to Ensure Result

The Materialize grid system was used to ensure data displayed in a satisfactory manner on vaious screen sizes. CSS was used to make images responsive and create appropriate behavour
within the 'card' element provided by materialize.

On Chrome Developer Tools the following devices were emulated to check responsiveness:

- Moto G4 (smallest phone screen width available)
- Pixel XL
- iPhone X
- iPad


These physical devices were also used for testing:

- Macbook Pro 15-inch retina screen
- HP e233 23-inch monitor
- Samsung S10e
- iPhone SE2020

#### Verdict

Le Munch adapts to most tested screen sizes and devices and displays as expected but on very small screen widths there were some issues.
Samsung fold device when emulated on google dev tools made some contact link jump to a new line.  This was not deemed to be too big an issue
as the dev tools only show 1 half of the screen.  It is assumed that this would display correctly on the device.

### Cross-browser Compatability

#### Desired Result

Display correctly in any browser users are likely to use.

#### Steps Taken to Ensure Result

Tested site on the following browsers:

- [Chrome](https://www.google.com/chrome/) - Desktop and Mobile
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) - Desktop and Mobile
- [Opera](https://www.opera.com/) - Dekstop and Mobile
- [Safari](https://www.safari.com/) - Desktop and Mobile
- [DuckDuckGo](https://duckduckgo.com) - Mobile

#### Verdict

No obvious bugs were detected in any of the tested browsers. :heavy_check_mark:

### Behaviour of Shared Site Components

#### Preloader

- Indeterminate time loading bar from materialize displays a the top of the page when page is loading and disappears when correct information has all loaded

#### Navbar (Navigation Bar)

- Click on Home, App Logo, Sign in and Sign Up navigation links to confirm correct redirection to the correct pages :heavy_check_mark:
- Hover display when cursor is above nav link :heavy_check_mark:
- Burger menu icon displays on small and medium sized screens :heavy_check_mark:
- Clicking Burger icon triggers visibility of the side navigation menu for small and medium sized screens :heavy_check_mark:
- Verify that the the appropriate navigation bar is displayed :heavy_check_mark:

#### Footer

- Social Media icons display for twitter, instagram and facebook.  Clicking these takes user to the appropriate site :heavy_check_mark:
- Copyright information displays in the bottom left and contact link displays in the bottom right :heavy_check_mark:

#### Vertical Sidenav for user admin

- Displays on larger screens functions, 'change user password', 'edit usder data' and 'logout' :heavy_check_mark:
- Clicking on 'change user password', 'edit user data' takes you to the correct screen :heavy_check_mark:
- Clicking logout takes user back to the index/splash page and logs them out.  Feedback is provided to user via a message :heavy_check_mark:
- Burger icon displays on smaller screens to give access to user admin functions, 'change user password', 'edit user data' and 'logout' :heavy_check_mark:
- Hovering over Vertical sidenav elements on larger screens provides user feedback :heavy_check_mark:

#### Profile navbar (green)

- Displays on all screens when user is logged in :heavy_check_mark:
- Displays 'my recipes', 'browse' and 'search' functions and clicking on these take you to the correct page :heavy_check_mark:
- Hovering over green 'profile' navbar options provides user feedback :heavy_check_mark:
- Current screen green 'profile' navbar option is highlighted :heavy_check_mark:


### Behaviour of App Pages

#### Index/splash page (index.html)

- UX information to introduce new users to the site displays correctly :heavy_check_mark:
- Top 3 most popular recipes display in order with most 'likes' at the top :heavy_check_mark:
- View recipe link works correctly and takes user to the correct page :heavy_check_mark:
- Feedback to user generated when hovering over view recipe link :heavy_check_mark:
- Register button displays and when clicked takes user to Registration page :heavy_check_mark:
- Feedback to user generated when hovering over Register button :heavy_check_mark:

#### Sign in (login) page (signin.html)

- Header text displays :heavy_check_mark:
- Username and password inputs display and go red if not filled in as they are required :heavy_check_mark:
- Submit button displays and clicking proceeds with log in :heavy_check_mark:
- Invite to register for new users displays with 'here' changing colour on hover :heavy_check_mark:
- If there are any issues the user is provided with feedback via a flash message

#### Sign up (register) page (signup.html)

- Header text displays :heavy_check_mark:
- Username, email, password and confirm password inputs display and go red if not filled in as they are required :heavy_check_mark:
- Submit button displays and clicking proceeds with registration :heavy_check_mark:
- If there are any issues the user is provided with feedback via a flash message :heavy_check_mark:

#### Change password page (change_password.html)

- Header text displays with personalised user information :heavy_check_mark:
- Old password, new password and confirm password inputs display and go red if not filled in as they are required :heavy_check_mark:
- Cancel button displays and clicking takes customer back to profile without taking any action :heavy_check_mark:
- Submit button displays and clicking proceeds with password change.  User feedback is provided that the password has been changed when the user is directed back to the profile page :heavy_check_mark:

#### Edit User Data page (edit_user.html)

- Header text displays :heavy_check_mark:
- Username and email inputs display.  They are pre-populated with current user information and go red if not filled in as they are required :heavy_check_mark:
- Cancel button displays and clicking takes customer back to profile without taking any action :heavy_check_mark:
- Submit button displays and clicking proceeds with edit of data.  User feedback is provided that the information has been changed when the user is directed back to the profile page :heavy_check_mark:

#### Profile page (profile.html)

- If user has just logged in 'login successful' displayed :heavy_check_mark:
- Personalised greeting for user displays with instructions on how to use page :heavy_check_mark:
- If user has no recipes message is displayed inviting them to add recipe :heavy_check_mark:
- Add recipe button displays and hovering over it provides information on what clicking the button does :heavy_check_mark:
- If user has recipes uploaded to database they display in card form in order with the newest at the top.  User can scroll down to access older recipes :heavy_check_mark:
- If the user has provided a picture URL is displays the picture in the recipe card if not it uses a static image not displayed picture :heavy_check_mark:
- A description of the recipe and the number of likes it has are displayed :heavy_check_mark:
- View recipe and edit recipe links display in the recipe card.  Clicking the links displays the correct page.  Hovering over the links provides user feedback  :heavy_check_mark:

#### Browse page (browse.html)

- Instructions on how to use page display at the top :heavy_check_mark:
- Add recipe button displays and hovering over it provides information on what clicking the button does :heavy_check_mark:
- Sort by buttons 'Newest' and 'Likes' display.  'Newest' is highlighted as the default which displays the recipes in date order descending with the newest at the top :heavy_check_mark:
- Clicking 'likes' sort the recipes in descending order and those with the most likes are at the top :heavy_check_mark:
- All recipes uploaded to database they display in card form.  The user and scroll down to view recipes :heavy_check_mark:
- Picture URL is displays the picture in the recipe card if not it uses a static image not displayed picture :heavy_check_mark:
- A description of the recipe, the number of likes it has and who created it are displayed :heavy_check_mark:
- In the recipe card, view recipe is displayed for all users and edit recipe is displayed if the current user created the recipe.  Clicking the links displays the correct page.  Hovering over the links provides user feedback  :heavy_check_mark:

#### Search page (search.html)

- Instructions on how to use page display at the top :heavy_check_mark:
- Search input displays and goes red if not filled in as it is required :heavy_check_mark:
- Submit button displays and clicking proceeds with search :heavy_check_mark:
- If search is successful a message displays informing the user and recipes are displayed in the same format as on the browse page.  User can use the form to search again :heavy_check_mark:
- If search is unsuccessful a message displays informing the user and they can use the form to search again.  Message invites them to do so :heavy_check_mark:

#### View recipe page (view_recipe.html)

- Picture URL is displays the picture in the recipe card if not it uses a static image not displayed picture :heavy_check_mark:
- A description of the recipe, its type, the number of likes it has, whether the current user likes it and who created it are displayed :heavy_check_mark:
- The ingredients and method steps are displayed below other recipe elements :heavy_check_mark:
- Back button is displayed and clicking it takes the user back to the profile page :heavy_check_mark:
- Floating action button is displayed in the bottom right corner and hovering over it (clicking on smaller screens) provides the user with options to click.  Hovering over the option will tell the user what the button does :heavy_check_mark:
- From the floating action button the user can edit the current recipe, like the current recipe, add a new recipe or delete the current recipe :heavy_check_mark:
- Clicking add or edit from the floating action button takes the user to the crrrect screen :heavy_check_mark:
- Clicking like from the floating action button keeps them on the view page and increases the number of likes the recipe has.  Clicking like again will unlike the recipe and user will be provided with feedback telling them this if they hover over the button.  Like button also displays lighter when current user likes the recipe :heavy_check_mark:

#### Add recipe page (add_recipe.html)

- Header text displays :heavy_check_mark:
- Recipe type input displays and go red if not filled in as it is required.  Options are called from the recipe type database :heavy_check_mark:
- Name, description, ingredients and method steps inputs display and go red if not filled in as they are required :heavy_check_mark:
- Picture input can be left blank or URL for an uploaded picture can be entered in the correct format :heavy_check_mark:
- Instructions on how to upload a picture to a 3rd party resource are included and clicking the link takes the user to a site where they can obtain an appropriate file from a picture they upload :heavy_check_mark:
- Add buttons for ingredient and step are displayed if user wants to increase the number of these elements dynamically :heavy_check_mark:
- Remove buttons for ingredient and step are displayed if user wants to decrease the number of these elements dynamically :heavy_check_mark:
- Submit button displays and clicking proceeds with adding recipe.  User feedback is provided that it has been successful when they are routed to the profile page :heavy_check_mark:
- Cancel button displays and clicking takes customer back to profile without taking any action :heavy_check_mark:

#### Edit recipe page (edit_recipe.html)

- Header text displays :heavy_check_mark:
- All inputs pre-populated with information from the database for the current fields :heavy_check_mark:
- Information displays in the same way as above for the add recipe funtion including add and remove buttons for ingredients and method steps :heavy_check_mark:
- Remove buttons for ingredient and step are displayed if user wants to decrease the number of these elements dynamically :heavy_check_mark:
- Submit button displays and clicking proceeds with editing recipe.  User feedback is provided that it has been successful when they are routed to the profile page :heavy_check_mark:
- Cancel button displays and clicking takes customer back to profile without taking any action :heavy_check_mark:

#### Contact page (contact.html)

- Header text displays :heavy_check_mark:
- Name, email, password and query inputs display and go red if not filled in as they are required :heavy_check_mark:
- Submit button displays and clicking proceeds with sending contact email to the app admin.  Users are routed back to the profile screen and provided with feedback that their request has been sent :heavy_check_mark:

#### Error pages (403.html, 404.html, 405.html, 500.html)

- Error message displays with error type :heavy_check_mark:
- User can still use nav elements within the app :heavy_check_mark:

### Debugging information


|   Bug	|  Fix	|
|-------|-------|
| Not connecting to database to show user info | correct database not used in MongoURI.  Updated.
| Not displaying recipe type names in add recipe page | incorrect syntax when attempting to call type name from database
| Not redirecting to profile page correctly after adding recipe | redirect syntax not in the correct format to read session cookie data
| Showing edit and delete recipe buttons on browse page for all users | added if statement checking if user in recipe database is user in session
| Recipe link options displaying in a disjointed way on small screens | removed right align class and now they appear more uniform|
| User delete function works on my recipes page but not on browse page | user variable being used was for user was 'session.user' which did not access the database for the user so no database actions could be completed.  Had to refactor the routes using this variable to call the database.
| Error page brought up when edit recipe was clicked after going back to profile in home  | same issue as previous bug and same fix
| Previous user variable fix only worked for user delete function but broke edit recipe function | Changed back to session user variable for edit recipe and delete recipe
| Delete user function didn't work correctly again | I had moved the modal for this to base.html which created an error when routing to signin.html as the user variable was not define.   I moved the modal content to profile.html and browse.html and this fixed the issue.  Now routes correctly back to signin page after user is deleted.
| Delete recipe modals where only coming up for one recipe even when button was clicked for other recipes | appears to be an issue with materialize modals.  have deleted this modal for the moment as this is a short term fix for this bug
| When user was edited the profile screen did not display any recipes | I was using the database user as the variable for the profile instead of the session user so the jinja tmeplate was not calling the correct information from the database
| On add recipe screen there was whitespace present in the recipe description textarea | put the html tag on one line which fixed issue
| Change password function does not upadte database when both new passwords match | new_password id not called correcly as there was a rouge space
| Add ingredient and remove ingredient buttons weren't working on edit recipe screen | had a class name wrong so the javascript function wasn't calling correctly
| When like/unlike button is clicked by user it continues to decrement below zero | The likes database was not being called accurately with both user data and recipe data resulting in errors
| Browse, view recipe and profile pages did not display recipe information in a user friendly manner on all devices | refactored code and simplfied
| Side nav in all pages which display has been moved while putting splash page in.  It does not show correctly at the side of the page as it should.  It is currently in 1 line at the top | changed div row and column structure until I got the layout i was looking for
| Emails not working correctly when contact form was submitted | Had to allow gmail to use less secure apps and enable 'display unlock captcha' in settings

### Automated testing

#### W3C HTML Validation

Raw code from the following pages were run through w3c HTML validator without any errors or warnings:

- Index page
- Main profile page
- Browse page
- Add recipe page
- Search page
- Edit recipe page
- View recipe page
- Sign in page
- Sign up page
- Change password
- Edit user data
- Contact form

#### W3C CSS Validation

Custom static CSS file run through w3c CSS validator without any issues.

#### Google Lighthouse Testing information

PDFs of expanded Google Lighthouse testing for Performance, Accessability, Best Practices and Search Engine Optimisation can be found [here](https://github.com/markj0hnst0n/LeMunch/tree/master/testing/google-lighthouse-testing)