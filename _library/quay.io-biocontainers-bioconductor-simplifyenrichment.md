---
layout: container
name:  "quay.io/biocontainers/bioconductor-simplifyenrichment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simplifyenrichment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simplifyenrichment/container.yaml"
updated_at: "2024-03-05 02:42:29.564546"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simplifyenrichment"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simplifyenrichment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simplifyenrichment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simplifyenrichment", "latest": {"1.12.0--r43hdfd78af_0": "sha256:07f5c5eaaf12f4ef4866cf92f4cee2508778e3aa7bfca86532b78a7a4b878e71"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:63dbc2701b9e1ed8fceebf4bec87ef86294e0598300932bcf7ab66828cab7d4c", "1.8.0--r42hdfd78af_0": "sha256:5d8e622b9eec3b4744c4c07a74c064fe1559e175521072d321dc4f471aac3011", "1.10.0--r43hdfd78af_0": "sha256:6d9b09d3f3978c7276ec30768895e9af5343f15325d1c49cc48eb907d326ef51", "1.12.0--r43hdfd78af_0": "sha256:07f5c5eaaf12f4ef4866cf92f4cee2508778e3aa7bfca86532b78a7a4b878e71"}, "docker": "quay.io/biocontainers/bioconductor-simplifyenrichment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simplifyenrichment.
shpc-registry automated BioContainers addition for bioconductor-simplifyenrichment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simplifyenrichment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simplifyenrichment:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simplifyenrichment/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-simplifyenrichment/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simplifyenrichment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simplifyenrichment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simplifyenrichment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simplifyenrichment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simplifyenrichment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simplifyenrichment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-simplifyenrichment

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