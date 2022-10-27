---
layout: container
name:  "quay.io/biocontainers/shigeifinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shigeifinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/shigeifinder/container.yaml"
updated_at: "2022-10-27 00:43:29.997053"
latest: "1.3.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/shigeifinder"
aliases:
 - "shigeifinder"
versions:
 - "1.3.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for shigeifinder"
config: {"url": "https://biocontainers.pro/tools/shigeifinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shigeifinder", "latest": {"1.3.2--pyhdfd78af_0": "sha256:9fdc17b500161739a1a84e01de72699c8b65600eb8388cfa9508331a0d4eace8"}, "tags": {"1.3.2--pyhdfd78af_0": "sha256:9fdc17b500161739a1a84e01de72699c8b65600eb8388cfa9508331a0d4eace8"}, "docker": "quay.io/biocontainers/shigeifinder", "aliases": {"shigeifinder": "/usr/local/bin/shigeifinder"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shigeifinder.
shpc-registry automated BioContainers addition for shigeifinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shigeifinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shigeifinder:1.3.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shigeifinder/1.3.2--pyhdfd78af_0
$ module help quay.io/biocontainers/shigeifinder/1.3.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shigeifinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shigeifinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shigeifinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shigeifinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shigeifinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shigeifinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### shigeifinder

```bash
$ singularity exec <container> /usr/local/bin/shigeifinder
$ podman run --it --rm --entrypoint /usr/local/bin/shigeifinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shigeifinder   -v ${PWD} -w ${PWD} <container> -c " $@"
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