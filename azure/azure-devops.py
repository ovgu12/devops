import os
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Fill in with your personal access token and org URL
personal_access_token = os.environ.get('SYSTEM_ACCESSTOKEN')
organization_url = 'https://dev.azure.com/Okarben'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()

# Get projects
get_projects_response = core_client.get_projects()

for project in get_projects_response:
    print(project.name)