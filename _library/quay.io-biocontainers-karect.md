---
layout: container
name:  "quay.io/biocontainers/karect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/karect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/karect/container.yaml"
updated_at: "2023-09-11 03:23:11.517336"
latest: "1.0--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/karect"
aliases:
 - "karect"
versions:
 - "1.0--h9f5acd7_4"
 - "1.0--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for karect"
config: {"url": "https://biocontainers.pro/tools/karect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for karect", "latest": {"1.0--h4ac6f70_6": "sha256:8956608740893088f301b3251a68c7e2c6bee8254b27416eb2f6cffbad843389"}, "tags": {"1.0--h9f5acd7_4": "sha256:5c49a42ea8edf231d2b624faa2290254e7fa948b1b1407b7b08ff5c5138de2df", "1.0--h4ac6f70_6": "sha256:8956608740893088f301b3251a68c7e2c6bee8254b27416eb2f6cffbad843389"}, "docker": "quay.io/biocontainers/karect", "aliases": {"karect": "/usr/local/bin/karect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/karect.
shpc-registry automated BioContainers addition for karect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/karect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/karect:1.0--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/karect/1.0--h4ac6f70_6
$ module help quay.io/biocontainers/karect/1.0--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### karect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### karect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### karect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### karect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### karect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### karect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### karect

```bash
$ singularity exec <container> /usr/local/bin/karect
$ podman run --it --rm --entrypoint /usr/local/bin/karect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/karect   -v ${PWD} -w ${PWD} <container> -c " $@"
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