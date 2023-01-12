---
layout: container
name:  "quay.io/biocontainers/bioconductor-ahcytobands"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ahcytobands/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ahcytobands/container.yaml"
updated_at: "2023-01-12 03:13:14.704044"
latest: "0.99.1--r42hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-ahcytobands"

versions:
 - "0.99.1--r41hdfd78af_1"
 - "0.99.1--r42hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-ahcytobands"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ahcytobands", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ahcytobands", "latest": {"0.99.1--r42hdfd78af_2": "sha256:6b51c847a7f3ba6d3542e452ed1e3dc2d7481996a425ac74f65769b714d20f8f"}, "tags": {"0.99.1--r41hdfd78af_1": "sha256:5e9593d2a59d55700e9b7c552a1dad0ec851b3f29a7efbef99c0d41847a04d74", "0.99.1--r42hdfd78af_2": "sha256:6b51c847a7f3ba6d3542e452ed1e3dc2d7481996a425ac74f65769b714d20f8f"}, "docker": "quay.io/biocontainers/bioconductor-ahcytobands"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ahcytobands.
shpc-registry automated BioContainers addition for bioconductor-ahcytobands
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ahcytobands
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ahcytobands:0.99.1--r42hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ahcytobands/0.99.1--r42hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-ahcytobands/0.99.1--r42hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ahcytobands-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahcytobands-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahcytobands-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ahcytobands-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ahcytobands-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ahcytobands-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ahcytobands

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