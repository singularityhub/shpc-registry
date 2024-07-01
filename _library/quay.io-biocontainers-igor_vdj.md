---
layout: container
name:  "quay.io/biocontainers/igor_vdj"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/igor_vdj/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/igor_vdj/container.yaml"
updated_at: "2024-07-01 02:58:43.762866"
latest: "1.4.0--he1b5a44_0"
container_url: "https://biocontainers.pro/tools/igor_vdj"
aliases:
 - "igor"
 - "igor-compute_pgen"
versions:
 - "1.4.0--he1b5a44_0"
description: "shpc-registry automated BioContainers addition for igor_vdj"
config: {"url": "https://biocontainers.pro/tools/igor_vdj", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for igor_vdj", "latest": {"1.4.0--he1b5a44_0": "sha256:8d53c165970f45a4840dc9e154b83a4f23d85b279c66af11ce37a47b8f450c63"}, "tags": {"1.4.0--he1b5a44_0": "sha256:8d53c165970f45a4840dc9e154b83a4f23d85b279c66af11ce37a47b8f450c63"}, "docker": "quay.io/biocontainers/igor_vdj", "aliases": {"igor": "/usr/local/bin/igor", "igor-compute_pgen": "/usr/local/bin/igor-compute_pgen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/igor_vdj.
shpc-registry automated BioContainers addition for igor_vdj
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/igor_vdj
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/igor_vdj:1.4.0--he1b5a44_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/igor_vdj/1.4.0--he1b5a44_0
$ module help quay.io/biocontainers/igor_vdj/1.4.0--he1b5a44_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igor_vdj-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igor_vdj-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igor_vdj-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igor_vdj-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igor_vdj-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igor_vdj-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### igor

```bash
$ singularity exec <container> /usr/local/bin/igor
$ podman run --it --rm --entrypoint /usr/local/bin/igor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igor-compute_pgen

```bash
$ singularity exec <container> /usr/local/bin/igor-compute_pgen
$ podman run --it --rm --entrypoint /usr/local/bin/igor-compute_pgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igor-compute_pgen   -v ${PWD} -w ${PWD} <container> -c " $@"
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