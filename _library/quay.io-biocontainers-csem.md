---
layout: container
name:  "quay.io/biocontainers/csem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/csem/container.yaml"
updated_at: "2026-06-23 16:44:44.055159"
latest: "2.4--h47932c3_1"
container_url: "https://biocontainers.pro/tools/csem"
aliases:
 - "csem"
 - "csem-bam-processor"
 - "csem-bam2wig"
 - "csem-generate-input"
 - "run-csem"
versions:
 - "2.4--h47932c3_0"
 - "2.4--h47932c3_1"
description: "singularity registry hpc automated addition for csem"
config: {"url": "https://biocontainers.pro/tools/csem", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for csem", "latest": {"2.4--h47932c3_1": "sha256:fef21cc8b9478bbb3b9104f2afebee79f8e63628d2b8ab6f6e0dda094c641cdd"}, "tags": {"2.4--h47932c3_0": "sha256:99d1f09da122beeb76bd0dd4dbd2931f460b030bae039b1eeb3f66f7a49fce95", "2.4--h47932c3_1": "sha256:fef21cc8b9478bbb3b9104f2afebee79f8e63628d2b8ab6f6e0dda094c641cdd"}, "docker": "quay.io/biocontainers/csem", "aliases": {"csem": "/usr/local/bin/csem", "csem-bam-processor": "/usr/local/bin/csem-bam-processor", "csem-bam2wig": "/usr/local/bin/csem-bam2wig", "csem-generate-input": "/usr/local/bin/csem-generate-input", "run-csem": "/usr/local/bin/run-csem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csem.
singularity registry hpc automated addition for csem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csem:2.4--h47932c3_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csem/2.4--h47932c3_1
$ module help quay.io/biocontainers/csem/2.4--h47932c3_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csem

```bash
$ singularity exec <container> /usr/local/bin/csem
$ podman run --it --rm --entrypoint /usr/local/bin/csem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csem-bam-processor

```bash
$ singularity exec <container> /usr/local/bin/csem-bam-processor
$ podman run --it --rm --entrypoint /usr/local/bin/csem-bam-processor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csem-bam-processor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csem-bam2wig

```bash
$ singularity exec <container> /usr/local/bin/csem-bam2wig
$ podman run --it --rm --entrypoint /usr/local/bin/csem-bam2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csem-bam2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csem-generate-input

```bash
$ singularity exec <container> /usr/local/bin/csem-generate-input
$ podman run --it --rm --entrypoint /usr/local/bin/csem-generate-input   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csem-generate-input   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-csem

```bash
$ singularity exec <container> /usr/local/bin/run-csem
$ podman run --it --rm --entrypoint /usr/local/bin/run-csem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-csem   -v ${PWD} -w ${PWD} <container> -c " $@"
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