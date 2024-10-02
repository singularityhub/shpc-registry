---
layout: container
name:  "quay.io/biocontainers/bioconductor-intansv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-intansv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-intansv/container.yaml"
updated_at: "2024-10-02 03:05:07.630666"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-intansv"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-intansv"
config: {"url": "https://biocontainers.pro/tools/bioconductor-intansv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-intansv", "latest": {"1.42.0--r43hdfd78af_0": "sha256:e18cf6bd3cd79b5ed95fbe3aa66766d7e527e112d25043ab70dab5b5aec18f15"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:2bae398c16ae60623e833bad136f0d3f13540432bbf708360195abf946d0ef49", "1.38.0--r42hdfd78af_0": "sha256:829771977a7b5ed54ded15edaf53c8f7d44cb3ed6d74749370af2a2029d81781", "1.40.0--r43hdfd78af_0": "sha256:0bb4d9748672d1b77e424d4fe497b3119ed9c3eddd44642a763ebd828a0003c8", "1.42.0--r43hdfd78af_0": "sha256:e18cf6bd3cd79b5ed95fbe3aa66766d7e527e112d25043ab70dab5b5aec18f15"}, "docker": "quay.io/biocontainers/bioconductor-intansv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-intansv.
shpc-registry automated BioContainers addition for bioconductor-intansv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-intansv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-intansv:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-intansv/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-intansv/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-intansv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-intansv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-intansv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-intansv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-intansv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-intansv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-intansv

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