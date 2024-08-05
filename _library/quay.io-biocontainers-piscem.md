---
layout: container
name:  "quay.io/biocontainers/piscem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piscem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piscem/container.yaml"
updated_at: "2024-08-05 04:04:09.087314"
latest: "0.10.2--h7c313c4_1"
container_url: "https://biocontainers.pro/tools/piscem"
aliases:
 - "piscem"
versions:
 - "0.4.3--h52b76fa_0"
 - "0.6.0--h52b76fa_0"
 - "0.5.1--h52b76fa_0"
 - "0.6.0--h52b76fa_1"
 - "0.6.0--h09b9a2f_2"
 - "0.6.1--h09b9a2f_0"
 - "0.6.3--h09b9a2f_0"
 - "0.7.0--h7c313c4_0"
 - "0.7.1--h7c313c4_0"
 - "0.8.0--h7c313c4_0"
 - "0.10.2--h7c313c4_1"
 - "0.9.0--h7c313c4_1"
description: "singularity registry hpc automated addition for piscem"
config: {"url": "https://biocontainers.pro/tools/piscem", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for piscem", "latest": {"0.10.2--h7c313c4_1": "sha256:459fb3daece699f9a4b26287a588b4116fd8465b3f95042ae26b5f66bba07659"}, "tags": {"0.4.3--h52b76fa_0": "sha256:e69951f3697fc1c9b7b4ba5fa3b31c01db5a2e8d60f684d84587bb55339ce716", "0.6.0--h52b76fa_0": "sha256:f68a973ae119249ef22b36583b9a530280e54e5b242a8f3aec1ae890bb00cf6d", "0.5.1--h52b76fa_0": "sha256:d3f0daed723ae8abee2013f21b2c26073b1753dd0626cb0d355e49c19577d782", "0.6.0--h52b76fa_1": "sha256:8e9623dd2007ea746aadd283627680064ac1f3e244d35a47bab70374ac3dc216", "0.6.0--h09b9a2f_2": "sha256:a3476b421adc7f646228d4549f98382aec8a9326f038958705e0b2bb63d27c53", "0.6.1--h09b9a2f_0": "sha256:638f76b0cc75a00735b8caee440de327fa7a5ab8c31cb598da9d3dddb7977871", "0.6.3--h09b9a2f_0": "sha256:fc38783ef8d1ca9d77f833c6b4d9d35fe03adcf5f5ec6f9e89291b6f168cf1a7", "0.7.0--h7c313c4_0": "sha256:123c699b0af36e8211c0c9bf9afd745a0164a3b0965b343a9de74522a856a6c6", "0.7.1--h7c313c4_0": "sha256:19d0dca3936d797e0bae3e2826af3ffde8271861afc7b42e0f5b232d9fcf9565", "0.8.0--h7c313c4_0": "sha256:75dae6599cfe7397e4804bb9e4f48f8966dc3e1cd0c15225cbbeb32c369e4c48", "0.10.2--h7c313c4_1": "sha256:459fb3daece699f9a4b26287a588b4116fd8465b3f95042ae26b5f66bba07659", "0.9.0--h7c313c4_1": "sha256:b9f86483903adc30775b58b0a2bba65c1cbc3a404b11495841b302abc0e73e45"}, "docker": "quay.io/biocontainers/piscem", "aliases": {"piscem": "/usr/local/bin/piscem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piscem.
singularity registry hpc automated addition for piscem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piscem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piscem:0.10.2--h7c313c4_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piscem/0.10.2--h7c313c4_1
$ module help quay.io/biocontainers/piscem/0.10.2--h7c313c4_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piscem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piscem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piscem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piscem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piscem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piscem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### piscem

```bash
$ singularity exec <container> /usr/local/bin/piscem
$ podman run --it --rm --entrypoint /usr/local/bin/piscem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piscem   -v ${PWD} -w ${PWD} <container> -c " $@"
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