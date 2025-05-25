---
layout: container
name:  "quay.io/biocontainers/bindashtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bindashtree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bindashtree/container.yaml"
updated_at: "2025-05-25 03:43:43.228138"
latest: "0.1.1--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/bindashtree"
aliases:
 - "bindashtree"
versions:
 - "0.1.0--h3ab6199_0"
 - "0.1.1--h3ab6199_0"
description: "singularity registry hpc automated addition for bindashtree"
config: {"url": "https://biocontainers.pro/tools/bindashtree", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bindashtree", "latest": {"0.1.1--h3ab6199_0": "sha256:81c71654ab6879f6c3c968de7bc7486029a23dea0e57fbe38ab047f7ddecec70"}, "tags": {"0.1.0--h3ab6199_0": "sha256:f8e2a48517ae821333fd39d3e535753443a7b3e8d628583295d3b628b7a07908", "0.1.1--h3ab6199_0": "sha256:81c71654ab6879f6c3c968de7bc7486029a23dea0e57fbe38ab047f7ddecec70"}, "docker": "quay.io/biocontainers/bindashtree", "aliases": {"bindashtree": "/usr/local/bin/bindashtree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bindashtree.
singularity registry hpc automated addition for bindashtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bindashtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bindashtree:0.1.1--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bindashtree/0.1.1--h3ab6199_0
$ module help quay.io/biocontainers/bindashtree/0.1.1--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bindashtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bindashtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bindashtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bindashtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bindashtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bindashtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bindashtree

```bash
$ singularity exec <container> /usr/local/bin/bindashtree
$ podman run --it --rm --entrypoint /usr/local/bin/bindashtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bindashtree   -v ${PWD} -w ${PWD} <container> -c " $@"
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