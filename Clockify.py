import API_KEY_FILE

from clockify_api_client.client import ClockifyAPIClient

API_KEY = API_KEY_FILE.API_KEY
API_URL = 'api.clockify.me/v1'

client = ClockifyAPIClient().build(API_KEY, API_URL)

workspaces = client.workspaces.get_workspaces()
workspace_id = workspaces[0]['id']

projects = client.projects.get_projects(workspace_id)
project_id = projects[0]['id']

tasks = client.tasks.get_tasks(workspace_id, project_id)

task_list = [task['name'] for task in tasks[::-1]]
time_list = [task['duration'][2:] for task in tasks[::-1]]

number_of_tasks = len(task_list)
all_spent_time = projects[0]['duration'][2:]

for i in range(0, len(task_list)):
    print(f'{task_list[i]} \nI spend for this task: {time_list[i]}\n')