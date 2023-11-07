---
layout: container
name:  "quay.io/biocontainers/cuttlefish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cuttlefish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cuttlefish/container.yaml"
updated_at: "2023-11-07 03:17:44.558495"
latest: "2.2.0--h6a68c12_2"
container_url: "https://biocontainers.pro/tools/cuttlefish"
aliases:
 - "cuttlefish"
versions:
 - "2.1.0--hf1761c0_0"
 - "2.1.1--hf1761c0_0"
 - "2.2.0--hf1761c0_0"
 - "2.2.0--h6a68c12_2"
description: "shpc-registry automated BioContainers addition for cuttlefish"
config: {"url": "https://biocontainers.pro/tools/cuttlefish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cuttlefish", "latest": {"2.2.0--h6a68c12_2": "sha256:3686e0b6e29fad1b1c4e345b5ed9a84c02535b59740f2d8be80014c9bf34c891"}, "tags": {"2.1.0--hf1761c0_0": "sha256:aa009abd48c372125e060d39f49f1690be74b6dac276d451bf1cc4c847a914d6", "2.1.1--hf1761c0_0": "sha256:8bccced83dd6bbf87843cf08851563c812ef7c36afda2efbcf0d54f9102b913f", "2.2.0--hf1761c0_0": "sha256:63cdd7778b144a37684ae53b8e760ed00852f3010aa79292b3f1a6a6470f0992", "2.2.0--h6a68c12_2": "sha256:3686e0b6e29fad1b1c4e345b5ed9a84c02535b59740f2d8be80014c9bf34c891"}, "docker": "quay.io/biocontainers/cuttlefish", "aliases": {"cuttlefish": "/usr/local/bin/cuttlefish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cuttlefish.
shpc-registry automated BioContainers addition for cuttlefish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cuttlefish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cuttlefish:2.2.0--h6a68c12_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cuttlefish/2.2.0--h6a68c12_2
$ module help quay.io/biocontainers/cuttlefish/2.2.0--h6a68c12_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cuttlefish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cuttlefish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cuttlefish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cuttlefish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cuttlefish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cuttlefish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cuttlefish

```bash
$ singularity exec <container> /usr/local/bin/cuttlefish
$ podman run --it --rm --entrypoint /usr/local/bin/cuttlefish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cuttlefish   -v ${PWD} -w ${PWD} <container> -c " $@"
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