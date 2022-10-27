---
layout: container
name:  "quay.io/biocontainers/sinto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sinto/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sinto/container.yaml"
updated_at: "2022-10-27 00:22:14.817114"
latest: "0.9.0--pyh086e186_0"
container_url: "https://biocontainers.pro/tools/sinto"
aliases:
 - "sinto"
versions:
 - "0.9.0--pyh086e186_0"
description: "shpc-registry automated BioContainers addition for sinto"
config: {"url": "https://biocontainers.pro/tools/sinto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sinto", "latest": {"0.9.0--pyh086e186_0": "sha256:0b1b32fc0db0891d7a3914628a7e6e4a5411eb5774a589daa15c61d2634397ca"}, "tags": {"0.9.0--pyh086e186_0": "sha256:0b1b32fc0db0891d7a3914628a7e6e4a5411eb5774a589daa15c61d2634397ca"}, "docker": "quay.io/biocontainers/sinto", "aliases": {"sinto": "/usr/local/bin/sinto"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sinto.
shpc-registry automated BioContainers addition for sinto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sinto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sinto:0.9.0--pyh086e186_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sinto/0.9.0--pyh086e186_0
$ module help quay.io/biocontainers/sinto/0.9.0--pyh086e186_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sinto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sinto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sinto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sinto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sinto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sinto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sinto

```bash
$ singularity exec <container> /usr/local/bin/sinto
$ podman run --it --rm --entrypoint /usr/local/bin/sinto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sinto   -v ${PWD} -w ${PWD} <container> -c " $@"
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