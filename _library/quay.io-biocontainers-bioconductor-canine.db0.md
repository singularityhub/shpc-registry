---
layout: container
name:  "quay.io/biocontainers/bioconductor-canine.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-canine.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-canine.db0/container.yaml"
updated_at: "2025-02-21 02:53:14.980295"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-canine.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-canine.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-canine.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-canine.db0", "latest": {"3.20.0--r44hdfd78af_0": "sha256:2f4ea9619a21e0b28e48fb86f1effbfaa8e29300552e246426ff5329a43da7aa"}, "tags": {"3.8.2--r36_1": "sha256:8451eca5e679b12daae623eea6ed109cb13890652528de71597b3c0dae657b16", "3.16.0--r42hdfd78af_0": "sha256:9adb613b1a20190edc3cfe3730e0e30a93736dc7fede63a7876a36334204a277", "3.14.0--r41hdfd78af_1": "sha256:889fe1dcf9c7655a59914ebcb8a8293982e0c2eba0a522e6787766051ae97556", "3.13.0--r41hdfd78af_0": "sha256:aafc5bf00a56694483d1cc89ede71e5b4eb421bf19b90bcce0f851457a985b0b", "3.12.0--r40hdfd78af_1": "sha256:28ed1e25c8964c6c7a51e7db2787b5e032e673c44e77fdfe648716f89f08d625", "3.11.2--r40_0": "sha256:e9a62ff1c410c5c8858352d590c165fac9da90557cfb26f7d3764c22a7319872", "3.17.0--r43hdfd78af_0": "sha256:b73ead9074b094e0c47301cb0e9d254a0fa7edf7e0ee510200eb2afb5e58a291", "3.18.0--r43hdfd78af_0": "sha256:c071fa745227a4ecd3eaabb01aa4b51669176fe3363bf9d49b513f7231698f2e", "3.20.0--r44hdfd78af_0": "sha256:2f4ea9619a21e0b28e48fb86f1effbfaa8e29300552e246426ff5329a43da7aa"}, "docker": "quay.io/biocontainers/bioconductor-canine.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-canine.db0.
shpc-registry automated BioContainers addition for bioconductor-canine.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-canine.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-canine.db0:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-canine.db0/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-canine.db0/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-canine.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canine.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-canine.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-canine.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-canine.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-canine.db0-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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