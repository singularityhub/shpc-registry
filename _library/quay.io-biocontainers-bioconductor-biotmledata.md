---
layout: container
name:  "quay.io/biocontainers/bioconductor-biotmledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biotmledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biotmledata/container.yaml"
updated_at: "2025-06-19 03:39:57.234798"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biotmledata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.21.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.13.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biotmledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biotmledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biotmledata", "latest": {"1.30.0--r44hdfd78af_0": "sha256:bfb86610459c8627ccc2d40697e7f3812c1b4fbe412df49bea5861c6e5459517"}, "tags": {"1.8.0--r36_1": "sha256:637da0744847ae68f589270c11f59a29ae8f24c9b010e2afacc5f03d467846f1", "1.21.0--r42hdfd78af_0": "sha256:25e38d11cfc4c8047c912c0ad460c6541557d290b4c6aa4c052cc9267f07d1f6", "1.18.0--r41hdfd78af_1": "sha256:55f1403a712efdc614cc3bc589696442d29ef5e9ce4a19a5f80ad5c1969c9442", "1.16.0--r41hdfd78af_0": "sha256:f0204656f91be6efd456de5a7d8d815f5cc9831a9140909f83f60a0505faede9", "1.14.0--r40hdfd78af_1": "sha256:5d5a154ea2faf1f57fd1ffa01eb21b66b4b6c73cb364b9dbaa3640eaa6ecd8f4", "1.13.0--r40_0": "sha256:211410079f2bc9f052adcf68aa4a6e0689203ce8526c043e99d6e3d032706d54", "1.24.0--r43hdfd78af_0": "sha256:dafcaa80715e77e9f7c43b1553ff8bc31cc4c4c9d03e5ee772d6b560793c781a", "1.26.0--r43hdfd78af_0": "sha256:88498e6de8506c8e963b67a836cc0e32a0e9fc20382a8029bb9176b60c6c6f77", "1.30.0--r44hdfd78af_0": "sha256:bfb86610459c8627ccc2d40697e7f3812c1b4fbe412df49bea5861c6e5459517"}, "docker": "quay.io/biocontainers/bioconductor-biotmledata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biotmledata.
shpc-registry automated BioContainers addition for bioconductor-biotmledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biotmledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biotmledata:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biotmledata/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biotmledata/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biotmledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biotmledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biotmledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biotmledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biotmledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biotmledata-inspect-deffile:

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