---
layout: container
name:  "couchdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/couchdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/couchdb/container.yaml"
updated_at: "2025-03-24 03:04:16.992571"
latest: "3.4"
container_url: "https://hub.docker.com/_/couchdb"
aliases:
 - "couchdb"
 - "couchdb.cmd"
 - "couchjs"
 - "remsh"
versions:
 - "2"
 - "3.1.1"
 - "3.2.0"
 - "3.2.1"
 - "latest"
 - "3"
 - "3.2"
 - "3.1"
 - "3.0"
 - "3.3"
 - "3.4"
description: "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing."
config: {"docker": "couchdb", "url": "https://hub.docker.com/_/couchdb", "maintainer": "@vsoch", "description": "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.", "latest": {"3.4": "crane digest couchdb:3.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"2": "crane digest couchdb:2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.1.1": "crane digest couchdb:3.1.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.2.0": "crane digest couchdb:3.2.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.2.1": "crane digest couchdb:3.2.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "latest": "crane digest couchdb:latest: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3": "crane digest couchdb:3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.2": "crane digest couchdb:3.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.1": "crane digest couchdb:3.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.0": "crane digest couchdb:3.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.3": "crane digest couchdb:3.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "3.4": "crane digest couchdb:3.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "aliases": {"couchdb": "/opt/couchdb/bin/couchdb", "couchdb.cmd": "/opt/couchdb/bin/couchdb.cmd", "couchjs": "/opt/couchdb/bin/couchjs", "remsh": "/opt/couchdb/bin/remsh"}}
---

This module is a singularity container wrapper for couchdb.
CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install couchdb
```

Or a specific version:

```bash
$ shpc install couchdb:3.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load couchdb/3.4
$ module help couchdb/3.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### couchdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### couchdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### couchdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### couchdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### couchdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### couchdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### couchdb

```bash
$ singularity exec <container> /opt/couchdb/bin/couchdb
$ podman run --it --rm --entrypoint /opt/couchdb/bin/couchdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/couchdb/bin/couchdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### couchdb.cmd

```bash
$ singularity exec <container> /opt/couchdb/bin/couchdb.cmd
$ podman run --it --rm --entrypoint /opt/couchdb/bin/couchdb.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/couchdb/bin/couchdb.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### couchjs

```bash
$ singularity exec <container> /opt/couchdb/bin/couchjs
$ podman run --it --rm --entrypoint /opt/couchdb/bin/couchjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/couchdb/bin/couchjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remsh

```bash
$ singularity exec <container> /opt/couchdb/bin/remsh
$ podman run --it --rm --entrypoint /opt/couchdb/bin/remsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/couchdb/bin/remsh   -v ${PWD} -w ${PWD} <container> -c " $@"
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