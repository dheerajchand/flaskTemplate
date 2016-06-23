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

### Instructions (Step by Step)

###### 1. Data-only Container Setup

```

```

###### 2. Postgres DB Container Setup


```

```

###### 3. Flask Application Container Setup

```

```


### Important notes about using Docker



###### Acknowlegements
https://learning-continuous-deployment.github.io/docker/images/dockerfile/database/persistence/volumes/linking/container/2015/05/29/docker-and-databases/

Dockerhub





