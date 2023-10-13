---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhdf5filters"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhdf5filters/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhdf5filters/container.yaml"
updated_at: "2023-10-13 02:45:25.236426"
latest: "1.12.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rhdf5filters"

versions:
 - "1.6.0--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rhdf5filters"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhdf5filters", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhdf5filters", "latest": {"1.12.1--r43hf17093f_0": "sha256:10c8e7a5dff053f40686501c95bbb69143ce25e6cf32bde8356bc0c4d8470702"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:fc90ca5dbb2f4c319959d45d21106637bfaff171fb36c2bb53b2ec7d78f00f0c", "1.10.0--r42hc247a5b_0": "sha256:bb4aa87504c5b1c2dfb766bbf9c03e4ce697cb3f3a8dd5675b794d0d81855d82", "1.10.0--r42hf17093f_1": "sha256:f997a7ac121470265a4d3afe6fc011d4218d05f82578b5ae621ef747e7b6b7f4", "1.12.1--r43hf17093f_0": "sha256:10c8e7a5dff053f40686501c95bbb69143ce25e6cf32bde8356bc0c4d8470702"}, "docker": "quay.io/biocontainers/bioconductor-rhdf5filters"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhdf5filters.
shpc-registry automated BioContainers addition for bioconductor-rhdf5filters
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhdf5filters
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhdf5filters:1.12.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhdf5filters/1.12.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rhdf5filters/1.12.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhdf5filters-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhdf5filters-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhdf5filters-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhdf5filters-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhdf5filters-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhdf5filters-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rhdf5filters

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