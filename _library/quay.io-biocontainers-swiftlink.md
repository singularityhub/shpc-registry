---
layout: container
name:  "quay.io/biocontainers/swiftlink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/swiftlink/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/swiftlink/container.yaml"
updated_at: "2023-03-09 03:52:16.581426"
latest: "1.0--h20b91ae_2"
container_url: "https://biocontainers.pro/tools/swiftlink"
aliases:
 - "swiftlink"
versions:
 - "1.0--h20b91ae_2"
description: "shpc-registry automated BioContainers addition for swiftlink"
config: {"url": "https://biocontainers.pro/tools/swiftlink", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for swiftlink", "latest": {"1.0--h20b91ae_2": "sha256:733891f703642403133d20902a0ef3658e9c913bd47003532a488cd23460dbbf"}, "tags": {"1.0--h20b91ae_2": "sha256:733891f703642403133d20902a0ef3658e9c913bd47003532a488cd23460dbbf"}, "docker": "quay.io/biocontainers/swiftlink", "aliases": {"swiftlink": "/usr/local/bin/swiftlink"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/swiftlink.
shpc-registry automated BioContainers addition for swiftlink
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/swiftlink
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/swiftlink:1.0--h20b91ae_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/swiftlink/1.0--h20b91ae_2
$ module help quay.io/biocontainers/swiftlink/1.0--h20b91ae_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### swiftlink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### swiftlink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### swiftlink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### swiftlink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### swiftlink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### swiftlink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### swiftlink

```bash
$ singularity exec <container> /usr/local/bin/swiftlink
$ podman run --it --rm --entrypoint /usr/local/bin/swiftlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swiftlink   -v ${PWD} -w ${PWD} <container> -c " $@"
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