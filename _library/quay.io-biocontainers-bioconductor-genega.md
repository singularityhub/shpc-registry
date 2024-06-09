---
layout: container
name:  "quay.io/biocontainers/bioconductor-genega"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genega/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genega/container.yaml"
updated_at: "2024-06-09 03:02:23.928580"
latest: "1.52.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genega"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genega"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genega", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genega", "latest": {"1.52.0--r43hdfd78af_0": "sha256:238225371b75915f4cfdaad59a99295f0b85cebec591159e581a344f91b8a5d8"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:aab4f0174e4f2607662a3002907f06384361abb9f3537f8717e0c0ada7df7cda", "1.48.0--r42hdfd78af_0": "sha256:3e688616b99ad4af9cffa50ede5093dbbae1b21d2a827758abc9249dff278f54", "1.52.0--r43hdfd78af_0": "sha256:238225371b75915f4cfdaad59a99295f0b85cebec591159e581a344f91b8a5d8"}, "docker": "quay.io/biocontainers/bioconductor-genega"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genega.
shpc-registry automated BioContainers addition for bioconductor-genega
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genega
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genega:1.52.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genega/1.52.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genega/1.52.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genega-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genega-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genega-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genega-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genega-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genega-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genega

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