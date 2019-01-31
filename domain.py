import requests
from requests.auth import HTTPProxyAuth
import json
import os, os.path
import logging
from logging import NullHandler
from logging.config import fileConfig

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())


class AzureDevops(object):
    """DevOps Build Pipeline Class"""

    def __init__(self, org_name, project_name):
        self.org_name = org_name
        self.project_name = project_name
        self.auth = ''
        self.proxy = {
            'http'  : '', 
            'https' : ''
            }
        self.proxyauth = None
    
    def setauth(self, auth):
        self.auth = auth
        return None

    def setproxy(self, proxy, proxyauth):
        self.proxy['http'] = proxy
        self.proxy['https'] = proxy
        self.proxyauth = proxyauth
        return None

    def getbuilds(self):
        requesturl = 'https://dev.azure.com/{organization}/{project}/_apis/build/builds?api-version=5.0'.format(organization=self.org_name, project=self.project_name)
        headers = {
            'Authorization': self.auth,
            }
        response = requests.request("GET", url=requesturl, headers=headers, proxies=self.proxy, auth=self.proxyauth)
        return response.content
    
    def getbuildids(self):
        builds = json.loads(self.getbuilds())
        buildids = [build['id'] for build in builds['value']]
        logging.debug('Build Ids extracted..')
        return buildids

    def getbuildartifacts(self, buildid):
        requesturl = 'https://dev.azure.com/{organization}/{project}/_apis/build/builds/{buildId}/artifacts?api-version=5.0'.format(
            organization=self.org_name, 
            project=self.project_name,
            buildId=buildid
        )
        headers = {
            'Authorization': self.auth,
            }
        response = requests.request("GET", url=requesturl, headers=headers, proxies=self.proxy, auth=self.proxyauth)
        return json.loads(response.content)
    
    def downloadartifact(self, buildid, artifact):
        requesturl = artifact['resource']['downloadUrl']
        filename = '{name}.zip'.format(name = artifact['name'])
        filepath = './BuildArtifacts/{buildid}/{filename}'.format(filename=filename, buildid=buildid)
        headers = {
            'Authorization': self.auth,
            }
        response = requests.request("GET", url=requesturl, headers=headers, proxies=self.proxy, auth=self.proxyauth)
        
        if not os.path.exists("./BuildArtifacts/{buildid}".format(buildid=buildid)):
            os.makedirs("./BuildArtifacts/{buildid}".format(buildid=buildid))
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return None