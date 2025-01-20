---
layout: container
name:  "quay.io/biocontainers/bioconductor-msqrob2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msqrob2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msqrob2/container.yaml"
updated_at: "2025-01-20 03:50:23.880213"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msqrob2"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msqrob2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msqrob2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msqrob2", "latest": {"1.14.0--r44hdfd78af_0": "sha256:918b3a0abb6d72adbc681a8b65bfd2215ac3e44ba51566c854a5f605b911d0de"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:9ec5889158be1cead005cc1b4cb5715654021d345247f45eded020027e5b57b8", "1.6.0--r42hdfd78af_0": "sha256:d37f9392ea9d36da9912c5c20f7f589c387b700a5103d4ad35047ded7932aec8", "1.8.0--r43hdfd78af_0": "sha256:aae6100b16c215be6149440958ae3c079e4a380f01b02ca79e26a6ae15438fed", "1.10.0--r43hdfd78af_0": "sha256:b7c3d0dfe822b9936bae2740eb02396defc3034690a22dac507132aefdc5b880", "1.14.0--r44hdfd78af_0": "sha256:918b3a0abb6d72adbc681a8b65bfd2215ac3e44ba51566c854a5f605b911d0de"}, "docker": "quay.io/biocontainers/bioconductor-msqrob2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msqrob2.
shpc-registry automated BioContainers addition for bioconductor-msqrob2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msqrob2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msqrob2:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msqrob2/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msqrob2/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msqrob2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msqrob2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msqrob2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msqrob2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msqrob2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msqrob2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msqrob2

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