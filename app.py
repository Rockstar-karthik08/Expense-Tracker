from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
filename = "tasks.txt"

# Load tasks from a file if it exists
def load_tasks():
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file]
    return tasks

# Save tasks to a file
def save_tasks(tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
