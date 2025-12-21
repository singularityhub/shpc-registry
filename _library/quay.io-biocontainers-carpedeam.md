---
layout: container
name:  "quay.io/biocontainers/carpedeam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/carpedeam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/carpedeam/container.yaml"
updated_at: "2025-12-21 04:32:45.199298"
latest: "1.0.1--hd6d6fdc_0"
container_url: "https://biocontainers.pro/tools/carpedeam"
aliases:
 - "carpedeam"
 - "gawk-5.3.0"
 - "gawkbug"
 - "awk"
 - "gawk"
versions:
 - "1.0.0--pl5321h6a68c12_0"
 - "1.0.1--hd6d6fdc_0"
description: "singularity registry hpc automated addition for carpedeam"
config: {"url": "https://biocontainers.pro/tools/carpedeam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for carpedeam", "latest": {"1.0.1--hd6d6fdc_0": "sha256:476a66e8d260667306cb0d00f9b060527b0de7c29d2bdc58c16c9da3bb7d875e"}, "tags": {"1.0.0--pl5321h6a68c12_0": "sha256:8a9c3213abc0b5323e90af83f8d66cbc5917cbe4921394f5b6ce4de8ee8af023", "1.0.1--hd6d6fdc_0": "sha256:476a66e8d260667306cb0d00f9b060527b0de7c29d2bdc58c16c9da3bb7d875e"}, "docker": "quay.io/biocontainers/carpedeam", "aliases": {"carpedeam": "/usr/local/bin/carpedeam", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "gawkbug": "/usr/local/bin/gawkbug", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/carpedeam.
singularity registry hpc automated addition for carpedeam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/carpedeam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/carpedeam:1.0.1--hd6d6fdc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/carpedeam/1.0.1--hd6d6fdc_0
$ module help quay.io/biocontainers/carpedeam/1.0.1--hd6d6fdc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### carpedeam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### carpedeam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### carpedeam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### carpedeam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### carpedeam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### carpedeam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### carpedeam

```bash
$ singularity exec <container> /usr/local/bin/carpedeam
$ podman run --it --rm --entrypoint /usr/local/bin/carpedeam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/carpedeam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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