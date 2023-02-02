FROM python:3-alpine  
# alpine : to keep the docker file low (zipped imgs)

#creating working directory as service i.e root folder
WORKDIR /service

  # copying requirements.txt file to the root folder('.'d i.e service)
COPY requirements.txt .

# I will run a command as  i.e used to install all the files and dependencies that we are having in that file
RUN pip3 install -r requirements.txt

# copy from source i.e working-dir(env) to the destination(service)
# all the things that i am copying , it will get copied into my service directory of docker image
# from my root dir(.) to the root-dir of docker
# copying app.py file to the service-directory of the docker file
COPY . ./

EXPOSE 8082

ENTRYPOINT ["python3", "app.py"]
