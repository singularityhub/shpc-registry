---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipxpress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipxpress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipxpress/container.yaml"
updated_at: "2025-01-29 03:14:59.366197"
latest: "1.42.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipxpress"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipxpress"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipxpress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipxpress", "latest": {"1.42.0--r42hdfd78af_0": "sha256:88c347a6acc4102ce0eb2b872d3f8d19962844e38e0ead648924f7b2fe91d180"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:3a91a505453cd6a893955913ad0c42994d2f89d13a132aeac690dc241ecf5caf", "1.42.0--r42hdfd78af_0": "sha256:88c347a6acc4102ce0eb2b872d3f8d19962844e38e0ead648924f7b2fe91d180"}, "docker": "quay.io/biocontainers/bioconductor-chipxpress"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipxpress.
shpc-registry automated BioContainers addition for bioconductor-chipxpress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipxpress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipxpress:1.42.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipxpress/1.42.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipxpress/1.42.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipxpress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipxpress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipxpress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipxpress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipxpress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipxpress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chipxpress

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