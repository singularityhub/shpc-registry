---
layout: container
name:  "quay.io/biocontainers/bioconductor-bhc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bhc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bhc/container.yaml"
updated_at: "2023-02-07 03:32:19.625767"
latest: "1.50.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bhc"

versions:
 - "1.46.0--r41hc247a5b_2"
 - "1.50.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bhc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bhc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bhc", "latest": {"1.50.0--r42hc247a5b_0": "sha256:06d11ac54cd4f9d13c39d9d369a2ceb630f556886d6fb3f3403df9a043f1d268"}, "tags": {"1.46.0--r41hc247a5b_2": "sha256:eaeaa5fce595d8fd891d3565ed3ec6843b64905ec66b0e7dbf831abc1fb26db3", "1.50.0--r42hc247a5b_0": "sha256:06d11ac54cd4f9d13c39d9d369a2ceb630f556886d6fb3f3403df9a043f1d268"}, "docker": "quay.io/biocontainers/bioconductor-bhc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bhc.
shpc-registry automated BioContainers addition for bioconductor-bhc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bhc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bhc:1.50.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bhc/1.50.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-bhc/1.50.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bhc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bhc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bhc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bhc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bhc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bhc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bhc

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