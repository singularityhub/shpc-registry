---
layout: container
name:  "quay.io/biocontainers/aster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aster/container.yaml"
updated_at: "2025-10-03 03:09:41.205700"
latest: "1.23--h9948957_0"
container_url: "https://biocontainers.pro/tools/aster"
aliases:
 - "asterisk"
 - "astral"
 - "astral-pro"
versions:
 - "1.3--h9f5acd7_1"
 - "1.13--h9f5acd7_1"
 - "1.10--h9f5acd7_0"
 - "1.15--h9f5acd7_0"
 - "1.15--h4ac6f70_2"
 - "1.16--h4ac6f70_1"
 - "1.16--h4ac6f70_2"
 - "1.19--h4ac6f70_0"
 - "1.19--h9948957_1"
 - "1.19--h9948957_2"
 - "1.22--h9948957_0"
 - "1.22--h9948957_1"
 - "1.23--h9948957_0"
description: "singularity registry hpc automated addition for aster"
config: {"url": "https://biocontainers.pro/tools/aster", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aster", "latest": {"1.23--h9948957_0": "sha256:26a499caa50b7c77f68ed72de0767c2389db4ab5ca8ff10de7d11c4826d82e14"}, "tags": {"1.3--h9f5acd7_1": "sha256:7662b11a19008b7a13b77ae116f2d20231d3ca19b47fabf4977b90b438fd4d9f", "1.13--h9f5acd7_1": "sha256:e920b1c7056a761b814990427ee02e0912436dfb1a2c577a9e06d7e0daad50fc", "1.10--h9f5acd7_0": "sha256:560eb7339e54eed72efd2206afd091a429200cba29787b2821bc4a0f86da3065", "1.15--h9f5acd7_0": "sha256:448675af5acef5e394212ed13e27508b496c9b0e38ec12eae3e9d4f304e03846", "1.15--h4ac6f70_2": "sha256:6a4a575329c24067145d5f98e368e032eef5d68d27527918e5429c0d8af9aed6", "1.16--h4ac6f70_1": "sha256:69aceadbe6052bebe779cf030deb63604c667a16a12e85eac1fd822b1989cc68", "1.16--h4ac6f70_2": "sha256:f46b3f0223878eadf569bb18b3c1a149183244bd50062221ce5065f6e2049c67", "1.19--h4ac6f70_0": "sha256:654a76711a94f2e9cacb085963e59e85a057e9aca695949665ff4b29b4b8487f", "1.19--h9948957_1": "sha256:028290b0dcb7d75794c35a95d28c6954c087793ad04f032e742fb3b8201d9c6b", "1.19--h9948957_2": "sha256:5466ad863f9544a92208ab1b2b922c45a6622f92c4bc1eadef235947c1ac6fd2", "1.22--h9948957_0": "sha256:6a543134e106b6d6f4ba87fe0786e1ba2622f5148bdfcda8846a165a8acfd811", "1.22--h9948957_1": "sha256:35e1f3bcf72fb9f889d0d583080af94019676f945c4c02d045f78058cce41852", "1.23--h9948957_0": "sha256:26a499caa50b7c77f68ed72de0767c2389db4ab5ca8ff10de7d11c4826d82e14"}, "docker": "quay.io/biocontainers/aster", "aliases": {"asterisk": "/usr/local/bin/asterisk", "astral": "/usr/local/bin/astral", "astral-pro": "/usr/local/bin/astral-pro"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aster.
singularity registry hpc automated addition for aster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aster:1.23--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aster/1.23--h9948957_0
$ module help quay.io/biocontainers/aster/1.23--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asterisk

```bash
$ singularity exec <container> /usr/local/bin/asterisk
$ podman run --it --rm --entrypoint /usr/local/bin/asterisk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asterisk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### astral

```bash
$ singularity exec <container> /usr/local/bin/astral
$ podman run --it --rm --entrypoint /usr/local/bin/astral   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/astral   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### astral-pro

```bash
$ singularity exec <container> /usr/local/bin/astral-pro
$ podman run --it --rm --entrypoint /usr/local/bin/astral-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/astral-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
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