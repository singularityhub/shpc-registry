---
layout: container
name:  "quay.io/biocontainers/r-nbpseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-nbpseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-nbpseq/container.yaml"
updated_at: "2025-02-07 02:52:29.705282"
latest: "0.3.1--r44h5ef9028_4"
container_url: "https://biocontainers.pro/tools/r-nbpseq"

versions:
 - "0.3.1--r41h73dbb54_0"
 - "0.3.1--r42h73dbb54_1"
 - "0.3.1--r42h56115f1_2"
 - "0.3.1--r43h56115f1_3"
 - "0.3.1--r44h5ef9028_4"
description: "shpc-registry automated BioContainers addition for r-nbpseq"
config: {"url": "https://biocontainers.pro/tools/r-nbpseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-nbpseq", "latest": {"0.3.1--r44h5ef9028_4": "sha256:f0b148d39adb2d9b48aa22a84598d83ccda2299a47fc2825c5705db70ee10ebb"}, "tags": {"0.3.1--r41h73dbb54_0": "sha256:ab30ce73564cc8e4c2bc7e96fe80ef86fd3805b2ec98d699ace24b99b2383fcd", "0.3.1--r42h73dbb54_1": "sha256:3f497fbf5186d9ffe320bed5e38bd90c6b1294befdb385ace296c0da174794ba", "0.3.1--r42h56115f1_2": "sha256:bbfde707be1f32da8ca5ca735019a85a79c4a5452dc22b54059ad6c08fba62a2", "0.3.1--r43h56115f1_3": "sha256:c77415737a2ed05172618180e89f79837b6310e9eb05472f7173139d1965476d", "0.3.1--r44h5ef9028_4": "sha256:f0b148d39adb2d9b48aa22a84598d83ccda2299a47fc2825c5705db70ee10ebb"}, "docker": "quay.io/biocontainers/r-nbpseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-nbpseq.
shpc-registry automated BioContainers addition for r-nbpseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-nbpseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-nbpseq:0.3.1--r44h5ef9028_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-nbpseq/0.3.1--r44h5ef9028_4
$ module help quay.io/biocontainers/r-nbpseq/0.3.1--r44h5ef9028_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-nbpseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-nbpseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-nbpseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-nbpseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-nbpseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-nbpseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-nbpseq

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