---
layout: container
name:  "julia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/julia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/julia/container.yaml"
updated_at: "2025-09-06 03:49:06.934662"
latest: "1.11.6"
container_url: "https://hub.docker.com/_/julia"
aliases:
 - "julia"
versions:
 - "1.8.3"
 - "1.8.5"
 - "1.9.0"
 - "1.9.1"
 - "1.9.2"
 - "1.9.3"
 - "1.9.4"
 - "1.10.0"
 - "1.10.1"
 - "1.10.2"
 - "1.10.3"
 - "1.10.4"
 - "1.10.5"
 - "1.11.1"
 - "1.10.6"
 - "1.11.2"
 - "1.10.7"
 - "1.11.3"
 - "1.10.8"
 - "1.11.4"
 - "1.10.9"
 - "1.11.5"
 - "1.11.6"
 - "1.10.10"
description: "An interpreted, high-level, high-performance dynamic programming language for technical computing."
config: {"docker": "julia", "url": "https://hub.docker.com/_/julia", "maintainer": "@marcodelapierre", "description": "An interpreted, high-level, high-performance dynamic programming language for technical computing.", "latest": {"1.11.6": "sha256:584cb02c203791e0abdf7e8c060b6e33334c91c1fae493c85fde188eb1b39015"}, "tags": {"1.8.3": "sha256:172938f81c0a5f607a71c6babeb6f0d0aac7a9bb3d43b000734b80f764748448", "1.8.5": "sha256:c9c13e38ea7ef6a893b97834e75f00fec4fc07b24072088e1360171cb192ebb0", "1.9.0": "sha256:a4eba1f0c1c2076eef737f5f441c80de87997faab982e816fd256e50326c6c8d", "1.9.1": "sha256:9313aec843ab5395eb0898b004737497da2b7ed50d72b53fc94dfca014af7d51", "1.9.2": "sha256:f4ec5401b88c20c01565ad55b826821f987369ab461dedb72706d95798d4ddb0", "1.9.3": "sha256:2bb36ee0d8b44fb2a1e034fa4e636c66ccc713fa0a41ca23b5d9207b837cb41a", "1.9.4": "sha256:829ddd53a80d14cfc02bae02198254ddef1de292c7cd6af694312fa8ad341290", "1.10.0": "sha256:3c56c7763e097e17ef158dd7e72acaa3284d51dbf111adae0eccd5782e78bdbc", "1.10.1": "sha256:2d992bcdfd817a11bfa70918879674b62dcd0a497e079116605c33dc9979589e", "1.10.2": "sha256:63ae8a0184a85382e68b0af0a1d5491db66cb490059b1ab2a76b831e43bc7147", "1.10.3": "sha256:d2375e33738225f57caa34096ad0a15c699512027931324c62ed1949d797a2ff", "1.10.4": "sha256:48c57c62ee9c56d11e4e4aea03dbeca89af22817232c074debe9941e44d749d3", "1.10.5": "sha256:6ddde25fefaa2ec11a4bb9a8cc5ad113daf3a8e11792f17bac6aa5fdec83649d", "1.11.1": "sha256:b3aca3cb8b8d22c8d260cc0144d1c08f6479bf0247bff7675a9b36cf133aa91e", "1.10.6": "sha256:b225307b26934292657b222d2c3c87dcaa8ecd1e83d648b2554a4369efb13826", "1.11.2": "sha256:9a2879323aa5509465343c7debfcee1d7e94e5728c39f0cd40bd07db84cca3f7", "1.10.7": "sha256:b939e747dd91e2b63293854ed8d239dab9858aa33c8c0f6b3c0f23db11ffde4d", "1.11.3": "sha256:e40252e43c10ac586b4c015c01a38d7c9664edf5bc9b260071b4d657ff74fff2", "1.10.8": "sha256:e3a998f7446b2ba8f3baaafaa38c5d891e0da830ae3d55cb1e7e5336538aca4c", "1.11.4": "sha256:0dac143b88447355086289ec08e2234e664c05821664182845764dda3fb0a8ee", "1.10.9": "sha256:ac905ae0a2807bd1d5cc70496ec7c170127519a1ecdd1f62ded4927acdf493cf", "1.11.5": "sha256:4594fded2b95069e815000aad7fe5038287627d9be0bd977bc275483cdece643", "1.11.6": "sha256:584cb02c203791e0abdf7e8c060b6e33334c91c1fae493c85fde188eb1b39015", "1.10.10": "sha256:0e2ce556c5a80a3908a066ff756a2455a7a1f663fb55f858af5d6077a9197ef3"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"julia": "/usr/local/julia/bin/julia"}}
---

This module is a singularity container wrapper for julia.
An interpreted, high-level, high-performance dynamic programming language for technical computing.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install julia
```

Or a specific version:

```bash
$ shpc install julia:1.11.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load julia/1.11.6
$ module help julia/1.11.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### julia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### julia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### julia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### julia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### julia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### julia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### julia

```bash
$ singularity exec <container> /usr/local/julia/bin/julia
$ podman run --it --rm --entrypoint /usr/local/julia/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/julia/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
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