---
layout: container
name:  "quay.io/biocontainers/confindr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/confindr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/confindr/container.yaml"
updated_at: "2022-10-27 01:01:40.016877"
latest: "0.7.4--py_0"
container_url: "https://biocontainers.pro/tools/confindr"
aliases:
 - "confindr"
 - "confindr.py"
 - "confindr_create_db"
 - "confindr_database_setup"
versions:
 - "0.7.4--py_0"
description: "shpc-registry automated BioContainers addition for confindr"
config: {"url": "https://biocontainers.pro/tools/confindr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for confindr", "latest": {"0.7.4--py_0": "sha256:f282610616c8fd04bafcd365303b6c9dbdc010406fea44f3bcdd7c0010e55688"}, "tags": {"0.7.4--py_0": "sha256:f282610616c8fd04bafcd365303b6c9dbdc010406fea44f3bcdd7c0010e55688"}, "docker": "quay.io/biocontainers/confindr", "aliases": {"confindr": "/usr/local/bin/confindr", "confindr.py": "/usr/local/bin/confindr.py", "confindr_create_db": "/usr/local/bin/confindr_create_db", "confindr_database_setup": "/usr/local/bin/confindr_database_setup"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/confindr.
shpc-registry automated BioContainers addition for confindr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/confindr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/confindr:0.7.4--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/confindr/0.7.4--py_0
$ module help quay.io/biocontainers/confindr/0.7.4--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### confindr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### confindr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### confindr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### confindr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### confindr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### confindr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### confindr

```bash
$ singularity exec <container> /usr/local/bin/confindr
$ podman run --it --rm --entrypoint /usr/local/bin/confindr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr.py

```bash
$ singularity exec <container> /usr/local/bin/confindr.py
$ podman run --it --rm --entrypoint /usr/local/bin/confindr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr_create_db

```bash
$ singularity exec <container> /usr/local/bin/confindr_create_db
$ podman run --it --rm --entrypoint /usr/local/bin/confindr_create_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr_create_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confindr_database_setup

```bash
$ singularity exec <container> /usr/local/bin/confindr_database_setup
$ podman run --it --rm --entrypoint /usr/local/bin/confindr_database_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/confindr_database_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
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