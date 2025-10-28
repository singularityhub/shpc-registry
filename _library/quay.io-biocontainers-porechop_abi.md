---
layout: container
name:  "quay.io/biocontainers/porechop_abi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/porechop_abi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/porechop_abi/container.yaml"
updated_at: "2025-10-28 03:38:59.548139"
latest: "0.5.1--py310h275bdba_0"
container_url: "https://biocontainers.pro/tools/porechop_abi"
aliases:
 - "porechop_abi"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.5.0--py39h6935b12_0"
 - "0.5.0--py310h2b6aa90_2"
 - "0.5.0--py38he0f268d_2"
 - "0.5.0--py312ha1f7cf2_3"
 - "0.5.0--py312h5e9d817_5"
 - "0.5.1--py310h275bdba_0"
description: "singularity registry hpc automated addition for porechop_abi"
config: {"url": "https://biocontainers.pro/tools/porechop_abi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for porechop_abi", "latest": {"0.5.1--py310h275bdba_0": "sha256:0fb86e1505894c4e5d39310f2aecce347ff346673e164c5b269d88dcb69d05c1"}, "tags": {"0.5.0--py39h6935b12_0": "sha256:818644f677de42bcc5b39aa2bff63ca7487823d67aa0cbcbd06e8590adba44fc", "0.5.0--py310h2b6aa90_2": "sha256:6422fdb833aff59574b946f92f7d8eb7f49ff13ac76591a2cfc79a9b335d153f", "0.5.0--py38he0f268d_2": "sha256:212b60abee0b05e0b709ad0cb830442b68b1068c234e697a44af1a762e8146ce", "0.5.0--py312ha1f7cf2_3": "sha256:4348ed046662bea837867259d0bdea1d136d85d493e59d7a4a4eb93526efd677", "0.5.0--py312h5e9d817_5": "sha256:65b60c935c87b5660c4be07b1ae34ffcc69da953273d05d18df9947349f2bdfd", "0.5.1--py310h275bdba_0": "sha256:0fb86e1505894c4e5d39310f2aecce347ff346673e164c5b269d88dcb69d05c1"}, "docker": "quay.io/biocontainers/porechop_abi", "aliases": {"porechop_abi": "/usr/local/bin/porechop_abi", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/porechop_abi.
singularity registry hpc automated addition for porechop_abi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/porechop_abi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/porechop_abi:0.5.1--py310h275bdba_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/porechop_abi/0.5.1--py310h275bdba_0
$ module help quay.io/biocontainers/porechop_abi/0.5.1--py310h275bdba_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### porechop_abi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### porechop_abi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### porechop_abi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### porechop_abi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### porechop_abi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### porechop_abi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### porechop_abi

```bash
$ singularity exec <container> /usr/local/bin/porechop_abi
$ podman run --it --rm --entrypoint /usr/local/bin/porechop_abi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop_abi   -v ${PWD} -w ${PWD} <container> -c " $@"
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