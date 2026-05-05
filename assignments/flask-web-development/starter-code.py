from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory task list (temporary storage)
tasks = [
    "Learn Flask fundamentals",
    "Create HTML templates",
    "Build a form to add tasks"
]

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/tasks')
def view_tasks():
    """Display all tasks"""
    return render_template('tasks.html', tasks=tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    """Handle new task submission"""
    task_description = request.form.get('task')
    if task_description:
        tasks.append(task_description)
    return redirect('/tasks')

@app.route('/delete-task/<int:index>', methods=['POST'])
def delete_task(index):
    """Delete a task by index"""
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/tasks')

if __name__ == '__main__':
    app.run(debug=True)
