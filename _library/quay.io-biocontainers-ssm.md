---
layout: container
name:  "quay.io/biocontainers/ssm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ssm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ssm/container.yaml"
updated_at: "2025-12-12 03:59:04.150949"
latest: "1.4--h503566f_1"
container_url: "https://biocontainers.pro/tools/ssm"
aliases:
 - "x86_64-conda-linux-gnu-pkg-config"
 - "pkg-config"
 - "pkg-config.bin"
versions:
 - "1.4--h503566f_0"
 - "1.4--h503566f_1"
description: "singularity registry hpc automated addition for ssm"
config: {"url": "https://biocontainers.pro/tools/ssm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ssm", "latest": {"1.4--h503566f_1": "sha256:8076b35756146a5a29105b9b2b24c3ad14eaac8a98ec49a5086e6869dba81bcd"}, "tags": {"1.4--h503566f_0": "sha256:d6fa86bff564c981c07ed310a8b9d1b6faf3f507f7e9758c719232ac11f1d4a6", "1.4--h503566f_1": "sha256:8076b35756146a5a29105b9b2b24c3ad14eaac8a98ec49a5086e6869dba81bcd"}, "docker": "quay.io/biocontainers/ssm", "aliases": {"x86_64-conda-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda-linux-gnu-pkg-config", "pkg-config": "/usr/local/bin/pkg-config", "pkg-config.bin": "/usr/local/bin/pkg-config.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ssm.
singularity registry hpc automated addition for ssm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ssm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ssm:1.4--h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ssm/1.4--h503566f_1
$ module help quay.io/biocontainers/ssm/1.4--h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ssm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ssm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ssm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ssm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ssm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ssm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config

```bash
$ singularity exec <container> /usr/local/bin/pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkg-config.bin

```bash
$ singularity exec <container> /usr/local/bin/pkg-config.bin
$ podman run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkg-config.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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