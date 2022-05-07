# Resume Automation Portal

You can access the portal directly in the hosted format by using the link

https://share.streamlit.io/kartik-genpact/resume-automation/final-version/app.py

# Portal Details 
There are two ways to start the portal:
## Running in Python dev environment
1. Clone the repository
2. Install all the dependencies and libraries from requirements.txt file.
3. Make sure the folder structure is same as in the repository here
4. Go to the terminal and type:
`streamlit run app.py`

## Running through Docker
1. Clone the repository
2. Make sure the folder structure is same as in the repository here
3. Go to the terminal and type the following command (Make sure Docker is installed on your system):
`docker build -t myapp:1.0 . `
This will create an image from the Dockerfile
4. Then to create and start the container, type :
`docker run -p 8080:8050 myapp:1.0`
5. If you are running on localhost, go to:
`http://localhost:8502/` 
or if you are on the server side, go to the specified port or generated link.
