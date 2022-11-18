---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqgsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqgsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqgsea/container.yaml"
updated_at: "2022-11-18 00:43:48.643157"
latest: "1.34.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqgsea"

versions:
 - "1.34.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqgsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqgsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqgsea", "latest": {"1.34.0--r41hdfd78af_0": "sha256:115a05679209753c65940e42c53d5b4d99b0f479eb0df3547b2f8ce894d8c7b4"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:115a05679209753c65940e42c53d5b4d99b0f479eb0df3547b2f8ce894d8c7b4"}, "docker": "quay.io/biocontainers/bioconductor-seqgsea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqgsea.
shpc-registry automated BioContainers addition for bioconductor-seqgsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqgsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqgsea:1.34.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqgsea/1.34.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqgsea/1.34.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqgsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqgsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqgsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqgsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqgsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqgsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqgsea

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