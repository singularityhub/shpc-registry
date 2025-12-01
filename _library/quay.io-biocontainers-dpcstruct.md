---
layout: container
name:  "quay.io/biocontainers/dpcstruct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dpcstruct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dpcstruct/container.yaml"
updated_at: "2025-12-01 03:55:14.221939"
latest: "0.1.1--h9948957_0"
container_url: "https://biocontainers.pro/tools/dpcstruct"
aliases:
 - "dpcstruct"
 - "dpcstruct-postfilters"
 - "dpcstruct-prefilters"
 - "dpcstruct-primarycluster"
 - "dpcstruct-secondarycluster"
 - "dpcstruct-traceback"
versions:
 - "0.1.1--h9948957_0"
description: "singularity registry hpc automated addition for dpcstruct"
config: {"url": "https://biocontainers.pro/tools/dpcstruct", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dpcstruct", "latest": {"0.1.1--h9948957_0": "sha256:335be7f0625002e142be64084a6c634b4636436b2028dc1f8908add2795a17bd"}, "tags": {"0.1.1--h9948957_0": "sha256:335be7f0625002e142be64084a6c634b4636436b2028dc1f8908add2795a17bd"}, "docker": "quay.io/biocontainers/dpcstruct", "aliases": {"dpcstruct": "/usr/local/bin/dpcstruct", "dpcstruct-postfilters": "/usr/local/bin/dpcstruct-postfilters", "dpcstruct-prefilters": "/usr/local/bin/dpcstruct-prefilters", "dpcstruct-primarycluster": "/usr/local/bin/dpcstruct-primarycluster", "dpcstruct-secondarycluster": "/usr/local/bin/dpcstruct-secondarycluster", "dpcstruct-traceback": "/usr/local/bin/dpcstruct-traceback"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dpcstruct.
singularity registry hpc automated addition for dpcstruct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dpcstruct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dpcstruct:0.1.1--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dpcstruct/0.1.1--h9948957_0
$ module help quay.io/biocontainers/dpcstruct/0.1.1--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dpcstruct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dpcstruct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dpcstruct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dpcstruct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dpcstruct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dpcstruct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dpcstruct

```bash
$ singularity exec <container> /usr/local/bin/dpcstruct
$ podman run --it --rm --entrypoint /usr/local/bin/dpcstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpcstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dpcstruct-postfilters

```bash
$ singularity exec <container> /usr/local/bin/dpcstruct-postfilters
$ podman run --it --rm --entrypoint /usr/local/bin/dpcstruct-postfilters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpcstruct-postfilters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dpcstruct-prefilters

```bash
$ singularity exec <container> /usr/local/bin/dpcstruct-prefilters
$ podman run --it --rm --entrypoint /usr/local/bin/dpcstruct-prefilters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpcstruct-prefilters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dpcstruct-primarycluster

```bash
$ singularity exec <container> /usr/local/bin/dpcstruct-primarycluster
$ podman run --it --rm --entrypoint /usr/local/bin/dpcstruct-primarycluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpcstruct-primarycluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dpcstruct-secondarycluster

```bash
$ singularity exec <container> /usr/local/bin/dpcstruct-secondarycluster
$ podman run --it --rm --entrypoint /usr/local/bin/dpcstruct-secondarycluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpcstruct-secondarycluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dpcstruct-traceback

```bash
$ singularity exec <container> /usr/local/bin/dpcstruct-traceback
$ podman run --it --rm --entrypoint /usr/local/bin/dpcstruct-traceback   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpcstruct-traceback   -v ${PWD} -w ${PWD} <container> -c " $@"
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