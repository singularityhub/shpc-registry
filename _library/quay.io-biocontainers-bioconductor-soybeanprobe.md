---
layout: container
name:  "quay.io/biocontainers/bioconductor-soybeanprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-soybeanprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-soybeanprobe/container.yaml"
updated_at: "2024-06-19 03:17:02.151063"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-soybeanprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-soybeanprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-soybeanprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-soybeanprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:59c7d1d2ee7d5cef2e81a648886b0f3a2263a4aa6d2af799dcc2bc16af61bbb1"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:7359ed7d23d87323de396b142cedc67a4536be4626246e92ede1c4f2115e9737", "2.18.0--r42hdfd78af_10": "sha256:9b04c483828c04bafc13325c589c59a53ea3b3916dc1b329371847c355f16871", "2.18.0--r43hdfd78af_11": "sha256:faa603a0e3a2b5d6ea8530250687eb17dd9443d96f2da057da58fd21f1f1df1b", "2.18.0--r43hdfd78af_12": "sha256:59c7d1d2ee7d5cef2e81a648886b0f3a2263a4aa6d2af799dcc2bc16af61bbb1"}, "docker": "quay.io/biocontainers/bioconductor-soybeanprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-soybeanprobe.
shpc-registry automated BioContainers addition for bioconductor-soybeanprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-soybeanprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-soybeanprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-soybeanprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-soybeanprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-soybeanprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-soybeanprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-soybeanprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-soybeanprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-soybeanprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-soybeanprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-soybeanprobe

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