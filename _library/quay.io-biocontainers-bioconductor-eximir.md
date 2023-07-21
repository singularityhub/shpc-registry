---
layout: container
name:  "quay.io/biocontainers/bioconductor-eximir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eximir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eximir/container.yaml"
updated_at: "2023-07-21 02:57:22.412679"
latest: "2.40.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eximir"

versions:
 - "2.36.0--r41hdfd78af_0"
 - "2.40.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-eximir"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eximir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eximir", "latest": {"2.40.0--r42hdfd78af_0": "sha256:f0e41171f4dceb2550055552eae6e83a1209e621ba2075d1c2f9a0d7eea0d2e7"}, "tags": {"2.36.0--r41hdfd78af_0": "sha256:545c9e82cf70919e1723a0514f17121b7b7521e9bb63d7b98a3f6d3402f21536", "2.40.0--r42hdfd78af_0": "sha256:f0e41171f4dceb2550055552eae6e83a1209e621ba2075d1c2f9a0d7eea0d2e7"}, "docker": "quay.io/biocontainers/bioconductor-eximir"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eximir.
shpc-registry automated BioContainers addition for bioconductor-eximir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eximir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eximir:2.40.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eximir/2.40.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-eximir/2.40.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eximir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eximir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eximir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eximir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eximir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eximir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-eximir

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