---
layout: container
name:  "quay.io/biocontainers/tbvcfreport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tbvcfreport/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tbvcfreport/container.yaml"
updated_at: "2022-10-27 00:41:13.529766"
latest: "0.1.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/tbvcfreport"
aliases:
 - "tbvcfreport"
versions:
 - "0.1.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for tbvcfreport"
config: {"url": "https://biocontainers.pro/tools/tbvcfreport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tbvcfreport", "latest": {"0.1.8--pyhdfd78af_0": "sha256:36dccde2b2093c77644ae8d0e6c8f1246361673531be953e775325b6196f6704"}, "tags": {"0.1.8--pyhdfd78af_0": "sha256:36dccde2b2093c77644ae8d0e6c8f1246361673531be953e775325b6196f6704"}, "docker": "quay.io/biocontainers/tbvcfreport", "aliases": {"tbvcfreport": "/usr/local/bin/tbvcfreport"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tbvcfreport.
shpc-registry automated BioContainers addition for tbvcfreport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tbvcfreport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tbvcfreport:0.1.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tbvcfreport/0.1.8--pyhdfd78af_0
$ module help quay.io/biocontainers/tbvcfreport/0.1.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tbvcfreport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tbvcfreport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tbvcfreport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tbvcfreport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tbvcfreport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tbvcfreport-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tbvcfreport

```bash
$ singularity exec <container> /usr/local/bin/tbvcfreport
$ podman run --it --rm --entrypoint /usr/local/bin/tbvcfreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbvcfreport   -v ${PWD} -w ${PWD} <container> -c " $@"
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