## Testing

Manual testing was used to test navigation, responsiveness on different screen sizes and database operations (Create, Read, Update and Delete).

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

Le Munch adapts to all tested screen sizes and devices and displays as expected. :heavy_check_mark:

### Cross-browser Compatability

#### Desired Result

Display correctly in any browser users are likely to use.

#### Steps Taken to Ensure Result

A a range of browsers were used to test the site, and where I did not have access to it - such as Safari - I borrowed Apple devices to test for potential bugs.

Browsers tested include:

- [Chrome](https://www.google.com/chrome/) - Desktop and Mobile
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) - Desktop and Mobile
- [Opera](https://www.opera.com/) - Dekstop and Mobile
- [Safari](https://www.safari.com/) - Desktop and Mobile
- [DuckDuckGo](https://duckduckgo.com) - Mobile

#### Verdict

No obvious bugs were detected in any of the tested browsers. :heavy_check_mark:

### Behaviour of Shared Site Components

#### Navbar (Navigation Bar)

- Click on Home, App Logo, Sign in and Sign Up navigation links to confirm correct redirection to the correct pages :heavy_check_mark:
- Hover display when cursor is above nav link :heavy_check_mark:
- Burger menu icon displays on small and medium sized screens :heavy_check_mark:
- Clicking Burger icon triggers visibility of the side navigation menu for small and medium sized screens :heavy_check_mark:
- Verify that the the appropriate navigation bar is displayed :heavy_check_mark:

#### Footer

- Social Media icons display for twitter, instagram and facebook.  Clicking these takes user to the appropriate site :heavy_check_mark:
- Copyright information displays in the bottom left and contact link displays in the bottom right :heavy_check_mark:
- Register button displays and when clicked takes user to Registration page :heavy_check_mark:

### Behaviour of App Pages

#### Index/splash page (index.html)

- UX information to introduce new users to the site displays correctly :heavy_check_mark:
- Top 3 most popular recipes display in order with most 'likes' at the top :heavy_check_mark:
- View recipe link works correctly and takes user to the correct page :heavy_check_mark:
- Feedback to user generated when hovering over view recipe link :heavy_check_mark:
- Register button displays and when clicked takes user to Registration page :heavy_check_mark:
- Feedback to user generated when hovering over Register button :heavy_check_mark:



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