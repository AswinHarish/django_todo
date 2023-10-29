# TODO App with Django for CS50x

#### Description:
This project is a simple todo application developed using Django for the CS50x course. The application allows users to manage their daily tasks by adding, updating, and deleting them. The primary goal of this project is to demonstrate the capabilities of Django in creating web applications efficiently and effectively.

## Project Structure:

### `todo_app/`
The root directory of the project.

- **`django_todo/`**:
    Contains configuration and initialization files for the Django project.

    - **`base/`**:
        Houses the core logic and templates for the todo application.

        - **`migrations/`**:
            Contains Django-generated files to manage and apply changes to the database schema.

            - `0001_initial.py`: Initial migration file for setting up the database.

        - **`templates/`**:
            HTML templates used to render views in the web application.

            - **`base/`**:
                A subdirectory for base templates.

                - `login.html`: Template for the login page.
                - `main.html`: The main template that other templates inherit from.
                - `register.html`: Template for the registration page.
                - `task_confirm_delete.html`: Template to confirm the deletion of a task.
                - `task_form.html`: Template for adding and updating tasks.
                - `task_list.html`: Template to display the list of tasks.

        - `admin.py`: Configuration for Django's admin panel.
        - `apps.py`: Application specific configurations.
        - `models.py`: Defines the data models for the application.
        - `tests.py`: Contains unit tests for the application.
        - `urls.py`: URL configurations for the application views.
        - `views.py`: Contains the view logic and handlers for the application.

    - **`todo_app/`**:
        Contains initialization files for the project.

        - `asgi.py`: ASGI compatible entry point for the project.
        - `settings.py`: Contains settings/configuration for the Django project.
        - `urls.py`: Main URL configurations for the project.
        - `wsgi.py`: WSGI compatible entry point for the project.

- `db.sqlite3`: SQLite database file for the project.
- `manage.py`: A command-line tool for administrative tasks.

- `requirements.txt`: Contains a list of all the dependencies and libraries required to run the project.


## Files and Implementations:

## `manage.py`:

This is Django's command-line utility for administrative tasks. It is used to run various management commands for this Django project.

- `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')`: Sets the Django settings module to 'todo_app.settings'.

- The script tries to import Django's core management module and execute management commands.

- If Django is not imported successfully, an error message is raised, indicating potential issues with Django installation or the Python environment.

- The script checks if it's the main entry point for execution and runs administrative tasks based on the command-line arguments.

This script serves as the entry point for various administrative tasks such as running the development server, performing database migrations, and more for this Django project.


## `views.py`:

This file contains the main functionalities for our TODO app. Here's a breakdown of the classes and their functionalities:

- **CustomLoginView**: Allows users to log in using the default Django authentication. It uses the `login.html` template to render the login page and redirects authenticated users to the task page.

- **RegisterPage**: This view supports user registration. It makes use of Django's `UserCreationForm` to manage user sign-ups and log in the user once the registration is successful. If the user is already authenticated, they are redirected to the tasks page.

- **TaskList**: Lists all the tasks associated with the logged-in user. There's an added functionality to filter tasks based on their completion status. Users can also search for specific tasks by providing a keyword in the 'search-area'.

- **TaskCreate**: Enables the user to create a new task. The user needs to provide details like title, description, and completion status. Once the task is created, it's associated with the logged-in user.

- **TaskUpdate**: Provides functionality to update the details of an existing task, including the title, description, and completion status.

- **Delete**: As the name suggests, it lets users delete a task. Post deletion, users are redirected to the main tasks page.


## `models.py`:

This file defines the data structure of our application.

### **Task**:
The primary model for our app. Here's a breakdown of its fields:

- **user**: A foreign key relation to Django's built-in User model. This ensures that each task is associated with a user.

- **title**: A character field with a maximum length of 200 characters. It stores the title of the task.

- **description**: A text field to provide additional details or description for the task. It's optional.

- **complete**: A boolean field indicating whether a task is completed or not. By default, when a task is created, it's set to False.

- **created**: A datetime field that automatically captures the date and time when a task is created.


## `urls.py`:

This file defines the routing and the endpoints for our application.

- **Login**: Path `login/` is associated with the `CustomLoginView`. This view manages the authentication process for users.

- **Logout**: Path `logout/` uses Django's built-in `LogoutView`. After logging out, users are redirected to the login page.

- **Register**: Path `register/` is mapped to `RegisterPage`. This view handles the user registration process.

- **Tasks List**: The root path (`''`) lists all the tasks for the authenticated user using the `TaskList` view.

- **Task Creation**: Path `create/` allows users to create a new task using the `TaskCreate` view.

- **Task Update**: Path `task/<int:pk>/` is designed for updating existing tasks. It employs the `TaskUpdate` view and requires an integer primary key to identify the task.

