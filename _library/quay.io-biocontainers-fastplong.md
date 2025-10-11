---
layout: container
name:  "quay.io/biocontainers/fastplong"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastplong/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastplong/container.yaml"
updated_at: "2025-10-11 03:05:46.343126"
latest: "0.4.1--h224cc79_0"
container_url: "https://biocontainers.pro/tools/fastplong"
aliases:
 - "fastplong"
 - "igzip"
versions:
 - "0.2.0--h125f33a_0"
 - "0.2.2--heae3180_0"
 - "0.3.0--h224cc79_0"
 - "0.4.1--h224cc79_0"
description: "singularity registry hpc automated addition for fastplong"
config: {"url": "https://biocontainers.pro/tools/fastplong", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastplong", "latest": {"0.4.1--h224cc79_0": "sha256:964674a0c7433fe85b00a319c9f9f7909ac69ca882700cea2a9f06aca04dd879"}, "tags": {"0.2.0--h125f33a_0": "sha256:b015a7fc10675cd23f6191ef26e1d8d8cd42453a794587309ceb4785bf065485", "0.2.2--heae3180_0": "sha256:ad1b620b4899fdb37a90388b9db0f35adb5952caddcccef495a2e392d6387192", "0.3.0--h224cc79_0": "sha256:cb798120d765a97db01c8a4e7a71ced8add45010bd6073fe8a191e84a0ee5498", "0.4.1--h224cc79_0": "sha256:964674a0c7433fe85b00a319c9f9f7909ac69ca882700cea2a9f06aca04dd879"}, "docker": "quay.io/biocontainers/fastplong", "aliases": {"fastplong": "/usr/local/bin/fastplong", "igzip": "/usr/local/bin/igzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastplong.
singularity registry hpc automated addition for fastplong
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastplong
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastplong:0.4.1--h224cc79_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastplong/0.4.1--h224cc79_0
$ module help quay.io/biocontainers/fastplong/0.4.1--h224cc79_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastplong-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastplong-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastplong-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastplong-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastplong-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastplong-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastplong

```bash
$ singularity exec <container> /usr/local/bin/fastplong
$ podman run --it --rm --entrypoint /usr/local/bin/fastplong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastplong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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