---
layout: container
name:  "quay.io/biocontainers/liquorice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/liquorice/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/liquorice/container.yaml"
updated_at: "2022-10-27 00:47:58.967509"
latest: "0.5.5--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/liquorice"
aliases:
 - "LIQUORICE"
 - "LIQUORICE_summary"
versions:
 - "0.5.5--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for liquorice"
config: {"url": "https://biocontainers.pro/tools/liquorice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for liquorice", "latest": {"0.5.5--pyhdfd78af_1": "sha256:4e2a6292eb7c95b57e2cf4842956e91128067f943d29e93cd7c778153c5f636e"}, "tags": {"0.5.5--pyhdfd78af_1": "sha256:4e2a6292eb7c95b57e2cf4842956e91128067f943d29e93cd7c778153c5f636e"}, "docker": "quay.io/biocontainers/liquorice", "aliases": {"LIQUORICE": "/usr/local/bin/LIQUORICE", "LIQUORICE_summary": "/usr/local/bin/LIQUORICE_summary"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/liquorice.
shpc-registry automated BioContainers addition for liquorice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/liquorice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/liquorice:0.5.5--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/liquorice/0.5.5--pyhdfd78af_1
$ module help quay.io/biocontainers/liquorice/0.5.5--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### liquorice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### liquorice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### liquorice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### liquorice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### liquorice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### liquorice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LIQUORICE

```bash
$ singularity exec <container> /usr/local/bin/LIQUORICE
$ podman run --it --rm --entrypoint /usr/local/bin/LIQUORICE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LIQUORICE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LIQUORICE_summary

```bash
$ singularity exec <container> /usr/local/bin/LIQUORICE_summary
$ podman run --it --rm --entrypoint /usr/local/bin/LIQUORICE_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LIQUORICE_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
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