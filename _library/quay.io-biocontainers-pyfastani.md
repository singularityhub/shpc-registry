---
layout: container
name:  "quay.io/biocontainers/pyfastani"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyfastani/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyfastani/container.yaml"
updated_at: "2025-01-16 03:00:49.581660"
latest: "0.6.0--py311hc84137b_1"
container_url: "https://biocontainers.pro/tools/pyfastani"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.4.1--py39h2add14b_0"
 - "0.4.1--py39h4e691d4_3"
 - "0.5.1--py38h5cf8b27_0"
 - "0.5.1--py39h4e691d4_0"
 - "0.4.1--py38h5cf8b27_3"
 - "0.5.1--py38h40d3509_1"
 - "0.6.0--py310hdf79db3_0"
 - "0.6.0--py311hc84137b_1"
description: "singularity registry hpc automated addition for pyfastani"
config: {"url": "https://biocontainers.pro/tools/pyfastani", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyfastani", "latest": {"0.6.0--py311hc84137b_1": "sha256:373bf92ff75cfa8bbf993105dae7ca42f6d9debc3ed2597b107773506e49c3ed"}, "tags": {"0.4.1--py39h2add14b_0": "sha256:6d64b2758d97d4e89f64635e226878075f5629c650141452af088c793b204f04", "0.4.1--py39h4e691d4_3": "sha256:e84548ee3b5f15b62aac4e98e5c3d7aa8c860760d5f06821fb34ec9ac807b16f", "0.5.1--py38h5cf8b27_0": "sha256:20d1137bf818313afb074cad634b74249f0048058faa7d188424b98edea83048", "0.5.1--py39h4e691d4_0": "sha256:4de20ca96fab0856ee9a15157ad172759dfa41d30cd2b3a496059ce9ffa7d80c", "0.4.1--py38h5cf8b27_3": "sha256:b64f3e48930f1dfad58935d8683e47c1b133a0a9608bb0fe89f22df4352b2e0e", "0.5.1--py38h40d3509_1": "sha256:2bf0853f3cf21e9e324705fd38f2e4a4aa724a64c853fb88c355cce07b6a113b", "0.6.0--py310hdf79db3_0": "sha256:52b572e0dda9e2763d548308e2addbfc712006fa9c00b40b9fd4ef1405609fe4", "0.6.0--py311hc84137b_1": "sha256:373bf92ff75cfa8bbf993105dae7ca42f6d9debc3ed2597b107773506e49c3ed"}, "docker": "quay.io/biocontainers/pyfastani", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyfastani.
singularity registry hpc automated addition for pyfastani
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyfastani
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyfastani:0.6.0--py311hc84137b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyfastani/0.6.0--py311hc84137b_1
$ module help quay.io/biocontainers/pyfastani/0.6.0--py311hc84137b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyfastani-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyfastani-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyfastani-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyfastani-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyfastani-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyfastani-inspect-deffile:

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