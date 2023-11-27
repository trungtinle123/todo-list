function addTask() {
    const task = document.querySelector ("#task")
    const level = document.querySelector ("#level")
    const start_time = document.querySelector ("#start_time")
    const end_time = document.querySelector ("#end_time")
    
    const task_value = task.value;
    const level_value = level.value;
    const start_time_value = start_time.value;
    const end_time_value = end_time.value;
    window.location.href = '/insert/row?task='+task_value+'&level='+level_value+'&start_time='+start_time_value+'&end_time='+end_time_value

}

