---
layout: container
name:  "ghcr.io/autamus/r-seqlogo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/r-seqlogo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/r-seqlogo/container.yaml"
updated_at: "2025-05-19 03:20:53.673165"
latest: "1.62.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/r-seqlogo"

versions:
 - "1.56.0"
 - "latest"
 - "1.62.0"
description: "Sequence logos for DNA sequence alignments"
config: {"docker": "ghcr.io/autamus/r-seqlogo", "url": "https://github.com/orgs/autamus/packages/container/package/r-seqlogo", "maintainer": "@vsoch", "description": "Sequence logos for DNA sequence alignments", "latest": {"1.62.0": "sha256:8407d10c2c94789c55509081af05e50767ae8337942fd761daffb9293be72f70"}, "tags": {"1.56.0": "sha256:761a07e0c24d4fc7657c99825128717253a616fd1f0e00a48ab611f899649724", "latest": "sha256:8407d10c2c94789c55509081af05e50767ae8337942fd761daffb9293be72f70", "1.62.0": "sha256:8407d10c2c94789c55509081af05e50767ae8337942fd761daffb9293be72f70"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/r-seqlogo.
Sequence logos for DNA sequence alignments
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/r-seqlogo
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/r-seqlogo:1.62.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/r-seqlogo/1.62.0
$ module help ghcr.io/autamus/r-seqlogo/1.62.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-seqlogo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-seqlogo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-seqlogo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-seqlogo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-seqlogo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-seqlogo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-seqlogo

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