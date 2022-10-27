---
layout: container
name:  "quay.io/biocontainers/checkm-genome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/checkm-genome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/checkm-genome/container.yaml"
updated_at: "2022-10-27 00:56:17.537539"
latest: "1.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/checkm-genome"
aliases:
 - ".checkm-genome-post-link.sh"
 - ".checkm-genome-pre-unlink.sh"
 - "checkm"
versions:
 - "1.2.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for checkm-genome"
config: {"url": "https://biocontainers.pro/tools/checkm-genome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for checkm-genome", "latest": {"1.2.1--pyhdfd78af_0": "sha256:17878d360b193a74c71b35a0f3d1dd979c833d6e49e67eb9c2d7001f4b6d3eeb"}, "tags": {"1.2.1--pyhdfd78af_0": "sha256:17878d360b193a74c71b35a0f3d1dd979c833d6e49e67eb9c2d7001f4b6d3eeb"}, "docker": "quay.io/biocontainers/checkm-genome", "aliases": {".checkm-genome-post-link.sh": "/usr/local/bin/.checkm-genome-post-link.sh", ".checkm-genome-pre-unlink.sh": "/usr/local/bin/.checkm-genome-pre-unlink.sh", "checkm": "/usr/local/bin/checkm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/checkm-genome.
shpc-registry automated BioContainers addition for checkm-genome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/checkm-genome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/checkm-genome:1.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/checkm-genome/1.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/checkm-genome/1.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### checkm-genome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### checkm-genome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### checkm-genome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### checkm-genome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### checkm-genome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### checkm-genome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .checkm-genome-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.checkm-genome-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.checkm-genome-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.checkm-genome-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .checkm-genome-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.checkm-genome-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.checkm-genome-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.checkm-genome-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
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