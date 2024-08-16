---
layout: container
name:  "quay.io/biocontainers/sentieon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sentieon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sentieon/container.yaml"
updated_at: "2024-08-16 02:44:31.420367"
latest: "202308.03--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/sentieon"
aliases:
 - "sentieon"
 - "sentieon-bwa"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "202112.05--h5b5514e_1"
 - "202112.06--h5b5514e_0"
 - "202112.06--h5b5514e_1"
 - "202112.07--h5b5514e_0"
 - "202112.07--h43eeafb_2"
 - "202112.07--h43eeafb_3"
 - "202308--h43eeafb_0"
 - "202308.01--h43eeafb_0"
 - "202308.02--h43eeafb_0"
 - "202308.03--h43eeafb_0"
description: "shpc-registry automated BioContainers addition for sentieon"
config: {"url": "https://biocontainers.pro/tools/sentieon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sentieon", "latest": {"202308.03--h43eeafb_0": "sha256:4a98fbe69ed9b046b79070d3597a833c5b825618705a0516a9388f23ae7b741f"}, "tags": {"202112.05--h5b5514e_1": "sha256:77ac2ecdf69680d30338e4c369f69795d40d9a44f6da1099ec00e602ef2e44d6", "202112.06--h5b5514e_0": "sha256:3c10a25f512c051776d9cfb77984b0c9b4c2a2ff1c2adaf5d6533a083e469665", "202112.06--h5b5514e_1": "sha256:2f8ef0f9155f837fcb4c053aea22fc94540592d0e3fcbf32956ea83f6e686a85", "202112.07--h5b5514e_0": "sha256:eef3a77dfa211ca808f7e12dbcb45bcf3c24f7bdffa9b6e63518d3d49c64d1fb", "202112.07--h43eeafb_2": "sha256:8a9c7893da49f3e0f6635a1dc6bedd62caf756df723bf802ddec181e25f90a01", "202112.07--h43eeafb_3": "sha256:18bb7678fb2fa2418903315133b9b606d513d0abce3a74cb36aaa2ef164f4553", "202308--h43eeafb_0": "sha256:a5f0d6c049a4bd360633fc2abb64e3ef911e9be7b9acee11532b44e1ececd59e", "202308.01--h43eeafb_0": "sha256:488ac234b5da1d64454ab0601b6c8c70958b6bdb88010b767f3daaa2ff26f685", "202308.02--h43eeafb_0": "sha256:cc2dfed85c76974210f2fa454b9c80013fdfeed86c9ffd3deeb003fd8e08b8ab", "202308.03--h43eeafb_0": "sha256:4a98fbe69ed9b046b79070d3597a833c5b825618705a0516a9388f23ae7b741f"}, "docker": "quay.io/biocontainers/sentieon", "aliases": {"sentieon": "/usr/local/bin/sentieon", "sentieon-bwa": "/usr/local/bin/sentieon-bwa", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sentieon.
shpc-registry automated BioContainers addition for sentieon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sentieon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sentieon:202308.03--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sentieon/202308.03--h43eeafb_0
$ module help quay.io/biocontainers/sentieon/202308.03--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sentieon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sentieon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sentieon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sentieon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sentieon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sentieon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sentieon

```bash
$ singularity exec <container> /usr/local/bin/sentieon
$ podman run --it --rm --entrypoint /usr/local/bin/sentieon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sentieon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sentieon-bwa

```bash
$ singularity exec <container> /usr/local/bin/sentieon-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/sentieon-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sentieon-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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