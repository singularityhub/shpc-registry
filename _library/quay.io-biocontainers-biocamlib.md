---
layout: container
name:  "quay.io/biocontainers/biocamlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biocamlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biocamlib/container.yaml"
updated_at: "2024-11-15 03:35:27.081853"
latest: "1.0.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/biocamlib"
aliases:
 - "FASTools"
 - "Octopus"
 - "Parallel"
 - "RC"
versions:
 - "1.0.0--h9ee0642_0"
description: "singularity registry hpc automated addition for biocamlib"
config: {"url": "https://biocontainers.pro/tools/biocamlib", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biocamlib", "latest": {"1.0.0--h9ee0642_0": "sha256:aa5f1ed2f11a681edd0a3c958a5c6cf2ffd6df9e35ee4c063be0d00885a17ade"}, "tags": {"1.0.0--h9ee0642_0": "sha256:aa5f1ed2f11a681edd0a3c958a5c6cf2ffd6df9e35ee4c063be0d00885a17ade"}, "docker": "quay.io/biocontainers/biocamlib", "aliases": {"FASTools": "/usr/local/bin/FASTools", "Octopus": "/usr/local/bin/Octopus", "Parallel": "/usr/local/bin/Parallel", "RC": "/usr/local/bin/RC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biocamlib.
singularity registry hpc automated addition for biocamlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biocamlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biocamlib:1.0.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biocamlib/1.0.0--h9ee0642_0
$ module help quay.io/biocontainers/biocamlib/1.0.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biocamlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biocamlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biocamlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biocamlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biocamlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocamlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FASTools

```bash
$ singularity exec <container> /usr/local/bin/FASTools
$ podman run --it --rm --entrypoint /usr/local/bin/FASTools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FASTools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Octopus

```bash
$ singularity exec <container> /usr/local/bin/Octopus
$ podman run --it --rm --entrypoint /usr/local/bin/Octopus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Octopus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Parallel

```bash
$ singularity exec <container> /usr/local/bin/Parallel
$ podman run --it --rm --entrypoint /usr/local/bin/Parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RC

```bash
$ singularity exec <container> /usr/local/bin/RC
$ podman run --it --rm --entrypoint /usr/local/bin/RC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RC   -v ${PWD} -w ${PWD} <container> -c " $@"
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