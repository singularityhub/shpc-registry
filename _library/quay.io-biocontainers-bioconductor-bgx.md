---
layout: container
name:  "quay.io/biocontainers/bioconductor-bgx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bgx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bgx/container.yaml"
updated_at: "2023-11-22 02:51:24.234519"
latest: "1.66.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bgx"

versions:
 - "1.60.0--r41hc247a5b_2"
 - "1.64.0--r42hc247a5b_0"
 - "1.64.0--r42hf17093f_1"
 - "1.66.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bgx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bgx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bgx", "latest": {"1.66.0--r43hf17093f_0": "sha256:fc89a741cc35e7aa7a289ac769f593d63ff24f7fa3250181efae886229c6d97b"}, "tags": {"1.60.0--r41hc247a5b_2": "sha256:2fdd5f2dbbb89182d18c611ab2fa9630d992ee6f9e4ee2ce194d1af3ceb6bb6a", "1.64.0--r42hc247a5b_0": "sha256:99bcdeae18fcc6ed0afc495a82ece4aa52806f52842619881a661ff6f5ad2d2b", "1.64.0--r42hf17093f_1": "sha256:fc3b7c9f3623dfff28e47e29160fa984a8af88d77f93518f6b727e35386bf86a", "1.66.0--r43hf17093f_0": "sha256:fc89a741cc35e7aa7a289ac769f593d63ff24f7fa3250181efae886229c6d97b"}, "docker": "quay.io/biocontainers/bioconductor-bgx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bgx.
shpc-registry automated BioContainers addition for bioconductor-bgx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bgx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bgx:1.66.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bgx/1.66.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bgx/1.66.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bgx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bgx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bgx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bgx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bgx

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