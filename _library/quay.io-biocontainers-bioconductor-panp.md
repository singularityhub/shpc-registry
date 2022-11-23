---
layout: container
name:  "quay.io/biocontainers/bioconductor-panp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-panp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-panp/container.yaml"
updated_at: "2022-11-23 00:07:07.625448"
latest: "1.68.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-panp"

versions:
 - "1.64.0--r41hdfd78af_0"
 - "1.68.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-panp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-panp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-panp", "latest": {"1.68.0--r42hdfd78af_0": "sha256:83a4b5da08988b57a96c7d8a68f3ebfacf2b32efa356d4c2f4237ce4066268e7"}, "tags": {"1.64.0--r41hdfd78af_0": "sha256:d420bfc23d539b3de01d43623806e8115e747d69d314d11e4de63333697cd4d7", "1.68.0--r42hdfd78af_0": "sha256:83a4b5da08988b57a96c7d8a68f3ebfacf2b32efa356d4c2f4237ce4066268e7"}, "docker": "quay.io/biocontainers/bioconductor-panp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-panp.
shpc-registry automated BioContainers addition for bioconductor-panp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-panp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-panp:1.68.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-panp/1.68.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-panp/1.68.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-panp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-panp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-panp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-panp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-panp

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