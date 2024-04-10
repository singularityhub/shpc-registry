---
layout: container
name:  "quay.io/biocontainers/progressivemauve"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/progressivemauve/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/progressivemauve/container.yaml"
updated_at: "2024-04-10 02:24:09.659345"
latest: "snapshot_2015_02_13--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/progressivemauve"
aliases:
 - "progressiveMauve"
versions:
 - "snapshot_2015_02_13--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for progressivemauve"
config: {"url": "https://biocontainers.pro/tools/progressivemauve", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for progressivemauve", "latest": {"snapshot_2015_02_13--h9ee0642_3": "sha256:1ef6c12869b7654e14c8ac8befbc30b132da1488c6103ab326761057a1f56c3b"}, "tags": {"snapshot_2015_02_13--h9ee0642_3": "sha256:1ef6c12869b7654e14c8ac8befbc30b132da1488c6103ab326761057a1f56c3b"}, "docker": "quay.io/biocontainers/progressivemauve", "aliases": {"progressiveMauve": "/usr/local/bin/progressiveMauve"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/progressivemauve.
shpc-registry automated BioContainers addition for progressivemauve
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/progressivemauve
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/progressivemauve:snapshot_2015_02_13--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/progressivemauve/snapshot_2015_02_13--h9ee0642_3
$ module help quay.io/biocontainers/progressivemauve/snapshot_2015_02_13--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### progressivemauve-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### progressivemauve-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### progressivemauve-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### progressivemauve-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### progressivemauve-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### progressivemauve-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### progressiveMauve

```bash
$ singularity exec <container> /usr/local/bin/progressiveMauve
$ podman run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progressiveMauve   -v ${PWD} -w ${PWD} <container> -c " $@"
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