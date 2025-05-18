---
layout: container
name:  "ghcr.io/autamus/eagle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/eagle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/eagle/container.yaml"
updated_at: "2025-05-18 03:19:35.844007"
latest: "1.1.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/eagle"
aliases:
 - "eagle"
 - "eagle-nm"
 - "eagle-rc"
versions:
 - "1.1.2"
 - "latest"
 - "1.1.3"
description: "Explicit Alternative Genome Likelihood Evaluator"
config: {"docker": "ghcr.io/autamus/eagle", "url": "https://github.com/orgs/autamus/packages/container/package/eagle", "maintainer": "@vsoch", "description": "Explicit Alternative Genome Likelihood Evaluator", "latest": {"1.1.2": "sha256:852fec8c165a5a23f4cf9de32bb2d4873c04fd092ab0442aef6403a2d63da15d"}, "tags": {"1.1.2": "sha256:852fec8c165a5a23f4cf9de32bb2d4873c04fd092ab0442aef6403a2d63da15d", "latest": "sha256:dd3376b547bce29434ccef72a49c42c0dcdb116bdf255aa77d6e868f5a369e35", "1.1.3": "sha256:dd3376b547bce29434ccef72a49c42c0dcdb116bdf255aa77d6e868f5a369e35"}, "aliases": {"eagle": "/opt/view/bin/eagle", "eagle-nm": "/opt/view/bin/eagle-nm", "eagle-rc": "/opt/view/bin/eagle-rc"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/eagle.
Explicit Alternative Genome Likelihood Evaluator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/eagle
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/eagle:1.1.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/eagle/1.1.2
$ module help ghcr.io/autamus/eagle/1.1.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eagle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eagle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eagle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eagle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eagle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eagle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eagle

```bash
$ singularity exec <container> /opt/view/bin/eagle
$ podman run --it --rm --entrypoint /opt/view/bin/eagle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/eagle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eagle-nm

```bash
$ singularity exec <container> /opt/view/bin/eagle-nm
$ podman run --it --rm --entrypoint /opt/view/bin/eagle-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/eagle-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eagle-rc

```bash
$ singularity exec <container> /opt/view/bin/eagle-rc
$ podman run --it --rm --entrypoint /opt/view/bin/eagle-rc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/eagle-rc   -v ${PWD} -w ${PWD} <container> -c " $@"
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