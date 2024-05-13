---
layout: container
name:  "quay.io/biocontainers/quicktree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quicktree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quicktree/container.yaml"
updated_at: "2024-05-13 03:14:14.049170"
latest: "2.5--h031d066_6"
container_url: "https://biocontainers.pro/tools/quicktree"
aliases:
 - "quicktree"
versions:
 - "2.5--hec16e2b_2"
 - "2.5--h031d066_4"
 - "2.5--h031d066_6"
description: "shpc-registry automated BioContainers addition for quicktree"
config: {"url": "https://biocontainers.pro/tools/quicktree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for quicktree", "latest": {"2.5--h031d066_6": "sha256:a0f6e98307cd192dd8a8667c8aeb922a66acd0333a5ca9cbabcb8f54a3e39bc2"}, "tags": {"2.5--hec16e2b_2": "sha256:d64436ddbbbf92083b7d7a1acba36192ab78bf45fbfcc360a1c6834e886dcc9a", "2.5--h031d066_4": "sha256:d99994f63ca16fdae59083db0c0690995d58255f114e824640f4923e16589711", "2.5--h031d066_6": "sha256:a0f6e98307cd192dd8a8667c8aeb922a66acd0333a5ca9cbabcb8f54a3e39bc2"}, "docker": "quay.io/biocontainers/quicktree", "aliases": {"quicktree": "/usr/local/bin/quicktree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quicktree.
shpc-registry automated BioContainers addition for quicktree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quicktree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quicktree:2.5--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quicktree/2.5--h031d066_6
$ module help quay.io/biocontainers/quicktree/2.5--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quicktree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quicktree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quicktree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quicktree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quicktree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quicktree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### quicktree

```bash
$ singularity exec <container> /usr/local/bin/quicktree
$ podman run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quicktree   -v ${PWD} -w ${PWD} <container> -c " $@"
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