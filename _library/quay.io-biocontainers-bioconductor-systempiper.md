---
layout: container
name:  "quay.io/biocontainers/bioconductor-systempiper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-systempiper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-systempiper/container.yaml"
updated_at: "2024-08-23 03:23:48.711596"
latest: "2.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-systempiper"

versions:
 - "2.0.0--r41hdfd78af_0"
 - "2.4.0--r42hdfd78af_0"
 - "2.6.3--r43hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-systempiper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-systempiper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-systempiper", "latest": {"2.8.0--r43hdfd78af_0": "sha256:11ffc96d5ca91bc58a0ccee48182a26a8da34866b767d34e4961be82e350f097"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:fc009d0e65a30b3f125dfeb5d32d1eb5febe3a35ed7d09d83cf488eb9240cdf5", "2.4.0--r42hdfd78af_0": "sha256:19e13eabe86b608f8357fa31c1e78014e1ff5ddc7d6a23d621f58a89e87228eb", "2.6.3--r43hdfd78af_0": "sha256:87bcf3be7fe347d7d8a26fb43360273329801ab67aa0a3f3f93ca20928217ef1", "2.8.0--r43hdfd78af_0": "sha256:11ffc96d5ca91bc58a0ccee48182a26a8da34866b767d34e4961be82e350f097"}, "docker": "quay.io/biocontainers/bioconductor-systempiper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-systempiper.
shpc-registry automated BioContainers addition for bioconductor-systempiper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-systempiper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-systempiper:2.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-systempiper/2.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-systempiper/2.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-systempiper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-systempiper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-systempiper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-systempiper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-systempiper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-systempiper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-systempiper

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