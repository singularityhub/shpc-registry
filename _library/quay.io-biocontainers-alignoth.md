---
layout: container
name:  "quay.io/biocontainers/alignoth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alignoth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alignoth/container.yaml"
updated_at: "2023-11-21 02:34:41.080883"
latest: "0.10.0--hb27afe3_0"
container_url: "https://biocontainers.pro/tools/alignoth"
aliases:
 - "alignoth"
versions:
 - "0.7.0--h02737ae_0"
 - "0.7.1--h02737ae_0"
 - "0.7.3--h02737ae_0"
 - "0.8.2--h02737ae_0"
 - "0.8.2--hb27afe3_2"
 - "0.10.0--hb27afe3_0"
 - "0.9.0--hb27afe3_0"
description: "singularity registry hpc automated addition for alignoth"
config: {"url": "https://biocontainers.pro/tools/alignoth", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for alignoth", "latest": {"0.10.0--hb27afe3_0": "sha256:e35811610b268d7f0cdc790ec4446d31d80014ccae2fb37c44fc9438de3e9a18"}, "tags": {"0.7.0--h02737ae_0": "sha256:4faa632928afff6b8b32b42890cde8c0f8e47a3432ed02d110432df8de51b1d9", "0.7.1--h02737ae_0": "sha256:03525a1c72f0bbfafc5f6d116a740c78673d14a2311894f2d1be4d916888bd24", "0.7.3--h02737ae_0": "sha256:386499b883965cb54e42aa13605cf1202a727968d6c23279024c05c95b5aee42", "0.8.2--h02737ae_0": "sha256:8989e1442c915b2b1516982d419774dffbf568531f00562bda4cf4b1f6cc9efe", "0.8.2--hb27afe3_2": "sha256:1e7f23b529513a2422981c3a6ef47c0a436c587fceac667ffc84d65ab1e06b4e", "0.10.0--hb27afe3_0": "sha256:e35811610b268d7f0cdc790ec4446d31d80014ccae2fb37c44fc9438de3e9a18", "0.9.0--hb27afe3_0": "sha256:4fda78c554da26397b27d060d9b08ac452158d5ecbbcbb3fa4b76508072f4e70"}, "docker": "quay.io/biocontainers/alignoth", "aliases": {"alignoth": "/usr/local/bin/alignoth"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alignoth.
singularity registry hpc automated addition for alignoth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alignoth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alignoth:0.10.0--hb27afe3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alignoth/0.10.0--hb27afe3_0
$ module help quay.io/biocontainers/alignoth/0.10.0--hb27afe3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alignoth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alignoth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alignoth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alignoth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alignoth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alignoth-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alignoth

```bash
$ singularity exec <container> /usr/local/bin/alignoth
$ podman run --it --rm --entrypoint /usr/local/bin/alignoth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignoth   -v ${PWD} -w ${PWD} <container> -c " $@"
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