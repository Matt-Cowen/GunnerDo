<h1> Gunner Do </h1>

## UX
The UX was developed with the target user in mind. The target is a wide net, and as such the UX had to be accessible and attractive to a wide range of user.

The users will be looking for:

An easy to navigate site, with clear signposting for browsing, uploading and saving recipes
The ability to sign up to add and save recipes.
The ability to collect recipes that they like into their own dedicated recipe book.
the ability to edit and recipes that they have submitted.
The site admin will be looking for:

an easy and intuitive way of managing content and users on the site.

## Scope
Site Features
1. Navigation Bar
The navigation bar appears on every page so users can easily navigate through the site. It adds an active class to the current url for better UX.
Navigation bar has links for "Home", "Recipe Library", "Register" and "Login" when there is no logged in user.
Navigation bar has links for "Home", "Recipe Library", "My Recipe Boook", "Add Recipe" and "Logout" when a user is logged in.
If the user is logged in then their username will appear on the right hand side of the nav bar.
The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size.

2. Footer
The footer, present on all pages, comprises of copyright information on the left hand side, and social links on the right.

3. Landing Page
The landing page offers a simple hero section with a call to action to either start viewing recipes (available to both logged in and non-registered users) or to sign up (only displays if user is not logged in).

## Wireframes
## Database Schema

Before I set to migrating any models to my database, I created an entity relationship diagram to help me see how the models would link together.
The entity relationship diagrams were created using dbdiagram.io.

### ERD

![ERD](/media/ERD%20GunnerDo.png)

## Testing

### Code Validation
#### HTML
#### CSS
#### JS

### Manual Testing 
All responsiveness and basic functionality of the site was tested manually, and ran into no issues.

## Deployment
The site was deployed on Heroku and connected to GitHub for version control. This was done by following the below steps:

Log in to GitHub and create a new repository, using the Code Institute template.

Sign up for Heroku and create a new account.

Create a new app and choose a suitable region for deployment.

In the app settings, go to config vars and click "reveal config vars".

The app requires configuration for the following variables: SECRET_KEY, DATABASE_URL, CLOUDINARY_URL. Assign the corresponding values from your project's env.py to these variables.

Integrate Heroku with your GitHub by choosing the GitHub integration option in Heroku.

Locate and select the GitHub repository you created earlier from the CI template.

Choose manual deployment from the selected branch of your GitHub repository.

Deploy by clicking the manual deploy button.

Once deployed, the site is accessible through the live link provided at the top of the document.

## Technologies Used
#### Languages:
- HTML5
- CSS3
- JavaScript
- Python
#### Frameworks, Libraries and Programs:
- GitHub - GitHub is a web-based platform for version control using Git, enabling collaborative software development and hosting of code repositories. GitHub connects to GitPod and - - Heroku.
- GitPod - Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository.
- Heroku - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilized/tested.
- Django - Django is a high-level web framework for building web applications rapidly with a clean and pragmatic design.
- ElephantSQL - ElephantSQL is a hosted PostgreSQL database service that can be seamlessly integrated with Django applications, providing scalable and reliable database solutions.
- Gunicorn - Gunicorn is a pure-Python HTTP server for WSGI applications.
- Dj Database URL - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- Bootstrap - Bootstrap is a front-end framework for developing responsive and mobile-first websites quickly and efficiently.
- Cloudinary - Cloudinary is a cloud-based media management platform that offers solutions for storing, optimizing, and delivering images and videos for web and mobile applications.
- Psycopg2 - Psycopg is a PostgreSQL adapter for the Python programming language, providing a robust and efficient interface to interact with PostgreSQL databases.
- Summernote - Summernote is a Django app that enables users to easily integrate a rich text editor into their web applications, enhancing event creation and description functionality.
- Django-allauth - A comprehensive authentication app for Django, supporting social authentication, registration, and account management.
- Django-crispy-forms - Django Crispy Forms is a Django app that provides a better way to generate forms in your Django application.
- Whitenoise - WhiteNoise allows your web app to serve its own static files, making it simpler to deploy on services like Heroku.
- Font Awesome - Font Awesome is a library of scalable vector icons that can be easily customized and used to enhance the visual appeal of websites and applications.
- Balsamiq - Balsamiq is a wireframing tool used for creating low-fidelity mockups of user interfaces, allowing for quick and easy visualization of design ideas.
- Am I Responsive - Am I Responsive is a web tool that allows users to quickly preview how their website appears on various devices and screen sizes, helping to ensure responsiveness and compatibility across platforms.
- W3C CSS Validator - The W3C CSS Validator is a tool used to check the validity and syntax of CSS code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).
- W3C Markup Validator - The W3C Markup Validator is a tool used to check the validity and syntax of HTML code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).
- JSHint - JSHint is a static code analysis tool used for checking JavaScript code for errors, potential problems, and stylistic inconsistencies.
- Pep8ci - Pep8ci provides Python developers with a tool to check their code against the PEP 8 style guide for adherence to coding standards.

The full list of requirements for the project along with versions can be seen below.

asgiref==3.8.1

cloudinary==1.36.0 
crispy-bootstrap5==0.7

dj-database-url==0.5.0

dj3-cloudinary-storage==0.0.6

Django==4.2.7

django-allauth==0.57.0

django-bootstrap-v5==1.0.11

django-crispy-forms==2.1

django-multiselectfield==0.1.13

django-summernote==0.8.20.0

gunicorn==20.1.0

oauthlib==3.2.2

psycopg2==2.9.6

PyJWT==2.8.0

python3-openid==3.2.0

requests-oauthlib==1.3.1

sqlparse==0.5.2

urllib3==1.26.20

whitenoise==5.3.0
