---
layout: container
name:  "quay.io/biocontainers/teloscope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/teloscope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/teloscope/container.yaml"
updated_at: "2025-08-28 03:47:39.152513"
latest: "0.1.2--h35c04b2_0"
container_url: "https://biocontainers.pro/tools/teloscope"
aliases:
 - "teloscope"
versions:
 - "0.0.2--hdcf5f25_0"
 - "0.0.4--hdcf5f25_0"
 - "0.0.5--h077b44d_0"
 - "0.0.7--h35c04b2_0"
 - "0.0.8--h35c04b2_0"
 - "0.1.0--h35c04b2_0"
 - "0.0.9--h35c04b2_0"
 - "0.1.1--h35c04b2_0"
 - "0.1.2--h35c04b2_0"
description: "singularity registry hpc automated addition for teloscope"
config: {"url": "https://biocontainers.pro/tools/teloscope", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for teloscope", "latest": {"0.1.2--h35c04b2_0": "sha256:f83c5c39e00d869288faf54b70dda19cb59f5e7b3c405a3207089d19d3e0e738"}, "tags": {"0.0.2--hdcf5f25_0": "sha256:85e24762b701b9f61f1640106667cfc49efeec4f1802aca6ed065e476a3957b8", "0.0.4--hdcf5f25_0": "sha256:7cd57bf7997d591a2d07d51642765cbf934e2ecf021dffcc911e4eb7bbe6778e", "0.0.5--h077b44d_0": "sha256:15df901f23adea483e373a17a157a415a75fc185c7824ffd42fac9596bd03a18", "0.0.7--h35c04b2_0": "sha256:d5a96c5b9baafec3005ea5181c58532d0f8fd205c30a52d7d575e8563df3a63b", "0.0.8--h35c04b2_0": "sha256:929d40ecf2f9a916b093a3fd5614b474adc1033e1e92687827d648a6626661da", "0.1.0--h35c04b2_0": "sha256:e2a7048e544f8da42869b6b06eab4d9e327effb9eb84a1c7ee401e4d8e987591", "0.0.9--h35c04b2_0": "sha256:e9c61c760fe83206cd695b2e97633133d2505d29b83f375fcd0b53a5d992671d", "0.1.1--h35c04b2_0": "sha256:97edfa398e690cf6dc52f047e6e8767367df024e4a56da94da186c53fe923506", "0.1.2--h35c04b2_0": "sha256:f83c5c39e00d869288faf54b70dda19cb59f5e7b3c405a3207089d19d3e0e738"}, "docker": "quay.io/biocontainers/teloscope", "aliases": {"teloscope": "/usr/local/bin/teloscope"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/teloscope.
singularity registry hpc automated addition for teloscope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/teloscope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/teloscope:0.1.2--h35c04b2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/teloscope/0.1.2--h35c04b2_0
$ module help quay.io/biocontainers/teloscope/0.1.2--h35c04b2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### teloscope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### teloscope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### teloscope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### teloscope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### teloscope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### teloscope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### teloscope

```bash
$ singularity exec <container> /usr/local/bin/teloscope
$ podman run --it --rm --entrypoint /usr/local/bin/teloscope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/teloscope   -v ${PWD} -w ${PWD} <container> -c " $@"
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