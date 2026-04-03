---
layout: container
name:  "quay.io/biocontainers/echtvar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/echtvar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/echtvar/container.yaml"
updated_at: "2026-04-03 05:17:52.425568"
latest: "0.2.3--h443f417_0"
container_url: "https://biocontainers.pro/tools/echtvar"
aliases:
 - "echtvar"
versions:
 - "0.2.2--h443f417_0"
 - "0.2.3--h443f417_0"
description: "singularity registry hpc automated addition for echtvar"
config: {"url": "https://biocontainers.pro/tools/echtvar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for echtvar", "latest": {"0.2.3--h443f417_0": "sha256:ded1ddb38576c95740b1e373ab10713fc0596166d7c3e00001a06959e1a1bbbb"}, "tags": {"0.2.2--h443f417_0": "sha256:8083e3c47b8e5fad1210453ee7b14a53656ab472244e79931e88ba9519039e9d", "0.2.3--h443f417_0": "sha256:ded1ddb38576c95740b1e373ab10713fc0596166d7c3e00001a06959e1a1bbbb"}, "docker": "quay.io/biocontainers/echtvar", "aliases": {"echtvar": "/usr/local/bin/echtvar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/echtvar.
singularity registry hpc automated addition for echtvar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/echtvar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/echtvar:0.2.3--h443f417_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/echtvar/0.2.3--h443f417_0
$ module help quay.io/biocontainers/echtvar/0.2.3--h443f417_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### echtvar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### echtvar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### echtvar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### echtvar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### echtvar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### echtvar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### echtvar

```bash
$ singularity exec <container> /usr/local/bin/echtvar
$ podman run --it --rm --entrypoint /usr/local/bin/echtvar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/echtvar   -v ${PWD} -w ${PWD} <container> -c " $@"
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