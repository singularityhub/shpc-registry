---
layout: container
name:  "quay.io/biocontainers/galaxy-objectstore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/galaxy-objectstore/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/galaxy-objectstore/container.yaml"
updated_at: "2022-10-29 05:30:58.404314"
latest: "22.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/galaxy-objectstore"
aliases:
 - "2to3-3.10"
 - "cheetah"
 - "cheetah-analyze"
 - "cheetah-compile"
 - "docutils"
 - "futurize"
 - "idle3.10"
 - "normalizer"
 - "pasteurize"
 - "pydoc3.10"
versions:
 - "22.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for galaxy-objectstore"
config: {"url": "https://biocontainers.pro/tools/galaxy-objectstore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for galaxy-objectstore", "latest": {"22.1.1--pyhdfd78af_0": "sha256:61ccf6a893390ea655b838478affed3fb4967fc79914ef306d7631caec6c77a5"}, "tags": {"22.1.1--pyhdfd78af_0": "sha256:61ccf6a893390ea655b838478affed3fb4967fc79914ef306d7631caec6c77a5"}, "docker": "quay.io/biocontainers/galaxy-objectstore", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "cheetah": "/usr/local/bin/cheetah", "cheetah-analyze": "/usr/local/bin/cheetah-analyze", "cheetah-compile": "/usr/local/bin/cheetah-compile", "docutils": "/usr/local/bin/docutils", "futurize": "/usr/local/bin/futurize", "idle3.10": "/usr/local/bin/idle3.10", "normalizer": "/usr/local/bin/normalizer", "pasteurize": "/usr/local/bin/pasteurize", "pydoc3.10": "/usr/local/bin/pydoc3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/galaxy-objectstore.
shpc-registry automated BioContainers addition for galaxy-objectstore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/galaxy-objectstore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/galaxy-objectstore:22.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/galaxy-objectstore/22.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/galaxy-objectstore/22.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### galaxy-objectstore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-objectstore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### galaxy-objectstore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### galaxy-objectstore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### galaxy-objectstore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### galaxy-objectstore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah

```bash
$ singularity exec <container> /usr/local/bin/cheetah
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-analyze

```bash
$ singularity exec <container> /usr/local/bin/cheetah-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-compile

```bash
$ singularity exec <container> /usr/local/bin/cheetah-compile
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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