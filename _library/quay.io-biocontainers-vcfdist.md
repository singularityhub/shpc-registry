---
layout: container
name:  "quay.io/biocontainers/vcfdist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcfdist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcfdist/container.yaml"
updated_at: "2025-04-24 03:38:09.089268"
latest: "2.4.0--h84372a0_0"
container_url: "https://biocontainers.pro/tools/vcfdist"
aliases:
 - "vcfdist"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.4.0--h84372a0_0"
description: "singularity registry hpc automated addition for vcfdist"
config: {"url": "https://biocontainers.pro/tools/vcfdist", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vcfdist", "latest": {"2.4.0--h84372a0_0": "sha256:a4391dab9ffad1563f6a5f12924d1939e2d4aea7399c2a626ca4e36e19231e1b"}, "tags": {"2.4.0--h84372a0_0": "sha256:a4391dab9ffad1563f6a5f12924d1939e2d4aea7399c2a626ca4e36e19231e1b"}, "docker": "quay.io/biocontainers/vcfdist", "aliases": {"vcfdist": "/usr/local/bin/vcfdist", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcfdist.
singularity registry hpc automated addition for vcfdist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcfdist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcfdist:2.4.0--h84372a0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcfdist/2.4.0--h84372a0_0
$ module help quay.io/biocontainers/vcfdist/2.4.0--h84372a0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcfdist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcfdist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcfdist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcfdist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcfdist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcfdist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcfdist

```bash
$ singularity exec <container> /usr/local/bin/vcfdist
$ podman run --it --rm --entrypoint /usr/local/bin/vcfdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfdist   -v ${PWD} -w ${PWD} <container> -c " $@"
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