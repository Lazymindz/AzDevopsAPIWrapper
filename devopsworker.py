from domain import AzureDevops
import logging
from logging import NullHandler

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())

# New Instance of the Project Repo
def task_create_worker(org_name, project_name, basicpattoken, proxy, proxy_auth):
    azuredevops = AzureDevops(org_name, project_name)
    azuredevops.setauth(basicpattoken)
    azuredevops.setproxy(proxy,proxy_auth)
    return azuredevops

def task_download_artifacts(azuredevops, buildids):
        for build in buildids:
            artifactslist = azuredevops.getbuildartifacts(build)
            for artifact in artifactslist['value']:
                azuredevops.downloadartifact(build, artifact)

def dojob(org_name, project_name, basicpattoken, proxy, proxy_auth):
    # Task 1 : Create a worker with Authentication
    azuredevops = task_create_worker(org_name, project_name, basicpattoken, proxy, proxy_auth)
    
    # Task 2 : Get all builds for the Project
    buildids = azuredevops.getbuildids()

    # Task 3 : Download artifacts
    task_download_artifacts(azuredevops, buildids)