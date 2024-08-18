---
layout: container
name:  "quay.io/biocontainers/bioconductor-diffutr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-diffutr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-diffutr/container.yaml"
updated_at: "2024-08-18 02:49:59.620633"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-diffutr"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-diffutr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-diffutr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-diffutr", "latest": {"1.10.0--r43hdfd78af_0": "sha256:1cf0f3f1875f5d935397de83b43f7f344e338a8007220021cd3e857721cd6dd5"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:a1c0f0e250e4306116cd75d59cab9c3ecd2e20247485fa8eff8887c14811a4d7", "1.6.0--r42hdfd78af_0": "sha256:80280f21dbfde64a94220d4dcdb5803417e8f1d6b86cd0ceddaf8efdfe7da1e8", "1.8.0--r43hdfd78af_0": "sha256:beb21c4610c30b52d293c045eb353c5a19ba14e19e90da2ee5098054bcda8fee", "1.10.0--r43hdfd78af_0": "sha256:1cf0f3f1875f5d935397de83b43f7f344e338a8007220021cd3e857721cd6dd5"}, "docker": "quay.io/biocontainers/bioconductor-diffutr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-diffutr.
shpc-registry automated BioContainers addition for bioconductor-diffutr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-diffutr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-diffutr:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-diffutr/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-diffutr/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-diffutr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffutr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffutr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-diffutr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-diffutr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-diffutr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-diffutr

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