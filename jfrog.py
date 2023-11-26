import requests
import subprocess

def jfrogUpload():
    url = ''
    file_path = ''
    username = ''
    password = ''

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


