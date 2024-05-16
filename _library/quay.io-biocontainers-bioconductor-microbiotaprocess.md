---
layout: container
name:  "quay.io/biocontainers/bioconductor-microbiotaprocess"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-microbiotaprocess/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-microbiotaprocess/container.yaml"
updated_at: "2024-05-16 02:47:22.499012"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-microbiotaprocess"

versions:
 - "1.6.1--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.2--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-microbiotaprocess"
config: {"url": "https://biocontainers.pro/tools/bioconductor-microbiotaprocess", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-microbiotaprocess", "latest": {"1.14.0--r43hdfd78af_0": "sha256:1ecec7872e98b727a3ba430dd9f2c9a67117e1c629cc52ac1b734be6e9f8dd53"}, "tags": {"1.6.1--r41hdfd78af_0": "sha256:d141d9822d1e21216d3bbdbc938946c16ba01b6361a9db6721d96d86ad2598c4", "1.10.0--r42hdfd78af_0": "sha256:ed4fdfb7c9bd8f733935e46192d26a9cb92a645a863d43c6bc7fe2a020502145", "1.12.2--r43hdfd78af_0": "sha256:411f4c539dc17a18f4e5e46049591079162a3cbe7e84bb2a81d4b1db708fb16d", "1.14.0--r43hdfd78af_0": "sha256:1ecec7872e98b727a3ba430dd9f2c9a67117e1c629cc52ac1b734be6e9f8dd53"}, "docker": "quay.io/biocontainers/bioconductor-microbiotaprocess"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-microbiotaprocess.
shpc-registry automated BioContainers addition for bioconductor-microbiotaprocess
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-microbiotaprocess
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-microbiotaprocess:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-microbiotaprocess/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-microbiotaprocess/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-microbiotaprocess-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-microbiotaprocess-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-microbiotaprocess-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-microbiotaprocess-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-microbiotaprocess-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-microbiotaprocess-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-microbiotaprocess

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