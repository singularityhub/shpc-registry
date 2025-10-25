---
layout: container
name:  "quay.io/biocontainers/diamond"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/diamond/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/diamond/container.yaml"
updated_at: "2025-10-25 03:51:56.209304"
latest: "2.1.13--h13889ed_0"
container_url: "https://biocontainers.pro/tools/diamond"
aliases:
 - "diamond"
versions:
 - "2.0.14--hdcc8f71_0"
 - "2.1.9--h43eeafb_0"
 - "2.0.15--hb97b32f_1"
 - "2.1.10--h43eeafb_2"
 - "2.1.10--h5ca1c30_3"
 - "2.1.11--h5ca1c30_0"
 - "2.1.11--h5ca1c30_1"
 - "2.1.11--h5ca1c30_2"
 - "2.1.12--h13889ed_2"
 - "2.1.12--h13889ed_3"
 - "2.1.13--h13889ed_0"
description: "shpc-registry automated BioContainers addition for diamond"
config: {"url": "https://biocontainers.pro/tools/diamond", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for diamond", "latest": {"2.1.13--h13889ed_0": "sha256:a83a54a8f07531e47355f6cdf8eb03124b520fffb2b217c344591747c529f928"}, "tags": {"2.0.14--hdcc8f71_0": "sha256:275f3b3c587f8a40a39693db8acd91da8be6f053ff1426863da22061bd4e7957", "2.1.9--h43eeafb_0": "sha256:c3d56ca63d8061357ba0375d8d636519155b5601f6e93b807a827aa988f7e1d8", "2.0.15--hb97b32f_1": "sha256:192e0c2b5b9bffe0d7636af1e24ed83a1f5e3d4a20fcdd9cd62504fdeba6361d", "2.1.10--h43eeafb_2": "sha256:0ba585799731f988fbd20280c49a4406656302c513b7939770f86b7bab983b24", "2.1.10--h5ca1c30_3": "sha256:c04973fb22eb7faafd09adb9a06b0f6b027fd458038d3c1beece746e3f543f0b", "2.1.11--h5ca1c30_0": "sha256:b15db7a8300fbc65954a33675e15c9f2caa6f36b2ef0ff7e1bd76615f6472a2d", "2.1.11--h5ca1c30_1": "sha256:93031dd340eb1ded816be3fe1a8a0b6b2d6a454ef8d21865bf2042dc45be6586", "2.1.11--h5ca1c30_2": "sha256:1a857e1f94240e2ccee64c05c5108e0b86d58a2c83f52d293ac557933d167f10", "2.1.12--h13889ed_2": "sha256:ed18d53ad44875cece0cf1f1d6aea4a29d89c1379edd0b590cb30d4f54ccc774", "2.1.12--h13889ed_3": "sha256:ccd81a043d34598c83f7d05cb3da36b3a1a1b7f603bfd2e3835369db5cbb5a47", "2.1.13--h13889ed_0": "sha256:a83a54a8f07531e47355f6cdf8eb03124b520fffb2b217c344591747c529f928"}, "docker": "quay.io/biocontainers/diamond", "aliases": {"diamond": "/usr/local/bin/diamond"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/diamond.
shpc-registry automated BioContainers addition for diamond
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/diamond
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/diamond:2.1.13--h13889ed_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/diamond/2.1.13--h13889ed_0
$ module help quay.io/biocontainers/diamond/2.1.13--h13889ed_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### diamond-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### diamond-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### diamond-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### diamond-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### diamond-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### diamond-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
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