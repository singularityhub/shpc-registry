---
layout: container
name:  "quay.io/biocontainers/extracthifi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/extracthifi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/extracthifi/container.yaml"
updated_at: "2025-10-26 03:24:33.388066"
latest: "1.0.0--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/extracthifi"
aliases:
 - "extracthifi"
versions:
 - "1.0.0--0"
 - "1.0.0--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for extracthifi"
config: {"url": "https://biocontainers.pro/tools/extracthifi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for extracthifi", "latest": {"1.0.0--h9ee0642_1": "sha256:9aaf86402fe56992af469292f7694e5fe4584283a64df57b4d565da92ad843c6"}, "tags": {"1.0.0--0": "sha256:a46b2bff402296dc5ea06a767ae464112f756552b7df67a9c0b815221d3720fa", "1.0.0--h9ee0642_1": "sha256:9aaf86402fe56992af469292f7694e5fe4584283a64df57b4d565da92ad843c6"}, "docker": "quay.io/biocontainers/extracthifi", "aliases": {"extracthifi": "/usr/local/bin/extracthifi"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/extracthifi.
shpc-registry automated BioContainers addition for extracthifi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/extracthifi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/extracthifi:1.0.0--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/extracthifi/1.0.0--h9ee0642_1
$ module help quay.io/biocontainers/extracthifi/1.0.0--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### extracthifi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### extracthifi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### extracthifi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### extracthifi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### extracthifi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### extracthifi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extracthifi

```bash
$ singularity exec <container> /usr/local/bin/extracthifi
$ podman run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
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