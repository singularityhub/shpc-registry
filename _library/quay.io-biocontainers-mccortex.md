---
layout: container
name:  "quay.io/biocontainers/mccortex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mccortex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mccortex/container.yaml"
updated_at: "2024-05-13 02:35:36.460688"
latest: "1.0--hd03093a_5"
container_url: "https://biocontainers.pro/tools/mccortex"
aliases:
 - "mccortex"
 - "mccortex127"
 - "mccortex31"
 - "mccortex63"
 - "mccortex95"
versions:
 - "1.0--hd03093a_5"
description: "shpc-registry automated BioContainers addition for mccortex"
config: {"url": "https://biocontainers.pro/tools/mccortex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mccortex", "latest": {"1.0--hd03093a_5": "sha256:21b784cc4ff2cef9ff84aa966fc88b0f496d763cbfe3e6cd406ac59eccb980a0"}, "tags": {"1.0--hd03093a_5": "sha256:21b784cc4ff2cef9ff84aa966fc88b0f496d763cbfe3e6cd406ac59eccb980a0"}, "docker": "quay.io/biocontainers/mccortex", "aliases": {"mccortex": "/usr/local/bin/mccortex", "mccortex127": "/usr/local/bin/mccortex127", "mccortex31": "/usr/local/bin/mccortex31", "mccortex63": "/usr/local/bin/mccortex63", "mccortex95": "/usr/local/bin/mccortex95"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mccortex.
shpc-registry automated BioContainers addition for mccortex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mccortex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mccortex:1.0--hd03093a_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mccortex/1.0--hd03093a_5
$ module help quay.io/biocontainers/mccortex/1.0--hd03093a_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mccortex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mccortex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mccortex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mccortex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mccortex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mccortex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mccortex

```bash
$ singularity exec <container> /usr/local/bin/mccortex
$ podman run --it --rm --entrypoint /usr/local/bin/mccortex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mccortex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mccortex127

```bash
$ singularity exec <container> /usr/local/bin/mccortex127
$ podman run --it --rm --entrypoint /usr/local/bin/mccortex127   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mccortex127   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mccortex31

```bash
$ singularity exec <container> /usr/local/bin/mccortex31
$ podman run --it --rm --entrypoint /usr/local/bin/mccortex31   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mccortex31   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mccortex63

```bash
$ singularity exec <container> /usr/local/bin/mccortex63
$ podman run --it --rm --entrypoint /usr/local/bin/mccortex63   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mccortex63   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mccortex95

```bash
$ singularity exec <container> /usr/local/bin/mccortex95
$ podman run --it --rm --entrypoint /usr/local/bin/mccortex95   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mccortex95   -v ${PWD} -w ${PWD} <container> -c " $@"
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