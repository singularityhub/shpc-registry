---
layout: container
name:  "quay.io/biocontainers/squigulator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/squigulator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/squigulator/container.yaml"
updated_at: "2025-02-18 03:10:25.624818"
latest: "0.4.0--h5ca1c30_2"
container_url: "https://biocontainers.pro/tools/squigulator"
aliases:
 - "squigulator"
versions:
 - "0.2.0--h5b5514e_0"
 - "0.2.0--h43eeafb_2"
 - "0.2.1--h43eeafb_0"
 - "0.2.2--h43eeafb_0"
 - "0.3.0--h43eeafb_0"
 - "0.4.0--h43eeafb_1"
 - "0.4.0--h5ca1c30_2"
description: "singularity registry hpc automated addition for squigulator"
config: {"url": "https://biocontainers.pro/tools/squigulator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for squigulator", "latest": {"0.4.0--h5ca1c30_2": "sha256:f52a9c8ca957e64f44cc43ee6b1472833ba6dc97fc63bbe577a6bcacc4ab252e"}, "tags": {"0.2.0--h5b5514e_0": "sha256:8b5af8cb0b36a2afb2c9c7d44e3cbdff7415a5dc9b90e353d899b9cfa34b3644", "0.2.0--h43eeafb_2": "sha256:1579d3e0ba087c901c21e06e6257d340fc6e01013bfcee3802680223321bbe98", "0.2.1--h43eeafb_0": "sha256:90c6a3211bd3bfc3ae8c5d7bfa19e5d83f6b79811fafb9d247ed34b2059fe4bb", "0.2.2--h43eeafb_0": "sha256:58ffd2b55bbc2e44a628f58216a2d1ef78f961fa66cc275798971c3ac8d3866d", "0.3.0--h43eeafb_0": "sha256:bc88c6334f21619d7c7bb1723c57ed416d295ed5e8c599ce1d093a5ffcc9e28f", "0.4.0--h43eeafb_1": "sha256:dea4f045fa5ea8746a05dc027dfd86eaa0edc4e04e614c64848a6d28c4c481be", "0.4.0--h5ca1c30_2": "sha256:f52a9c8ca957e64f44cc43ee6b1472833ba6dc97fc63bbe577a6bcacc4ab252e"}, "docker": "quay.io/biocontainers/squigulator", "aliases": {"squigulator": "/usr/local/bin/squigulator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/squigulator.
singularity registry hpc automated addition for squigulator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/squigulator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/squigulator:0.4.0--h5ca1c30_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/squigulator/0.4.0--h5ca1c30_2
$ module help quay.io/biocontainers/squigulator/0.4.0--h5ca1c30_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### squigulator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### squigulator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### squigulator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### squigulator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### squigulator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### squigulator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### squigulator

```bash
$ singularity exec <container> /usr/local/bin/squigulator
$ podman run --it --rm --entrypoint /usr/local/bin/squigulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/squigulator   -v ${PWD} -w ${PWD} <container> -c " $@"
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