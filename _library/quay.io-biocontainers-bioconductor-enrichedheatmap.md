---
layout: container
name:  "quay.io/biocontainers/bioconductor-enrichedheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enrichedheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enrichedheatmap/container.yaml"
updated_at: "2025-09-06 03:22:59.830011"
latest: "1.36.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enrichedheatmap"

versions:
 - "1.24.0--r41hc247a5b_2"
 - "1.27.2--r42hc247a5b_0"
 - "1.27.2--r42hf17093f_1"
 - "1.30.0--r43hf17093f_0"
 - "1.32.0--r43hf17093f_0"
 - "1.36.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enrichedheatmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enrichedheatmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enrichedheatmap", "latest": {"1.36.0--r44he5774e6_0": "sha256:382b278130d405be8068d63434f3b037e3c6528f1fbcd0c9b0aa3cabe708f6f8"}, "tags": {"1.24.0--r41hc247a5b_2": "sha256:60171a93bee57a9c114ea1523e46b5de3d61500b24d5c94f7fb16a38e54078e9", "1.27.2--r42hc247a5b_0": "sha256:300d0907c65fb6750c4ecc9a0d9462d901e66d94ce109e109ede3d98a035b3e3", "1.27.2--r42hf17093f_1": "sha256:a60984339235bda46bf71eef8576468aab29bf63507b058684d1c274e941117f", "1.30.0--r43hf17093f_0": "sha256:647d48e4d5587c9ce27a8d2a7d49c2e634d126da2df191fef118789db6fe6c5f", "1.32.0--r43hf17093f_0": "sha256:5e32e11069bde8c523bdcfc9a6db6006e0358abadaeab0c6f55b8de997f154de", "1.36.0--r44he5774e6_0": "sha256:382b278130d405be8068d63434f3b037e3c6528f1fbcd0c9b0aa3cabe708f6f8"}, "docker": "quay.io/biocontainers/bioconductor-enrichedheatmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enrichedheatmap.
shpc-registry automated BioContainers addition for bioconductor-enrichedheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enrichedheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enrichedheatmap:1.36.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enrichedheatmap/1.36.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-enrichedheatmap/1.36.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enrichedheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enrichedheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enrichedheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enrichedheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enrichedheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enrichedheatmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-enrichedheatmap

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