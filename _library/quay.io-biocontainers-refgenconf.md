---
layout: container
name:  "quay.io/biocontainers/refgenconf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/refgenconf/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/refgenconf/container.yaml"
updated_at: "2022-10-27 00:32:03.039277"
latest: "0.9.3--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/refgenconf"

versions:
 - "0.9.3--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for refgenconf"
config: {"url": "https://biocontainers.pro/tools/refgenconf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for refgenconf", "latest": {"0.9.3--pyh3252c3a_0": "sha256:340fd3ca078477ca4647c6a0e0580927b5c746fb63db3f90b6f7271e3a7502e4"}, "tags": {"0.9.3--pyh3252c3a_0": "sha256:340fd3ca078477ca4647c6a0e0580927b5c746fb63db3f90b6f7271e3a7502e4"}, "docker": "quay.io/biocontainers/refgenconf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/refgenconf.
shpc-registry automated BioContainers addition for refgenconf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/refgenconf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/refgenconf:0.9.3--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/refgenconf/0.9.3--pyh3252c3a_0
$ module help quay.io/biocontainers/refgenconf/0.9.3--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### refgenconf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### refgenconf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### refgenconf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### refgenconf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### refgenconf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### refgenconf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### refgenconf

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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