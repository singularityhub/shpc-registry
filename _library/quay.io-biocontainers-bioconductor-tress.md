---
layout: container
name:  "quay.io/biocontainers/bioconductor-tress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tress/container.yaml"
updated_at: "2026-01-26 04:46:36.788575"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tress"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tress"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tress", "latest": {"1.12.0--r44hdfd78af_0": "sha256:e2111d0c480c230c4bda74c8f691059c860f1a5709b0529a8cb8e41eb5459474"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:b7ae25fa223fd8ff805c8939711cd7e680000d9dd77e21e7cbb135ec8377dbce", "1.4.0--r42hdfd78af_0": "sha256:9478ea4946efe543cb892f4f0f6a7ebbc3c499c25bc8c0fc0d0728bf0d3a9a15", "1.6.0--r43hdfd78af_0": "sha256:d3b8bbf26a4964d85f717d90d9df37f57f8f1a594b5098e28a0bea6a12abd981", "1.8.0--r43hdfd78af_0": "sha256:b21dd3aa9b7040589a0ce229f5c45590c5cbb426942a46a7eafed3fa00c64f12", "1.12.0--r44hdfd78af_0": "sha256:e2111d0c480c230c4bda74c8f691059c860f1a5709b0529a8cb8e41eb5459474"}, "docker": "quay.io/biocontainers/bioconductor-tress"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tress.
shpc-registry automated BioContainers addition for bioconductor-tress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tress:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tress/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tress/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tress

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