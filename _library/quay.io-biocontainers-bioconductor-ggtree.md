---
layout: container
name:  "quay.io/biocontainers/bioconductor-ggtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ggtree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ggtree/container.yaml"
updated_at: "2024-02-18 02:56:50.699533"
latest: "3.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ggtree"

versions:
 - "3.2.0--r41hdfd78af_0"
 - "3.6.0--r42hdfd78af_0"
 - "3.8.0--r43hdfd78af_0"
 - "3.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ggtree"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ggtree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ggtree", "latest": {"3.10.0--r43hdfd78af_0": "sha256:cb699cb149d84198362356b785e6a64c21e67fae4892995289db6c5ff5433ef5"}, "tags": {"3.2.0--r41hdfd78af_0": "sha256:a0af31913e626c8c9cba9f1a3c5cb5263cb17b0ca1f4a978a1642702797f1a81", "3.6.0--r42hdfd78af_0": "sha256:9caa20a693c096ea924c989750b583303ded3b304bae5ff802ac48482027d88b", "3.8.0--r43hdfd78af_0": "sha256:a3d8243668a252490603ba6b7b564635ee6cf6bf4e09bf291bd99b9c705307c6", "3.10.0--r43hdfd78af_0": "sha256:cb699cb149d84198362356b785e6a64c21e67fae4892995289db6c5ff5433ef5"}, "docker": "quay.io/biocontainers/bioconductor-ggtree"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ggtree.
shpc-registry automated BioContainers addition for bioconductor-ggtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ggtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ggtree:3.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ggtree/3.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ggtree/3.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ggtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ggtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ggtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ggtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ggtree

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