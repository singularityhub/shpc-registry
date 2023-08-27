---
layout: container
name:  "quay.io/biocontainers/bioconductor-lefser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lefser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lefser/container.yaml"
updated_at: "2023-08-27 02:49:58.679852"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lefser"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lefser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lefser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lefser", "latest": {"1.10.0--r43hdfd78af_0": "sha256:96da4a3194ea4d0a35a40632b35aab49fe8aeb17b48981b665fa5bddd99e66f2"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:1d3729ad19a24b30413f0ec80b1610967909e8ccf2d2926e5f16f0baee1f34a8", "1.8.0--r42hdfd78af_0": "sha256:8dd8a4b0b5de57cd4d40377a6bc9c40f7f9071555dfff5a6e8d1f336b01959a4", "1.10.0--r43hdfd78af_0": "sha256:96da4a3194ea4d0a35a40632b35aab49fe8aeb17b48981b665fa5bddd99e66f2"}, "docker": "quay.io/biocontainers/bioconductor-lefser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lefser.
shpc-registry automated BioContainers addition for bioconductor-lefser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lefser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lefser:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lefser/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lefser/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lefser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lefser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lefser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lefser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lefser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lefser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lefser

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