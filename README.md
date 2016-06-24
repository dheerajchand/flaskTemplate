## Docker setup for a Flask Development Environment

### Description

We will create 3 different Docker containers for our setup.

###### 1. Data-only Container *(data)*
* References the volume /data/db (the default directory for storing data)

###### 2. Postgres DB Container *(postgres)*
* Sets up the configuration for a postgres database and runs it

###### 3. Flask Application Container *(flask)*
* Creates a Flask environment with proper python packages

Now to explain the relationship between these three containers. We mount the volume from **data** when we run **postgres** so that any database operations are persisted. Then, when we run **flask**, we link **postgres** to it so that it can connect appropriately.

The use of these Docker containers is mainly for development, as we would usually keep our database on an entirely separate machine from our application in production. 

#### Why use this approach???
This setup allows us to separate all of our functionality neatly. So if we wanted to mount a different data container to our postgres container we could very easily. We can also start multiple applications that could all connect to a single postgres container, thus sharing a data source. **This gives us an incredible amount of flexibility, portability, and modularity.**

### Instructions (Step by Step)

First make sure that to have Docker installed on your machine:
<https://www.docker.com/products/overview#/install_the_platform>

Open a Docker Terminal before proceding. 

##### 1. Data-only Container Setup

We simply need to create the container based on the already existing ubuntu image. There is no need for a separate Dockerfile or further setup, since this container's only function is to maintain the data volume.

```
docker create -v /var/lib/postgresql/data --name data-container ubuntu
```

##### 2. Postgres DB Container Setup

Build the custom postgres image from the appropriate Dockerfile.

```
docker build -f ./Dockerfile-postgres -t postgres-container .
```

Now when we run this image to create our container we mount the volume from the **data_container**.
We use the -d option to daemonize this process so that we can finish our build.

```
docker run -d --volumes-from data-container --name pgdb-1 postgres-container
```

We can access the psql shell of our container using the following :

```
docker run -it --rm --link pgdb-1:postgres postgres psql -h postgres -U postgres
```
*Side note: The -h flag is used to tell psql that our host is our newly linked pgdb-1*


##### 3. Flask Application Container Setup

Build our flask image from the appropriate Dockerfile.
```
docker build -f ./Dockerfile-flask -t flask-container .
```
Now to run our new container and if our flask app wants to, we can link to our postgres container.

```
docker run -it -v $(pwd)/flask-app:/flask-app -p 5000:5000 --name flask-1 --link pgdb-1:pg flask-container
```
We use -p to specify a host and port mapping so that we are able to access the socket our flask app starts from within the container.

Notice that we use -v flag to mount our flask application directory. This makes it so that changes made to our flask application on our host will also be seen within our container. As a result, we can edit our application files using whatever file editor we like that is native to our machine (i.e. Sublime Text, PyCharm) 

Now we are in our flask container's console and have access to our flask-app. We can now develop was we normally would, using a text editor locally and the console to make updates to our requirements.txt and start the server

Our build does NOT automatically install the basic required libraries for a flask application from the included requirements.txt file. This can easily be done with a call to `pip install -r requirements.txt` .

###### IMPORTANT NOTE FOR OSX
It is likely you are using Virtual Box as part of the Docker Toolbox in order to use docker on OSX. When we go to access our web app endpoints locally at `localhost:5000` we will get nothing! This is because the Virtual Box adds another linux layer in order to properly run docker, necessitating an IP mapping.

Here is the solution:
run `docker-machine ls` and find the IP listed in the URL section.
For example, we might see `tcp://192.168.99.100:2376`, and then our IP would be 192.168.99.100.
Since we mapped port 5000 from our flask container, we can now access our endpoints at `192.168.99.100:5000`
Remember that this is an example and the IP is probably different on your machine.

### Notes about using Docker

Containers have the notion of being started and stopped. When we run a container it is started. If we are in the console for a given container and we run `exit`, then this stops the container and brings us back to our local console. If we want to go back to our container, we must first restart the container and then reattach to it.
```
docker start container_name && docker attach container_name
```

If we want to remove a container we use:
```
docker rm container_name
```
This will only work if the container is stopped so if necessary run `docker stop container_name` first.

### Acknowlegements

##### Docker image extentions :
https://hub.docker.com/_/postgres/

##### Container structure inspiration :
https://learning-continuous-deployment.github.io/docker/images/dockerfile/database/persistence/volumes/linking/container/2015/05/29/docker-and-databases/

##### For structuring flask applications :
http://flask.pocoo.org/docs/0.11/patterns/appfactories/

### Authors

Jonathan Kramer,
jonkramer@circavictor.com,
*Circa Victor Software Engineer*

