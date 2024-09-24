---
layout: container
name:  "quay.io/biocontainers/agg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/agg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/agg/container.yaml"
updated_at: "2024-09-24 03:23:18.573440"
latest: "0.3.6--h8b12597_1"
container_url: "https://biocontainers.pro/tools/agg"
aliases:
 - "agg"
versions:
 - "0.3.6--h8b12597_1"
description: "shpc-registry automated BioContainers addition for agg"
config: {"url": "https://biocontainers.pro/tools/agg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for agg", "latest": {"0.3.6--h8b12597_1": "sha256:038e4f9cbc43406d9d30484401c0e34d3316ee6b9559a2414a9c7aac34b4dac6"}, "tags": {"0.3.6--h8b12597_1": "sha256:038e4f9cbc43406d9d30484401c0e34d3316ee6b9559a2414a9c7aac34b4dac6"}, "docker": "quay.io/biocontainers/agg", "aliases": {"agg": "/usr/local/bin/agg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/agg.
shpc-registry automated BioContainers addition for agg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/agg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/agg:0.3.6--h8b12597_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/agg/0.3.6--h8b12597_1
$ module help quay.io/biocontainers/agg/0.3.6--h8b12597_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### agg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### agg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### agg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### agg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### agg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### agg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### agg

```bash
$ singularity exec <container> /usr/local/bin/agg
$ podman run --it --rm --entrypoint /usr/local/bin/agg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agg   -v ${PWD} -w ${PWD} <container> -c " $@"
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