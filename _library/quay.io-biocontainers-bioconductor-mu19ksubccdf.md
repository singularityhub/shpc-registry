---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu19ksubccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu19ksubccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu19ksubccdf/container.yaml"
updated_at: "2024-02-12 02:51:29.730892"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mu19ksubccdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mu19ksubccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu19ksubccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu19ksubccdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:6909b788091707dd761fbef0b994e68cdea366e9263db92c2779610eb7c7d94a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:587a0a74cf5d8dad781b2385294ed2a7905f4b2e100d2e1fbbfe26ef7df9bcba", "2.18.0--r42hdfd78af_10": "sha256:f5d2c709f24f2c09f076eb48169bc8da000bc2fd62b7884bc5501de5790e7c89", "2.18.0--r43hdfd78af_11": "sha256:55eb7c35e32ef6ca2510510669c15f23d2d8cf70bb0f69d4c85c7cccf4d3e433", "2.18.0--r43hdfd78af_12": "sha256:6909b788091707dd761fbef0b994e68cdea366e9263db92c2779610eb7c7d94a"}, "docker": "quay.io/biocontainers/bioconductor-mu19ksubccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu19ksubccdf.
shpc-registry automated BioContainers addition for bioconductor-mu19ksubccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubccdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu19ksubccdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mu19ksubccdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu19ksubccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu19ksubccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu19ksubccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu19ksubccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu19ksubccdf

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