---
layout: container
name:  "quay.io/biocontainers/bioconductor-bacon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bacon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bacon/container.yaml"
updated_at: "2024-07-12 02:48:15.743136"
latest: "1.30.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bacon"

versions:
 - "1.8.0--r351h470a237_0"
 - "1.26.0--r42hc0cfd56_0"
 - "1.22.0--r41hc0cfd56_2"
 - "1.20.0--r41hd029910_0"
 - "1.18.0--r40hd029910_1"
 - "1.16.0--r40h037d062_0"
 - "1.26.0--r42ha9d7317_1"
 - "1.28.0--r43ha9d7317_0"
 - "1.30.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bacon"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bacon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bacon", "latest": {"1.30.0--r43ha9d7317_0": "sha256:ce0e9328c7b8e5267973af431b0e1358aa37bbf9c3ae39ece1adfd27016f7e8e"}, "tags": {"1.8.0--r351h470a237_0": "sha256:e5c781d246e15de32735f03940a8b95a4b9a1592ed3d73d10fae1138c3abe75e", "1.26.0--r42hc0cfd56_0": "sha256:93884ea1f691e5de3a9534d387407c08ec838e5ef92a375addf55af32ff6b8ab", "1.22.0--r41hc0cfd56_2": "sha256:da59ba3e085e68d5f4bde0f201f533e556ae2b17d7ea31865aa3439f7fa9d6f4", "1.20.0--r41hd029910_0": "sha256:6e1e4219fa71ce5c3e30e9eea5e91dd6823cd6584842143ad4dc5c4c0998c5ce", "1.18.0--r40hd029910_1": "sha256:1aadf04c6d8a8149383901558e1df7797ca4959fb2ab9ee899cf86fe72e52a82", "1.16.0--r40h037d062_0": "sha256:3c32104ec41b42f8d2f58836bc7ed209ad280d144c17563a9f5b83ac1b122bb9", "1.26.0--r42ha9d7317_1": "sha256:6232efdae20b28a605157190329ce0ee9cf1061a0ab694bbbb08770c58a3af37", "1.28.0--r43ha9d7317_0": "sha256:c7f491459fdc8df219fa281e06b631b1431135c9ba76b5f61955c9171913a705", "1.30.0--r43ha9d7317_0": "sha256:ce0e9328c7b8e5267973af431b0e1358aa37bbf9c3ae39ece1adfd27016f7e8e"}, "docker": "quay.io/biocontainers/bioconductor-bacon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bacon.
shpc-registry automated BioContainers addition for bioconductor-bacon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bacon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bacon:1.30.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bacon/1.30.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-bacon/1.30.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bacon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bacon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bacon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bacon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bacon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bacon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bacon

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