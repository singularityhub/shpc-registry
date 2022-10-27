---
layout: container
name:  "quay.io/biocontainers/dazz_db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dazz_db/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dazz_db/container.yaml"
updated_at: "2022-10-27 01:09:14.997147"
latest: "1.0p2--h7132678_5"
container_url: "https://biocontainers.pro/tools/dazz_db"
aliases:
 - "DB2arrow"
 - "DB2quiva"
 - "DBdump"
 - "DBtrim"
 - "DBwipe"
 - "arrow2DB"
 - "quiva2DB"
 - "rangen"
versions:
 - "1.0p2--h7132678_5"
description: "shpc-registry automated BioContainers addition for dazz_db"
config: {"url": "https://biocontainers.pro/tools/dazz_db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dazz_db", "latest": {"1.0p2--h7132678_5": "sha256:63780c37204dbffed831851aeedf19894beb07a814a26ab7e04baec771792227"}, "tags": {"1.0p2--h7132678_5": "sha256:63780c37204dbffed831851aeedf19894beb07a814a26ab7e04baec771792227"}, "docker": "quay.io/biocontainers/dazz_db", "aliases": {"DB2arrow": "/usr/local/bin/DB2arrow", "DB2quiva": "/usr/local/bin/DB2quiva", "DBdump": "/usr/local/bin/DBdump", "DBtrim": "/usr/local/bin/DBtrim", "DBwipe": "/usr/local/bin/DBwipe", "arrow2DB": "/usr/local/bin/arrow2DB", "quiva2DB": "/usr/local/bin/quiva2DB", "rangen": "/usr/local/bin/rangen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dazz_db.
shpc-registry automated BioContainers addition for dazz_db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dazz_db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dazz_db:1.0p2--h7132678_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dazz_db/1.0p2--h7132678_5
$ module help quay.io/biocontainers/dazz_db/1.0p2--h7132678_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dazz_db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dazz_db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dazz_db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dazz_db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dazz_db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dazz_db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DB2arrow

```bash
$ singularity exec <container> /usr/local/bin/DB2arrow
$ podman run --it --rm --entrypoint /usr/local/bin/DB2arrow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DB2arrow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DB2quiva

```bash
$ singularity exec <container> /usr/local/bin/DB2quiva
$ podman run --it --rm --entrypoint /usr/local/bin/DB2quiva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DB2quiva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBdump

```bash
$ singularity exec <container> /usr/local/bin/DBdump
$ podman run --it --rm --entrypoint /usr/local/bin/DBdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBtrim

```bash
$ singularity exec <container> /usr/local/bin/DBtrim
$ podman run --it --rm --entrypoint /usr/local/bin/DBtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBwipe

```bash
$ singularity exec <container> /usr/local/bin/DBwipe
$ podman run --it --rm --entrypoint /usr/local/bin/DBwipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBwipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arrow2DB

```bash
$ singularity exec <container> /usr/local/bin/arrow2DB
$ podman run --it --rm --entrypoint /usr/local/bin/arrow2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arrow2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quiva2DB

```bash
$ singularity exec <container> /usr/local/bin/quiva2DB
$ podman run --it --rm --entrypoint /usr/local/bin/quiva2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quiva2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rangen

```bash
$ singularity exec <container> /usr/local/bin/rangen
$ podman run --it --rm --entrypoint /usr/local/bin/rangen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rangen   -v ${PWD} -w ${PWD} <container> -c " $@"
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