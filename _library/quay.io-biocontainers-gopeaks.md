---
layout: container
name:  "quay.io/biocontainers/gopeaks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gopeaks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gopeaks/container.yaml"
updated_at: "2026-01-01 03:56:09.564018"
latest: "1.0.0--h047eeb3_3"
container_url: "https://biocontainers.pro/tools/gopeaks"
aliases:
 - "gopeaks"
versions:
 - "1.0.0--hf05dbd8_0"
 - "1.0.0--heaae5f8_2"
 - "1.0.0--h047eeb3_3"
description: "singularity registry hpc automated addition for gopeaks"
config: {"url": "https://biocontainers.pro/tools/gopeaks", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gopeaks", "latest": {"1.0.0--h047eeb3_3": "sha256:3c0d0c4626708b3af9f1982010a7fb225685e9bd6e062a9db2b607fb55ea4c28"}, "tags": {"1.0.0--hf05dbd8_0": "sha256:63aec61503a6dd7a2f750a8c64fcf82d6834541adcf966c7b1b1b48a2d36cc88", "1.0.0--heaae5f8_2": "sha256:1fe73ab2a24a527d34584c2104a9ebc0b791175760c5b3963aaa07b5be9c4fc8", "1.0.0--h047eeb3_3": "sha256:3c0d0c4626708b3af9f1982010a7fb225685e9bd6e062a9db2b607fb55ea4c28"}, "docker": "quay.io/biocontainers/gopeaks", "aliases": {"gopeaks": "/usr/local/bin/gopeaks"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gopeaks.
singularity registry hpc automated addition for gopeaks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gopeaks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gopeaks:1.0.0--h047eeb3_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gopeaks/1.0.0--h047eeb3_3
$ module help quay.io/biocontainers/gopeaks/1.0.0--h047eeb3_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gopeaks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gopeaks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gopeaks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gopeaks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gopeaks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gopeaks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gopeaks

```bash
$ singularity exec <container> /usr/local/bin/gopeaks
$ podman run --it --rm --entrypoint /usr/local/bin/gopeaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gopeaks   -v ${PWD} -w ${PWD} <container> -c " $@"
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