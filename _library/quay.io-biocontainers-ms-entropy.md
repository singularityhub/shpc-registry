---
layout: container
name:  "quay.io/biocontainers/ms-entropy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ms-entropy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ms-entropy/container.yaml"
updated_at: "2024-03-25 03:02:47.261916"
latest: "1.1.2--py38he5da3d1_0"
container_url: "https://biocontainers.pro/tools/ms-entropy"
aliases:
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.9.11--py39hf95cd2a_0"
 - "0.9.12--py39hf95cd2a_0"
 - "1.0.2--py38he5da3d1_0"
 - "1.1.1--py39hf95cd2a_0"
 - "1.0.4--py39hf95cd2a_0"
 - "1.1.2--py38he5da3d1_0"
 - "1.1.2--py39hf95cd2a_0"
 - "1.0.4--py38he5da3d1_0"
 - "0.9.12--py310h4b81fae_0"
description: "singularity registry hpc automated addition for ms-entropy"
config: {"url": "https://biocontainers.pro/tools/ms-entropy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ms-entropy", "latest": {"1.1.2--py38he5da3d1_0": "sha256:aab9c476ff3e6bcc05649501f7bdea067d2bcf4f19c12ad30e27b836d0572ca9"}, "tags": {"0.9.11--py39hf95cd2a_0": "sha256:9a214f867f7e25607222706c91c9e85003bdffabd968d1a66dd033b24026fc3a", "0.9.12--py39hf95cd2a_0": "sha256:7e003f0fbcac40d0083c5dd52d9e480eef120f804b8a0bb70862ac98c4bc8222", "1.0.2--py38he5da3d1_0": "sha256:137e0aa1e63664ce757b015c3614d2010ef8f376414f73917ac63f9ae9ba25b8", "1.1.1--py39hf95cd2a_0": "sha256:884532bba6b8755a13fb3935c0d6a7102ce281e3adc5e25a247d121adc1cefa6", "1.0.4--py39hf95cd2a_0": "sha256:7ab28059fd65e8bc3204a088eb1fdf01c2628dcf8361879efca07206dcddf0f6", "1.1.2--py38he5da3d1_0": "sha256:aab9c476ff3e6bcc05649501f7bdea067d2bcf4f19c12ad30e27b836d0572ca9", "1.1.2--py39hf95cd2a_0": "sha256:93c45dbda07cb2856bb0c78e12eeccf3e2b67c342c3fda6eb7084b64506f56c4", "1.0.4--py38he5da3d1_0": "sha256:c17461cd4cb253c879b206ffaa9a61c9c5fc3ebe041c012156340dfe4895af9e", "0.9.12--py310h4b81fae_0": "sha256:18c02b6bb949a6aa8b26f6a33c568f4d408fe95d351b6fe725bccb23c9688548"}, "docker": "quay.io/biocontainers/ms-entropy", "aliases": {"f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ms-entropy.
singularity registry hpc automated addition for ms-entropy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ms-entropy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ms-entropy:1.1.2--py38he5da3d1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ms-entropy/1.1.2--py38he5da3d1_0
$ module help quay.io/biocontainers/ms-entropy/1.1.2--py38he5da3d1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ms-entropy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ms-entropy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ms-entropy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ms-entropy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ms-entropy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ms-entropy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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