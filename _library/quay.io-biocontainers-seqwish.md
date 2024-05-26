---
layout: container
name:  "quay.io/biocontainers/seqwish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqwish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqwish/container.yaml"
updated_at: "2024-05-26 03:10:34.936368"
latest: "0.7.10--h43eeafb_0"
container_url: "https://biocontainers.pro/tools/seqwish"
aliases:
 - "seqwish"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.7.6--h5b5514e_1"
 - "0.7.7--h5b5514e_1"
 - "0.7.8--h5b5514e_0"
 - "0.7.9--h43eeafb_2"
 - "0.7.10--h43eeafb_0"
description: "shpc-registry automated BioContainers addition for seqwish"
config: {"url": "https://biocontainers.pro/tools/seqwish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqwish", "latest": {"0.7.10--h43eeafb_0": "sha256:00c849e96cbcdc782bd6f17fa7d18c78b3743491b37675e5790fd620d35d29f7"}, "tags": {"0.7.6--h5b5514e_1": "sha256:04e9f1ccfb56b084970ef38390b02e035b79c825ac0e65e7cd7f06ab6521ff90", "0.7.7--h5b5514e_1": "sha256:3101b83e7532c616472607336b18aecf7088ee0314623154ae9fbb7510daee13", "0.7.8--h5b5514e_0": "sha256:775ebb3f80b4cdec22eb7a3286366a9913425bc19c64fc1fc46432cf58010124", "0.7.9--h43eeafb_2": "sha256:1e93a45d3a5c5f1d3e1f63d6b29930e34b64fe7b0e818407e801814fd0564d31", "0.7.10--h43eeafb_0": "sha256:00c849e96cbcdc782bd6f17fa7d18c78b3743491b37675e5790fd620d35d29f7"}, "docker": "quay.io/biocontainers/seqwish", "aliases": {"seqwish": "/usr/local/bin/seqwish", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqwish.
shpc-registry automated BioContainers addition for seqwish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqwish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqwish:0.7.10--h43eeafb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqwish/0.7.10--h43eeafb_0
$ module help quay.io/biocontainers/seqwish/0.7.10--h43eeafb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqwish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqwish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqwish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqwish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqwish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqwish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqwish

```bash
$ singularity exec <container> /usr/local/bin/seqwish
$ podman run --it --rm --entrypoint /usr/local/bin/seqwish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqwish   -v ${PWD} -w ${PWD} <container> -c " $@"
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