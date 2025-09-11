---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedbreastdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedbreastdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedbreastdata/container.yaml"
updated_at: "2025-09-11 03:31:21.638447"
latest: "2.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedbreastdata"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "2.22.0--r41hdfd78af_1"
 - "2.26.0--r42hdfd78af_0"
 - "2.28.0--r43hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedbreastdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedbreastdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedbreastdata", "latest": {"2.34.0--r44hdfd78af_0": "sha256:bd566121c6efb48978da96b2472986bce28892e6abefccf93fd7649ba7b824ae"}, "tags": {"2.22.0--r41hdfd78af_1": "sha256:a168390133760194b739602867e0f2ab4d66daf764d1a3f8784f207e45dea146", "2.26.0--r42hdfd78af_0": "sha256:0223f4d2bad8b97caaacf7e9fde7601ca70fc4a7d94b259d074e929ba2fed131", "2.28.0--r43hdfd78af_0": "sha256:09efe0dd68fdde6db4bb4a6f323255a48cc1608bcda505fde6f50c9d9b8e44fc", "2.30.0--r43hdfd78af_0": "sha256:e9947684afc0a0c6d03850e51061085571863d3b2cef014ee7e04a757a0d9324", "2.34.0--r44hdfd78af_0": "sha256:bd566121c6efb48978da96b2472986bce28892e6abefccf93fd7649ba7b824ae"}, "docker": "quay.io/biocontainers/bioconductor-curatedbreastdata", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedbreastdata.
shpc-registry automated BioContainers addition for bioconductor-curatedbreastdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedbreastdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedbreastdata:2.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedbreastdata/2.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedbreastdata/2.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedbreastdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedbreastdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedbreastdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedbreastdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedbreastdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedbreastdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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