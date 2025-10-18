---
layout: container
name:  "quay.io/biocontainers/cyushuffle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cyushuffle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cyushuffle/container.yaml"
updated_at: "2025-10-18 03:01:36.146025"
latest: "1.1.2--py39hbcbf7aa_7"
container_url: "https://biocontainers.pro/tools/cyushuffle"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.1.2--py39hbf8eff0_3"
 - "1.1.2--py310h4b81fae_5"
 - "1.1.2--py39hf95cd2a_5"
 - "1.1.2--py311hdad781d_6"
 - "1.1.2--py39hbcbf7aa_7"
description: "shpc-registry automated BioContainers addition for cyushuffle"
config: {"url": "https://biocontainers.pro/tools/cyushuffle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cyushuffle", "latest": {"1.1.2--py39hbcbf7aa_7": "sha256:c88ce278a39f20fb97f2a49b36b86cf48f41e285934002749718fbb0aa0bc10f"}, "tags": {"1.1.2--py39hbf8eff0_3": "sha256:4b723525bd15ddbe8f48e2eea10288c65a0c737ee4c929dd38719e3460cab357", "1.1.2--py310h4b81fae_5": "sha256:9e2ebbf5dd99b27071f7cb4afc3918c6880b6364f9de16d3923019b887a2cada", "1.1.2--py39hf95cd2a_5": "sha256:ec4c7424ea1aa08aacde8f68b0c1d24635568c62010aeda2b09c563b96f143de", "1.1.2--py311hdad781d_6": "sha256:3d7b6b97c5b438b8138ef7547571c96ea76455097ed0ca4c4a7fb2abad871b32", "1.1.2--py39hbcbf7aa_7": "sha256:c88ce278a39f20fb97f2a49b36b86cf48f41e285934002749718fbb0aa0bc10f"}, "docker": "quay.io/biocontainers/cyushuffle", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cyushuffle.
shpc-registry automated BioContainers addition for cyushuffle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cyushuffle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cyushuffle:1.1.2--py39hbcbf7aa_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cyushuffle/1.1.2--py39hbcbf7aa_7
$ module help quay.io/biocontainers/cyushuffle/1.1.2--py39hbcbf7aa_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cyushuffle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cyushuffle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cyushuffle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cyushuffle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cyushuffle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cyushuffle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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