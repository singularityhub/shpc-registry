---
layout: container
name:  "quay.io/biocontainers/methplotlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/methplotlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/methplotlib/container.yaml"
updated_at: "2025-11-29 02:25:35.032992"
latest: "0.21.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/methplotlib"
aliases:
 - "allele_specific_modification"
 - "differential_modification"
 - "methplotlib"
 - "tabulate"
 - "natsort"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
versions:
 - "0.8.0--py_0"
 - "0.20.1--pyhdfd78af_0"
 - "0.19.0--pyhdfd78af_0"
 - "0.18.1--pyhdfd78af_0"
 - "0.17.0--py_0"
 - "0.14.1--py_0"
 - "0.21.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for methplotlib"
config: {"url": "https://biocontainers.pro/tools/methplotlib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for methplotlib", "latest": {"0.21.2--pyhdfd78af_0": "sha256:5d4239cd3fdafa04e67b6a93864234ad61bcf992cf84537f79e1abdf98b67a14"}, "tags": {"0.8.0--py_0": "sha256:3b96772549b32b6e8789439cfacae28f286c5a2b1a00d565a2604e0002740aa5", "0.20.1--pyhdfd78af_0": "sha256:65296658df2a13fdbd5ad056459c817538e6e7708c8a0f25cb6a2867682d8e90", "0.19.0--pyhdfd78af_0": "sha256:35e67db9af411957e0bf714f0685f961be9e37df1e515778e44bc6648827234e", "0.18.1--pyhdfd78af_0": "sha256:40d45aa3eb110f307e09bd5f2f0c54eed7c5a7dd21c917a5c250073ffea736b4", "0.17.0--py_0": "sha256:ed0f745f05ecd9d2b056c633f47e035b4f3cf5ed0a5fde41322dddf102c6783c", "0.14.1--py_0": "sha256:9ab71e0bb3c95c8531ecc79b30a6f2d7f5221a64f3808d395d570d3cc8e09ab3", "0.21.2--pyhdfd78af_0": "sha256:5d4239cd3fdafa04e67b6a93864234ad61bcf992cf84537f79e1abdf98b67a14"}, "docker": "quay.io/biocontainers/methplotlib", "aliases": {"allele_specific_modification": "/usr/local/bin/allele_specific_modification", "differential_modification": "/usr/local/bin/differential_modification", "methplotlib": "/usr/local/bin/methplotlib", "tabulate": "/usr/local/bin/tabulate", "natsort": "/usr/local/bin/natsort", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/methplotlib.
shpc-registry automated BioContainers addition for methplotlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/methplotlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/methplotlib:0.21.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/methplotlib/0.21.2--pyhdfd78af_0
$ module help quay.io/biocontainers/methplotlib/0.21.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### methplotlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### methplotlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### methplotlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### methplotlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### methplotlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### methplotlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### allele_specific_modification

```bash
$ singularity exec <container> /usr/local/bin/allele_specific_modification
$ podman run --it --rm --entrypoint /usr/local/bin/allele_specific_modification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/allele_specific_modification   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### differential_modification

```bash
$ singularity exec <container> /usr/local/bin/differential_modification
$ podman run --it --rm --entrypoint /usr/local/bin/differential_modification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/differential_modification   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### methplotlib

```bash
$ singularity exec <container> /usr/local/bin/methplotlib
$ podman run --it --rm --entrypoint /usr/local/bin/methplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/methplotlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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