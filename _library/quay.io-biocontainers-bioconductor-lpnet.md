---
layout: container
name:  "quay.io/biocontainers/bioconductor-lpnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lpnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lpnet/container.yaml"
updated_at: "2023-11-20 03:06:15.438600"
latest: "2.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lpnet"

versions:
 - "2.26.0--r41hdfd78af_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lpnet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lpnet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lpnet", "latest": {"2.32.0--r43hdfd78af_0": "sha256:16d88beffaed9be66c38feac6abc16b6ed5d4d7625a613ef3482d07b837de99a"}, "tags": {"2.26.0--r41hdfd78af_0": "sha256:7cd5422b6da8de307dafe7f210ee5f1b0f48e3982f403a6f27ddb442396800b2", "2.30.0--r42hdfd78af_0": "sha256:20eda3c3cef45af372e927d469ebc41ece7911778199e129b08d24b31a4a83fc", "2.32.0--r43hdfd78af_0": "sha256:16d88beffaed9be66c38feac6abc16b6ed5d4d7625a613ef3482d07b837de99a"}, "docker": "quay.io/biocontainers/bioconductor-lpnet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lpnet.
shpc-registry automated BioContainers addition for bioconductor-lpnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lpnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lpnet:2.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lpnet/2.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lpnet/2.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lpnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lpnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lpnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lpnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lpnet

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