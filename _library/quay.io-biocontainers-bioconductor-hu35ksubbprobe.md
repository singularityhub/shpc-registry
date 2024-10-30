---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu35ksubbprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu35ksubbprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu35ksubbprobe/container.yaml"
updated_at: "2024-10-30 03:32:03.107067"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hu35ksubbprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hu35ksubbprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu35ksubbprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu35ksubbprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:961721e68f2f860c7a336f06a9b530ec007c5f0a61e71a50395b19200a8dc92e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:2be6edd0c4f3362be2fe53945d4cfe3a1defb7cc47bf22c015c4b7d1a8b507f7", "2.18.0--r42hdfd78af_10": "sha256:8dcd25b6beac1b24f9aeae2e9a4c2a659ab7b8db97089258ac36a75665906ffd", "2.18.0--r43hdfd78af_11": "sha256:15d4d35506e4f35773369a478ec1fee766ea75126a9df598bd641371b07f114f", "2.18.0--r43hdfd78af_12": "sha256:961721e68f2f860c7a336f06a9b530ec007c5f0a61e71a50395b19200a8dc92e"}, "docker": "quay.io/biocontainers/bioconductor-hu35ksubbprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu35ksubbprobe.
shpc-registry automated BioContainers addition for bioconductor-hu35ksubbprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubbprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubbprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu35ksubbprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hu35ksubbprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu35ksubbprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubbprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubbprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu35ksubbprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu35ksubbprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu35ksubbprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu35ksubbprobe

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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