---
layout: container
name:  "quay.io/biocontainers/unum-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unum-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unum-bio/container.yaml"
updated_at: "2026-08-31 08:16:52.413834"
latest: "0.1.3--h0feb368_0"
container_url: "https://biocontainers.pro/tools/unum-bio"
aliases:
 - "unum"
versions:
 - "0.1.3--h0feb368_0"
description: "singularity registry hpc automated addition for unum-bio"
config: {"url": "https://biocontainers.pro/tools/unum-bio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unum-bio", "latest": {"0.1.3--h0feb368_0": "sha256:78f92b293b79754bc53773a6f9fa210e0d7e6b005dae2ac1065eea3b54e7dacf"}, "tags": {"0.1.3--h0feb368_0": "sha256:78f92b293b79754bc53773a6f9fa210e0d7e6b005dae2ac1065eea3b54e7dacf"}, "docker": "quay.io/biocontainers/unum-bio", "aliases": {"unum": "/usr/local/bin/unum"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unum-bio.
singularity registry hpc automated addition for unum-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unum-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unum-bio:0.1.3--h0feb368_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unum-bio/0.1.3--h0feb368_0
$ module help quay.io/biocontainers/unum-bio/0.1.3--h0feb368_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unum-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unum-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unum-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unum-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unum-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unum-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unum

```bash
$ singularity exec <container> /usr/local/bin/unum
$ podman run --it --rm --entrypoint /usr/local/bin/unum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unum   -v ${PWD} -w ${PWD} <container> -c " $@"
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