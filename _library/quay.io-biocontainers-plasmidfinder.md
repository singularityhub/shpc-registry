---
layout: container
name:  "quay.io/biocontainers/plasmidfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plasmidfinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/plasmidfinder/container.yaml"
updated_at: "2022-10-27 00:34:45.579751"
latest: "2.1.6--py310hdfd78af_1"
container_url: "https://biocontainers.pro/tools/plasmidfinder"
aliases:
 - ".plasmidfinder-post-link.sh"
 - "download-db.sh"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "plasmidfinder.py"
versions:
 - "2.1.6--py310hdfd78af_1"
description: "shpc-registry automated BioContainers addition for plasmidfinder"
config: {"url": "https://biocontainers.pro/tools/plasmidfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plasmidfinder", "latest": {"2.1.6--py310hdfd78af_1": "sha256:0b02ed6e441e055d3c6e6ed083ae8731430e009466aa82f8aad0484001ea41c3"}, "tags": {"2.1.6--py310hdfd78af_1": "sha256:0b02ed6e441e055d3c6e6ed083ae8731430e009466aa82f8aad0484001ea41c3"}, "docker": "quay.io/biocontainers/plasmidfinder", "aliases": {".plasmidfinder-post-link.sh": "/usr/local/bin/.plasmidfinder-post-link.sh", "download-db.sh": "/usr/local/bin/download-db.sh", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "plasmidfinder.py": "/usr/local/bin/plasmidfinder.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plasmidfinder.
shpc-registry automated BioContainers addition for plasmidfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plasmidfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plasmidfinder:2.1.6--py310hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plasmidfinder/2.1.6--py310hdfd78af_1
$ module help quay.io/biocontainers/plasmidfinder/2.1.6--py310hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasmidfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasmidfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasmidfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasmidfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasmidfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasmidfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .plasmidfinder-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.plasmidfinder-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.plasmidfinder-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.plasmidfinder-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-db.sh

```bash
$ singularity exec <container> /usr/local/bin/download-db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidfinder.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidfinder.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidfinder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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