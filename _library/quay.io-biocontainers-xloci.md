---
layout: container
name:  "quay.io/biocontainers/xloci"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xloci/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xloci/container.yaml"
updated_at: "2026-05-06 06:03:36.669780"
latest: "0.0.4--hd612981_0"
container_url: "https://biocontainers.pro/tools/xloci"
aliases:
 - "xloci"
versions:
 - "0.0.4--hd612981_0"
description: "singularity registry hpc automated addition for xloci"
config: {"url": "https://biocontainers.pro/tools/xloci", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for xloci", "latest": {"0.0.4--hd612981_0": "sha256:66c800a0028810d25e8768b8c4501c3cdb2c82ca4d250eb9a61808ef0facb073"}, "tags": {"0.0.4--hd612981_0": "sha256:66c800a0028810d25e8768b8c4501c3cdb2c82ca4d250eb9a61808ef0facb073"}, "docker": "quay.io/biocontainers/xloci", "aliases": {"xloci": "/usr/local/bin/xloci"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xloci.
singularity registry hpc automated addition for xloci
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xloci
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xloci:0.0.4--hd612981_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xloci/0.0.4--hd612981_0
$ module help quay.io/biocontainers/xloci/0.0.4--hd612981_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xloci-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xloci-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xloci-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xloci-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xloci-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xloci-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xloci

```bash
$ singularity exec <container> /usr/local/bin/xloci
$ podman run --it --rm --entrypoint /usr/local/bin/xloci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xloci   -v ${PWD} -w ${PWD} <container> -c " $@"
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