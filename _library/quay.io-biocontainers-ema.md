---
layout: container
name:  "quay.io/biocontainers/ema"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ema/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ema/container.yaml"
updated_at: "2025-11-20 03:27:08.343688"
latest: "0.7.0--h5ca1c30_2"
container_url: "https://biocontainers.pro/tools/ema"
aliases:
 - "ema"
versions:
 - "v0.6.2--hd28b015_1"
 - "0.6.2--h5b5514e_4"
 - "0.6.2--h43eeafb_6"
 - "0.7.0--h43eeafb_0"
 - "0.7.0--h5ca1c30_1"
 - "0.7.0--h5ca1c30_2"
description: "shpc-registry automated BioContainers addition for ema"
config: {"url": "https://biocontainers.pro/tools/ema", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ema", "latest": {"0.7.0--h5ca1c30_2": "sha256:b44272981e15c50be20654e9f90deae2916c5f38bfe4b8ef649d220efb753606"}, "tags": {"v0.6.2--hd28b015_1": "sha256:cbddfad4a5f9910eccc510e1fabb05d22a27f0315f3d17fe377c9d4ec20fb501", "0.6.2--h5b5514e_4": "sha256:6fc471216c51fe15f4266fd787c0fbf31dd267ef83cfa1f953cb723982bb99f9", "0.6.2--h43eeafb_6": "sha256:e5eae3e3a74d3d34ed8ba4a93ef68a41428185b05d0b8ff9c727cbc59813f248", "0.7.0--h43eeafb_0": "sha256:e531801356a0b342fd88b3913216ddd7bcc9069e9df1645937cde90fcb88abe9", "0.7.0--h5ca1c30_1": "sha256:129f67fbdf9d00deec8bb14bad359285ae30c2cc8eedda086ac93168074116ea", "0.7.0--h5ca1c30_2": "sha256:b44272981e15c50be20654e9f90deae2916c5f38bfe4b8ef649d220efb753606"}, "docker": "quay.io/biocontainers/ema", "aliases": {"ema": "/usr/local/bin/ema"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ema.
shpc-registry automated BioContainers addition for ema
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ema
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ema:0.7.0--h5ca1c30_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ema/0.7.0--h5ca1c30_2
$ module help quay.io/biocontainers/ema/0.7.0--h5ca1c30_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ema-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ema-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ema-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ema-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ema-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ema-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ema

```bash
$ singularity exec <container> /usr/local/bin/ema
$ podman run --it --rm --entrypoint /usr/local/bin/ema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ema   -v ${PWD} -w ${PWD} <container> -c " $@"
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