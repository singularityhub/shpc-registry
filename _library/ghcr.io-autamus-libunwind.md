---
layout: container
name:  "ghcr.io/autamus/libunwind"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/libunwind/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/libunwind/container.yaml"
updated_at: "2024-11-25 03:39:48.097111"
latest: "1.5"
container_url: "https://github.com/orgs/autamus/packages/container/package/libunwind"

versions:
 - "1.5"
 - "latest"
description: "A portable and efficient C programming interface (API) to determine the call-chain of a program."
config: {"docker": "ghcr.io/autamus/libunwind", "url": "https://github.com/orgs/autamus/packages/container/package/libunwind", "maintainer": "@vsoch", "description": "A portable and efficient C programming interface (API) to determine the call-chain of a program.", "latest": {"1.5": "sha256:aff63eeabf23a19a27aa54037a4d98def73b8b0ccb7fea7557b57d4918be17cb"}, "tags": {"1.5": "sha256:aff63eeabf23a19a27aa54037a4d98def73b8b0ccb7fea7557b57d4918be17cb", "latest": "sha256:aff63eeabf23a19a27aa54037a4d98def73b8b0ccb7fea7557b57d4918be17cb"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/libunwind.
A portable and efficient C programming interface (API) to determine the call-chain of a program.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/libunwind
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libunwind:1.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libunwind/1.5
$ module help ghcr.io/autamus/libunwind/1.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libunwind-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libunwind-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libunwind-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libunwind-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libunwind-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libunwind-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libunwind

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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