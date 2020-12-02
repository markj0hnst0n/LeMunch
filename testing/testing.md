### Debugging information


|   Bug	|  Fix	|
|-------|-------|
| Not connecting to database to show user info | correct database not used in MongoURI.  Updated.
| Not displaying recipe type names in add recipe page | incorrect syntax when attempting to call type name from database
| Not redirecting to profile page correctly after adding recipe | redirect syntax not in the correct format to read session cookie data
| Showing edit and delete recipe buttons on browse page for all users | added if statement checking if user in recipe database is user in session
| Recipe link options displaying in a disjointed way on small screens | removed right align class and now they appear more uniform|
| User delete function works on my recipes page but not on browse page |