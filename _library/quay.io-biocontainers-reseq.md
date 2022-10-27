---
layout: container
name:  "quay.io/biocontainers/reseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/reseq/container.yaml"
updated_at: "2022-10-27 00:45:57.746939"
latest: "1.1--py37h3a4aa43_2"
container_url: "https://biocontainers.pro/tools/reseq"
aliases:
 - "plotDataStats.py"
 - "reseq"
 - "reseq-prepare-names.py"
versions:
 - "1.1--py37h3a4aa43_2"
description: "shpc-registry automated BioContainers addition for reseq"
config: {"url": "https://biocontainers.pro/tools/reseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for reseq", "latest": {"1.1--py37h3a4aa43_2": "sha256:312c546111b31bcf8102850521306694b539350a3f744bdbacbcfa5edfe1c4e9"}, "tags": {"1.1--py37h3a4aa43_2": "sha256:312c546111b31bcf8102850521306694b539350a3f744bdbacbcfa5edfe1c4e9"}, "docker": "quay.io/biocontainers/reseq", "aliases": {"plotDataStats.py": "/usr/local/bin/plotDataStats.py", "reseq": "/usr/local/bin/reseq", "reseq-prepare-names.py": "/usr/local/bin/reseq-prepare-names.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reseq.
shpc-registry automated BioContainers addition for reseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reseq:1.1--py37h3a4aa43_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reseq/1.1--py37h3a4aa43_2
$ module help quay.io/biocontainers/reseq/1.1--py37h3a4aa43_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plotDataStats.py

```bash
$ singularity exec <container> /usr/local/bin/plotDataStats.py
$ podman run --it --rm --entrypoint /usr/local/bin/plotDataStats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotDataStats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reseq

```bash
$ singularity exec <container> /usr/local/bin/reseq
$ podman run --it --rm --entrypoint /usr/local/bin/reseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reseq-prepare-names.py

```bash
$ singularity exec <container> /usr/local/bin/reseq-prepare-names.py
$ podman run --it --rm --entrypoint /usr/local/bin/reseq-prepare-names.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reseq-prepare-names.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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