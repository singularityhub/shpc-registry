---
layout: container
name:  "ghcr.io/autamus/mercury"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/mercury/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/mercury/container.yaml"
updated_at: "2024-09-16 03:31:12.310384"
latest: "2.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/mercury"

versions:
 - "2.0.1"
 - "2.1.0"
 - "latest"
description: "Mercury is a C library for implementing RPC, optimized for HPC"
config: {"docker": "ghcr.io/autamus/mercury", "url": "https://github.com/orgs/autamus/packages/container/package/mercury", "maintainer": "@vsoch", "description": "Mercury is a C library for implementing RPC, optimized for HPC", "latest": {"2.1.0": "sha256:f5a6daec47307d9cfcb8686d256833c69007b4f098ffc039d847691503e8f53d"}, "tags": {"2.0.1": "sha256:03193fa2478d1cc5d0196145f6673727ab1456c386133b9fe0e164dce973e9f1", "2.1.0": "sha256:f5a6daec47307d9cfcb8686d256833c69007b4f098ffc039d847691503e8f53d", "latest": "sha256:f5a6daec47307d9cfcb8686d256833c69007b4f098ffc039d847691503e8f53d"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/mercury.
Mercury is a C library for implementing RPC, optimized for HPC
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/mercury
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mercury:2.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mercury/2.1.0
$ module help ghcr.io/autamus/mercury/2.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mercury-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mercury-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mercury-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mercury-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mercury-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mercury-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mercury

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