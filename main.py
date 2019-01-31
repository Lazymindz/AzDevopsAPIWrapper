import logging
from logging.config import fileConfig
from configparser import ConfigParser
import os, os.path
from requests.auth import HTTPProxyAuth
import devopsworker, zipfileworker

# Load Configuration for reading parameters
Config = ConfigParser()
Config.read('.\\settings.ini')

# Logging config
if not os.path.exists("./logs/"):
    os.makedirs("./logs/")

fileConfig('logging_config.ini')
logger = logging.getLogger()

# Artifacts save folder
if not os.path.exists("./BuildArtifacts/"):
    os.makedirs("./BuildArtifacts/")

if __name__ == "__main__":
    
    # Read Devops project details
    org_name = Config.get('devops_paths', 'org_name')
    project_name = Config.get('devops_paths', 'project_name')
    basicpattoken = Config.get('devops_paths', 'basicpattoken')

    # Read proxy details
    proxy = Config.get('proxy_details', 'ip')
    auth_user = Config.get('proxy_details', 'auth_user')
    auth_password = Config.get('proxy_details', 'auth_password')
    
    # Authentication for Proxy
    proxy_auth = HTTPProxyAuth(auth_user, auth_password)
    
    # Azure Devops Worker
    devopsworker.dojob(org_name, project_name, basicpattoken, proxy, proxy_auth)

    # Zipfile worker
    zipfileworker.dojob("./BuildArtifacts/")