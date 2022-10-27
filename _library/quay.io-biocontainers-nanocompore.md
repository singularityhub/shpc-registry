---
layout: container
name:  "quay.io/biocontainers/nanocompore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanocompore/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nanocompore/container.yaml"
updated_at: "2022-10-27 01:08:45.081005"
latest: "1.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nanocompore"
aliases:
 - "bedparse"
 - "nanocompore"
versions:
 - "1.0.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for nanocompore"
config: {"url": "https://biocontainers.pro/tools/nanocompore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanocompore", "latest": {"1.0.4--pyhdfd78af_0": "sha256:5ece0cff49e555fbbaca72b98efe6f1db1dd62a4cf471a2672ae254ed26e9575"}, "tags": {"1.0.4--pyhdfd78af_0": "sha256:5ece0cff49e555fbbaca72b98efe6f1db1dd62a4cf471a2672ae254ed26e9575"}, "docker": "quay.io/biocontainers/nanocompore", "aliases": {"bedparse": "/usr/local/bin/bedparse", "nanocompore": "/usr/local/bin/nanocompore"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanocompore.
shpc-registry automated BioContainers addition for nanocompore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanocompore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanocompore:1.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanocompore/1.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/nanocompore/1.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanocompore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanocompore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanocompore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanocompore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanocompore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanocompore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedparse

```bash
$ singularity exec <container> /usr/local/bin/bedparse
$ podman run --it --rm --entrypoint /usr/local/bin/bedparse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedparse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanocompore

```bash
$ singularity exec <container> /usr/local/bin/nanocompore
$ podman run --it --rm --entrypoint /usr/local/bin/nanocompore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanocompore   -v ${PWD} -w ${PWD} <container> -c " $@"
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