---
layout: container
name:  "quay.io/biocontainers/sylph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sylph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sylph/container.yaml"
updated_at: "2025-04-20 03:23:16.466405"
latest: "0.8.1--ha6fb395_0"
container_url: "https://biocontainers.pro/tools/sylph"
aliases:
 - "sylph"
versions:
 - "0.0.2--h4ac6f70_0"
 - "0.1.0--h4ac6f70_0"
 - "0.0.3--h4ac6f70_0"
 - "0.3.0--h4ac6f70_0"
 - "0.2.0--h4ac6f70_0"
 - "0.4.0--h4ac6f70_0"
 - "0.4.1--h4ac6f70_0"
 - "0.5.1--h4ac6f70_0"
 - "0.6.0--h4ac6f70_0"
 - "0.6.1--h4ac6f70_0"
 - "0.7.0--h919a2d8_0"
 - "0.7.0--ha6fb395_2"
 - "0.8.0--ha6fb395_0"
 - "0.8.1--ha6fb395_0"
description: "singularity registry hpc automated addition for sylph"
config: {"url": "https://biocontainers.pro/tools/sylph", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sylph", "latest": {"0.8.1--ha6fb395_0": "sha256:45dceee15ba690023312509b1947d7e194af84f76c726da63d78ec15892da284"}, "tags": {"0.0.2--h4ac6f70_0": "sha256:e6fa763794572d58c513e5111e11c9950003ce74b35bb321a90b89c321acd37c", "0.1.0--h4ac6f70_0": "sha256:ec01e69564473eeef93ebc9298537799d0cc085eef512f11fcc3279657e8f566", "0.0.3--h4ac6f70_0": "sha256:56ca8c3397cba26b1b830de76fdadb70f46b05a3e27e7dcc64b8efb8e39955e9", "0.3.0--h4ac6f70_0": "sha256:7d311510ed8d5bf26e1694784996714a7ac5e07fefed2d0f831c9b9322438c86", "0.2.0--h4ac6f70_0": "sha256:cf3a0e01b61430b60ae1c024f5deaa9f616f1d5d31f279dc3425e36b5f62accc", "0.4.0--h4ac6f70_0": "sha256:899e49ed128581c49a9989d4fe118f8c06a10a2e5930c4f55596bf4a8ab95653", "0.4.1--h4ac6f70_0": "sha256:4b563e9fc1b63d60f90b14553528e5291f6c0e5b8be1598dd25d6c7c10fbb968", "0.5.1--h4ac6f70_0": "sha256:d79089b75c1b9a1ea887cd7390fcfde178410e4a2c85337918c45804d7a225fd", "0.6.0--h4ac6f70_0": "sha256:89ecfcca12b8d360c13a846c30e008d4fef8ab7153afd51402b0fe33bfe063ec", "0.6.1--h4ac6f70_0": "sha256:781d32f6e29a5ef8140f0f459f645525f43d021d0b5388e6caf2071d2e33ffd4", "0.7.0--h919a2d8_0": "sha256:1d156c99bfbe04beadf200f7890e568990e3dad48eff37747fbf81408a6b601c", "0.7.0--ha6fb395_2": "sha256:3db846642677fcfee12c027b71728616d685cc921375c240359e8a4a01ea63b0", "0.8.0--ha6fb395_0": "sha256:b59b6fd4707351a0c392bd6178ab89430e4fd889f708b1b8d1f0fba25419bea5", "0.8.1--ha6fb395_0": "sha256:45dceee15ba690023312509b1947d7e194af84f76c726da63d78ec15892da284"}, "docker": "quay.io/biocontainers/sylph", "aliases": {"sylph": "/usr/local/bin/sylph"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sylph.
singularity registry hpc automated addition for sylph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sylph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sylph:0.8.1--ha6fb395_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sylph/0.8.1--ha6fb395_0
$ module help quay.io/biocontainers/sylph/0.8.1--ha6fb395_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sylph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sylph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sylph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sylph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sylph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sylph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sylph

```bash
$ singularity exec <container> /usr/local/bin/sylph
$ podman run --it --rm --entrypoint /usr/local/bin/sylph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sylph   -v ${PWD} -w ${PWD} <container> -c " $@"
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