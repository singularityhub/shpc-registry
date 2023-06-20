---
layout: container
name:  "rocker/shiny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/shiny/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/shiny/container.yaml"
updated_at: "2023-06-20 03:24:12.774145"
latest: "4.3.0"
container_url: "https://hub.docker.com/r/rocker/shiny"
aliases:
 - "rocker-shiny-run"
 - "shiny-server"
versions:
 - "4.2.2"
 - "3.6.3"
 - "4.1.3"
 - "4.0.5"
 - "4.2.3"
 - "4.3.0"
description: "Docker image with R + Shiny."
config: {"docker": "rocker/shiny", "url": "https://hub.docker.com/r/rocker/shiny", "maintainer": "@vsoch", "description": "Docker image with R + Shiny.", "latest": {"4.3.0": "sha256:5cbd00208337f4209f9f66215b01d5a87c8b5870178aff2b6d87e190fc13e375"}, "tags": {"4.2.2": "sha256:50a0d8cce493d0107bb45a835bab18a18e8b8fb94d614eebb2ad5cbff7cc4ea8", "3.6.3": "sha256:212182dd244edd0380f2f76521f2c10405504b632696852d776402585eb68625", "4.1.3": "sha256:37a490edbfa70895c37acef6250c0efbe4c77599e66f0cc7cd7ff8ce51847687", "4.0.5": "sha256:7e18a24dcc0bea484caad9b210f2a2cf7e85003d4532429a50c2b967b7e763c9", "4.2.3": "sha256:98615cd5e25a93efb719d73a99258b5985d26bf13021b29a6b7883e254db6cdf", "4.3.0": "sha256:5cbd00208337f4209f9f66215b01d5a87c8b5870178aff2b6d87e190fc13e375"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"rocker-shiny-run": "/bin/bash", "shiny-server": "/opt/shiny-server"}}
---

This module is a singularity container wrapper for rocker/shiny.
Docker image with R + Shiny.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/shiny
```

Or a specific version:

```bash
$ shpc install rocker/shiny:4.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/shiny/4.3.0
$ module help rocker/shiny/4.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shiny-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shiny-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shiny-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shiny-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shiny-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shiny-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rocker-shiny-run

```bash
$ singularity exec <container> /bin/bash
$ podman run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiny-server

```bash
$ singularity exec <container> /opt/shiny-server
$ podman run --it --rm --entrypoint /opt/shiny-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/shiny-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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