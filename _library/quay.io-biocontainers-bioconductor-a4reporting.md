---
layout: container
name:  "quay.io/biocontainers/bioconductor-a4reporting"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-a4reporting/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-a4reporting/container.yaml"
updated_at: "2023-03-11 02:55:52.925341"
latest: "1.46.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-a4reporting"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-a4reporting"
config: {"url": "https://biocontainers.pro/tools/bioconductor-a4reporting", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-a4reporting", "latest": {"1.46.0--r42hdfd78af_0": "sha256:308d8ad5c13aa978ad8248fe5ecac7368f7832f8ab801ded45f49afa446e61d2"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:9ceac085084893736e383f45959e9483c5d278f16bd797c7189d26ebae73a491", "1.46.0--r42hdfd78af_0": "sha256:308d8ad5c13aa978ad8248fe5ecac7368f7832f8ab801ded45f49afa446e61d2"}, "docker": "quay.io/biocontainers/bioconductor-a4reporting"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-a4reporting.
shpc-registry automated BioContainers addition for bioconductor-a4reporting
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-a4reporting
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-a4reporting:1.46.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-a4reporting/1.46.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-a4reporting/1.46.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-a4reporting-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4reporting-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4reporting-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-a4reporting-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-a4reporting-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-a4reporting-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-a4reporting

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