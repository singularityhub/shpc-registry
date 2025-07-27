---
layout: container
name:  "quay.io/biocontainers/r-tmae"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-tmae/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-tmae/container.yaml"
updated_at: "2025-07-27 04:36:33.578768"
latest: "1.0.5--r44h9ee0642_0"
container_url: "https://biocontainers.pro/tools/r-tmae"

versions:
 - "1.0.4--r41h9ee0642_0"
 - "1.0.4--r42h9ee0642_1"
 - "1.0.4--r43h9ee0642_2"
 - "1.0.5--r44h9ee0642_0"
description: "shpc-registry automated BioContainers addition for r-tmae"
config: {"url": "https://biocontainers.pro/tools/r-tmae", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-tmae", "latest": {"1.0.5--r44h9ee0642_0": "sha256:bc57c8d4a541586c40aec3228a2576137cb36bcb0982240d25d956d5eee44301"}, "tags": {"1.0.4--r41h9ee0642_0": "sha256:335ad6afe01c4a10e59e857f8c91e20b26df217c29e83c7166e93b429d3d9438", "1.0.4--r42h9ee0642_1": "sha256:9ea953175e38584f93152e9d7867c1a9654e47cf91ee1e01ae41cb06d421057b", "1.0.4--r43h9ee0642_2": "sha256:47f734beb1b254ac4d9e8d819952d3d36bed30a12835ed2c00ddd8ecffd1f1a1", "1.0.5--r44h9ee0642_0": "sha256:bc57c8d4a541586c40aec3228a2576137cb36bcb0982240d25d956d5eee44301"}, "docker": "quay.io/biocontainers/r-tmae"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-tmae.
shpc-registry automated BioContainers addition for r-tmae
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-tmae
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-tmae:1.0.5--r44h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-tmae/1.0.5--r44h9ee0642_0
$ module help quay.io/biocontainers/r-tmae/1.0.5--r44h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-tmae-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-tmae-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-tmae-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-tmae-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-tmae-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-tmae-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-tmae

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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