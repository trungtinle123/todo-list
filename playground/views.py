from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.http import JsonResponse
from .models import Task
import MySQLdb


def delete_row(request):
    db = MySQLdb.connect(host="localhost", user="root", password="", database="todolist")
    id = request.GET.get('id')
    if db:
        cursor = db.cursor()
        
        # Delete the row
        delete_query = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(delete_query, (id,))
        
        # Reset the IDENTITY column to 0
        reset_query = "ALTER TABLE tasks AUTO_INCREMENT = 1"
        cursor.execute(reset_query)
        
        db.commit()
        cursor.close()
        db.close()
        return redirect('/hello/')
    else:
        return redirect('/error/')
    
    
def insert_row(request):
    db = MySQLdb.connect(host="localhost", user="root", password="", database="todolist")
    task = request.GET.get ('task')
    level = request.GET.get ('level')
    start_time = request.GET.get ('start_time')
    end_time = request.GET.get ('end_time')
    if db:
        cursor = db.cursor()
        query = "INSERT INTO tasks (name, rare, start_date, end_date) VALUES (%s, %s, %s, %s);"
        cursor.execute (query, (task,level, start_time, end_time,))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/hello/')
    else:
        return redirect('/error/')
    

def hello(request):
    db = MySQLdb.connect(host="localhost", user="root", password="", database="todolist")
    if db:
        cursor = db.cursor()
        query = "SELECT * FROM tasks"
        cursor.execute(query)
        tasks = cursor.fetchall()
        cursor.close()
        db.close()

        # Get the sum of tasks to complete
        sum_of_tasks = len(tasks)

        context = {
            'tasks': tasks,
            'sum_of_tasks': sum_of_tasks
        }
        return render(request, 'hello.html', context)
    else:
        return render(request, 'error.html')

def update_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        
        # Update the status in the database
        db = MySQLdb.connect(host="localhost", user="root", password="", database="todolist")
        if db:
            cursor = db.cursor()
            update_query = "UPDATE tasks SET status = 'complete' WHERE id = %s"
            cursor.execute(update_query, (task_id,))
            db.commit()
            cursor.close()
            db.close()
            
            # Return a JSON response with the updated status
            response = {
                'status': 'complete',
                'class': 'bg-success'  # CSS class for completed status
            }
            return JsonResponse(response)
        else:
            return render(request, 'error.html')
    