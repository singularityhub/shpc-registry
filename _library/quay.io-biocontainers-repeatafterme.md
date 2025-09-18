---
layout: container
name:  "quay.io/biocontainers/repeatafterme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/repeatafterme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/repeatafterme/container.yaml"
updated_at: "2025-09-18 05:38:46.018199"
latest: "0.0.7--h7b50bb2_0"
container_url: "https://biocontainers.pro/tools/repeatafterme"
aliases:
 - "RAMExtend"
 - "calcPaths.pl"
 - "davidExtendConsRAM.pl"
 - "extend-stk.pl"
 - "twoBitToFa"
versions:
 - "0.0.7--h7b50bb2_0"
description: "singularity registry hpc automated addition for repeatafterme"
config: {"url": "https://biocontainers.pro/tools/repeatafterme", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for repeatafterme", "latest": {"0.0.7--h7b50bb2_0": "sha256:dc1efa0774bcb83fd937b3cdf5bc1b879919092f08bb2c1c31badfa4f67bac0b"}, "tags": {"0.0.7--h7b50bb2_0": "sha256:dc1efa0774bcb83fd937b3cdf5bc1b879919092f08bb2c1c31badfa4f67bac0b"}, "docker": "quay.io/biocontainers/repeatafterme", "aliases": {"RAMExtend": "/usr/local/bin/RAMExtend", "calcPaths.pl": "/usr/local/bin/calcPaths.pl", "davidExtendConsRAM.pl": "/usr/local/bin/davidExtendConsRAM.pl", "extend-stk.pl": "/usr/local/bin/extend-stk.pl", "twoBitToFa": "/usr/local/bin/twoBitToFa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/repeatafterme.
singularity registry hpc automated addition for repeatafterme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/repeatafterme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/repeatafterme:0.0.7--h7b50bb2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/repeatafterme/0.0.7--h7b50bb2_0
$ module help quay.io/biocontainers/repeatafterme/0.0.7--h7b50bb2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### repeatafterme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### repeatafterme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### repeatafterme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### repeatafterme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### repeatafterme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### repeatafterme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RAMExtend

```bash
$ singularity exec <container> /usr/local/bin/RAMExtend
$ podman run --it --rm --entrypoint /usr/local/bin/RAMExtend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RAMExtend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calcPaths.pl

```bash
$ singularity exec <container> /usr/local/bin/calcPaths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/calcPaths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calcPaths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### davidExtendConsRAM.pl

```bash
$ singularity exec <container> /usr/local/bin/davidExtendConsRAM.pl
$ podman run --it --rm --entrypoint /usr/local/bin/davidExtendConsRAM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/davidExtendConsRAM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extend-stk.pl

```bash
$ singularity exec <container> /usr/local/bin/extend-stk.pl
$ podman run --it --rm --entrypoint /usr/local/bin/extend-stk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extend-stk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twoBitToFa

```bash
$ singularity exec <container> /usr/local/bin/twoBitToFa
$ podman run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twoBitToFa   -v ${PWD} -w ${PWD} <container> -c " $@"
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