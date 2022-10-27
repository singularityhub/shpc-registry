---
layout: container
name:  "quay.io/biocontainers/mess"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mess/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mess/container.yaml"
updated_at: "2022-10-27 01:08:22.053114"
latest: "v0.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mess"
aliases:
 - "mess"
versions:
 - "v0.2.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for mess"
config: {"url": "https://biocontainers.pro/tools/mess", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mess", "latest": {"v0.2.1--pyhdfd78af_0": "sha256:075b9a2353137cadffd70344aa01537de415419bf09a66eee659d674b4c1f581"}, "tags": {"v0.2.1--pyhdfd78af_0": "sha256:075b9a2353137cadffd70344aa01537de415419bf09a66eee659d674b4c1f581"}, "docker": "quay.io/biocontainers/mess", "aliases": {"mess": "/usr/local/bin/mess"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mess.
shpc-registry automated BioContainers addition for mess
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mess
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mess:v0.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mess/v0.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/mess/v0.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mess-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mess-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mess-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mess-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mess-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mess-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mess

```bash
$ singularity exec <container> /usr/local/bin/mess
$ podman run --it --rm --entrypoint /usr/local/bin/mess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mess   -v ${PWD} -w ${PWD} <container> -c " $@"
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