---
layout: container
name:  "quay.io/vgteam/vg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/vgteam/vg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/vgteam/vg/container.yaml"
updated_at: "2023-11-02 03:20:09.778871"
latest: "latest"
container_url: "https://quay.io/repository/vgteam/vg?tab=info"
aliases:
 - "vg"
versions:
 - "latest"
description: "Tools for working with genomic variation graphs. https://github.com/vgteam/vg"
config: {"docker": "quay.io/vgteam/vg", "url": "https://quay.io/repository/vgteam/vg?tab=info", "maintainer": "@vsoch", "description": "Tools for working with genomic variation graphs. https://github.com/vgteam/vg", "latest": {"latest": "sha256:aa26003ead727916c6cb6062f73b9a17df04a519aa22942d64f93a8b653b358b"}, "tags": {"latest": "sha256:aa26003ead727916c6cb6062f73b9a17df04a519aa22942d64f93a8b653b358b"}, "filter": ["latest"], "aliases": {"vg": "/vg/bin/vg"}}
---

This module is a singularity container wrapper for quay.io/vgteam/vg.
Tools for working with genomic variation graphs. https://github.com/vgteam/vg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/vgteam/vg
```

Or a specific version:

```bash
$ shpc install quay.io/vgteam/vg:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/vgteam/vg/latest
$ module help quay.io/vgteam/vg/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vg

```bash
$ singularity exec <container> /vg/bin/vg
$ podman run --it --rm --entrypoint /vg/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /vg/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
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