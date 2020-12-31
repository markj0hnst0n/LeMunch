<div align="center">
<h1>Le Munch</h1>
</div>

![]()

Le Munch is here to help you decide what to have for your next meal!  You can upload your own recipes so you have your own online cookbook and
search and browse through other users recipes to give you ideas of what to cook.  Develop your love of food by deep diving on food pics and 
connecting with other users through the recipes they've uploaded.

To go to the live site click [here](http://le-munch-flask-markjohnston.herokuapp.com/)


# UX

## Conceptual Database Design

![](readme/images/conceptual-database-design.png)

## Logical Data Model

![](readme/images/logical-data-model.png)

## User Stories

There will be 2 main user types and the user types are not mutually exclusive.  The same user could fall into both categories dependent on the their behaviour.

The uploader user will be the primary content creators and will produce the recipes for the site.  Their goal is to show off what they can do and see how popular their recipes are.

- As an uploader user I want to upload a recipe so that other users can see if for inspiration about their own meals and so that I have a record for my online cookbook.

- As an uploader user I want functionality to upload a photo to so that users are enticed to read my recipes.

- As an uploader userI want to be able to edit and delete recipes so that I can customise my online cookbook to suit my ongoing needs.

- As an uploader user I want other users to be able to ‘upvote’ or ‘like’ my recipes so that I can understand how popular they are.

- As an uploader user I want to be able to add, edit the type of recipe so that other users easily can browse the right category to find recipes to suit their needs.

The browser user will be mainly focused on looking at recipe pictures and recipe content.  They can give their approval to recipes through ‘likes’ or ‘upvotes’ and are mainly there to find inspiration for what to cook or look at nice food pictures.

- As a browser user I want to be able to browse by recipes ranked by likes so that I can see the most popular recipes to get inspiration about what to cook.

- As a browser user I want to be able to browse other users so that I can see who is creating the most popular recipes to get inspiration about what to cook.

- As a browser user I want to be able to search other users so that I can look up my favourite users.

- As a browser user I want to be able to search by recipes so that I can find my favourite recipes to see how other cooks do them.

Site owner goal

- As site owner I want to create a welcome space for users to connect over food and develop their love of cooking.

See separate Testing.md file for information on how these user stories were tested [here](testing/testing.md)

## Wireframes

Basic wireframes for this project were created using Balsamiq and you can find a link to the balsamiq project file (right click on the button and save file) [here](!)

[Wireframes Pictures Repository](!)

## Colour Scheme

An explantion fof the colour scheme will go here.

[Coolors](https://coolors.co/)


### Features

#### Navbar

- Easily navigate the website via the navbar

#### Sign up or Login

- Sign Up / Sign In to the website so that a unique user is created or their unique profile is added

#### Edit Profile

- Edit user info

#### Profile page

- Use the tabs to navigate easily once a user is logged in

#### Recipe upload

- Add/upload recipes

#### Browse

- Browse my recipes and recipes of other users.  Sorting by number of likes or unsorted.  Also browse users.

#### Search function

- Search for my favourite recipe

#### Like/Upvote

- Upvote/like recipe.  Each user can only like a recipe once.



# Technologies Used

[HTML5](https://en.wikipedia.org/wiki/HTML5)
for the structure of the website

[CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
for the look of the website

[Materialize](https://materializecss.com/) website framework with html, css and javascript.

[Fontawesome](https://fontawesome.com/) for icons.

[Javascript](https://en.wikipedia.org/wiki/JavaScript)
for the logic of the game.  To manipulate the HTML and CSS on the screen.

[jQuery](https://en.wikipedia.org/wiki/JQuery)
To manipulate the HTML and CSS on the screen.

[JShint](https://jshint.com/)
To validate javscript code.

[Coolors](https://coolors.co/)
For help with colours and colours scheme.

[Post Images](https://postimages.org/)
To allow users to upload photos and get addresses for their pictures.

[PicResize](https://picresize.com/)
For image formatting.

[Webformatter](https://webformatter.com/)
For formatting HTML, CSS and javascript code.

[Asana](https://asana.com/)
for project management

[Balsamiq Wireframes](https://balsamiq.com/wireframes/)
for creating Wireframes for initial visual development

[Gitpod](https://www.gitpod.io/) for writing and testing code.

[GitHub](https://github.com/) for storing code.

[Google Fonts](https://fonts.google.com/) for fonts used in the project.

[Google Chrome Development Tools](https://developers.google.com/web/tools/chrome-devtools) for testing code on various device sizes during development and debugging.

[Amazon Web Services](https://aws.amazon.com/)
Simple Email Service for STMP mail server

[Troy](http://troy.labs.daum.net/) to test website on different device types and sizes

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) for testing code health, accessibility, speed and search engine optimisation

# Testing

See separate Testing.md file [here](testing/testing.md)

# Deployment

## Using Heroku

step by step deployment info

## Run Locally

In the GitHub Repository from the project (#)

1. Click Clone or Download
2. Copy Git URL from the dialogue box
3. Open your developement editor of choice and open a terminal window in a directory of your choice
4. Use the 'git clone' command in terminal followed by the copied git URL
5. A clone of the project will be created locally on your machine

# Credits

## Content

Written content by Mark Johnston

## Media

Information about media used

## Influences

https://www.youtube.com/watch?v=2Zz97NVbH0U&feature=emb_logo

User Authentication via session

https://github.com/MiroslavSvec/DCD_lead

adding input fields dynamically using jquery

https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery

flask mail

https://pythonhosted.org/Flask-Mail/

debugging contact emails

https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

Preloader using javascript and css

https://www.kingsubash.com/simple-page-preloader-with-css-and-javascript

## Acknowledgements

Thanks to the following people for making the project happen:

- My Mentor 
- The [Code Institute](https://codeinstitute.net/) Slack Community.
- The [Code Institute](https://codeinstitute.net/) tutors and instructional material.  Espcially tutor Johann for his help with the like functionality.
- My Wife Joanna Johnston for her (constructive) criticism and understanding when I lock myself away in the attic for hours on end