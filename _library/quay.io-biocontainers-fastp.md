---
layout: container
name:  "quay.io/biocontainers/fastp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastp/container.yaml"
updated_at: "2025-04-09 03:40:32.622505"
latest: "0.24.0--heae3180_1"
container_url: "https://biocontainers.pro/tools/fastp"
aliases:
 - "fastp"
versions:
 - "0.22.0--h2e03b76_0"
 - "0.23.2--h5f740d0_3"
 - "0.23.4--h5f740d0_0"
 - "0.23.4--hadf994f_2"
 - "0.23.4--hadf994f_3"
 - "0.23.4--h125f33a_4"
 - "0.23.4--h125f33a_5"
 - "0.24.0--heae3180_1"
description: "shpc-registry automated BioContainers addition for fastp"
config: {"url": "https://biocontainers.pro/tools/fastp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastp", "latest": {"0.24.0--heae3180_1": "sha256:fe647f76dbda3af58a4e159ec4662b7c11f29ee65a44a9b8f43ba018fee8e8a5"}, "tags": {"0.22.0--h2e03b76_0": "sha256:e94097ae4ca17394b35d59a20d9a9f6d8972992bd47d1783f00c26e86ca82c2b", "0.23.2--h5f740d0_3": "sha256:2489fe56260bde05bdf72a8ead4892033b9a05dc4525affb909405bea7839d1b", "0.23.4--h5f740d0_0": "sha256:b635334b6bb25eba14d0b8c240a45a51234984247d79715f8cd0b7959df850c2", "0.23.4--hadf994f_2": "sha256:1fcefd00ab08856727a2cfe097d88eb400829d449114d6939b68cdf67b7b7d54", "0.23.4--hadf994f_3": "sha256:4b218ce3d002b8fbed0cd2be1df4255969203f4c233408c0b3939a873e8b46d0", "0.23.4--h125f33a_4": "sha256:4d3241f1ec6f67faf152a1602df1bf0249278ec8907bf2fc0eeeb2f5eec12707", "0.23.4--h125f33a_5": "sha256:e497f7d3518f4ea10ec03d0e6f9f311d5f8a6486e94d6e0e2847b257f3a6aa6c", "0.24.0--heae3180_1": "sha256:fe647f76dbda3af58a4e159ec4662b7c11f29ee65a44a9b8f43ba018fee8e8a5"}, "docker": "quay.io/biocontainers/fastp", "aliases": {"fastp": "/usr/local/bin/fastp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastp.
shpc-registry automated BioContainers addition for fastp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastp:0.24.0--heae3180_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastp/0.24.0--heae3180_1
$ module help quay.io/biocontainers/fastp/0.24.0--heae3180_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
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