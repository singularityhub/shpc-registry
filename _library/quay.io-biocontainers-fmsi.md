---
layout: container
name:  "quay.io/biocontainers/fmsi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fmsi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fmsi/container.yaml"
updated_at: "2025-11-21 03:47:21.784258"
latest: "0.4.0--h077b44d_0"
container_url: "https://biocontainers.pro/tools/fmsi"
aliases:
 - "fmsi"
versions:
 - "0.2.4--hdcf5f25_0"
 - "0.3.1--hdcf5f25_0"
 - "0.2.4--hdcf5f25_1"
 - "0.3.1--h077b44d_1"
 - "0.4.0--h077b44d_0"
description: "singularity registry hpc automated addition for fmsi"
config: {"url": "https://biocontainers.pro/tools/fmsi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fmsi", "latest": {"0.4.0--h077b44d_0": "sha256:4c1ecaf3bb55779ce3d2b07f2107a1187af7a2a40696235e69ce7d9c92c3f24b"}, "tags": {"0.2.4--hdcf5f25_0": "sha256:4212e1972eff71367528d7efd4b107cc52a91d60e43e4a018b79798f67d2118d", "0.3.1--hdcf5f25_0": "sha256:82a74477f66d00c17ea2b7114bd6fd7d42702c179938c2d9cc6395be2bbe1be7", "0.2.4--hdcf5f25_1": "sha256:f33f6d33ce5d1bfde0ee18b79bb01bdcea9a0a9f77d86bc5f3151a2724967419", "0.3.1--h077b44d_1": "sha256:72ff5e86e89410f338db345da39d4666c1ebee47baaa4f5991024c128e7a8627", "0.4.0--h077b44d_0": "sha256:4c1ecaf3bb55779ce3d2b07f2107a1187af7a2a40696235e69ce7d9c92c3f24b"}, "docker": "quay.io/biocontainers/fmsi", "aliases": {"fmsi": "/usr/local/bin/fmsi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fmsi.
singularity registry hpc automated addition for fmsi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fmsi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fmsi:0.4.0--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fmsi/0.4.0--h077b44d_0
$ module help quay.io/biocontainers/fmsi/0.4.0--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fmsi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fmsi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fmsi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fmsi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fmsi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fmsi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fmsi

```bash
$ singularity exec <container> /usr/local/bin/fmsi
$ podman run --it --rm --entrypoint /usr/local/bin/fmsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fmsi   -v ${PWD} -w ${PWD} <container> -c " $@"
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