---
layout: container
name:  "quay.io/biocontainers/spliceai-wrapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spliceai-wrapper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/spliceai-wrapper/container.yaml"
updated_at: "2022-10-27 00:56:24.836840"
latest: "0.1.0--0"
container_url: "https://biocontainers.pro/tools/spliceai-wrapper"
aliases:
 - "spliceai"
 - "spliceai-wrapper"
versions:
 - "0.1.0--0"
description: "shpc-registry automated BioContainers addition for spliceai-wrapper"
config: {"url": "https://biocontainers.pro/tools/spliceai-wrapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spliceai-wrapper", "latest": {"0.1.0--0": "sha256:b223dae229ab4615e45d5d15279a663a8f6802ef82e3e7f08454ff81c1da9bec"}, "tags": {"0.1.0--0": "sha256:b223dae229ab4615e45d5d15279a663a8f6802ef82e3e7f08454ff81c1da9bec"}, "docker": "quay.io/biocontainers/spliceai-wrapper", "aliases": {"spliceai": "/usr/local/bin/spliceai", "spliceai-wrapper": "/usr/local/bin/spliceai-wrapper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spliceai-wrapper.
shpc-registry automated BioContainers addition for spliceai-wrapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spliceai-wrapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spliceai-wrapper:0.1.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spliceai-wrapper/0.1.0--0
$ module help quay.io/biocontainers/spliceai-wrapper/0.1.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spliceai-wrapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spliceai-wrapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spliceai-wrapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spliceai-wrapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spliceai-wrapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spliceai-wrapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spliceai

```bash
$ singularity exec <container> /usr/local/bin/spliceai
$ podman run --it --rm --entrypoint /usr/local/bin/spliceai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spliceai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spliceai-wrapper

```bash
$ singularity exec <container> /usr/local/bin/spliceai-wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/spliceai-wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spliceai-wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
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