---
layout: container
name:  "quay.io/biocontainers/fastq-and-furious"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-and-furious/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-and-furious/container.yaml"
updated_at: "2025-12-26 03:50:29.069322"
latest: "0.3.2--py311haab0aaa_6"
container_url: "https://biocontainers.pro/tools/fastq-and-furious"
aliases:
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3.2--py39hbf8eff0_0"
 - "0.3.2--py39hf95cd2a_3"
 - "0.3.2--py38he5da3d1_3"
 - "0.3.2--py312hf67a6ed_4"
 - "0.3.2--py311haab0aaa_5"
 - "0.3.2--py311haab0aaa_6"
description: "shpc-registry automated BioContainers addition for fastq-and-furious"
config: {"url": "https://biocontainers.pro/tools/fastq-and-furious", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-and-furious", "latest": {"0.3.2--py311haab0aaa_6": "sha256:383e12e7200196e3e8065df2dfa2a1fe9d4c88758877576424961e4f6fa3c584"}, "tags": {"0.3.2--py39hbf8eff0_0": "sha256:bb8c5c3846656e29b325f0c6cd6b3e5254d8d2947afe827a1d55e8df0b38aa66", "0.3.2--py39hf95cd2a_3": "sha256:4095229570443a3f7a69cf6151102123068773ecbd8df2dcad161bb449807bf9", "0.3.2--py38he5da3d1_3": "sha256:88aaf9729bb72a20adddd2fa527b42e9603be0083b0d486993d52cc7bd7e53d6", "0.3.2--py312hf67a6ed_4": "sha256:4293b687989ce2c11aaf60fc3feb54e9f40f88b288b987ac3d8e181f512151ef", "0.3.2--py311haab0aaa_5": "sha256:ec06444bfb2f440d3a80c89d8352de7d6c10fe19718d16554015bf15b37115d8", "0.3.2--py311haab0aaa_6": "sha256:383e12e7200196e3e8065df2dfa2a1fe9d4c88758877576424961e4f6fa3c584"}, "docker": "quay.io/biocontainers/fastq-and-furious", "aliases": {"2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-and-furious.
shpc-registry automated BioContainers addition for fastq-and-furious
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-and-furious
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-and-furious:0.3.2--py311haab0aaa_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-and-furious/0.3.2--py311haab0aaa_6
$ module help quay.io/biocontainers/fastq-and-furious/0.3.2--py311haab0aaa_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-and-furious-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-and-furious-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-and-furious-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-and-furious-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-and-furious-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-and-furious-inspect-deffile:

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