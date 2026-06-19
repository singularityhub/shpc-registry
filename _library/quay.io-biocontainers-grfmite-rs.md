---
layout: container
name:  "quay.io/biocontainers/grfmite-rs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grfmite-rs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grfmite-rs/container.yaml"
updated_at: "2026-06-19 07:12:11.779092"
latest: "0.3.0--hfa8f182_0"
container_url: "https://biocontainers.pro/tools/grfmite-rs"
aliases:
 - "grf_rs"
 - "grfmite-rs"
versions:
 - "0.2.1--hfa8f182_0"
 - "0.3.0--hfa8f182_0"
description: "singularity registry hpc automated addition for grfmite-rs"
config: {"url": "https://biocontainers.pro/tools/grfmite-rs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grfmite-rs", "latest": {"0.3.0--hfa8f182_0": "sha256:92ca3d6a37bb904fc00fa1cea7083858a4eb9a16f59b53605f0e8e52dd952dcb"}, "tags": {"0.2.1--hfa8f182_0": "sha256:2364d8b65c34449b0eb98990e8d2a8befec72285b463be5ec4face2b1aac9e5d", "0.3.0--hfa8f182_0": "sha256:92ca3d6a37bb904fc00fa1cea7083858a4eb9a16f59b53605f0e8e52dd952dcb"}, "docker": "quay.io/biocontainers/grfmite-rs", "aliases": {"grf_rs": "/usr/local/bin/grf_rs", "grfmite-rs": "/usr/local/bin/grfmite-rs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grfmite-rs.
singularity registry hpc automated addition for grfmite-rs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grfmite-rs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grfmite-rs:0.3.0--hfa8f182_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grfmite-rs/0.3.0--hfa8f182_0
$ module help quay.io/biocontainers/grfmite-rs/0.3.0--hfa8f182_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grfmite-rs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grfmite-rs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grfmite-rs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grfmite-rs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grfmite-rs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grfmite-rs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grf_rs

```bash
$ singularity exec <container> /usr/local/bin/grf_rs
$ podman run --it --rm --entrypoint /usr/local/bin/grf_rs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf_rs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grfmite-rs

```bash
$ singularity exec <container> /usr/local/bin/grfmite-rs
$ podman run --it --rm --entrypoint /usr/local/bin/grfmite-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grfmite-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
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