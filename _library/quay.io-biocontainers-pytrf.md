---
layout: container
name:  "quay.io/biocontainers/pytrf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pytrf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pytrf/container.yaml"
updated_at: "2024-11-16 03:42:35.367572"
latest: "1.3.3--py312hf67a6ed_0"
container_url: "https://biocontainers.pro/tools/pytrf"
aliases:
 - "pytrf"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
versions:
 - "1.2.1--py311h031d066_0"
 - "1.2.1--py38he5da3d1_1"
 - "1.3.0--py310h4b81fae_0"
 - "1.3.0--py39hf95cd2a_0"
 - "1.2.1--py39hf95cd2a_1"
 - "1.3.0--py310h7c593f9_1"
 - "1.3.3--py312hf67a6ed_0"
description: "singularity registry hpc automated addition for pytrf"
config: {"url": "https://biocontainers.pro/tools/pytrf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pytrf", "latest": {"1.3.3--py312hf67a6ed_0": "sha256:60d1a8495351a2b2eaf4620923a4210f52bdcccca5f2edaaf7d5086376203bb0"}, "tags": {"1.2.1--py311h031d066_0": "sha256:f456cb9560503e9078253b4ab1ede244736c96b7e57f4091fa65fe08116ec5a3", "1.2.1--py38he5da3d1_1": "sha256:a8965ef1f3031be7626e26448e8c5c178a280fa8a24429f14f0bc201f65f461d", "1.3.0--py310h4b81fae_0": "sha256:8196d705b6bbc727abf0ad2cd1b230961e38ec2cb12642fd2ec00ded4074e358", "1.3.0--py39hf95cd2a_0": "sha256:5703c1d5a142b1172ad8b1d267d6e969c598d9308606946ee1192fa81c07c42c", "1.2.1--py39hf95cd2a_1": "sha256:4c2cdd9aa2e0a0172bc0aed5fee498eb11a39553a207b0e26e1f946bc1f04c19", "1.3.0--py310h7c593f9_1": "sha256:ce15629125a658da109738ba81718f5c53edbd037163d86c46b946fa9689cfb1", "1.3.3--py312hf67a6ed_0": "sha256:60d1a8495351a2b2eaf4620923a4210f52bdcccca5f2edaaf7d5086376203bb0"}, "docker": "quay.io/biocontainers/pytrf", "aliases": {"pytrf": "/usr/local/bin/pytrf", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pytrf.
singularity registry hpc automated addition for pytrf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pytrf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pytrf:1.3.3--py312hf67a6ed_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pytrf/1.3.3--py312hf67a6ed_0
$ module help quay.io/biocontainers/pytrf/1.3.3--py312hf67a6ed_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pytrf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pytrf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pytrf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pytrf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pytrf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pytrf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pytrf

```bash
$ singularity exec <container> /usr/local/bin/pytrf
$ podman run --it --rm --entrypoint /usr/local/bin/pytrf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytrf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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