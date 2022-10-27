---
layout: container
name:  "quay.io/biocontainers/gatb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gatb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gatb/container.yaml"
updated_at: "2022-10-27 00:20:26.814505"
latest: "1.4.2--hbeba21e_1"
container_url: "https://biocontainers.pro/tools/gatb"
aliases:
 - "dbgh5"
 - "dbginfo"
 - "leon"
versions:
 - "1.4.2--hbeba21e_1"
description: "shpc-registry automated BioContainers addition for gatb"
config: {"url": "https://biocontainers.pro/tools/gatb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gatb", "latest": {"1.4.2--hbeba21e_1": "sha256:460a7c23cad7716d6b5f717dda0d342f1affc3caa231242300e51c24dc160a0a"}, "tags": {"1.4.2--hbeba21e_1": "sha256:460a7c23cad7716d6b5f717dda0d342f1affc3caa231242300e51c24dc160a0a"}, "docker": "quay.io/biocontainers/gatb", "aliases": {"dbgh5": "/usr/local/bin/dbgh5", "dbginfo": "/usr/local/bin/dbginfo", "leon": "/usr/local/bin/leon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gatb.
shpc-registry automated BioContainers addition for gatb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gatb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gatb:1.4.2--hbeba21e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gatb/1.4.2--hbeba21e_1
$ module help quay.io/biocontainers/gatb/1.4.2--hbeba21e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gatb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gatb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gatb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gatb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gatb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gatb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dbgh5

```bash
$ singularity exec <container> /usr/local/bin/dbgh5
$ podman run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbgh5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbginfo

```bash
$ singularity exec <container> /usr/local/bin/dbginfo
$ podman run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### leon

```bash
$ singularity exec <container> /usr/local/bin/leon
$ podman run --it --rm --entrypoint /usr/local/bin/leon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leon   -v ${PWD} -w ${PWD} <container> -c " $@"
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