- **Task Deletion**: Path `delete/<int:pk>/` is used to delete a task. Like the update view, it requires an integer primary key and is associated with the `Delete` view.


## `apps.py`:

This file is responsible for the configuration of the application.

### `BaseConfig` class:

- **`default_auto_field`**: Specifies the type of auto-created primary key field. In this case, it's set to `'django.db.models.BigAutoField'`.

- **`name`**: Indicates the name of the application. It's set to `'base'`.


## `admin.py`:

This file facilitates the integration of the application's models with Django's built-in admin interface.

### Models registered:

- **`Task`**: The `Task` model from the `models.py` file is registered with the admin site. This enables management of task entries directly through the Django admin dashboard.


## `db.sqlite3`:

This file is the SQLite database used by this Django application. It stores data and records related to this application, including tasks and user information. SQLite is a lightweight and serverless database engine often used during development. While convenient for testing and development, it's recommended to switch to a more robust database system (e.g., PostgreSQL, MySQL) for production deployments.


## `base/templates/main.html`:

- `<!DOCTYPE html>`: Declares the document type and version.
- `<html>`: The root element of the HTML document.
  - `<head>`: Contains metadata and links to external resources.
    - `<meta>`: Sets the character encoding and viewport settings.
    - `<title>`: Defines the title of the web page.
    - `<link>`: Imports external fonts from Google Fonts.
  - `<body>`: The main content of the web page.
    - `<div class="container">`: A container that wraps the content of the web page. It provides consistent styling for this application.

## Styles and Design

- CSS styles are embedded in the `<style>` block within the `<head>`. These styles define the layout and appearance of the entire web page.

- The background color, font family, and padding are defined for the `<body>`. Custom fonts are linked from Google Fonts.

- Specific font styles for headings, links, and paragraphs are set using CSS classes.

- The page layout includes a header bar with a gradient background, providing a consistent design element.

- Task items are displayed in a list with alternating background colors and appropriate styling for titles and completion icons.

- Delete links for tasks are styled with a distinctive font, size, and color.

- Form elements, including text inputs, labels, and buttons, have consistent styling for user input.

## Content and Dynamic Elements

- The content of specific pages within app is inserted within the `{% block content %}` and `{% endblock content %}` tags. This structure allows for content inheritance in child templates.

## Design Choices

- The design aims for a clean and modern look with attention to detail, including the use of gradients, custom fonts, and consistent styling for various elements.

- The use of CSS classes like `.task-complete-icon` and `.task-incomplete-icon` allows for clear differentiation between completed and incomplete tasks.

- The "SignUp" button in the child template is styled using the `.button` class defined in the base template.


## `base/templates/login.html`:

This template is designed for user authentication in application.

### Structure:

- **Extension**: The template extends `base/main.html` which likely contains the foundational layout and structure for this application's templates.

- **Header**: There's a header section with the title "Login".

- **Login Form**:
  - Method: The form employs the POST method to submit login data.
  - CSRF Token: The `{% csrf_token %}` tag is included to ensure security during form submission in Django.
  - Form Fields: Django form fields are rendered using `{{form.as_p}}`, which displays the form fields wrapped in paragraph tags.
  - Submit Button: The form contains a styled submit button with the value "Login".

- **SignUp Link**: Beneath the form, there's a link allowing users to navigate to the SignUp page if they don't have an account.


## `base/templates/register.html`:

This HTML file is a template for the registration page in Django TODO app. It extends the `base/main.html` template and provides the content specific to user registration. Below is a breakdown of its structure and elements:


- `{% extends 'base/main.html' %}`: This line specifies that this template extends the `base/main.html` template, inheriting its structure and styles.

- `<div class="header-bar">`: A header bar with the title "SignUp."

- `<div class="card-body">`: This section contains the registration form and additional links.

- `<form method="POST">`: A form element with the HTTP POST method for submitting user registration data.

- `{% csrf_token %}`: A security token to prevent Cross-Site Request Forgery (CSRF) attacks.

- Labels and form fields: The form includes labels and input fields for the user's username and password.

- `<input class="button" type="submit" value="SignUp">`: A button element for submitting the registration form.

- `<a href="{% url 'login' %}">Login</a>`: A link that redirects users to the login page.


## `base/templates/task_confirm_delete.html`:
- This HTML template is designed to provide users with a confirmation page for deleting tasks in the Django TODO app.
- It displays a message asking if the user is sure they want to delete a specific task and provides a "Delete" button for confirmation.


## `base/templates/task_form.html`:

This HTML file is a template for a form used in this Django TODO app for creating or updating tasks. It extends the `base/main.html` template and provides the content for inputting task details. Below is an overview of its structure and elements:


- The design of the form page follows the styling provided by the base template (`base/main.html`).

