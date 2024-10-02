---
layout: container
name:  "quay.io/biocontainers/veryfasttree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/veryfasttree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/veryfasttree/container.yaml"
updated_at: "2024-10-02 03:34:36.273884"
latest: "4.0.03--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/veryfasttree"
aliases:
 - "VeryFastTree"
versions:
 - "3.1.1--h9f5acd7_1"
 - "3.2.0--h9f5acd7_0"
 - "3.2.1--h9f5acd7_0"
 - "3.2.1--h9f5acd7_1"
 - "3.2.1--h4ac6f70_2"
 - "4.0.03--h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for veryfasttree"
config: {"url": "https://biocontainers.pro/tools/veryfasttree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for veryfasttree", "latest": {"4.0.03--h4ac6f70_0": "sha256:f405576afe74c31ca5895f72718f716dc317e3c82707b9681607f1e4f395876f"}, "tags": {"3.1.1--h9f5acd7_1": "sha256:f61eb7aa8aa0a69a1791d3c702c78d32a5ed85af370c8da20dec66b837eed066", "3.2.0--h9f5acd7_0": "sha256:7e5264ed5c77c98926ba6f6e18f713fa46b726b4b3f5fe5fc365c2276f987e06", "3.2.1--h9f5acd7_0": "sha256:5989eb9fc4676857e014f33e788adb763e1889592a3229fca6199a862b30ee51", "3.2.1--h9f5acd7_1": "sha256:9b009f1ad5f7127a775f92d95b3ce1333b7d6faf805f5e180f71527cad9f972a", "3.2.1--h4ac6f70_2": "sha256:62c98ae016b14751ca7a4f6dd807d8a63c2a1a2d68cc50969a2b39685c11783e", "4.0.03--h4ac6f70_0": "sha256:f405576afe74c31ca5895f72718f716dc317e3c82707b9681607f1e4f395876f"}, "docker": "quay.io/biocontainers/veryfasttree", "aliases": {"VeryFastTree": "/usr/local/bin/VeryFastTree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/veryfasttree.
shpc-registry automated BioContainers addition for veryfasttree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/veryfasttree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/veryfasttree:4.0.03--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/veryfasttree/4.0.03--h4ac6f70_0
$ module help quay.io/biocontainers/veryfasttree/4.0.03--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### veryfasttree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### veryfasttree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### veryfasttree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### veryfasttree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### veryfasttree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### veryfasttree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### VeryFastTree

```bash
$ singularity exec <container> /usr/local/bin/VeryFastTree
$ podman run --it --rm --entrypoint /usr/local/bin/VeryFastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VeryFastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
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