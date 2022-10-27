---
layout: container
name:  "quay.io/biocontainers/faststructure"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/faststructure/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/faststructure/container.yaml"
updated_at: "2022-10-27 00:53:59.594999"
latest: "1.0--py27h6b1b274_5"
container_url: "https://biocontainers.pro/tools/faststructure"
aliases:
 - "chooseK.py"
 - "distruct.py"
 - "structure.py"
versions:
 - "1.0--py27h6b1b274_5"
description: "shpc-registry automated BioContainers addition for faststructure"
config: {"url": "https://biocontainers.pro/tools/faststructure", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for faststructure", "latest": {"1.0--py27h6b1b274_5": "sha256:47cfb5483e5a7682dbaaf8f945bb905b1aa1f35fddf2de8ea55b46acc214deda"}, "tags": {"1.0--py27h6b1b274_5": "sha256:47cfb5483e5a7682dbaaf8f945bb905b1aa1f35fddf2de8ea55b46acc214deda"}, "docker": "quay.io/biocontainers/faststructure", "aliases": {"chooseK.py": "/usr/local/bin/chooseK.py", "distruct.py": "/usr/local/bin/distruct.py", "structure.py": "/usr/local/bin/structure.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/faststructure.
shpc-registry automated BioContainers addition for faststructure
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/faststructure
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/faststructure:1.0--py27h6b1b274_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/faststructure/1.0--py27h6b1b274_5
$ module help quay.io/biocontainers/faststructure/1.0--py27h6b1b274_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### faststructure-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### faststructure-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### faststructure-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### faststructure-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### faststructure-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### faststructure-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chooseK.py

```bash
$ singularity exec <container> /usr/local/bin/chooseK.py
$ podman run --it --rm --entrypoint /usr/local/bin/chooseK.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chooseK.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distruct.py

```bash
$ singularity exec <container> /usr/local/bin/distruct.py
$ podman run --it --rm --entrypoint /usr/local/bin/distruct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distruct.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### structure.py

```bash
$ singularity exec <container> /usr/local/bin/structure.py
$ podman run --it --rm --entrypoint /usr/local/bin/structure.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/structure.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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