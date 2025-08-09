---
layout: container
name:  "quay.io/biocontainers/bioconductor-meb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meb/container.yaml"
updated_at: "2025-08-09 04:01:29.342554"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meb"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meb", "latest": {"1.20.0--r44hdfd78af_0": "sha256:46035d53e2f1502bb5d83a95b59f4811f9d393f055fcb4b2caea5cc8c55cf22b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:ed83a3cc8cf4e3ff44a0c2d80431d98256e74e6d7dcad932b9b88f0731756707", "1.12.0--r42hdfd78af_0": "sha256:bc021e42d7ce7be9054f95a847d1676155ee68ca032b04eb3c7580e7c74d72de", "1.14.0--r43hdfd78af_0": "sha256:d054b12927ba2319edf141c371350fda48afc388ccf4796b4d3b56d3b2f529a2", "1.16.0--r43hdfd78af_0": "sha256:78d9d3557db62055d8391729e29cf35fa5e9f64b79f233b201afca598a432344", "1.20.0--r44hdfd78af_0": "sha256:46035d53e2f1502bb5d83a95b59f4811f9d393f055fcb4b2caea5cc8c55cf22b"}, "docker": "quay.io/biocontainers/bioconductor-meb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meb.
shpc-registry automated BioContainers addition for bioconductor-meb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meb:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meb/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meb/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-meb

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