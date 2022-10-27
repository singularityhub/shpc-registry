---
layout: container
name:  "quay.io/biocontainers/curesim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/curesim/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/curesim/container.yaml"
updated_at: "2022-10-27 00:32:56.488144"
latest: "1.3--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/curesim"
aliases:
 - "curesim"
versions:
 - "1.3--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for curesim"
config: {"url": "https://biocontainers.pro/tools/curesim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for curesim", "latest": {"1.3--hdfd78af_3": "sha256:1264bef2698d7e7a6851b675e598755b774ba915e6f83cfb403e59cff57a6ce4"}, "tags": {"1.3--hdfd78af_3": "sha256:1264bef2698d7e7a6851b675e598755b774ba915e6f83cfb403e59cff57a6ce4"}, "docker": "quay.io/biocontainers/curesim", "aliases": {"curesim": "/usr/local/bin/curesim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/curesim.
shpc-registry automated BioContainers addition for curesim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/curesim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/curesim:1.3--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/curesim/1.3--hdfd78af_3
$ module help quay.io/biocontainers/curesim/1.3--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### curesim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### curesim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### curesim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### curesim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### curesim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### curesim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### curesim

```bash
$ singularity exec <container> /usr/local/bin/curesim
$ podman run --it --rm --entrypoint /usr/local/bin/curesim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curesim   -v ${PWD} -w ${PWD} <container> -c " $@"
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