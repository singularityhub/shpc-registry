---
layout: container
name:  "quay.io/biocontainers/bioconductor-chetah"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chetah/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chetah/container.yaml"
updated_at: "2024-05-31 03:01:35.395300"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chetah"

versions:
 - "1.9.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chetah"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chetah", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chetah", "latest": {"1.18.0--r43hdfd78af_0": "sha256:937e0b0a80ef290a9127c299e58e081cf7c0cad71a9546aa1b50ecb1c1f37abc"}, "tags": {"1.9.0--r41hdfd78af_0": "sha256:491780cde0a96cab9ca8a25a8eb7053d2aa17cf97eed380c12c711c50b40a464", "1.14.0--r42hdfd78af_0": "sha256:3d1a2b3d429ece58837b6c17c2a97c07aa0015e655c497023ba22ea474065599", "1.16.0--r43hdfd78af_0": "sha256:cdae6284d1289a0dde9d9f8d062774db42e0f0572133654485ccdc1bcf9f5e45", "1.18.0--r43hdfd78af_0": "sha256:937e0b0a80ef290a9127c299e58e081cf7c0cad71a9546aa1b50ecb1c1f37abc"}, "docker": "quay.io/biocontainers/bioconductor-chetah"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chetah.
shpc-registry automated BioContainers addition for bioconductor-chetah
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chetah
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chetah:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chetah/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chetah/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chetah-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chetah-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chetah-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chetah-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chetah-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chetah-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chetah

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