---
layout: container
name:  "quay.io/biocontainers/wgatools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wgatools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wgatools/container.yaml"
updated_at: "2025-03-23 03:18:11.647130"
latest: "1.0.0--hf6a8760_0"
container_url: "https://biocontainers.pro/tools/wgatools"
aliases:
 - "wgatools"
versions:
 - "0.1.0--h7c767d4_1"
 - "0.1.1--h7c767d4_0"
 - "0.1.1--hf6a8760_1"
 - "1.0.0--hf6a8760_0"
description: "singularity registry hpc automated addition for wgatools"
config: {"url": "https://biocontainers.pro/tools/wgatools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for wgatools", "latest": {"1.0.0--hf6a8760_0": "sha256:94bfaeab50d123cce8ef54f85cb75a646f337027f380b8501b252cbd6587b5ba"}, "tags": {"0.1.0--h7c767d4_1": "sha256:d7eab7965f7ca4fe8c25f98b6382ab87abce14ac42eebc72d184150244a5cabb", "0.1.1--h7c767d4_0": "sha256:262cc07f7d99ec72f7ac5e473afb17537de0e110f561e79662041e1422762d5f", "0.1.1--hf6a8760_1": "sha256:36c9d312df021d313df3057409d6650828ba5fce96661e3f432be29e7375abea", "1.0.0--hf6a8760_0": "sha256:94bfaeab50d123cce8ef54f85cb75a646f337027f380b8501b252cbd6587b5ba"}, "docker": "quay.io/biocontainers/wgatools", "aliases": {"wgatools": "/usr/local/bin/wgatools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wgatools.
singularity registry hpc automated addition for wgatools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wgatools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wgatools:1.0.0--hf6a8760_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wgatools/1.0.0--hf6a8760_0
$ module help quay.io/biocontainers/wgatools/1.0.0--hf6a8760_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wgatools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wgatools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wgatools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wgatools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wgatools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wgatools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wgatools

```bash
$ singularity exec <container> /usr/local/bin/wgatools
$ podman run --it --rm --entrypoint /usr/local/bin/wgatools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgatools   -v ${PWD} -w ${PWD} <container> -c " $@"
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