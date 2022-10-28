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

users = client.users.get_users(workspace_id)
user_id = users[0]['id']

times = client.time_entries.get_time_entries(workspace_id, user_id)

task_list = [task['name'] for task in tasks[::-1]]
time_list = [task['duration'][2:] for task in tasks[::-1]]

number_of_tasks = len(task_list)
all_spent_time = projects[0]['duration'][2:]

task_name = []
task_duration = []
task_date = []

for time in times:
    for task in tasks:
        if time['taskId'] == task['id']:
            task_name.append(task['name'])
            task_duration.append(time['timeInterval']['duration'][2:])
            temp_split = time['timeInterval']['start'][:19].split('T')
            task_date.append('  '.join(temp_split))
