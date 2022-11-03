---
layout: container
name:  "quay.io/biocontainers/csvtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csvtk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/csvtk/container.yaml"
updated_at: "2022-11-03 00:55:39.274287"
latest: "0.9.1--0"
container_url: "https://biocontainers.pro/tools/csvtk"
aliases:
 - "csvtk"
versions:
 - "0.9.1--0"
description: "shpc-registry automated BioContainers addition for csvtk"
config: {"url": "https://biocontainers.pro/tools/csvtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for csvtk", "latest": {"0.9.1--0": "sha256:4d8e2983a10ddadb8d674ab14b9b3410acc470a5503db510f6fef0cf2021c0ff"}, "tags": {"0.9.1--0": "sha256:4d8e2983a10ddadb8d674ab14b9b3410acc470a5503db510f6fef0cf2021c0ff"}, "docker": "quay.io/biocontainers/csvtk", "aliases": {"csvtk": "/usr/local/bin/csvtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csvtk.
shpc-registry automated BioContainers addition for csvtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csvtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csvtk:0.9.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csvtk/0.9.1--0
$ module help quay.io/biocontainers/csvtk/0.9.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csvtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csvtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csvtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csvtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csvtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csvtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csvtk

```bash
$ singularity exec <container> /usr/local/bin/csvtk
$ podman run --it --rm --entrypoint /usr/local/bin/csvtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csvtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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