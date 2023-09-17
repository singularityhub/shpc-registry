---
layout: container
name:  "quay.io/biocontainers/rapifilt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rapifilt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rapifilt/container.yaml"
updated_at: "2023-09-17 00:16:52.477890"
latest: "1.0--h2202e69_5"
container_url: "https://biocontainers.pro/tools/rapifilt"
aliases:
 - "rapifilt"
versions:
 - "1.0--hb97b32f_3"
 - "1.0--hb97b32f_4"
 - "1.0--h2202e69_5"
description: "shpc-registry automated BioContainers addition for rapifilt"
config: {"url": "https://biocontainers.pro/tools/rapifilt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rapifilt", "latest": {"1.0--h2202e69_5": "sha256:0394a95ff52ccf492b788244be4d88500e669bb5aac544c00c50714617eb7dc4"}, "tags": {"1.0--hb97b32f_3": "sha256:6d51fddf2e855204a838fbac981dd5320e61ca1d96cf3ef0a50eba97db21541b", "1.0--hb97b32f_4": "sha256:1dce6346ddccf78dc916397722e3cfa3aa88b9562cb28e2faf3b832b730a17e0", "1.0--h2202e69_5": "sha256:0394a95ff52ccf492b788244be4d88500e669bb5aac544c00c50714617eb7dc4"}, "docker": "quay.io/biocontainers/rapifilt", "aliases": {"rapifilt": "/usr/local/bin/rapifilt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rapifilt.
shpc-registry automated BioContainers addition for rapifilt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rapifilt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rapifilt:1.0--h2202e69_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rapifilt/1.0--h2202e69_5
$ module help quay.io/biocontainers/rapifilt/1.0--h2202e69_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapifilt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapifilt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapifilt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapifilt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapifilt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapifilt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rapifilt

```bash
$ singularity exec <container> /usr/local/bin/rapifilt
$ podman run --it --rm --entrypoint /usr/local/bin/rapifilt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapifilt   -v ${PWD} -w ${PWD} <container> -c " $@"
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