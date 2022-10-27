---
layout: container
name:  "quay.io/biocontainers/dropest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dropest/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dropest/container.yaml"
updated_at: "2022-10-27 00:38:30.343307"
latest: "0.8.6--r41he6cf555_4"
container_url: "https://biocontainers.pro/tools/dropest"
aliases:
 - "dropReport.Rsc"
 - "dropest"
 - "droptag"
versions:
 - "0.8.6--r41he6cf555_4"
description: "shpc-registry automated BioContainers addition for dropest"
config: {"url": "https://biocontainers.pro/tools/dropest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dropest", "latest": {"0.8.6--r41he6cf555_4": "sha256:5ff67249afd14e5c1e7f2785442885a75cc509377780be54d8585fb57ba94cb9"}, "tags": {"0.8.6--r41he6cf555_4": "sha256:5ff67249afd14e5c1e7f2785442885a75cc509377780be54d8585fb57ba94cb9"}, "docker": "quay.io/biocontainers/dropest", "aliases": {"dropReport.Rsc": "/usr/local/bin/dropReport.Rsc", "dropest": "/usr/local/bin/dropest", "droptag": "/usr/local/bin/droptag"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dropest.
shpc-registry automated BioContainers addition for dropest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dropest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dropest:0.8.6--r41he6cf555_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dropest/0.8.6--r41he6cf555_4
$ module help quay.io/biocontainers/dropest/0.8.6--r41he6cf555_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dropest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dropest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dropest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dropest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dropest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dropest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dropReport.Rsc

```bash
$ singularity exec <container> /usr/local/bin/dropReport.Rsc
$ podman run --it --rm --entrypoint /usr/local/bin/dropReport.Rsc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropReport.Rsc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropest

```bash
$ singularity exec <container> /usr/local/bin/dropest
$ podman run --it --rm --entrypoint /usr/local/bin/dropest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dropest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### droptag

```bash
$ singularity exec <container> /usr/local/bin/droptag
$ podman run --it --rm --entrypoint /usr/local/bin/droptag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/droptag   -v ${PWD} -w ${PWD} <container> -c " $@"
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