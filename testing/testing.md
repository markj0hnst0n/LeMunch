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
| side nav in all pages which display has been moved while putting splash page in.  It does not show correctly at the side of the page as it should.  It is currently in 1 line at the top |