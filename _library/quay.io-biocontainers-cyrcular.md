---
layout: container
name:  "quay.io/biocontainers/cyrcular"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cyrcular/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cyrcular/container.yaml"
updated_at: "2025-04-10 03:44:50.514300"
latest: "0.3.0--ha8ac579_1"
container_url: "https://biocontainers.pro/tools/cyrcular"
aliases:
 - "cyrcular"
versions:
 - "0.3.0--h769f52f_0"
 - "0.3.0--ha8ac579_1"
description: "singularity registry hpc automated addition for cyrcular"
config: {"url": "https://biocontainers.pro/tools/cyrcular", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cyrcular", "latest": {"0.3.0--ha8ac579_1": "sha256:ea7996da63d0832f7d09c852fa7b8b1e58df01eb1465aff0d70994a8cc7196bd"}, "tags": {"0.3.0--h769f52f_0": "sha256:a919d60112b607e945cc68f2bed29aa162c0c5eba0e0b8cf8332fda19d5dc61f", "0.3.0--ha8ac579_1": "sha256:ea7996da63d0832f7d09c852fa7b8b1e58df01eb1465aff0d70994a8cc7196bd"}, "docker": "quay.io/biocontainers/cyrcular", "aliases": {"cyrcular": "/usr/local/bin/cyrcular"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cyrcular.
singularity registry hpc automated addition for cyrcular
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cyrcular
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cyrcular:0.3.0--ha8ac579_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cyrcular/0.3.0--ha8ac579_1
$ module help quay.io/biocontainers/cyrcular/0.3.0--ha8ac579_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cyrcular-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cyrcular-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cyrcular-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cyrcular-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cyrcular-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cyrcular-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cyrcular

```bash
$ singularity exec <container> /usr/local/bin/cyrcular
$ podman run --it --rm --entrypoint /usr/local/bin/cyrcular   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyrcular   -v ${PWD} -w ${PWD} <container> -c " $@"
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