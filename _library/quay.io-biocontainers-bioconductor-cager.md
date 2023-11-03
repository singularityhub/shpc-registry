---
layout: container
name:  "quay.io/biocontainers/bioconductor-cager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cager/container.yaml"
updated_at: "2023-11-03 02:26:42.351830"
latest: "2.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cager"

versions:
 - "2.0.1--r41hdfd78af_0"
 - "2.4.0--r42hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cager"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cager", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cager", "latest": {"2.6.0--r43hdfd78af_0": "sha256:e05733d6e728781ff5652446ac673f232f380320ee314bd960ee78e88f428b30"}, "tags": {"2.0.1--r41hdfd78af_0": "sha256:5ef5ec5ad4e946ab2ac07292492868f0ce42cee3ac3d8f0bda65dd44024c9a83", "2.4.0--r42hdfd78af_0": "sha256:9d1bbee057e9a52c2f310a2f2f0b293ed8c298c3a971db9c5778c97026982e75", "2.6.0--r43hdfd78af_0": "sha256:e05733d6e728781ff5652446ac673f232f380320ee314bd960ee78e88f428b30"}, "docker": "quay.io/biocontainers/bioconductor-cager"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cager.
shpc-registry automated BioContainers addition for bioconductor-cager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cager:2.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cager/2.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cager/2.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cager

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