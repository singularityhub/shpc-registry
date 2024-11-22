---
layout: container
name:  "quay.io/biocontainers/bifrost"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bifrost/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bifrost/container.yaml"
updated_at: "2024-11-22 03:22:04.972271"
latest: "1.3.5--h43eeafb_1"
container_url: "https://biocontainers.pro/tools/bifrost"
aliases:
 - "Bifrost"
versions:
 - "1.0.6.5--h5b5514e_1"
 - "1.2.0--h5b5514e_0"
 - "1.2.0--h43eeafb_2"
 - "1.2.1--h43eeafb_0"
 - "1.3.1--h43eeafb_0"
 - "1.3.5--h43eeafb_0"
 - "1.3.5--h43eeafb_1"
description: "shpc-registry automated BioContainers addition for bifrost"
config: {"url": "https://biocontainers.pro/tools/bifrost", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bifrost", "latest": {"1.3.5--h43eeafb_1": "sha256:ee4a7b0b96bf6c2513837ef5d74c9cfdc45dc0b0d5781a54257ae97072e7ee95"}, "tags": {"1.0.6.5--h5b5514e_1": "sha256:933b5a1374ae058685ce41ba2e0f1e5b8d25078a0acceb6064758af2d7272dfe", "1.2.0--h5b5514e_0": "sha256:506e372ae617f1cb6b05ae9a19562cf4b06ce0f41931caee777c1101cc37576d", "1.2.0--h43eeafb_2": "sha256:a003f4b3ee571fa7119ec58e626f5f712972bd53fbcc1b79c02041fd0c685f1b", "1.2.1--h43eeafb_0": "sha256:6fe5c765eb938512b5b0796bdcd34184ce7a3ea25b0f43eaaff49e517e34133f", "1.3.1--h43eeafb_0": "sha256:930a4e4d5709d78168a333e3058ba7274e337deeaa7b97a2a80245b09f68426b", "1.3.5--h43eeafb_0": "sha256:89395689cf0bc7c7a8763a69c0f04f96db0f56b6609f9ce02343416a725a2ca5", "1.3.5--h43eeafb_1": "sha256:ee4a7b0b96bf6c2513837ef5d74c9cfdc45dc0b0d5781a54257ae97072e7ee95"}, "docker": "quay.io/biocontainers/bifrost", "aliases": {"Bifrost": "/usr/local/bin/Bifrost"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bifrost.
shpc-registry automated BioContainers addition for bifrost
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bifrost
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bifrost:1.3.5--h43eeafb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bifrost/1.3.5--h43eeafb_1
$ module help quay.io/biocontainers/bifrost/1.3.5--h43eeafb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bifrost-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bifrost-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bifrost-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bifrost-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bifrost-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bifrost-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bifrost

```bash
$ singularity exec <container> /usr/local/bin/Bifrost
$ podman run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bifrost   -v ${PWD} -w ${PWD} <container> -c " $@"
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