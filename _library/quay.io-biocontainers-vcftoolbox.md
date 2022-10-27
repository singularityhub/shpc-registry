---
layout: container
name:  "quay.io/biocontainers/vcftoolbox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcftoolbox/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vcftoolbox/container.yaml"
updated_at: "2022-10-27 01:10:47.036418"
latest: "1.5.1--py_0"
container_url: "https://biocontainers.pro/tools/vcftoolbox"
aliases:
 - "vcftoolbox"
versions:
 - "1.5.1--py_0"
description: "shpc-registry automated BioContainers addition for vcftoolbox"
config: {"url": "https://biocontainers.pro/tools/vcftoolbox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcftoolbox", "latest": {"1.5.1--py_0": "sha256:19d02030a8946c3b6019ab72c592e9660224d9adf1bbc78b5f22def11a42d053"}, "tags": {"1.5.1--py_0": "sha256:19d02030a8946c3b6019ab72c592e9660224d9adf1bbc78b5f22def11a42d053"}, "docker": "quay.io/biocontainers/vcftoolbox", "aliases": {"vcftoolbox": "/usr/local/bin/vcftoolbox"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcftoolbox.
shpc-registry automated BioContainers addition for vcftoolbox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcftoolbox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcftoolbox:1.5.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcftoolbox/1.5.1--py_0
$ module help quay.io/biocontainers/vcftoolbox/1.5.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcftoolbox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcftoolbox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcftoolbox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcftoolbox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcftoolbox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcftoolbox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcftoolbox

```bash
$ singularity exec <container> /usr/local/bin/vcftoolbox
$ podman run --it --rm --entrypoint /usr/local/bin/vcftoolbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcftoolbox   -v ${PWD} -w ${PWD} <container> -c " $@"
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