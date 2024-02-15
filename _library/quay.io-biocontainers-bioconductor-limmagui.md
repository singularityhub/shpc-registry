---
layout: container
name:  "quay.io/biocontainers/bioconductor-limmagui"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-limmagui/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-limmagui/container.yaml"
updated_at: "2024-02-15 03:56:03.394865"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-limmagui"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-limmagui"
config: {"url": "https://biocontainers.pro/tools/bioconductor-limmagui", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-limmagui", "latest": {"1.78.0--r43hdfd78af_0": "sha256:fb6d8de05de177e48365fab2831a733a4c300d462263e66bdc9c6ffc98c8e215"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:01e3e6e68fb10608fbc57cce89e9e978ae36d50715f764f5626409a9ef276a31", "1.74.0--r42hdfd78af_0": "sha256:93a9d1548ee7ffa78ab483a45962a85c471021cb69e8175c2c674abee25ff9d8", "1.76.0--r43hdfd78af_0": "sha256:d93b1fbf2d266797ee032bd09232c66f32222e7d6e91ae3e6308a7739da1323b", "1.78.0--r43hdfd78af_0": "sha256:fb6d8de05de177e48365fab2831a733a4c300d462263e66bdc9c6ffc98c8e215"}, "docker": "quay.io/biocontainers/bioconductor-limmagui"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-limmagui.
shpc-registry automated BioContainers addition for bioconductor-limmagui
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-limmagui
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-limmagui:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-limmagui/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-limmagui/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-limmagui-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-limmagui-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-limmagui-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-limmagui-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-limmagui-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-limmagui-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-limmagui

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