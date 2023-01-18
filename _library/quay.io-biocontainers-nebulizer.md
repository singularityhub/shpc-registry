---
layout: container
name:  "quay.io/biocontainers/nebulizer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nebulizer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nebulizer/container.yaml"
updated_at: "2023-01-18 03:22:20.107838"
latest: "0.7.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/nebulizer"
aliases:
 - "bioblend-galaxy-tests"
 - "nebulizer"
 - "mako-render"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
versions:
 - "0.7.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for nebulizer"
config: {"url": "https://biocontainers.pro/tools/nebulizer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nebulizer", "latest": {"0.7.1--pyh5e36f6f_0": "sha256:6f6f78ac54712ca22a6e2663237084f732cf4659e3a9ceb32c5e56090e7fe9f9"}, "tags": {"0.7.1--pyh5e36f6f_0": "sha256:6f6f78ac54712ca22a6e2663237084f732cf4659e3a9ceb32c5e56090e7fe9f9"}, "docker": "quay.io/biocontainers/nebulizer", "aliases": {"bioblend-galaxy-tests": "/usr/local/bin/bioblend-galaxy-tests", "nebulizer": "/usr/local/bin/nebulizer", "mako-render": "/usr/local/bin/mako-render", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nebulizer.
shpc-registry automated BioContainers addition for nebulizer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nebulizer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nebulizer:0.7.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nebulizer/0.7.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/nebulizer/0.7.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nebulizer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nebulizer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nebulizer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nebulizer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nebulizer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nebulizer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioblend-galaxy-tests

```bash
$ singularity exec <container> /usr/local/bin/bioblend-galaxy-tests
$ podman run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nebulizer

```bash
$ singularity exec <container> /usr/local/bin/nebulizer
$ podman run --it --rm --entrypoint /usr/local/bin/nebulizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nebulizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
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