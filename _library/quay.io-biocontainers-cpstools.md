---
layout: container
name:  "quay.io/biocontainers/cpstools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cpstools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cpstools/container.yaml"
updated_at: "2025-01-09 03:41:57.387100"
latest: "2.0.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cpstools"
aliases:
 - "cpstools"
 - "numpy-config"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "1.0.0--pyhdfd78af_0"
 - "1.0.13--pyhdfd78af_0"
 - "2.0.0--pyhdfd78af_0"
 - "2.0.2--pyhdfd78af_0"
 - "2.0.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for cpstools"
config: {"url": "https://biocontainers.pro/tools/cpstools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cpstools", "latest": {"2.0.5--pyhdfd78af_0": "sha256:8561d39234727074fb158044ec533fb33004e60fafc6f1fdc9e5bb74cccafa62"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:65268e0b5137b99eaf798e9ad45296cfd01e9275f3c86d732167b41549b99806", "1.0.13--pyhdfd78af_0": "sha256:a27f850ee691dac04365b3c0d3186fbf08ce314c40b6ffdc845ae9e9750eb589", "2.0.0--pyhdfd78af_0": "sha256:6dabcaeb6dfcf791395d5afacab918afc68e1f6dfe1a3bb72205e7aebf974ae3", "2.0.2--pyhdfd78af_0": "sha256:ea234c2796a4cdca015b5f7474b5703ac3d177bbea0b516e020d59e53fc8dd1d", "2.0.5--pyhdfd78af_0": "sha256:8561d39234727074fb158044ec533fb33004e60fafc6f1fdc9e5bb74cccafa62"}, "docker": "quay.io/biocontainers/cpstools", "aliases": {"cpstools": "/usr/local/bin/cpstools", "numpy-config": "/usr/local/bin/numpy-config", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cpstools.
singularity registry hpc automated addition for cpstools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cpstools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cpstools:2.0.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cpstools/2.0.5--pyhdfd78af_0
$ module help quay.io/biocontainers/cpstools/2.0.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cpstools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cpstools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cpstools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cpstools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cpstools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cpstools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpstools

```bash
$ singularity exec <container> /usr/local/bin/cpstools
$ podman run --it --rm --entrypoint /usr/local/bin/cpstools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpstools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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