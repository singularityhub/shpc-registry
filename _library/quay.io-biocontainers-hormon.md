---
layout: container
name:  "quay.io/biocontainers/hormon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hormon/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hormon/container.yaml"
updated_at: "2022-10-27 01:16:01.186972"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/hormon"
aliases:
 - "HORmon"
 - "monomer_inference"
 - "stringdecomposer"
versions:
 - "1.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for hormon"
config: {"url": "https://biocontainers.pro/tools/hormon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hormon", "latest": {"1.0.0--pyhdfd78af_0": "sha256:5a9e5c74b0c1d94bbd145eee617ced61a653a9f6d78757b283f14c196024f7b2"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:5a9e5c74b0c1d94bbd145eee617ced61a653a9f6d78757b283f14c196024f7b2"}, "docker": "quay.io/biocontainers/hormon", "aliases": {"HORmon": "/usr/local/bin/HORmon", "monomer_inference": "/usr/local/bin/monomer_inference", "stringdecomposer": "/usr/local/bin/stringdecomposer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hormon.
shpc-registry automated BioContainers addition for hormon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hormon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hormon:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hormon/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/hormon/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hormon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hormon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hormon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hormon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hormon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hormon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HORmon

```bash
$ singularity exec <container> /usr/local/bin/HORmon
$ podman run --it --rm --entrypoint /usr/local/bin/HORmon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HORmon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monomer_inference

```bash
$ singularity exec <container> /usr/local/bin/monomer_inference
$ podman run --it --rm --entrypoint /usr/local/bin/monomer_inference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monomer_inference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stringdecomposer

```bash
$ singularity exec <container> /usr/local/bin/stringdecomposer
$ podman run --it --rm --entrypoint /usr/local/bin/stringdecomposer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stringdecomposer   -v ${PWD} -w ${PWD} <container> -c " $@"
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