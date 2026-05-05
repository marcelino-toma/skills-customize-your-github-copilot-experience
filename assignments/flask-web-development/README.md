# 📘 Assignment: Flask Web Development

## 🎯 Objective

Build an interactive web application using Flask to understand how web frameworks work. You'll create routes, templates, and handle user input through HTML forms to create a simple task manager application.

## 📝 Tasks

### 🛠️ Set Up Flask and Create Basic Routes

#### Description
Initialize a Flask application with basic routes that return HTML pages to the user.

#### Requirements
Completed program should:

- Import `Flask` and create a Flask application instance
- Define a root route (`/`) that returns an HTML welcome page
- Define a `/tasks` route that displays a list of tasks
- Use `render_template()` to serve HTML files from a `templates/` folder
- Tasks can be stored as a Python list in the application

### 🛠️ Create HTML Templates and Static Styling

#### Description
Design HTML templates and CSS styling to make the web application user-friendly and visually appealing.

#### Requirements
Completed program should:

- Create a base template with consistent navigation and styling
- Create a tasks page template that displays tasks in a readable format (list or table)
- Add a `style.css` file with basic styling (colors, fonts, layout)
- Use template variables to dynamically display tasks from your Python list

### 🛠️ Add Form Handling to Create New Tasks

#### Description
Implement a form that allows users to add new tasks to the list through the web interface.

#### Requirements
Completed program should:

- Create an HTML form on the tasks page with an input field for task descriptions
- Use a POST route (`/add-task`) to handle form submissions
- Add the new task to the tasks list and redirect back to `/tasks`
- Display confirmation or validation messages when tasks are added
- Example input: "Buy groceries" → displays as a new item in the task list

### 🛠️ Add Delete Functionality (Stretch Goal)

#### Description
Allow users to remove tasks from the list by clicking a delete button.

#### Requirements
Completed program should:

- Add a delete button or link next to each task
- Create a route that removes a task when clicked
- Update the task list and refresh the page
- Provide user feedback when a task is deleted
