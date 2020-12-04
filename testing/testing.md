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
| delete recipe modals where only coming up for one recipe even when button was clicked for other recipes | appears to be an issue with materialize modals.  have deleted this modal for the moment as this is a short term fix for this bug