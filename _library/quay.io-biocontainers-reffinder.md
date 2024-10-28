---
layout: container
name:  "quay.io/biocontainers/reffinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reffinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reffinder/container.yaml"
updated_at: "2024-10-28 03:41:48.974883"
latest: "0.81--h43eeafb_2"
container_url: "https://biocontainers.pro/tools/reffinder"
aliases:
 - "refFinder"
versions:
 - "0.81--h5b5514e_0"
 - "0.81--h43eeafb_2"
description: "singularity registry hpc automated addition for reffinder"
config: {"url": "https://biocontainers.pro/tools/reffinder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for reffinder", "latest": {"0.81--h43eeafb_2": "sha256:684c6302fee7b85e55f459335edeafde95d261432876805386faa90acafaade5"}, "tags": {"0.81--h5b5514e_0": "sha256:b35e910a4b43c4ccc023501601c5f3c784351381c8b6f7b164d1567911c0dc98", "0.81--h43eeafb_2": "sha256:684c6302fee7b85e55f459335edeafde95d261432876805386faa90acafaade5"}, "docker": "quay.io/biocontainers/reffinder", "aliases": {"refFinder": "/usr/local/bin/refFinder"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reffinder.
singularity registry hpc automated addition for reffinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reffinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reffinder:0.81--h43eeafb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reffinder/0.81--h43eeafb_2
$ module help quay.io/biocontainers/reffinder/0.81--h43eeafb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reffinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reffinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reffinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reffinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reffinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reffinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### refFinder

```bash
$ singularity exec <container> /usr/local/bin/refFinder
$ podman run --it --rm --entrypoint /usr/local/bin/refFinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refFinder   -v ${PWD} -w ${PWD} <container> -c " $@"
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