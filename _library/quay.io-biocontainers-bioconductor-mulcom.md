---
layout: container
name:  "quay.io/biocontainers/bioconductor-mulcom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mulcom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mulcom/container.yaml"
updated_at: "2023-05-22 03:25:18.621989"
latest: "1.48.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mulcom"

versions:
 - "1.44.0--r41hc247a5b_2"
 - "1.48.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mulcom"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mulcom", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mulcom", "latest": {"1.48.0--r42hc247a5b_0": "sha256:926f3137511c66d82c71680fb67653d889954cceaa685ed381ca223aaf9f3baa"}, "tags": {"1.44.0--r41hc247a5b_2": "sha256:1ffb54def1c1a9273d6a90050f91d3b8d987d6a913e4931383645b2111f3c589", "1.48.0--r42hc247a5b_0": "sha256:926f3137511c66d82c71680fb67653d889954cceaa685ed381ca223aaf9f3baa"}, "docker": "quay.io/biocontainers/bioconductor-mulcom"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mulcom.
shpc-registry automated BioContainers addition for bioconductor-mulcom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mulcom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mulcom:1.48.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mulcom/1.48.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-mulcom/1.48.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mulcom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mulcom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mulcom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mulcom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mulcom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mulcom-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mulcom

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