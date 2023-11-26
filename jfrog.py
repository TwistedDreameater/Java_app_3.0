#!/usr/bin/env python3
import requests
import subprocess

def jfrogUpload():
    url = 'http://54.208.57.226:8082/artifactory/generic-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = 'http://54.208.57.226:8082/artifactory/generic-local/'
    username = 'admin'
    password = 'Password1'

    with open(file_path, 'rb') as file:
        respose =  requests.put(url, auth=(username, password), data=file)

        if reponse.status_code == 201:
            print("\nPUT request was successfull")

        else:
            print(f"PUT request failed with status code (response.status_code)")
            print("Respose content:")
            print(response.text)

def mvnBuild():
  maven_command = "mvn clean install -DskipTests"
  try:
   subprocess.run|(maven_command, check==True, text==True, shell==True)
   print("\nMaven build completed successfully.")
  except subprocess.CalledProcessError as e:
   print(f"Error: Maven build failed with exit code (e.returncode)")

def main():
    mvnBuild()
    jfrogUpload()


