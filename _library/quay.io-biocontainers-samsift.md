---
layout: container
name:  "quay.io/biocontainers/samsift"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samsift/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/samsift/container.yaml"
updated_at: "2022-10-27 00:53:12.943036"
latest: "0.2.5--py_3"
container_url: "https://biocontainers.pro/tools/samsift"
aliases:
 - "samsift"
 - "samsift-norm-sam"
versions:
 - "0.2.5--py_3"
description: "shpc-registry automated BioContainers addition for samsift"
config: {"url": "https://biocontainers.pro/tools/samsift", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samsift", "latest": {"0.2.5--py_3": "sha256:30cbaad99fcb57d9618bc764e71573dfbf3cd4d431d9622d0aec170ac26f2c54"}, "tags": {"0.2.5--py_3": "sha256:30cbaad99fcb57d9618bc764e71573dfbf3cd4d431d9622d0aec170ac26f2c54"}, "docker": "quay.io/biocontainers/samsift", "aliases": {"samsift": "/usr/local/bin/samsift", "samsift-norm-sam": "/usr/local/bin/samsift-norm-sam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samsift.
shpc-registry automated BioContainers addition for samsift
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samsift
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samsift:0.2.5--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samsift/0.2.5--py_3
$ module help quay.io/biocontainers/samsift/0.2.5--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samsift-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samsift-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samsift-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samsift-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samsift-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samsift-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samsift

```bash
$ singularity exec <container> /usr/local/bin/samsift
$ podman run --it --rm --entrypoint /usr/local/bin/samsift   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samsift   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samsift-norm-sam

```bash
$ singularity exec <container> /usr/local/bin/samsift-norm-sam
$ podman run --it --rm --entrypoint /usr/local/bin/samsift-norm-sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samsift-norm-sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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