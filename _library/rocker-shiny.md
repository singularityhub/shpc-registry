---
layout: container
name:  "rocker/shiny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/shiny/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/shiny/container.yaml"
updated_at: "2025-02-21 02:52:12.041547"
latest: "4.4.2"
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
 - "4.3.1"
 - "4.3.2"
 - "4.3.3"
 - "4.4.0"
 - "4.4.1"
 - "4.4.2"
description: "Docker image with R + Shiny."
config: {"docker": "rocker/shiny", "url": "https://hub.docker.com/r/rocker/shiny", "maintainer": "@vsoch", "description": "Docker image with R + Shiny.", "latest": {"4.4.2": "sha256:4872209c141fde6caa4249d624e666e8749aa4da08f49acd82aecf689e2bd32c"}, "tags": {"4.2.2": "sha256:5a01f59096c1b86e283cf9756d8badf8f1760a565b82b0c02112f7ffabb81b8b", "3.6.3": "sha256:212182dd244edd0380f2f76521f2c10405504b632696852d776402585eb68625", "4.1.3": "sha256:2e13901182cd775624431cfb906c3b0c90eee1b824a102a213cc3f136dcbb9fa", "4.0.5": "sha256:4e68438dc5a553b440e148ba04832007a6949361c4c9796c042599a7b2444285", "4.2.3": "sha256:70fa9473de1c98d2f4e5393af76733db3a7e7f5d813664dda58b143d78a34dd5", "4.3.0": "sha256:15990f645e367bc020233dc6b4f929f98c22c2fb5a5413a294e14d5cd1fe3d38", "4.3.1": "sha256:c917230d2ebcae772ffae1192e06ba04125a6b512071d9c36d8e7155d4c8667a", "4.3.2": "sha256:882ffd767bc97fa310da50137f7539f548978a354b5e9d1e87b0f6741b81a44b", "4.3.3": "sha256:2552384e06381be996df2cd2d72020bf1c997e929d55e2826a9f9cfbe8d5dc69", "4.4.0": "sha256:a76bfc201e36b5da0727d99737a2e7bf0d9df56e812c6fb08774c59f17dac048", "4.4.1": "sha256:c50810df4747090eceb2f94da767ad27ad92dc78f96440577cfb8dbe46431026", "4.4.2": "sha256:4872209c141fde6caa4249d624e666e8749aa4da08f49acd82aecf689e2bd32c"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"rocker-shiny-run": "/bin/bash", "shiny-server": "/opt/shiny-server"}}
---

This module is a singularity container wrapper for rocker/shiny.
Docker image with R + Shiny.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/shiny
```

Or a specific version:

```bash
$ shpc install rocker/shiny:4.4.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/shiny/4.4.2
$ module help rocker/shiny/4.4.2
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