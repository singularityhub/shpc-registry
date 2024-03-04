---
layout: container
name:  "quay.io/biocontainers/bioconductor-phyloprofiledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phyloprofiledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phyloprofiledata/container.yaml"
updated_at: "2024-03-04 04:38:17.221998"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phyloprofiledata"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phyloprofiledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phyloprofiledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phyloprofiledata", "latest": {"1.16.0--r43hdfd78af_0": "sha256:46b12350031cf20384474d3ed7b6daccebf0eead4ff86ee48432e89b8a9a16d5"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:4847c039f56034d4a1088733f5bdc0ac704a6d0d32e83cc64daba7a4cdfd56c7", "1.12.0--r42hdfd78af_0": "sha256:c2d5b93513c35410b6db1cb8924423a8f1284007aa343fb57b419fd257aaf9b5", "1.14.0--r43hdfd78af_0": "sha256:07ee524cbbe94ecaa31b1af1755917282a7fbfccdecf4c9cb918bc4885f49d22", "1.16.0--r43hdfd78af_0": "sha256:46b12350031cf20384474d3ed7b6daccebf0eead4ff86ee48432e89b8a9a16d5"}, "docker": "quay.io/biocontainers/bioconductor-phyloprofiledata", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phyloprofiledata.
shpc-registry automated BioContainers addition for bioconductor-phyloprofiledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phyloprofiledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phyloprofiledata:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phyloprofiledata/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phyloprofiledata/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phyloprofiledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phyloprofiledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phyloprofiledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phyloprofiledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phyloprofiledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phyloprofiledata-inspect-deffile:

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