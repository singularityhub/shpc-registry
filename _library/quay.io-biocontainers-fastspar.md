---
layout: container
name:  "quay.io/biocontainers/fastspar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastspar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastspar/container.yaml"
updated_at: "2025-08-01 10:20:40.863411"
latest: "1.0.0--h1b620e3_6"
container_url: "https://biocontainers.pro/tools/fastspar"
aliases:
 - "fastspar"
 - "fastspar_bootstrap"
 - "fastspar_pvalues"
 - "fastspar_reduce"
versions:
 - "1.0.0--he5b3f4d_3"
 - "1.0.0--hac4c98c_5"
 - "1.0.0--h1b620e3_6"
description: "shpc-registry automated BioContainers addition for fastspar"
config: {"url": "https://biocontainers.pro/tools/fastspar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastspar", "latest": {"1.0.0--h1b620e3_6": "sha256:7389cb8df465663c0eed3b04d737cd93a2ee50cceca074a4f414c6a2e5a25b5a"}, "tags": {"1.0.0--he5b3f4d_3": "sha256:33bd34aa33f7d0b52778ebe9382a19f0c137920135acae647bb87e2dfead9a33", "1.0.0--hac4c98c_5": "sha256:384de55641349834be2e18a23bb8b7d64e317ed91eac6563ef9f57b6f38cae70", "1.0.0--h1b620e3_6": "sha256:7389cb8df465663c0eed3b04d737cd93a2ee50cceca074a4f414c6a2e5a25b5a"}, "docker": "quay.io/biocontainers/fastspar", "aliases": {"fastspar": "/usr/local/bin/fastspar", "fastspar_bootstrap": "/usr/local/bin/fastspar_bootstrap", "fastspar_pvalues": "/usr/local/bin/fastspar_pvalues", "fastspar_reduce": "/usr/local/bin/fastspar_reduce"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastspar.
shpc-registry automated BioContainers addition for fastspar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastspar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastspar:1.0.0--h1b620e3_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastspar/1.0.0--h1b620e3_6
$ module help quay.io/biocontainers/fastspar/1.0.0--h1b620e3_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastspar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastspar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastspar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastspar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastspar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastspar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastspar

```bash
$ singularity exec <container> /usr/local/bin/fastspar
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar_bootstrap

```bash
$ singularity exec <container> /usr/local/bin/fastspar_bootstrap
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar_bootstrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar_bootstrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar_pvalues

```bash
$ singularity exec <container> /usr/local/bin/fastspar_pvalues
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar_pvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar_pvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastspar_reduce

```bash
$ singularity exec <container> /usr/local/bin/fastspar_reduce
$ podman run --it --rm --entrypoint /usr/local/bin/fastspar_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastspar_reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
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