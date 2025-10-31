---
layout: container
name:  "quay.io/biocontainers/genometester4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genometester4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genometester4/container.yaml"
updated_at: "2025-10-31 04:33:32.858709"
latest: "4.0--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/genometester4"
aliases:
 - "glistcompare"
 - "glistmaker"
 - "glistquery"
 - "gmer_caller"
 - "gmer_counter"
versions:
 - "4.0--hec16e2b_4"
 - "4.0--h031d066_6"
 - "4.0--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for genometester4"
config: {"url": "https://biocontainers.pro/tools/genometester4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genometester4", "latest": {"4.0--h7b50bb2_7": "sha256:27df303c69850eb21fc83f1b8dca23439118b6e5921a476eefbe6e3cecd64af4"}, "tags": {"4.0--hec16e2b_4": "sha256:d03479ad3e891198a1056364ed0dde9389ba929bad199d67ad13ea8641f00424", "4.0--h031d066_6": "sha256:011cbf4d9652d9a37ac6bb6aa5e0d3b211cdb2f1fc402ab142011ab53f250baa", "4.0--h7b50bb2_7": "sha256:27df303c69850eb21fc83f1b8dca23439118b6e5921a476eefbe6e3cecd64af4"}, "docker": "quay.io/biocontainers/genometester4", "aliases": {"glistcompare": "/usr/local/bin/glistcompare", "glistmaker": "/usr/local/bin/glistmaker", "glistquery": "/usr/local/bin/glistquery", "gmer_caller": "/usr/local/bin/gmer_caller", "gmer_counter": "/usr/local/bin/gmer_counter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genometester4.
shpc-registry automated BioContainers addition for genometester4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genometester4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genometester4:4.0--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genometester4/4.0--h7b50bb2_7
$ module help quay.io/biocontainers/genometester4/4.0--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genometester4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genometester4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genometester4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genometester4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genometester4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genometester4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glistcompare

```bash
$ singularity exec <container> /usr/local/bin/glistcompare
$ podman run --it --rm --entrypoint /usr/local/bin/glistcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glistcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glistmaker

```bash
$ singularity exec <container> /usr/local/bin/glistmaker
$ podman run --it --rm --entrypoint /usr/local/bin/glistmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glistmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glistquery

```bash
$ singularity exec <container> /usr/local/bin/glistquery
$ podman run --it --rm --entrypoint /usr/local/bin/glistquery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glistquery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmer_caller

```bash
$ singularity exec <container> /usr/local/bin/gmer_caller
$ podman run --it --rm --entrypoint /usr/local/bin/gmer_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmer_caller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmer_counter

```bash
$ singularity exec <container> /usr/local/bin/gmer_counter
$ podman run --it --rm --entrypoint /usr/local/bin/gmer_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmer_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
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