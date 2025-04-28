---
layout: container
name:  "quay.io/biocontainers/bioconductor-stroma4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stroma4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stroma4/container.yaml"
updated_at: "2025-04-28 03:23:53.747677"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-stroma4"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-stroma4"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stroma4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stroma4", "latest": {"1.24.0--r43hdfd78af_0": "sha256:2024a4bf44c1a9a39c69437356820481f231b39bc21ec3cac00d5bb622812ac0"}, "tags": {"1.8.0--r36_1": "sha256:d1e6e4e4ba173cb391368e5d5dce1bdcb462ca57c71ad666e8cdba1ce7f78139", "1.22.0--r42hdfd78af_0": "sha256:6b6f965781b21c28c3c6a39afbadf47ee8d3a3ccb6faea6fcfce5536a31ec81a", "1.18.0--r41hdfd78af_0": "sha256:3d7c806cee1f95361b040aebeddb3f50eccbf6fe711a18112a0815aeeee37ab0", "1.16.0--r41hdfd78af_0": "sha256:a1f9097c79a6c7010913baa85bf1450a4e67f73ae5f0a60b359091f79b050ba4", "1.14.0--r40hdfd78af_1": "sha256:d6962cf7b53018394f0fa21fbe0f782406eea47367fdcdda573b99cdee12d16c", "1.12.0--r40_0": "sha256:505816d1eceb6a26f5cb413433125e893ff97af59da2d921ccab0c59a87f8679", "1.24.0--r43hdfd78af_0": "sha256:2024a4bf44c1a9a39c69437356820481f231b39bc21ec3cac00d5bb622812ac0"}, "docker": "quay.io/biocontainers/bioconductor-stroma4", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stroma4.
shpc-registry automated BioContainers addition for bioconductor-stroma4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stroma4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stroma4:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stroma4/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-stroma4/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stroma4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stroma4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stroma4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stroma4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stroma4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stroma4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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