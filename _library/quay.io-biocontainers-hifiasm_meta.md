---
layout: container
name:  "quay.io/biocontainers/hifiasm_meta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hifiasm_meta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hifiasm_meta/container.yaml"
updated_at: "2025-09-01 04:09:33.507654"
latest: "hamtv0.3.3--h5ca1c30_0"
container_url: "https://biocontainers.pro/tools/hifiasm_meta"
aliases:
 - "hifiasm_meta"
versions:
 - "hamtv0.3--h5b5514e_1"
 - "hamtv0.3.1--h43eeafb_2"
 - "hamtv0.3.2--h43eeafb_1"
 - "hamtv0.3.2--h5ca1c30_2"
 - "hamtv0.3.3--h5ca1c30_0"
description: "shpc-registry automated BioContainers addition for hifiasm_meta"
config: {"url": "https://biocontainers.pro/tools/hifiasm_meta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hifiasm_meta", "latest": {"hamtv0.3.3--h5ca1c30_0": "sha256:7bff0152ad71da4dab404f92289a0ffca4c5abb75b4426f100bcd0cd30c7b8c4"}, "tags": {"hamtv0.3--h5b5514e_1": "sha256:776514c78ca278f86cadebc71a9a0fb43d31959b55d795c5888e5784b9a1e0f9", "hamtv0.3.1--h43eeafb_2": "sha256:b75f269f9e8304a70b3c0f9eef4ae5570fecde7f9c880f9e5a30ecbd7c03c014", "hamtv0.3.2--h43eeafb_1": "sha256:6ee68d9007ff9e1ce4035b32f84b069e4cd00a0ed38ce9f7151aa645577d3714", "hamtv0.3.2--h5ca1c30_2": "sha256:4ca0575c48b8f6f5e12765c721f32d54a40309aaa4436a6061c77d3635a78f62", "hamtv0.3.3--h5ca1c30_0": "sha256:7bff0152ad71da4dab404f92289a0ffca4c5abb75b4426f100bcd0cd30c7b8c4"}, "docker": "quay.io/biocontainers/hifiasm_meta", "aliases": {"hifiasm_meta": "/usr/local/bin/hifiasm_meta"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hifiasm_meta.
shpc-registry automated BioContainers addition for hifiasm_meta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hifiasm_meta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hifiasm_meta:hamtv0.3.3--h5ca1c30_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hifiasm_meta/hamtv0.3.3--h5ca1c30_0
$ module help quay.io/biocontainers/hifiasm_meta/hamtv0.3.3--h5ca1c30_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hifiasm_meta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hifiasm_meta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hifiasm_meta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hifiasm_meta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hifiasm_meta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hifiasm_meta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hifiasm_meta

```bash
$ singularity exec <container> /usr/local/bin/hifiasm_meta
$ podman run --it --rm --entrypoint /usr/local/bin/hifiasm_meta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiasm_meta   -v ${PWD} -w ${PWD} <container> -c " $@"
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