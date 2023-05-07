---
layout: container
name:  "quay.io/biocontainers/bioconductor-psea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-psea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-psea/container.yaml"
updated_at: "2023-05-07 03:00:24.507183"
latest: "1.32.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-psea"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-psea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-psea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-psea", "latest": {"1.32.0--r42hdfd78af_0": "sha256:4b75a7517a65f0dab6611ed959f3553a4ea6c82f70d575474f423a992e108ef3"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:3c0826a387c94651164a928186e441b9a2aaf9b4300121a5fc57b5638d3152f5", "1.32.0--r42hdfd78af_0": "sha256:4b75a7517a65f0dab6611ed959f3553a4ea6c82f70d575474f423a992e108ef3"}, "docker": "quay.io/biocontainers/bioconductor-psea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-psea.
shpc-registry automated BioContainers addition for bioconductor-psea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-psea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-psea:1.32.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-psea/1.32.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-psea/1.32.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-psea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-psea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-psea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-psea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-psea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-psea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-psea

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