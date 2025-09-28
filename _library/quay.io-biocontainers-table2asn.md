---
layout: container
name:  "quay.io/biocontainers/table2asn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/table2asn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/table2asn/container.yaml"
updated_at: "2025-09-28 03:30:48.547025"
latest: "1.28.1179--he45da00_1"
container_url: "https://biocontainers.pro/tools/table2asn"
aliases:
 - "table2asn"
versions:
 - "1.27.792--h48fe88c_0"
 - "1.28.943--h48fe88c_0"
 - "1.28.1111--h48fe88c_0"
 - "1.28.1179--h48fe88c_0"
 - "1.28.1179--he45da00_1"
description: "singularity registry hpc automated addition for table2asn"
config: {"url": "https://biocontainers.pro/tools/table2asn", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for table2asn", "latest": {"1.28.1179--he45da00_1": "sha256:e579f85913352e173ce0695a5570bf7232f1ae058e1e62a683d16eaf7d4a5168"}, "tags": {"1.27.792--h48fe88c_0": "sha256:dd9bcea5b7b970c2a1824806772f2f691f408b37cc7de6f8559e0380d7245dda", "1.28.943--h48fe88c_0": "sha256:c996a40233e3fc82dcd99da7219a5f2f35b2315bc0505e8d8d0d080ecfdc7fdf", "1.28.1111--h48fe88c_0": "sha256:00cb9799cbd9c066f95c7500f72663c7ff9ca736a73235dcbbf16f7e96b49254", "1.28.1179--h48fe88c_0": "sha256:923de007ca993b8b564796eeef7cc474f8de5c52e6a10849d9ce4b888ded9a3e", "1.28.1179--he45da00_1": "sha256:e579f85913352e173ce0695a5570bf7232f1ae058e1e62a683d16eaf7d4a5168"}, "docker": "quay.io/biocontainers/table2asn", "aliases": {"table2asn": "/usr/local/bin/table2asn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/table2asn.
singularity registry hpc automated addition for table2asn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/table2asn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/table2asn:1.28.1179--he45da00_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/table2asn/1.28.1179--he45da00_1
$ module help quay.io/biocontainers/table2asn/1.28.1179--he45da00_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### table2asn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### table2asn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### table2asn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### table2asn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### table2asn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### table2asn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### table2asn

```bash
$ singularity exec <container> /usr/local/bin/table2asn
$ podman run --it --rm --entrypoint /usr/local/bin/table2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/table2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
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