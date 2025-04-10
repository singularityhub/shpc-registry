---
layout: container
name:  "quay.io/biocontainers/vembrane"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vembrane/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vembrane/container.yaml"
updated_at: "2025-04-10 03:15:48.775023"
latest: "1.0.7--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vembrane"
aliases:
 - "vembrane"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.8.0--pyhdfd78af_0"
 - "0.13.2--pyhdfd78af_0"
 - "0.12.1--pyhdfd78af_0"
 - "0.11.2--pyhdfd78af_0"
 - "0.10.1--pyhdfd78af_1"
 - "0.14.0--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_0"
 - "1.0.2--pyhdfd78af_0"
 - "1.0.3--pyhdfd78af_0"
 - "1.0.4--pyhdfd78af_0"
 - "1.0.5--pyhdfd78af_0"
 - "1.0.6--pyhdfd78af_0"
 - "1.0.7--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for vembrane"
config: {"url": "https://biocontainers.pro/tools/vembrane", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vembrane", "latest": {"1.0.7--pyhdfd78af_0": "sha256:b2a6ec54fb1176f2292a78667e536f9be4bb376341e42f778f50888425b92471"}, "tags": {"0.8.0--pyhdfd78af_0": "sha256:573262178d6cbb96d9bba0c5670657b1018b609a140cf730b3406a0c32c012a4", "0.13.2--pyhdfd78af_0": "sha256:40197cbbd8207933838f2f3ce6854b94f5ccc005fd85486c7ef5cb8b611610d0", "0.12.1--pyhdfd78af_0": "sha256:686538f47f83714b97caea0542bce5d0b8bd5156858309645fcb82930b89f802", "0.11.2--pyhdfd78af_0": "sha256:489b3a09a0b561fe4e374138d3a3caf2db16b36589eaed3762da16263b244ae7", "0.10.1--pyhdfd78af_1": "sha256:890896de65e18e8d70780d17f43a9fc60e4e102c6f7540dd80988982a0b7f252", "0.14.0--pyhdfd78af_0": "sha256:c609e33edb333796dac2da1ba7e286a40835798cd3aec4a0c5c5c9c5267963fd", "1.0.0--pyhdfd78af_0": "sha256:739c07511e80f9f8c0d933b53d83c92dcd0d475f6ff5df0957871b6bf75122b2", "1.0.1--pyhdfd78af_0": "sha256:0858f8494566ec157eb70582fe20fcc5e4868682257927178a9cd6617a297104", "1.0.2--pyhdfd78af_0": "sha256:bbada4c8a4fb4715d296dd22ce6192e0a91ad2573c3fa58aead6101bb2651e00", "1.0.3--pyhdfd78af_0": "sha256:92a86106c56d1333eda013cb9120caeb8ee829d2c0e4f251b4fd8afdabec30d1", "1.0.4--pyhdfd78af_0": "sha256:fc63868466bf5599b76626b63988f04bba74cfd8eb4ae0dde6f5dfb81a7523ea", "1.0.5--pyhdfd78af_0": "sha256:0fc6bc5f39e40ac9a4106bb0ddaf2e1b367219a443e21b4120f9e984756fe4e2", "1.0.6--pyhdfd78af_0": "sha256:85b5f861e743c6cb39b3b887e346a48bf979be1d28ec84ea0f5b11b665f23a74", "1.0.7--pyhdfd78af_0": "sha256:b2a6ec54fb1176f2292a78667e536f9be4bb376341e42f778f50888425b92471"}, "docker": "quay.io/biocontainers/vembrane", "aliases": {"vembrane": "/usr/local/bin/vembrane", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vembrane.
shpc-registry automated BioContainers addition for vembrane
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vembrane
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vembrane:1.0.7--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vembrane/1.0.7--pyhdfd78af_0
$ module help quay.io/biocontainers/vembrane/1.0.7--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vembrane-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vembrane-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vembrane-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vembrane-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vembrane-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vembrane-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vembrane

```bash
$ singularity exec <container> /usr/local/bin/vembrane
$ podman run --it --rm --entrypoint /usr/local/bin/vembrane   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vembrane   -v ${PWD} -w ${PWD} <container> -c " $@"
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