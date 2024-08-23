---
layout: container
name:  "quay.io/biocontainers/bioconductor-h5vc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-h5vc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-h5vc/container.yaml"
updated_at: "2024-08-23 02:40:14.525913"
latest: "2.36.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-h5vc"

versions:
 - "2.28.0--r41hc247a5b_2"
 - "2.32.0--r42hc247a5b_0"
 - "2.32.0--r42hf17093f_1"
 - "2.34.0--r43hf17093f_0"
 - "2.36.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-h5vc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-h5vc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-h5vc", "latest": {"2.36.0--r43hf17093f_0": "sha256:f9a1463bdb013b9aeb4792b4aa8275780699ea070e85f09b79e8d8409342eac7"}, "tags": {"2.28.0--r41hc247a5b_2": "sha256:7d6464937df00f4020ecc81bea94944060f8f022f3396bd0ff524a0ab8e104e6", "2.32.0--r42hc247a5b_0": "sha256:d7c8303b533c2f78df617bfc9bf04c6ea83e9146a3e11be65dd88573200b4364", "2.32.0--r42hf17093f_1": "sha256:5b661ae5a27866f8ce5300e2ce6cdafa2a5f1eafe0f0bccfc5aed490c33892a0", "2.34.0--r43hf17093f_0": "sha256:73a19d8a6378aa8abe1d9a360384db46e31e0e61584914df77f1f441c06983f1", "2.36.0--r43hf17093f_0": "sha256:f9a1463bdb013b9aeb4792b4aa8275780699ea070e85f09b79e8d8409342eac7"}, "docker": "quay.io/biocontainers/bioconductor-h5vc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-h5vc.
shpc-registry automated BioContainers addition for bioconductor-h5vc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-h5vc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-h5vc:2.36.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-h5vc/2.36.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-h5vc/2.36.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-h5vc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h5vc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h5vc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-h5vc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-h5vc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-h5vc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-h5vc

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