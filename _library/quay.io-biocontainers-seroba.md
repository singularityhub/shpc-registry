---
layout: container
name:  "quay.io/biocontainers/seroba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seroba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/seroba/container.yaml"
updated_at: "2022-10-27 00:40:08.519563"
latest: "1.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/seroba"
aliases:
 - "ariba"
 - "seroba"
versions:
 - "1.0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for seroba"
config: {"url": "https://biocontainers.pro/tools/seroba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seroba", "latest": {"1.0.2--pyhdfd78af_1": "sha256:36b6ec2c8091d38c0efd4814491e64886e48eaf41b434b5d1baf6ba95ddfef8b"}, "tags": {"1.0.2--pyhdfd78af_1": "sha256:36b6ec2c8091d38c0efd4814491e64886e48eaf41b434b5d1baf6ba95ddfef8b"}, "docker": "quay.io/biocontainers/seroba", "aliases": {"ariba": "/usr/local/bin/ariba", "seroba": "/usr/local/bin/seroba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seroba.
shpc-registry automated BioContainers addition for seroba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seroba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seroba:1.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seroba/1.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/seroba/1.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seroba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seroba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seroba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seroba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seroba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seroba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ariba

```bash
$ singularity exec <container> /usr/local/bin/ariba
$ podman run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seroba

```bash
$ singularity exec <container> /usr/local/bin/seroba
$ podman run --it --rm --entrypoint /usr/local/bin/seroba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seroba   -v ${PWD} -w ${PWD} <container> -c " $@"
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