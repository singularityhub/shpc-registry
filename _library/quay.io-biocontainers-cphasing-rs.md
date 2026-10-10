---
layout: container
name:  "quay.io/biocontainers/cphasing-rs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cphasing-rs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cphasing-rs/container.yaml"
updated_at: "2026-10-10 19:35:27.414860"
latest: "0.3.0--h6b974a3_0"
container_url: "https://biocontainers.pro/tools/cphasing-rs"
aliases:
 - "cphasing-rs"
versions:
 - "0.3.0--h6b974a3_0"
description: "singularity registry hpc automated addition for cphasing-rs"
config: {"url": "https://biocontainers.pro/tools/cphasing-rs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cphasing-rs", "latest": {"0.3.0--h6b974a3_0": "sha256:559acbd8a687510016de378b447f270cb626ca6ee5282cd8ee14dc520351838f"}, "tags": {"0.3.0--h6b974a3_0": "sha256:559acbd8a687510016de378b447f270cb626ca6ee5282cd8ee14dc520351838f"}, "docker": "quay.io/biocontainers/cphasing-rs", "aliases": {"cphasing-rs": "/usr/local/bin/cphasing-rs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cphasing-rs.
singularity registry hpc automated addition for cphasing-rs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cphasing-rs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cphasing-rs:0.3.0--h6b974a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cphasing-rs/0.3.0--h6b974a3_0
$ module help quay.io/biocontainers/cphasing-rs/0.3.0--h6b974a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cphasing-rs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cphasing-rs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cphasing-rs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cphasing-rs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cphasing-rs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cphasing-rs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cphasing-rs

```bash
$ singularity exec <container> /usr/local/bin/cphasing-rs
$ podman run --it --rm --entrypoint /usr/local/bin/cphasing-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cphasing-rs   -v ${PWD} -w ${PWD} <container> -c " $@"
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