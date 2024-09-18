---
layout: container
name:  "quay.io/biocontainers/strobealign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strobealign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strobealign/container.yaml"
updated_at: "2024-09-18 03:33:40.185405"
latest: "0.13.0--h43eeafb_1"
container_url: "https://biocontainers.pro/tools/strobealign"
aliases:
 - "strobealign"
versions:
 - "0.8.0--h5b5514e_0"
 - "0.9.0--h5b5514e_0"
 - "0.9.0--h43eeafb_2"
 - "0.10.0--h43eeafb_2"
 - "0.11.0--h43eeafb_0"
 - "0.12.0--h43eeafb_0"
 - "0.13.0--h43eeafb_0"
 - "0.13.0--h43eeafb_1"
description: "singularity registry hpc automated addition for strobealign"
config: {"url": "https://biocontainers.pro/tools/strobealign", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for strobealign", "latest": {"0.13.0--h43eeafb_1": "sha256:7ad41cf1601dd4310a693d45493a6cd677bf4b73a0a4ba8c41f0676e8af5cdde"}, "tags": {"0.8.0--h5b5514e_0": "sha256:ed5a49652c2d82798289955d567586f7accd48b2f0119a88eefef28d34cf63c5", "0.9.0--h5b5514e_0": "sha256:d7dc12a30ef323095218d88839e8a1ea88b1e96b13fc62acc620457eb76aa3ff", "0.9.0--h43eeafb_2": "sha256:1d61628d8d9756c471ba0c1695b2d943a7fe0a059068e8058325faf7f1e442cb", "0.10.0--h43eeafb_2": "sha256:6c06d7a62d3712468f5893d80638913e9e6e722edd26594a5bf4e7b88dd84007", "0.11.0--h43eeafb_0": "sha256:a9f2b5da4a363631cc5841416a21bf5e5eb27bb251a610948eab2c6c73824983", "0.12.0--h43eeafb_0": "sha256:c8e00d3b69607519fddd8f5913e4dd86bd5514b6b69e22ab96cd41ca7d943d00", "0.13.0--h43eeafb_0": "sha256:cf30daad8d8c0c5307232b58b4a3652676c22e524242db5cf40b0bea09789354", "0.13.0--h43eeafb_1": "sha256:7ad41cf1601dd4310a693d45493a6cd677bf4b73a0a4ba8c41f0676e8af5cdde"}, "docker": "quay.io/biocontainers/strobealign", "aliases": {"strobealign": "/usr/local/bin/strobealign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strobealign.
singularity registry hpc automated addition for strobealign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strobealign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strobealign:0.13.0--h43eeafb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strobealign/0.13.0--h43eeafb_1
$ module help quay.io/biocontainers/strobealign/0.13.0--h43eeafb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strobealign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strobealign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strobealign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strobealign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strobealign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strobealign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### strobealign

```bash
$ singularity exec <container> /usr/local/bin/strobealign
$ podman run --it --rm --entrypoint /usr/local/bin/strobealign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strobealign   -v ${PWD} -w ${PWD} <container> -c " $@"
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