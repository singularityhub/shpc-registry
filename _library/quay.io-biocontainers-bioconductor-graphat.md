---
layout: container
name:  "quay.io/biocontainers/bioconductor-graphat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-graphat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-graphat/container.yaml"
updated_at: "2024-11-23 02:57:26.326878"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-graphat"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-graphat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-graphat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-graphat", "latest": {"1.74.0--r43hdfd78af_0": "sha256:2e836a7a4f02cb8b7d82aadc4dd3d8ac38405c33e7bbd755a06c1958d5a4e688"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:9ea4e82629e22eee490537368ca749e36bcc38ac48508778b9476b08bc5b4ad0", "1.70.0--r42hdfd78af_0": "sha256:8516f40bb5783ba1387736aea371380d762c2121eaf199283cdb70b5e3d4caee", "1.72.0--r43hdfd78af_0": "sha256:f71441484b368a32a67d5a3d93e7851d25975292a181fb0a603a4815cba94900", "1.74.0--r43hdfd78af_0": "sha256:2e836a7a4f02cb8b7d82aadc4dd3d8ac38405c33e7bbd755a06c1958d5a4e688"}, "docker": "quay.io/biocontainers/bioconductor-graphat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-graphat.
shpc-registry automated BioContainers addition for bioconductor-graphat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-graphat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-graphat:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-graphat/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-graphat/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-graphat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-graphat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-graphat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-graphat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-graphat

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