## Docker setup for a Flask Development Environment

### Description and File Structure

We will create 3 different Docker containers for our setup.

###### 1. Data-only Container *(data)*
* References the volume /data/db (the default directory for storing data)

###### 2. Postgres DB Container *(postgres)*
* Sets up the configuration for a postgres database and runs it

###### 3. Flask Application Container *(flask)*
* Creates a Flask environment with proper python packages

Now to explain the relationship between these three containers. We mount the volume from **data** when we run **postgres** so that any database operations are persisted. Then, when we run **flask**, we link **postgres** to it so that it can connect appropriately.

The use of these Docker containers is mainly for development, as we would usually keep our database on an entirely separate machine from our application. 

### Instructions (Step by Step)

First make sure that to have Docker installed on your machine:
<https://www.docker.com/products/overview#/install_the_platform>

Open a Docker Terminal before proceding. 

###### 1. Data-only Container Setup

We simply need to create the container based on the already existing ubuntu image. There is no need for a separate Dockerfile or further setup, since this container's only function is to maintain the data volume.

```
docker create -v /data/db/ --name data_container ubuntu

```

###### 2. Postgres DB Container Setup

Build the custom postgres image from the appropriate Dockerfile. Something to note about this build is that we use the included postgres.conf file to setup our connection port and a root user and password at (). This can be adjusted if necessary.

```


```

Now when we run this image to create our container we mount the volume from the **data_container**.
We use the -d option to daemonize this process so that we can finish our build.

```
docker run -d -p :9895 --volumes-from data_container --name pgdb pgdb-1

```

If we wanted to enter terminal for this container for some reason, run 
```
docker attach pgdb-1

```

###### 3. Flask Application Container Setup

```

```


### Important notes about using Docker



### Acknowlegements
https://learning-continuous-deployment.github.io/docker/images/dockerfile/database/persistence/volumes/linking/container/2015/05/29/docker-and-databases/

Dockerhub

