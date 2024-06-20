---
layout: container
name:  "quay.io/biocontainers/covtobed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/covtobed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/covtobed/container.yaml"
updated_at: "2024-06-20 02:38:09.661396"
latest: "1.3.5--hf393df8_2"
container_url: "https://biocontainers.pro/tools/covtobed"
aliases:
 - "covtobed"
 - "bamtools"
versions:
 - "1.3.5--ha7703dc_1"
 - "1.3.5--hf393df8_2"
description: "shpc-registry automated BioContainers addition for covtobed"
config: {"url": "https://biocontainers.pro/tools/covtobed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for covtobed", "latest": {"1.3.5--hf393df8_2": "sha256:204a2db9004e10949855fa83de020f41d036719c695cc70626de17cb36a49131"}, "tags": {"1.3.5--ha7703dc_1": "sha256:12aaf04110f12cff1a9f45218eacb29265dbe81602fc3bf6f43adf64450aabeb", "1.3.5--hf393df8_2": "sha256:204a2db9004e10949855fa83de020f41d036719c695cc70626de17cb36a49131"}, "docker": "quay.io/biocontainers/covtobed", "aliases": {"covtobed": "/usr/local/bin/covtobed", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/covtobed.
shpc-registry automated BioContainers addition for covtobed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/covtobed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/covtobed:1.3.5--hf393df8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/covtobed/1.3.5--hf393df8_2
$ module help quay.io/biocontainers/covtobed/1.3.5--hf393df8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### covtobed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### covtobed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### covtobed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### covtobed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### covtobed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### covtobed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### covtobed

```bash
$ singularity exec <container> /usr/local/bin/covtobed
$ podman run --it --rm --entrypoint /usr/local/bin/covtobed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/covtobed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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