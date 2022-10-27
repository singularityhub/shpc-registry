---
layout: container
name:  "quay.io/biocontainers/serotypefinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/serotypefinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/serotypefinder/container.yaml"
updated_at: "2022-10-27 00:29:36.553575"
latest: "2.0.1--py39hdfd78af_0"
container_url: "https://biocontainers.pro/tools/serotypefinder"
aliases:
 - ".serotypefinder-post-link.sh"
 - "serotypefinder"
 - "update-serotypefinder-db"
versions:
 - "2.0.1--py39hdfd78af_0"
description: "shpc-registry automated BioContainers addition for serotypefinder"
config: {"url": "https://biocontainers.pro/tools/serotypefinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for serotypefinder", "latest": {"2.0.1--py39hdfd78af_0": "sha256:04d3dd31d77ca3f0d2d35dfb090c2beccad959f07fb9fe87a0c6db2d0650f99a"}, "tags": {"2.0.1--py39hdfd78af_0": "sha256:04d3dd31d77ca3f0d2d35dfb090c2beccad959f07fb9fe87a0c6db2d0650f99a"}, "docker": "quay.io/biocontainers/serotypefinder", "aliases": {".serotypefinder-post-link.sh": "/usr/local/bin/.serotypefinder-post-link.sh", "serotypefinder": "/usr/local/bin/serotypefinder", "update-serotypefinder-db": "/usr/local/bin/update-serotypefinder-db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/serotypefinder.
shpc-registry automated BioContainers addition for serotypefinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/serotypefinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/serotypefinder:2.0.1--py39hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/serotypefinder/2.0.1--py39hdfd78af_0
$ module help quay.io/biocontainers/serotypefinder/2.0.1--py39hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### serotypefinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### serotypefinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### serotypefinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### serotypefinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### serotypefinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### serotypefinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .serotypefinder-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.serotypefinder-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.serotypefinder-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.serotypefinder-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### serotypefinder

```bash
$ singularity exec <container> /usr/local/bin/serotypefinder
$ podman run --it --rm --entrypoint /usr/local/bin/serotypefinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/serotypefinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update-serotypefinder-db

```bash
$ singularity exec <container> /usr/local/bin/update-serotypefinder-db
$ podman run --it --rm --entrypoint /usr/local/bin/update-serotypefinder-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update-serotypefinder-db   -v ${PWD} -w ${PWD} <container> -c " $@"
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