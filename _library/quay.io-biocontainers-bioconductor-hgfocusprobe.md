---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgfocusprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgfocusprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgfocusprobe/container.yaml"
updated_at: "2024-12-19 04:42:32.301960"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgfocusprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgfocusprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgfocusprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgfocusprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:08d0284f18c5b23b8839bca46eac4e1f9d0375e00aaa9d5ad0b976d7572bc1b7"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:28ead63e2526d2e6bffef6d956db470c4573ca96efcd4125f4061ce7e5b4ae38", "2.18.0--r42hdfd78af_10": "sha256:e813c52395ba24ad7ad0583dc8a5c4425ea1f6f3f87a591f95e871d771e9de24", "2.18.0--r43hdfd78af_11": "sha256:c42c382e9a1d661e520cfcf71f68f91405447a31afef2210bab1926e53783c43", "2.18.0--r43hdfd78af_12": "sha256:08d0284f18c5b23b8839bca46eac4e1f9d0375e00aaa9d5ad0b976d7572bc1b7"}, "docker": "quay.io/biocontainers/bioconductor-hgfocusprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgfocusprobe.
shpc-registry automated BioContainers addition for bioconductor-hgfocusprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgfocusprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgfocusprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgfocusprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgfocusprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgfocusprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgfocusprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgfocusprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgfocusprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgfocusprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgfocusprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgfocusprobe

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