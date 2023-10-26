---
layout: container
name:  "quay.io/biocontainers/bioconductor-bsgenome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bsgenome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bsgenome/container.yaml"
updated_at: "2023-10-26 04:07:33.701449"
latest: "1.68.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bsgenome"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.1--r42hdfd78af_0"
 - "1.66.3--r42hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bsgenome"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bsgenome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bsgenome", "latest": {"1.68.0--r43hdfd78af_0": "sha256:d6199f425696411d019f67f280535057c0f051b8ad225a8ca6a7edf51d74d6e8"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:bffb3c8a796fe6d90a2e396d3057ca8466d4665e65f0e00bdffdc1ce32efeaae", "1.66.1--r42hdfd78af_0": "sha256:7efb620cefb91478615f1e4764a04900667d15abcd92a50fd39cd3a84c2aaba7", "1.66.3--r42hdfd78af_0": "sha256:edea25c2b9860e0bb8cc7f96344574bfc46c9c19ece7cc028b0e077c3d9b3928", "1.68.0--r43hdfd78af_0": "sha256:d6199f425696411d019f67f280535057c0f051b8ad225a8ca6a7edf51d74d6e8"}, "docker": "quay.io/biocontainers/bioconductor-bsgenome"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bsgenome.
shpc-registry automated BioContainers addition for bioconductor-bsgenome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bsgenome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bsgenome:1.68.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bsgenome/1.68.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bsgenome/1.68.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bsgenome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bsgenome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bsgenome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bsgenome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bsgenome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bsgenome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bsgenome

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