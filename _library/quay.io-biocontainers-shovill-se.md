---
layout: container
name:  "quay.io/biocontainers/shovill-se"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shovill-se/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/shovill-se/container.yaml"
updated_at: "2022-10-27 01:04:19.048451"
latest: "1.1.0se--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/shovill-se"
aliases:
 - "lighter"
 - "shovill"
 - "shovill-se"
versions:
 - "1.1.0se--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for shovill-se"
config: {"url": "https://biocontainers.pro/tools/shovill-se", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shovill-se", "latest": {"1.1.0se--hdfd78af_2": "sha256:3118f2893b1dd2a56e58033959c6aee69f9a4c87d89dea1344414a9ea468cde9"}, "tags": {"1.1.0se--hdfd78af_2": "sha256:3118f2893b1dd2a56e58033959c6aee69f9a4c87d89dea1344414a9ea468cde9"}, "docker": "quay.io/biocontainers/shovill-se", "aliases": {"lighter": "/usr/local/bin/lighter", "shovill": "/usr/local/bin/shovill", "shovill-se": "/usr/local/bin/shovill-se"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shovill-se.
shpc-registry automated BioContainers addition for shovill-se
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shovill-se
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shovill-se:1.1.0se--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shovill-se/1.1.0se--hdfd78af_2
$ module help quay.io/biocontainers/shovill-se/1.1.0se--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shovill-se-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shovill-se-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shovill-se-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shovill-se-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shovill-se-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shovill-se-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lighter

```bash
$ singularity exec <container> /usr/local/bin/lighter
$ podman run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shovill

```bash
$ singularity exec <container> /usr/local/bin/shovill
$ podman run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shovill-se

```bash
$ singularity exec <container> /usr/local/bin/shovill-se
$ podman run --it --rm --entrypoint /usr/local/bin/shovill-se   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shovill-se   -v ${PWD} -w ${PWD} <container> -c " $@"
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