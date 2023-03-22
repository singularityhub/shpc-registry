---
layout: container
name:  "quay.io/biocontainers/bioconductor-maigespack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maigespack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maigespack/container.yaml"
updated_at: "2023-03-22 03:04:53.821285"
latest: "1.62.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maigespack"

versions:
 - "1.58.0--r41h5c21468_1"
 - "1.62.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maigespack"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maigespack", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maigespack", "latest": {"1.62.0--r42hc0cfd56_0": "sha256:c3ee81bd0d29248278d2defb31bf5ee4a02b6b9463937d4e0d5156d30422a4da"}, "tags": {"1.58.0--r41h5c21468_1": "sha256:ef2839f049f3656cb74527a3a1879f5d2214e0474f040a4144a294b41e091465", "1.62.0--r42hc0cfd56_0": "sha256:c3ee81bd0d29248278d2defb31bf5ee4a02b6b9463937d4e0d5156d30422a4da"}, "docker": "quay.io/biocontainers/bioconductor-maigespack"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maigespack.
shpc-registry automated BioContainers addition for bioconductor-maigespack
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maigespack
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maigespack:1.62.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maigespack/1.62.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-maigespack/1.62.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maigespack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maigespack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maigespack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maigespack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maigespack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maigespack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maigespack

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