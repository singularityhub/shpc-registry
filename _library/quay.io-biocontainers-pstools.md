---
layout: container
name:  "quay.io/biocontainers/pstools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pstools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pstools/container.yaml"
updated_at: "2024-05-26 03:08:04.255592"
latest: "0.2a3--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/pstools"
aliases:
 - "pstools"
versions:
 - "0.2a3--hd03093a_1"
 - "0.2a3--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for pstools"
config: {"url": "https://biocontainers.pro/tools/pstools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pstools", "latest": {"0.2a3--hdcf5f25_3": "sha256:1c1d55dc8f8165b8a79f5554ae2aacc138ba289adc48cef75ce1c4a5555e9ebc"}, "tags": {"0.2a3--hd03093a_1": "sha256:1bea826891be47ef54403e8c67f759f35645aca366d73669e99c131014738c35", "0.2a3--hdcf5f25_3": "sha256:1c1d55dc8f8165b8a79f5554ae2aacc138ba289adc48cef75ce1c4a5555e9ebc"}, "docker": "quay.io/biocontainers/pstools", "aliases": {"pstools": "/usr/local/bin/pstools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pstools.
shpc-registry automated BioContainers addition for pstools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pstools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pstools:0.2a3--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pstools/0.2a3--hdcf5f25_3
$ module help quay.io/biocontainers/pstools/0.2a3--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pstools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pstools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pstools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pstools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pstools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pstools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pstools

```bash
$ singularity exec <container> /usr/local/bin/pstools
$ podman run --it --rm --entrypoint /usr/local/bin/pstools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstools   -v ${PWD} -w ${PWD} <container> -c " $@"
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