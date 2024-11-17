---
layout: container
name:  "ghcr.io/autamus/salmon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/salmon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/salmon/container.yaml"
updated_at: "2024-11-17 03:01:42.907277"
latest: "1.9.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/salmon"
aliases:
 - "salmon"
versions:
 - "1.4.0"
 - "1.5.2"
 - "latest"
 - "1.9.0"
description: "Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data."
config: {"docker": "ghcr.io/autamus/salmon", "url": "https://github.com/orgs/autamus/packages/container/package/salmon", "maintainer": "@vsoch", "description": "Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data.", "latest": {"1.9.0": "sha256:fae9d5b5a100649fbc708938f3c96779c1ca103ec6c42e2e4380d9a68a726c4c"}, "tags": {"1.4.0": "sha256:2fe7f560a48e93304f056cbb0abff46232d5471a225b390c06c3766c2821f23f", "1.5.2": "sha256:6b802de7c2b269a3a5b73a5160972d2a903192c67a0e9946999c8986fcdabc2c", "latest": "sha256:fae9d5b5a100649fbc708938f3c96779c1ca103ec6c42e2e4380d9a68a726c4c", "1.9.0": "sha256:fae9d5b5a100649fbc708938f3c96779c1ca103ec6c42e2e4380d9a68a726c4c"}, "aliases": {"salmon": "/opt/view/bin/salmon"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/salmon.
Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/salmon
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/salmon:1.9.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/salmon/1.9.0
$ module help ghcr.io/autamus/salmon/1.9.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### salmon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### salmon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### salmon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### salmon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### salmon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### salmon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### salmon

```bash
$ singularity exec <container> /opt/view/bin/salmon
$ podman run --it --rm --entrypoint /opt/view/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
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