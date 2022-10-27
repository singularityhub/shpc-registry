---
layout: container
name:  "quay.io/biocontainers/cramtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cramtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cramtools/container.yaml"
updated_at: "2022-10-27 01:00:54.278169"
latest: "3.0.b127--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/cramtools"
aliases:
 - "cramtools"
versions:
 - "3.0.b127--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for cramtools"
config: {"url": "https://biocontainers.pro/tools/cramtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cramtools", "latest": {"3.0.b127--hdfd78af_3": "sha256:2f2f49d7754e883f3053a9996575a5e1e895d0a3aa4e91d493a441d64a066b94"}, "tags": {"3.0.b127--hdfd78af_3": "sha256:2f2f49d7754e883f3053a9996575a5e1e895d0a3aa4e91d493a441d64a066b94"}, "docker": "quay.io/biocontainers/cramtools", "aliases": {"cramtools": "/usr/local/bin/cramtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cramtools.
shpc-registry automated BioContainers addition for cramtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cramtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cramtools:3.0.b127--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cramtools/3.0.b127--hdfd78af_3
$ module help quay.io/biocontainers/cramtools/3.0.b127--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cramtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cramtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cramtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cramtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cramtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cramtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cramtools

```bash
$ singularity exec <container> /usr/local/bin/cramtools
$ podman run --it --rm --entrypoint /usr/local/bin/cramtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cramtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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