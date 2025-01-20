---
layout: container
name:  "quay.io/biocontainers/extractpirs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/extractpirs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/extractpirs/container.yaml"
updated_at: "2025-01-20 03:38:19.145723"
latest: "1.0--he941832_2"
container_url: "https://biocontainers.pro/tools/extractpirs"
aliases:
 - "extractPIRs"
versions:
 - "1.0--he941832_2"
description: "shpc-registry automated BioContainers addition for extractpirs"
config: {"url": "https://biocontainers.pro/tools/extractpirs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for extractpirs", "latest": {"1.0--he941832_2": "sha256:452c858fcfbf32530ec4dfa98350f4db9cac4ec1b799cfd98f168383260eb22e"}, "tags": {"1.0--he941832_2": "sha256:452c858fcfbf32530ec4dfa98350f4db9cac4ec1b799cfd98f168383260eb22e"}, "docker": "quay.io/biocontainers/extractpirs", "aliases": {"extractPIRs": "/usr/local/bin/extractPIRs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/extractpirs.
shpc-registry automated BioContainers addition for extractpirs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/extractpirs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/extractpirs:1.0--he941832_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/extractpirs/1.0--he941832_2
$ module help quay.io/biocontainers/extractpirs/1.0--he941832_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### extractpirs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### extractpirs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### extractpirs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### extractpirs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### extractpirs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### extractpirs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extractPIRs

```bash
$ singularity exec <container> /usr/local/bin/extractPIRs
$ podman run --it --rm --entrypoint /usr/local/bin/extractPIRs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractPIRs   -v ${PWD} -w ${PWD} <container> -c " $@"
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