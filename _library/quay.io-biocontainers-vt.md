---
layout: container
name:  "quay.io/biocontainers/vt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vt/container.yaml"
updated_at: "2024-09-26 10:38:01.015562"
latest: "2015.11.10--h5ef6573_4"
container_url: "https://biocontainers.pro/tools/vt"
aliases:
 - "vt"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2015.11.10--h5ef6573_4"
description: "shpc-registry automated BioContainers addition for vt"
config: {"url": "https://biocontainers.pro/tools/vt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vt", "latest": {"2015.11.10--h5ef6573_4": "sha256:43e8bd11d199c37d62ff613f38cbf42ad957c950532392a3e257dacb62887e95"}, "tags": {"2015.11.10--h5ef6573_4": "sha256:43e8bd11d199c37d62ff613f38cbf42ad957c950532392a3e257dacb62887e95"}, "docker": "quay.io/biocontainers/vt", "aliases": {"vt": "/usr/local/bin/vt", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vt.
shpc-registry automated BioContainers addition for vt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vt:2015.11.10--h5ef6573_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vt/2015.11.10--h5ef6573_4
$ module help quay.io/biocontainers/vt/2015.11.10--h5ef6573_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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