---
layout: container
name:  "quay.io/biocontainers/bioconductor-obmiti"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-obmiti/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-obmiti/container.yaml"
updated_at: "2024-01-04 02:55:37.551067"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-obmiti"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-obmiti"
config: {"url": "https://biocontainers.pro/tools/bioconductor-obmiti", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-obmiti", "latest": {"1.10.0--r43hdfd78af_0": "sha256:5d41553e4197e2bf0ceae1f80654eb82df63f421587e0fb82dd9f10c6aa9ce45"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:34ce8122f09a99caee92b92fe14181466b2864996813a06e406714e45cb89dc9", "1.6.0--r42hdfd78af_0": "sha256:120dab87efcd76a9d3d3fcf0049c0f3cad77d07c12270fb78e30ceef0b353169", "1.8.0--r43hdfd78af_0": "sha256:7a81738a68f9ed85764f1a702648f5f43cd1bef6c35daeef2b9c0220c0718946", "1.10.0--r43hdfd78af_0": "sha256:5d41553e4197e2bf0ceae1f80654eb82df63f421587e0fb82dd9f10c6aa9ce45"}, "docker": "quay.io/biocontainers/bioconductor-obmiti"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-obmiti.
shpc-registry automated BioContainers addition for bioconductor-obmiti
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-obmiti
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-obmiti:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-obmiti/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-obmiti/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-obmiti-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-obmiti-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-obmiti-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-obmiti-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-obmiti-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-obmiti-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-obmiti

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