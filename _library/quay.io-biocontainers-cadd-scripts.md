---
layout: container
name:  "quay.io/biocontainers/cadd-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cadd-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cadd-scripts/container.yaml"
updated_at: "2025-05-15 03:56:48.754488"
latest: "1.7.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/cadd-scripts"
aliases:
 - "cadd-install.sh"
 - "cadd.sh"
 - "stone"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
versions:
 - "1.6--hdfd78af_1"
 - "1.7--hdfd78af_0"
 - "1.6.post1--hdfd78af_0"
 - "1.7.1--hdfd78af_0"
 - "1.7.2--hdfd78af_1"
 - "1.6.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for cadd-scripts"
config: {"url": "https://biocontainers.pro/tools/cadd-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cadd-scripts", "latest": {"1.7.2--hdfd78af_1": "sha256:922c3ab9dddc2308524299be6155be763303e0afb78a316880816546e40fda9a"}, "tags": {"1.6--hdfd78af_1": "sha256:74bbc85ed86e868598b2438dfad64aa902f6a5a6d6af73a380698a3136169b74", "1.7--hdfd78af_0": "sha256:3376f97e2cbab429b54d97cdea439b888439ae8f0778b20cda5c0990691fb38d", "1.6.post1--hdfd78af_0": "sha256:062d37a73b36d545e467e497310f1ca7902efc2a7ab6232be5c486f61838f835", "1.7.1--hdfd78af_0": "sha256:24bda52c2e6e89ef0a4a69655d4523791ad6fbd8e55a261ab8b1cdacfcdd137c", "1.7.2--hdfd78af_1": "sha256:922c3ab9dddc2308524299be6155be763303e0afb78a316880816546e40fda9a", "1.6.1--hdfd78af_0": "sha256:5f00e3040d564982667d5e5313ccb6a5e444328eb7b7bba660022d7d87a5e493"}, "docker": "quay.io/biocontainers/cadd-scripts", "aliases": {"cadd-install.sh": "/usr/local/bin/cadd-install.sh", "cadd.sh": "/usr/local/bin/cadd.sh", "stone": "/usr/local/bin/stone", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cadd-scripts.
shpc-registry automated BioContainers addition for cadd-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cadd-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cadd-scripts:1.7.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cadd-scripts/1.7.2--hdfd78af_1
$ module help quay.io/biocontainers/cadd-scripts/1.7.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cadd-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cadd-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cadd-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cadd-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cadd-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cadd-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cadd-install.sh

```bash
$ singularity exec <container> /usr/local/bin/cadd-install.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cadd-install.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cadd-install.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cadd.sh

```bash
$ singularity exec <container> /usr/local/bin/cadd.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cadd.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cadd.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
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