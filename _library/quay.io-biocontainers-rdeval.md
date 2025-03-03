---
layout: container
name:  "quay.io/biocontainers/rdeval"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rdeval/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rdeval/container.yaml"
updated_at: "2025-03-03 03:13:45.913766"
latest: "0.0.5--h35c04b2_0"
container_url: "https://biocontainers.pro/tools/rdeval"
aliases:
 - "rdeval"
versions:
 - "0.0.2--hdcf5f25_1"
 - "0.0.4--h35c04b2_0"
 - "0.0.5--h35c04b2_0"
description: "singularity registry hpc automated addition for rdeval"
config: {"url": "https://biocontainers.pro/tools/rdeval", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rdeval", "latest": {"0.0.5--h35c04b2_0": "sha256:51782ae6867e69707bacb7d1b37094f969e6adf46507d9de7a03bf52c3a67eb7"}, "tags": {"0.0.2--hdcf5f25_1": "sha256:3aebbe70df71e3c8c642ad5dea11f9ef431afad30631bcb96451abdcf5f02c24", "0.0.4--h35c04b2_0": "sha256:0870bbd69e1bca9b639a679077685bf7bb412d545580248ccf290896224038d8", "0.0.5--h35c04b2_0": "sha256:51782ae6867e69707bacb7d1b37094f969e6adf46507d9de7a03bf52c3a67eb7"}, "docker": "quay.io/biocontainers/rdeval", "aliases": {"rdeval": "/usr/local/bin/rdeval"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rdeval.
singularity registry hpc automated addition for rdeval
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rdeval
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rdeval:0.0.5--h35c04b2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rdeval/0.0.5--h35c04b2_0
$ module help quay.io/biocontainers/rdeval/0.0.5--h35c04b2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rdeval-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rdeval-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rdeval-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rdeval-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rdeval-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rdeval-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rdeval

```bash
$ singularity exec <container> /usr/local/bin/rdeval
$ podman run --it --rm --entrypoint /usr/local/bin/rdeval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdeval   -v ${PWD} -w ${PWD} <container> -c " $@"
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