---
layout: container
name:  "quay.io/biocontainers/repaq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/repaq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/repaq/container.yaml"
updated_at: "2023-12-09 02:29:44.631661"
latest: "0.3.0--h43eeafb_4"
container_url: "https://biocontainers.pro/tools/repaq"
aliases:
 - "repaq"
versions:
 - "0.3.0--h5b5514e_2"
 - "0.3.0--h43eeafb_4"
description: "shpc-registry automated BioContainers addition for repaq"
config: {"url": "https://biocontainers.pro/tools/repaq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for repaq", "latest": {"0.3.0--h43eeafb_4": "sha256:b4c3e20c78af9f220b208ce2ee8d2bf8b4e77dea9a75ffb74a65ab98cc8e5242"}, "tags": {"0.3.0--h5b5514e_2": "sha256:a3049ac4dd58c8c01b6109b6488c682f86f0d80bdd29ce4c605bc4b75a8740ea", "0.3.0--h43eeafb_4": "sha256:b4c3e20c78af9f220b208ce2ee8d2bf8b4e77dea9a75ffb74a65ab98cc8e5242"}, "docker": "quay.io/biocontainers/repaq", "aliases": {"repaq": "/usr/local/bin/repaq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/repaq.
shpc-registry automated BioContainers addition for repaq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/repaq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/repaq:0.3.0--h43eeafb_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/repaq/0.3.0--h43eeafb_4
$ module help quay.io/biocontainers/repaq/0.3.0--h43eeafb_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### repaq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### repaq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### repaq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### repaq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### repaq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### repaq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### repaq

```bash
$ singularity exec <container> /usr/local/bin/repaq
$ podman run --it --rm --entrypoint /usr/local/bin/repaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repaq   -v ${PWD} -w ${PWD} <container> -c " $@"
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