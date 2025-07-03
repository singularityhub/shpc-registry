---
layout: container
name:  "quay.io/biocontainers/fasttree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fasttree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fasttree/container.yaml"
updated_at: "2025-07-03 03:22:50.216209"
latest: "2.1.11--h7b50bb2_5"
container_url: "https://biocontainers.pro/tools/fasttree"
aliases:
 - "FastTree"
 - "FastTree.c"
 - "FastTreeMP"
 - "fasttree"
versions:
 - "2.1.9--2"
 - "2.1.11--hec16e2b_1"
 - "2.1.11--h031d066_2"
 - "2.1.11--h031d066_3"
 - "2.1.11--h031d066_4"
 - "2.1.11--h7b50bb2_5"
description: "shpc-registry automated BioContainers addition for fasttree"
config: {"url": "https://biocontainers.pro/tools/fasttree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fasttree", "latest": {"2.1.11--h7b50bb2_5": "sha256:0c7537252e91111dc75b51b9fca687fdbd9f70507d4663cf930269ae0cfa7884"}, "tags": {"2.1.9--2": "sha256:1ba40dd44d1185648df082abd3b9ce18887b02cdbd40482ccf952d317e6d40e7", "2.1.11--hec16e2b_1": "sha256:1e93e85fa7d768b9f80379ed14eaa03258487b73520537944029897347f2e38b", "2.1.11--h031d066_2": "sha256:054af636c18055bb38ff7f255e1cdefad891e173b0fc520d5334a5277be38dd9", "2.1.11--h031d066_3": "sha256:48f15c1c59bd01b4061426162bca87564d25f724c14a01a95399508e9015f3d0", "2.1.11--h031d066_4": "sha256:e60ee7c01b3c60efdc1fea9a05554d0867be9dccef91ab01d0209f675ede96df", "2.1.11--h7b50bb2_5": "sha256:0c7537252e91111dc75b51b9fca687fdbd9f70507d4663cf930269ae0cfa7884"}, "docker": "quay.io/biocontainers/fasttree", "aliases": {"FastTree": "/usr/local/bin/FastTree", "FastTree.c": "/usr/local/bin/FastTree.c", "FastTreeMP": "/usr/local/bin/FastTreeMP", "fasttree": "/usr/local/bin/fasttree"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fasttree.
shpc-registry automated BioContainers addition for fasttree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fasttree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fasttree:2.1.11--h7b50bb2_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fasttree/2.1.11--h7b50bb2_5
$ module help quay.io/biocontainers/fasttree/2.1.11--h7b50bb2_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fasttree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fasttree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fasttree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fasttree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fasttree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fasttree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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