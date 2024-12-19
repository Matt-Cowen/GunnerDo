<h1> Gunner Do </h1>


The goal of Gunner Do is to provide users with a dynamic, game-inspired interface that enhances productivity while keeping tasks organized. By incorporating an "Arsenal" theme, the app allows users to "Write up tactics" for their tasks and "Score" when a task is marked as completed, turning everyday tasks into a more engaging, goal-oriented experience. The design is focused on offering a fun, gamified approach to task management, motivating users to complete their goals through visual rewards and engaging features.

## UX
The UX was developed with the target user in mind. The target is a wide net, and as such the UX had to be accessible and attractive to a wide range of user.

User Story 1: 
User Registration and Login
As a user, I want to create an account and log in so that I can save my tasks and access them from any device.
Acceptance Criteria:
- A "Sign Up" form includes fields for username, email, and password.
- 	A "Login" form requires a username/email and password.
- 	Logged-in users see only their personal task list.
- 	Tasks are stored in the database and persist across sessions.

User Story 2: Add a Task
As a user, I want to add a task to my to-do list so that I can keep track of things I need to complete.
Acceptance Criteria:

- The user can input a task name into a text field.
- A "Add Task" button is present and clickable.
- After clicking the "Add Task" button:
- The new task is displayed in the task list.
- The task has a checkbox for marking it as complete.
- The input field is cleared for a new task.

User Story 3: View Tasks
As a user, I want to view all tasks in my to-do list so that I can see what needs to be done.
Acceptance Criteria:
- The website displays a list of all tasks in chronological order of creation.
- Tasks include their title and a checkbox to mark completion.
- If no tasks are present, a message is displayed (e.g., "No tasks added yet").

User Story 3: Edit a Task
As a user, I want to edit a task in my to-do list so that I can update its details.
Acceptance Criteria:
- Each task has an "Edit" button.
- Clicking the "Edit" button opens a text input pre-filled with the task's current title.
- The user can modify the task name and save the changes by clicking "Save".
-	The updated task is displayed in the list.
-	If the user cancels editing, the task remains unchanged.

User Story 4: Delete a Task
As a user, I want to delete a task from my to-do list so that I can remove tasks I no longer need to complete.
Acceptance Criteria:
-	Each task has a "Delete" button.
-	Clicking the "Delete" button removes the task from the list.
-	A confirmation message appears before deletion (e.g., "Are you sure you want to delete this task?").
-	The task is no longer displayed after deletion.

User Story 5: Mark a Task as Complete
As a user, I want to mark a task as complete so that I can track my progress.
Acceptance Criteria:
-	Each task has a checkbox next to its title.
-	Clicking the checkbox marks the task as complete:
-	The task title is visually updated (e.g., strike-through or gray text).
-	The status of the task is updated in the database.
-	Clicking the checkbox again marks the task as incomplete.


## Scope
Site Features
1. Navigation Bar

![Screenshot 2024-12-19 at 14 02 55](https://github.com/user-attachments/assets/1f71301e-37c1-4482-a871-1171312730a7)

The navigation bar appears on every page so users can easily navigate through the site. It adds an active class to the current url for better UX.
Navigation bar has links for "Home", "Tasks", "Register" and "Login" when there is no logged in user.
Navigation bar has links for "Home", "Taks" and "Logout" when a user is logged in.
If the user is logged in then their username will appear on the right hand side of the nav bar.
The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size.

3. Footer

![Screenshot 2024-12-19 at 14 03 15](https://github.com/user-attachments/assets/4913e99c-3f00-409e-9203-d9600718e2d6)

The footer, present on all pages, comprises of copyright information on the left hand side, and social links on the right.

4. Log-In Page / Register page:

![Screenshot 2024-12-19 at 14 03 49](https://github.com/user-attachments/assets/25809bad-17a7-4e0b-ac7c-db9cd7014c79)

- Gunner Do utilizes AllAuth for secure user authentication and authorization, allowing users to easily create accounts and log in to access their personalized to-do lists.


4. Task List page:

![Screenshot 2024-12-19 at 14 06 12](https://github.com/user-attachments/assets/88492c87-f143-4f6d-a83a-42c9c9835df6)


- The app is fully responsive, ensuring an optimal experience across various devices and screen sizes.
-  The app supports full CRUD (Create, Read, Update, Delete) operations, enabling users to add, view, modi
fy, and remove tasks as needed.
-  The app offers an intuitive interface that simplifies task management, with a clean design and minimal distractions for easy navigation.


## Wireframes

![Screenshot 2024-12-16 at 14 22 45](https://github.com/user-attachments/assets/6a8a8551-168d-4f42-b6dc-fc398aa83570)

![Screenshot 2024-12-19 at 13 50 02](https://github.com/user-attachments/assets/3f947c65-ffed-436b-9eae-443356be4b18)

![Screenshot 2024-12-19 at 13 49 24](https://github.com/user-attachments/assets/bb2e8b5d-d454-416c-8828-336e829243b9)

![Screenshot 2024-12-19 at 13 49 34](https://github.com/user-attachments/assets/564b00f9-edc3-495b-9b01-c0e48f8d52af)


## Database Schema

Before I set to migrating any models to my database, I created an entity relationship diagram to help me see how the models would link together.
The entity relationship diagrams were created using dbdiagram.io.

### ERD

![ERD](/media/ERD%20GunnerDo.png)

## Agile Methodology

For the development of Gunner Do, I followed an Agile methodology to ensure iterative and efficient progress throughout the project's lifecycle. A key part of this process was leveraging a Kanban board on GitHub Projects, which you can view <a> https://github.com/users/Matt-Cowen/projects/5 </a>

![Screenshot 2024-12-19 at 15 18 12](https://github.com/user-attachments/assets/19125a1d-6ab6-4a00-a16e-8cdc8fc2e87f)


To Do: This column housed tasks and user stories that had been identified but were awaiting development.

In Progress: This column tracked tasks currently being worked on.

Complete: This column lists tasks that have been finished and are awaiting for review or testing, highlighting progress and maintaining a log of completed work.

## Testing

### Code Validation
#### HTML

![Screenshot 2024-12-19 at 14 53 33](https://github.com/user-attachments/assets/75ebd2a0-b623-440d-b812-60842c93722e)

![Screenshot 2024-12-19 at 14 57 07](https://github.com/user-attachments/assets/1247f899-26ee-482a-ae36-3d1672f08d00)

#### CSS

![Screenshot 2024-12-19 at 15 07 56](https://github.com/user-attachments/assets/2cd1f29f-9eec-46e7-ae65-abb24f3f41f5)

#### JS

![Screenshot 2024-12-19 at 15 16 20](https://github.com/user-attachments/assets/28905934-1dd8-419c-9aee-34f65d2be64f)

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

# **Credits**

## **Tech Support**

- [W3Schools](https://www.w3schools.com/) - Used to help understand certain aspects of python.

- [Stack Overflow](https://stackoverflow.com/) - Used to detrmine whether other people have already figured out issues we were running into!

- [ChatGPT](https://openai.com/gpt) - Used for example text on the site and plain English explanations of particularly tricky bits of code.

- [Code Institute](https://codeinstitute.net/) - Taught me all I know, and provided the initial framework for the Recipe model, taken from the I think therefore I blog walkthrough project.

---


## **Media**

- [GoogleFonts](https://fonts.google.com/)

- [ChatGPT](https://chatgpt.com/) - ChatGPT was used to generate the logo artwork.

- [Unsplash](https://unsplash.com/) - Unsplash was used to access free license imagery.

---

### **Acknowledgements**

-Thank you to Alex for all his hard work.


