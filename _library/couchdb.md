---
layout: container
name:  "couchdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/couchdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/couchdb/container.yaml"
updated_at: "2026-02-06 05:08:39.713457"
latest: "3.5"
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
 - "3.5"
description: "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing."
config: {"docker": "couchdb", "url": "https://hub.docker.com/_/couchdb", "maintainer": "@vsoch", "description": "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.", "latest": {"3.5": "sha256:3d5bc0a2ccb6556a6361cf8b4c7f215568fb0c0c2e5e8b44a747e1c138d99f7c"}, "tags": {"2": "sha256:30dc067ce470fd437f4074d41f150fa81c1ff9c923a371d38f155d1a36159f4e", "3.1.1": "sha256:b422509b1648306dee1038f41756a982aefa17f986fa8ba18f6cd80e433dafdf", "3.2.0": "sha256:721df2c2a5da1b477e3976f3f10c3d1f015ba3c0101fb49efdcb7062b695a32c", "3.2.1": "sha256:37a7a9aab050c8c376b012d9c52da58e2c94d221b0eb5567edb88d8ceca096ee", "latest": "sha256:3d5bc0a2ccb6556a6361cf8b4c7f215568fb0c0c2e5e8b44a747e1c138d99f7c", "3": "sha256:3d5bc0a2ccb6556a6361cf8b4c7f215568fb0c0c2e5e8b44a747e1c138d99f7c", "3.2": "sha256:d32613dffcfb62cce58f65a9709fd46d66715db1a9dba3bb1033bc52df516d19", "3.1": "sha256:27e15e61dbdf09524f3246e187affedb1074b47be78d4d589c2c74570f846466", "3.0": "sha256:3257ad20542c483e744cf747641fb20d6b75ef627ff273f78be9e371e35f9608", "3.3": "sha256:307a3f5276f64c0db28f226b7b5c180b8f2c851afa681cfb4fbb1b1fe7fd5587", "3.4": "sha256:8336c8e64d3b2cd0acf439d6e653c2260d1d47ba6cd5cd17805dcefbb9da9a75", "3.5": "sha256:3d5bc0a2ccb6556a6361cf8b4c7f215568fb0c0c2e5e8b44a747e1c138d99f7c"}, "aliases": {"couchdb": "/opt/couchdb/bin/couchdb", "couchdb.cmd": "/opt/couchdb/bin/couchdb.cmd", "couchjs": "/opt/couchdb/bin/couchjs", "remsh": "/opt/couchdb/bin/remsh"}}
---

This module is a singularity container wrapper for couchdb.
CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install couchdb
```

Or a specific version:

```bash
$ shpc install couchdb:3.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load couchdb/3.5
$ module help couchdb/3.5
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