- The "Back" link in the header bar is styled as a button, allowing users to return to the tasks page.

- The form fields and the "Submit" button are styled consistently using the `.button` class defined in the base template.

This template provides the structure and design for the form used in this Django TODO app for creating and updating tasks, ensuring a uniform and user-friendly interface.



## `base/templates/task_list.html`:

This HTML file is a template for displaying tasks in this Django TODO app. It includes user information, task listing, and navigation options.

- User information and login/logout links are displayed in the header.
- Users can search for tasks and add new tasks.
- Tasks are listed with completion status, and users can delete tasks.


## `migrations/0001_initial.py`:

This migration file was generated by Django 4.2.5 on 2023-10-17 and defines the initial database schema for the TODO app. It creates the `Task` model with the following fields:

- `title`: A character field with a maximum length of 200 characters.
- `description`: A text field that can be blank or null.
- `complete`: A boolean field with a default value of `False`.
- `created`: A date and time field with auto-creation on each entry.
- `user`: A foreign key field related to the user model defined in the Django settings.

The `Task` model is ordered by the `complete` field, and the migration file represents the initial database structure for this application.

## `todo_app/asgi.py`:

This ASGI (Asynchronous Server Gateway Interface) configuration file is part of the `todo_app` project. It exposes the ASGI callable as a module-level variable named `application`.

- The `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')` line sets the Django settings module to `todo_app.settings`.

- The `get_asgi_application` function from `django.core.asgi` is used to get the ASGI application.

This file is responsible for configuring the ASGI application for this Django project, allowing it to handle asynchronous requests and connections.


## `todo_app/settings.py`:

This Django settings file is used for the `todo_app` project, and it was generated by 'django-admin startproject' using Django 4.0.4. It contains various configurations for this Django application. Below is an overview of some key settings:

- `SECRET_KEY`: A secret key used for security. It should be kept secret in production.

- `DEBUG`: Set to `True` for development, but should be `False` in production for security.

- `ALLOWED_HOSTS`: Specifies which hosts are allowed to access this application.

- `INSTALLED_APPS`: Lists the installed applications, including Django's core apps and this app named `base`.

- `MIDDLEWARE`: Defines the middleware classes used by this application.

- `ROOT_URLCONF`: Specifies the URL configuration for this project.

- `TEMPLATES`: Configures how templates are loaded and processed.

- `WSGI_APPLICATION`: Specifies the WSGI application for serving this Django application.

- `DATABASES`: Configures the default database connection.

- `AUTH_PASSWORD_VALIDATORS`: Defines password validation rules.

- `LANGUAGE_CODE` and `TIME_ZONE`: Define internationalization and time zone settings.

- `USE_I18N` and `USE_TZ`: Control internationalization and time zone support.

- `LOGIN_URL`: Specifies the URL for login redirection.

- `STATIC_URL`: Defines the URL for serving static files.

- `DEFAULT_AUTO_FIELD`: Configures the default primary key field type.

This file contains a range of settings that control various aspects of this Django application. Careful configuration is essential to ensure this application functions as expected.


## `todo_app/urls.py`:

This URL configuration file for the `todo_app` project is responsible for routing URLs to views. It includes a simple structure:

- `path('admin/', admin.site.urls)`: Routes requests to the Django admin site.

- `path('', include('base.urls'))`: Includes URLs defined in the `base` app.

This file defines how incoming requests are mapped to views, allowing this Django application to handle various URLs and direct them to the appropriate views.


## `todo_app/wsgi.py`:

This WSGI (Web Server Gateway Interface) configuration file is part of the `todo_app` project. It exposes the WSGI callable as a module-level variable named `application`.

- The `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')` line sets the Django settings module to `todo_app.settings`.

- The `get_wsgi_application` function from `django.core.wsgi` is used to get the WSGI application.

- The `app = application` line assigns the WSGI application to the `app` variable.

This file is responsible for configuring the WSGI application for this Django project, allowing it to communicate with web servers and serve this web application.


## `requirements.txt`:

This file lists the Python packages and their versions required for this Django project. These packages are essential for this project to run successfully. The versions specified ensure compatibility.

- `asgiref==3.7.2`: ASGI (Asynchronous Server Gateway Interface) framework for Django.
- `Django==4.2.5`: The Django web framework used for building this project.
- `sqlparse==0.4.4`: A SQL parsing library for Python.
- `typing_extensions==4.8.0`: A library providing additional type hints for Python.
- `tzdata==2023.3`: Time zone data library for Python.

These packages are used to provide essential functionality for this Django project and should be installed to ensure the project runs correctly.


## Design Choices:
During the development of this project, several design choices were made to ensure the application is user-friendly and efficient.

This project has been a valuable learning experience, showcasing the capabilities of Django in building robust web applications.
