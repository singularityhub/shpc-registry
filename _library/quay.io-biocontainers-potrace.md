---
layout: container
name:  "quay.io/biocontainers/potrace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/potrace/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/potrace/container.yaml"
updated_at: "2025-03-11 03:17:29.739742"
latest: "1.11--h577a1d6_7"
container_url: "https://biocontainers.pro/tools/potrace"
aliases:
 - "mkbitmap"
 - "potrace"
versions:
 - "1.11--h7132678_4"
 - "1.11--he4a0461_6"
 - "1.11--h577a1d6_7"
description: "shpc-registry automated BioContainers addition for potrace"
config: {"url": "https://biocontainers.pro/tools/potrace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for potrace", "latest": {"1.11--h577a1d6_7": "sha256:bd4b8bc9efc5ef056440dae51f91801262bbfb5c54c8401dbeacffaaed8fb56d"}, "tags": {"1.11--h7132678_4": "sha256:de45921cc951741c62b1a39ec9f605b44aac3431aa84636fcbdbe6362d2a4b46", "1.11--he4a0461_6": "sha256:49dac6feebafdde82f88a845db0d5c7f95854d033a0b4b1bb0bbb23f80f69b97", "1.11--h577a1d6_7": "sha256:bd4b8bc9efc5ef056440dae51f91801262bbfb5c54c8401dbeacffaaed8fb56d"}, "docker": "quay.io/biocontainers/potrace", "aliases": {"mkbitmap": "/usr/local/bin/mkbitmap", "potrace": "/usr/local/bin/potrace"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/potrace.
shpc-registry automated BioContainers addition for potrace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/potrace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/potrace:1.11--h577a1d6_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/potrace/1.11--h577a1d6_7
$ module help quay.io/biocontainers/potrace/1.11--h577a1d6_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### potrace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### potrace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### potrace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### potrace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### potrace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### potrace-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mkbitmap

```bash
$ singularity exec <container> /usr/local/bin/mkbitmap
$ podman run --it --rm --entrypoint /usr/local/bin/mkbitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkbitmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### potrace

```bash
$ singularity exec <container> /usr/local/bin/potrace
$ podman run --it --rm --entrypoint /usr/local/bin/potrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/potrace   -v ${PWD} -w ${PWD} <container> -c " $@"
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