# Azure Devops API Wrapper
Azure vsts Python's client library is still under heavy development and without documentation. I've had issues to make it work within Corporate environment with Proxies in place.

This repo is an example wrapper on top of Azure Devops API, which has helpful documentation.

Code I hope is easy to follow along.

Idea of the example is to:
- identify all the Builds in a pipeline
- Extract the Build artifacts
- Recursively read all the Zip files
- List out files generated in the build

Example is just to build a skeleton framework on top of the API documentation

Not done:
1. Logging (although the loggers and rotation has been added. Actual comments are not done)
2. Error handling. Feel free to fork and do so for your needs.

Steps to run the framework:
1. Create virtual environment (Python 3)
2. Install the requirements.txt
3. Modify and run main.py as needed

# References
[Azure DevOps Services REST API Reference](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.0)