---
layout: container
name:  "quay.io/biocontainers/sawfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sawfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sawfish/container.yaml"
updated_at: "2025-05-02 03:52:15.669587"
latest: "0.12.10--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/sawfish"
aliases:
 - "sawfish"
versions:
 - "0.12.1--h9ee0642_0"
 - "0.12.3--h9ee0642_0"
 - "0.12.4--h9ee0642_0"
 - "0.12.7--h9ee0642_0"
 - "0.12.8--h9ee0642_0"
 - "0.12.9--h9ee0642_0"
 - "0.12.10--h9ee0642_0"
description: "singularity registry hpc automated addition for sawfish"
config: {"url": "https://biocontainers.pro/tools/sawfish", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sawfish", "latest": {"0.12.10--h9ee0642_0": "sha256:072e1d1ce32878ce77ebd5575323434047777cfd422ac27ab62a0474b9dcb290"}, "tags": {"0.12.1--h9ee0642_0": "sha256:0de0ad7950f341793da2af2143b1f8a763eec1eb042a51e15132291ade2cde92", "0.12.3--h9ee0642_0": "sha256:31da5c53dee50431726e9f9eb709661ad99433fc01fa0c942825e6529b03efc7", "0.12.4--h9ee0642_0": "sha256:54ad9566a4a05934f7879d42f631cb8f61737f05ca9e7eb1751cb7b4e9c4d4db", "0.12.7--h9ee0642_0": "sha256:041e51c96eac3b68d987aef9a8d892bdd13467b3e554e50f67327ed29fd88041", "0.12.8--h9ee0642_0": "sha256:a73a4900f6c28c266811e6fa5266a0ccc731ce0075ee6842664387bb0043a765", "0.12.9--h9ee0642_0": "sha256:1b5d88fb8b49f7234937627ab09bbcfbfc6d5dc3477eb799c95b6dcb15ed26ee", "0.12.10--h9ee0642_0": "sha256:072e1d1ce32878ce77ebd5575323434047777cfd422ac27ab62a0474b9dcb290"}, "docker": "quay.io/biocontainers/sawfish", "aliases": {"sawfish": "/usr/local/bin/sawfish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sawfish.
singularity registry hpc automated addition for sawfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sawfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sawfish:0.12.10--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sawfish/0.12.10--h9ee0642_0
$ module help quay.io/biocontainers/sawfish/0.12.10--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sawfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sawfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sawfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sawfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sawfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sawfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sawfish

```bash
$ singularity exec <container> /usr/local/bin/sawfish
$ podman run --it --rm --entrypoint /usr/local/bin/sawfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sawfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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