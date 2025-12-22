---
layout: container
name:  "mongo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/mongo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/mongo/container.yaml"
updated_at: "2025-12-22 04:40:35.533845"
latest: "8.2"
container_url: "https://hub.docker.com/r/_/mongo"
aliases:
 - "mongo"
 - "mongod"
 - "mongodump"
 - "mongoexport"
 - "mongofiles"
 - "mongoimport"
 - "mongos"
 - "mongostat"
 - "mongostore"
 - "mongotop"
versions:
 - "4.4.5-bionic"
 - "4.4.6-bionic"
 - "5.0.0-focal"
 - "5.0.0-rc1-focal"
 - "5.0.2"
 - "5.0.3"
 - "5.0.4"
 - "5.0.5"
 - "5.0.6"
 - "latest"
 - "5"
 - "5.0"
 - "4"
 - "4.9-rc"
 - "4.4"
 - "6"
 - "6.0"
 - "7.0-rc"
 - "7"
 - "7.0"
 - "8.0-rc"
 - "8"
 - "8.0"
 - "8.2"
description: "MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata."
config: {"docker": "mongo", "url": "https://hub.docker.com/r/_/mongo", "maintainer": "@vsoch", "description": "MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.", "filter": ["^(?!.*nano).*$", "^(?!.*windows).*$"], "latest": {"8.2": "crane digest mongo:8.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"4.4.5-bionic": "sha256:cc8bb8711114fa726ca641f5644791d3d43bdd2c95dac541a5fa2c90a2e6e972", "4.4.6-bionic": "sha256:3d0e6df9fd5bc42cbf8ef8bc9e6c4e78f6f26c7157dbd7bdec72d202ab8ebe3a", "5.0.0-focal": "sha256:21aa30c16cf1f92c68890cefc612357bf856f94678cc4bfc0ef26bdeb7c34ad0", "5.0.0-rc1-focal": "crane digest mongo:5.0.0-rc1-focal: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0.2": "crane digest mongo:5.0.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0.3": "crane digest mongo:5.0.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0.4": "crane digest mongo:5.0.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0.5": "crane digest mongo:5.0.5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0.6": "crane digest mongo:5.0.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "latest": "crane digest mongo:latest: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5": "crane digest mongo:5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0": "crane digest mongo:5.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "4": "crane digest mongo:4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "4.9-rc": "crane digest mongo:4.9-rc: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "4.4": "crane digest mongo:4.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "6": "crane digest mongo:6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "6.0": "crane digest mongo:6.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "7.0-rc": "crane digest mongo:7.0-rc: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "7": "crane digest mongo:7: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "7.0": "crane digest mongo:7.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.0-rc": "crane digest mongo:8.0-rc: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8": "crane digest mongo:8: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.0": "crane digest mongo:8.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.2": "crane digest mongo:8.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "aliases": {"mongo": "/usr/bin/mongo", "mongod": "/usr/bin/mongod", "mongodump": "/usr/bin/mongodump", "mongoexport": "/usr/bin/mongoexport", "mongofiles": "/usr/bin/mongofiles", "mongoimport": "/usr/bin/mongoimport", "mongos": "/usr/bin/mongos", "mongostat": "/usr/bin/mongostat", "mongostore": "/usr/bin/mongorestore", "mongotop": "/usr/bin/mongotop"}}
---

This module is a singularity container wrapper for mongo.
MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install mongo
```

Or a specific version:

```bash
$ shpc install mongo:8.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mongo/8.2
$ module help mongo/8.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mongo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mongo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mongo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mongo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mongo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mongo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mongo

```bash
$ singularity exec <container> /usr/bin/mongo
$ podman run --it --rm --entrypoint /usr/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongod

```bash
$ singularity exec <container> /usr/bin/mongod
$ podman run --it --rm --entrypoint /usr/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongodump

```bash
$ singularity exec <container> /usr/bin/mongodump
$ podman run --it --rm --entrypoint /usr/bin/mongodump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongodump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongoexport

```bash
$ singularity exec <container> /usr/bin/mongoexport
$ podman run --it --rm --entrypoint /usr/bin/mongoexport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongoexport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongofiles

```bash
$ singularity exec <container> /usr/bin/mongofiles
$ podman run --it --rm --entrypoint /usr/bin/mongofiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongofiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongoimport

```bash
$ singularity exec <container> /usr/bin/mongoimport
$ podman run --it --rm --entrypoint /usr/bin/mongoimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongoimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongos

```bash
$ singularity exec <container> /usr/bin/mongos
$ podman run --it --rm --entrypoint /usr/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongostat

```bash
$ singularity exec <container> /usr/bin/mongostat
$ podman run --it --rm --entrypoint /usr/bin/mongostat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongostat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongostore

```bash
$ singularity exec <container> /usr/bin/mongorestore
$ podman run --it --rm --entrypoint /usr/bin/mongorestore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongorestore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongotop

```bash
$ singularity exec <container> /usr/bin/mongotop
$ podman run --it --rm --entrypoint /usr/bin/mongotop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongotop   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)