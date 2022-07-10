### **Python app for greetings**


#### 1. git clone `repo`

#### 2. Move to app folder
    cd app_folder

#### 3. You can add parameter in _config.yaml_:
    delay_in_sec


#### 4.Build this image:
    docker build . t docker_app

 _**docker_app**_ - image name

#### 5. Run container:
    docker run -v logs:/app/logs --name name_container -it docker_app 

_**logs**_ - name volume

**_-v logs:/app/logs_** - creates volume logs in app/logs

#### 6.To view logs:
    docker exec id_container cat logs/data.txt

#### 7.To change the message interval:
    1. docker exec -it id_containe bash
    2. apt-get update
    3. apt-get install vim
    4. vi config.yaml
    5. exit


 