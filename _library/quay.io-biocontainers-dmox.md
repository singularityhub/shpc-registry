---
layout: container
name:  "quay.io/biocontainers/dmox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dmox/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dmox/container.yaml"
updated_at: "2025-08-28 03:33:27.075448"
latest: "0.2.1--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/dmox"
aliases:
 - "dmox"
versions:
 - "0.1.3--h3ab6199_0"
 - "0.2.1--h3ab6199_0"
description: "singularity registry hpc automated addition for dmox"
config: {"url": "https://biocontainers.pro/tools/dmox", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dmox", "latest": {"0.2.1--h3ab6199_0": "sha256:dcb8c38a7cdf902c475cf24e2992ff6f20eca9157dbbc79f7bdd14d4fa476914"}, "tags": {"0.1.3--h3ab6199_0": "sha256:6052484f8f96034f14df49ca153de9d8fc17a7caf46a23f939614083b2a2feed", "0.2.1--h3ab6199_0": "sha256:dcb8c38a7cdf902c475cf24e2992ff6f20eca9157dbbc79f7bdd14d4fa476914"}, "docker": "quay.io/biocontainers/dmox", "aliases": {"dmox": "/usr/local/bin/dmox"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dmox.
singularity registry hpc automated addition for dmox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dmox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dmox:0.2.1--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dmox/0.2.1--h3ab6199_0
$ module help quay.io/biocontainers/dmox/0.2.1--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dmox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dmox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dmox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dmox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dmox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dmox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dmox

```bash
$ singularity exec <container> /usr/local/bin/dmox
$ podman run --it --rm --entrypoint /usr/local/bin/dmox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmox   -v ${PWD} -w ${PWD} <container> -c " $@"
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