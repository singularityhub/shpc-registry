---
layout: container
name:  "quay.io/biocontainers/clippy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clippy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/clippy/container.yaml"
updated_at: "2022-10-29 05:46:58.287996"
latest: "1.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/clippy"
aliases:
 - "clippy"
 - "2to3-3.9"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "brotli"
versions:
 - "1.5.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for clippy"
config: {"url": "https://biocontainers.pro/tools/clippy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clippy", "latest": {"1.5.0--pyhdfd78af_0": "sha256:8a162c87d0992ea655fcb7988a3d5b1354d48e7397b00bf84861519b1f14c303"}, "tags": {"1.5.0--pyhdfd78af_0": "sha256:8a162c87d0992ea655fcb7988a3d5b1354d48e7397b00bf84861519b1f14c303"}, "docker": "quay.io/biocontainers/clippy", "aliases": {"clippy": "/usr/local/bin/clippy", "2to3-3.9": "/usr/local/bin/2to3-3.9", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "brotli": "/usr/local/bin/brotli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clippy.
shpc-registry automated BioContainers addition for clippy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clippy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clippy:1.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clippy/1.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/clippy/1.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clippy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clippy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clippy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clippy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clippy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clippy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clippy

```bash
$ singularity exec <container> /usr/local/bin/clippy
$ podman run --it --rm --entrypoint /usr/local/bin/clippy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clippy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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