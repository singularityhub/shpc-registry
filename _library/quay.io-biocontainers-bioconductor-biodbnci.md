---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbnci"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbnci/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbnci/container.yaml"
updated_at: "2023-06-26 03:17:50.683075"
latest: "1.2.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbnci"

versions:
 - "1.2.0--r42hc247a5b_0"
 - "1.2.0--r42hf17093f_1"
description: "singularity registry hpc automated addition for bioconductor-biodbnci"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbnci", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biodbnci", "latest": {"1.2.0--r42hf17093f_1": "sha256:11d4d14f9c432be0b9e8ec3da37809f6b4fb902127194ca977053757941fc2bc"}, "tags": {"1.2.0--r42hc247a5b_0": "sha256:8d0deda2a9e4bafa50760cd5ba9df461051e744330ccee2d915c09feba5cf1ed", "1.2.0--r42hf17093f_1": "sha256:11d4d14f9c432be0b9e8ec3da37809f6b4fb902127194ca977053757941fc2bc"}, "docker": "quay.io/biocontainers/bioconductor-biodbnci"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbnci.
singularity registry hpc automated addition for bioconductor-biodbnci
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbnci
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbnci:1.2.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbnci/1.2.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-biodbnci/1.2.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbnci-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbnci-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbnci-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbnci-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbnci-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbnci-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbnci

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