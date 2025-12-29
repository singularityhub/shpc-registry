---
layout: container
name:  "quay.io/biocontainers/gxformat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gxformat2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gxformat2/container.yaml"
updated_at: "2025-12-29 04:31:16.499246"
latest: "0.21.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gxformat2"
aliases:
 - "bioblend-galaxy-tests"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
 - "glacier"
versions:
 - "0.9.0--py_0"
 - "0.16.0--pyh7cba7a3_0"
 - "0.15.0--pyh864c0ab_0"
 - "0.14.0--pyh864c0ab_0"
 - "0.13.1--pyh864c0ab_0"
 - "0.12.0--pyh864c0ab_0"
 - "0.17.0--pyh7cba7a3_0"
 - "0.18.0--pyh7cba7a3_0"
 - "0.19.0--pyhdfd78af_0"
 - "0.20.0--pyhdfd78af_0"
 - "0.21.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for gxformat2"
config: {"url": "https://biocontainers.pro/tools/gxformat2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gxformat2", "latest": {"0.21.0--pyhdfd78af_0": "sha256:4822e8c11280544b4454bf56f81e37dc2f65756f768d6cf1ce034d9b6a52ac36"}, "tags": {"0.9.0--py_0": "sha256:c25c10522db22ba9f35924da069ac51c82b7f4f39da058056802ce7b1908065a", "0.16.0--pyh7cba7a3_0": "sha256:6312ef9f5fd5c219ed578eb7901b82c851ae970b8c1a52e69d77ecaa989563c6", "0.15.0--pyh864c0ab_0": "sha256:c77ac4361ecf2ea4918b5030fd49593b6a18315b671d393c7beecc8dd38fd414", "0.14.0--pyh864c0ab_0": "sha256:8c1b303849d20ae49abea318b7fbbd4294461dec555704a5097c562f33178af2", "0.13.1--pyh864c0ab_0": "sha256:2c63ccd2121fa404373dc18889b1bc57d43c2d01fdfbee876a59bdac137a04ff", "0.12.0--pyh864c0ab_0": "sha256:b10cdb0d1ba15ea51e51353a8cb42a7d74dbd5c1a6f7ade6e874cc964ac839ba", "0.17.0--pyh7cba7a3_0": "sha256:e1ec5fa5f4083c5d7f04d35fe4d91a3a3c695ceda68833952d9db2ba1d20f095", "0.18.0--pyh7cba7a3_0": "sha256:87a346c0e71665f4690f09baa41f76f11243b7c7212a3ccef3747ac9f1498b14", "0.19.0--pyhdfd78af_0": "sha256:e5ca985913989e55760a3cb8a3be19e17c3005fdec2545bc3f42282a94abbe19", "0.20.0--pyhdfd78af_0": "sha256:a2f6bb54889ec0adabf6a6428d50b00e9cce3a80537c0b96a273d02cd78657ea", "0.21.0--pyhdfd78af_0": "sha256:4822e8c11280544b4454bf56f81e37dc2f65756f768d6cf1ce034d9b6a52ac36"}, "docker": "quay.io/biocontainers/gxformat2", "aliases": {"bioblend-galaxy-tests": "/usr/local/bin/bioblend-galaxy-tests", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file", "glacier": "/usr/local/bin/glacier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gxformat2.
shpc-registry automated BioContainers addition for gxformat2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gxformat2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gxformat2:0.21.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gxformat2/0.21.0--pyhdfd78af_0
$ module help quay.io/biocontainers/gxformat2/0.21.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gxformat2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gxformat2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gxformat2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gxformat2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gxformat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gxformat2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioblend-galaxy-tests

```bash
$ singularity exec <container> /usr/local/bin/bioblend-galaxy-tests
$ podman run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glacier

```bash
$ singularity exec <container> /usr/local/bin/glacier
$ podman run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
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