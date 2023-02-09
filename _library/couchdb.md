---
layout: container
name:  "couchdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/couchdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/couchdb/container.yaml"
updated_at: "2023-02-08 23:06:08.556216"
latest: "3.3"
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
description: "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing."
config: {"docker": "couchdb", "url": "https://hub.docker.com/_/couchdb", "maintainer": "@vsoch", "description": "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.", "latest": {"3.3": "sha256:09d5e033b3bc4bd43746529188747ea1f3171da37b030ed6d1870f69fcfb4ad2"}, "tags": {"2": "sha256:2e48c0f4c5bd780169441fcdc5e0ccc545e2f5df14a0e7fdb288bde4818beed4", "3.1.1": "sha256:b422509b1648306dee1038f41756a982aefa17f986fa8ba18f6cd80e433dafdf", "3.2.0": "sha256:721df2c2a5da1b477e3976f3f10c3d1f015ba3c0101fb49efdcb7062b695a32c", "3.2.1": "sha256:37a7a9aab050c8c376b012d9c52da58e2c94d221b0eb5567edb88d8ceca096ee", "latest": "sha256:09d5e033b3bc4bd43746529188747ea1f3171da37b030ed6d1870f69fcfb4ad2", "3": "sha256:09d5e033b3bc4bd43746529188747ea1f3171da37b030ed6d1870f69fcfb4ad2", "3.2": "sha256:824bfc746f289f37129c7bdf3f463564fcae874a316d1411cebf6c75deba6151", "3.1": "sha256:833f239931b93786e7bd6e01811c87c825a43168181cc00746e2f34707e8915a", "3.0": "sha256:3257ad20542c483e744cf747641fb20d6b75ef627ff273f78be9e371e35f9608", "3.3": "sha256:09d5e033b3bc4bd43746529188747ea1f3171da37b030ed6d1870f69fcfb4ad2"}, "aliases": {"couchdb": "/opt/couchdb/bin/couchdb", "couchdb.cmd": "/opt/couchdb/bin/couchdb.cmd", "couchjs": "/opt/couchdb/bin/couchjs", "remsh": "/opt/couchdb/bin/remsh"}}
---

This module is a singularity container wrapper for couchdb.
CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install couchdb
```

Or a specific version:

```bash
$ shpc install couchdb:3.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load couchdb/3.3
$ module help couchdb/3.3
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