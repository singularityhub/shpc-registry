---
layout: container
name:  "quay.io/biocontainers/bioconductor-htmg430aprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htmg430aprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htmg430aprobe/container.yaml"
updated_at: "2024-09-12 02:47:20.163105"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-htmg430aprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-htmg430aprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htmg430aprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htmg430aprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:7b221b000c60d040b0003dda8ccae0eed5baeca56110a52f7c30fca3da74c8aa"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:599a4ac0501e840386fd8322f63734593fdd3d2e83be04fd41d6649ef2e50146", "2.18.0--r42hdfd78af_10": "sha256:00985ac966690ddb1e43d84af47411551e2f5b60e0e703833b7c53e60e5592d2", "2.18.0--r43hdfd78af_11": "sha256:c8957c4a6235ea10467bbdda048ffc88c71656e31a671f01300935b3e7f91fa9", "2.18.0--r43hdfd78af_12": "sha256:7b221b000c60d040b0003dda8ccae0eed5baeca56110a52f7c30fca3da74c8aa"}, "docker": "quay.io/biocontainers/bioconductor-htmg430aprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htmg430aprobe.
shpc-registry automated BioContainers addition for bioconductor-htmg430aprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430aprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430aprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htmg430aprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-htmg430aprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htmg430aprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430aprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430aprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htmg430aprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htmg430aprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htmg430aprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htmg430aprobe

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