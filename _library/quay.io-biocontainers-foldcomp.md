---
layout: container
name:  "quay.io/biocontainers/foldcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/foldcomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/foldcomp/container.yaml"
updated_at: "2023-06-12 03:31:43.150944"
latest: "0.0.5--h5b5514e_1"
container_url: "https://biocontainers.pro/tools/foldcomp"
aliases:
 - "foldcomp"
versions:
 - "0.0.2--h5b5514e_0"
 - "0.0.4--h5b5514e_0"
 - "0.0.5--h5b5514e_1"
description: "singularity registry hpc automated addition for foldcomp"
config: {"url": "https://biocontainers.pro/tools/foldcomp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for foldcomp", "latest": {"0.0.5--h5b5514e_1": "sha256:9deaa7d3f8dd2d2a0d639ec8708f21d858a663dff964c29d17640b3de1957445"}, "tags": {"0.0.2--h5b5514e_0": "sha256:584a4c9cc9bcdb5c75f23d8621f827e6ac48013d4b00b16afc20815828cb7608", "0.0.4--h5b5514e_0": "sha256:e567e5da15a5e3d90327613333984776dfba0b8e9eb396d036fecf9b241563c2", "0.0.5--h5b5514e_1": "sha256:9deaa7d3f8dd2d2a0d639ec8708f21d858a663dff964c29d17640b3de1957445"}, "docker": "quay.io/biocontainers/foldcomp", "aliases": {"foldcomp": "/usr/local/bin/foldcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/foldcomp.
singularity registry hpc automated addition for foldcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/foldcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/foldcomp:0.0.5--h5b5514e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/foldcomp/0.0.5--h5b5514e_1
$ module help quay.io/biocontainers/foldcomp/0.0.5--h5b5514e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### foldcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### foldcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### foldcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### foldcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### foldcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### foldcomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### foldcomp

```bash
$ singularity exec <container> /usr/local/bin/foldcomp
$ podman run --it --rm --entrypoint /usr/local/bin/foldcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
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