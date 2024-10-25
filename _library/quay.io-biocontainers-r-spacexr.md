---
layout: container
name:  "quay.io/biocontainers/r-spacexr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-spacexr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-spacexr/container.yaml"
updated_at: "2024-10-25 03:21:23.325677"
latest: "2.2.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-spacexr"
aliases:
 - "pandoc-lua"
 - "pandoc-server"
 - "hb-info"
 - "pandoc"
 - "tjbench"
versions:
 - "2.2.1--r43hdfd78af_0"
description: "singularity registry hpc automated addition for r-spacexr"
config: {"url": "https://biocontainers.pro/tools/r-spacexr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-spacexr", "latest": {"2.2.1--r43hdfd78af_0": "sha256:95a4352354088a3ea1f7983d97a3d264cbe083d3444713251ce49717f54ec83a"}, "tags": {"2.2.1--r43hdfd78af_0": "sha256:95a4352354088a3ea1f7983d97a3d264cbe083d3444713251ce49717f54ec83a"}, "docker": "quay.io/biocontainers/r-spacexr", "aliases": {"pandoc-lua": "/usr/local/bin/pandoc-lua", "pandoc-server": "/usr/local/bin/pandoc-server", "hb-info": "/usr/local/bin/hb-info", "pandoc": "/usr/local/bin/pandoc", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-spacexr.
singularity registry hpc automated addition for r-spacexr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-spacexr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-spacexr:2.2.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-spacexr/2.2.1--r43hdfd78af_0
$ module help quay.io/biocontainers/r-spacexr/2.2.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-spacexr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-spacexr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-spacexr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-spacexr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-spacexr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-spacexr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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