---
layout: container
name:  "quay.io/biocontainers/unmux"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unmux/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unmux/container.yaml"
updated_at: "2026-08-06 05:46:13.593561"
latest: "0.4.0--hec9b1f2_0"
container_url: "https://biocontainers.pro/tools/unmux"
aliases:
 - "unmux"
versions:
 - "0.2.0--hec9b1f2_0"
 - "0.4.0--hec9b1f2_0"
 - "0.3.0--hec9b1f2_0"
description: "singularity registry hpc automated addition for unmux"
config: {"url": "https://biocontainers.pro/tools/unmux", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unmux", "latest": {"0.4.0--hec9b1f2_0": "sha256:3753faef019785bc98bf0fad3d01f868e748a4e744cee29b6f0e9c3afbaea81c"}, "tags": {"0.2.0--hec9b1f2_0": "sha256:6e3d7c9a2f50e66e06652abf7074ab8525e5d92bb01c817ca86cc987cc2de680", "0.4.0--hec9b1f2_0": "sha256:3753faef019785bc98bf0fad3d01f868e748a4e744cee29b6f0e9c3afbaea81c", "0.3.0--hec9b1f2_0": "sha256:6486d5294e5a9ba9fd49beeb326f188a2bfb26c8445111585bfc1ad6e64bcc1d"}, "docker": "quay.io/biocontainers/unmux", "aliases": {"unmux": "/usr/local/bin/unmux"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unmux.
singularity registry hpc automated addition for unmux
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unmux
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unmux:0.4.0--hec9b1f2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unmux/0.4.0--hec9b1f2_0
$ module help quay.io/biocontainers/unmux/0.4.0--hec9b1f2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unmux-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unmux-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unmux-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unmux-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unmux-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unmux-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unmux

```bash
$ singularity exec <container> /usr/local/bin/unmux
$ podman run --it --rm --entrypoint /usr/local/bin/unmux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unmux   -v ${PWD} -w ${PWD} <container> -c " $@"
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