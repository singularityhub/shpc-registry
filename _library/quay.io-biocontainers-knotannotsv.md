---
layout: container
name:  "quay.io/biocontainers/knotannotsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/knotannotsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/knotannotsv/container.yaml"
updated_at: "2026-04-05 05:09:30.572338"
latest: "1.1.5--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/knotannotsv"
aliases:
 - "crc32"
 - "extract_vba"
 - "knotAnnotSV.pl"
 - "knotAnnotSV2XL.pl"
 - "vbaProject.bin"
versions:
 - "1.1.5--hdfd78af_0"
description: "singularity registry hpc automated addition for knotannotsv"
config: {"url": "https://biocontainers.pro/tools/knotannotsv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for knotannotsv", "latest": {"1.1.5--hdfd78af_0": "sha256:eeee0b1a2143f7692968ed08182030d4787ca3c7125accd44d2901f1e54ab85d"}, "tags": {"1.1.5--hdfd78af_0": "sha256:eeee0b1a2143f7692968ed08182030d4787ca3c7125accd44d2901f1e54ab85d"}, "docker": "quay.io/biocontainers/knotannotsv", "aliases": {"crc32": "/usr/local/bin/crc32", "extract_vba": "/usr/local/bin/extract_vba", "knotAnnotSV.pl": "/usr/local/bin/knotAnnotSV.pl", "knotAnnotSV2XL.pl": "/usr/local/bin/knotAnnotSV2XL.pl", "vbaProject.bin": "/usr/local/bin/vbaProject.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/knotannotsv.
singularity registry hpc automated addition for knotannotsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/knotannotsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/knotannotsv:1.1.5--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/knotannotsv/1.1.5--hdfd78af_0
$ module help quay.io/biocontainers/knotannotsv/1.1.5--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### knotannotsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### knotannotsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### knotannotsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### knotannotsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### knotannotsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### knotannotsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crc32

```bash
$ singularity exec <container> /usr/local/bin/crc32
$ podman run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_vba

```bash
$ singularity exec <container> /usr/local/bin/extract_vba
$ podman run --it --rm --entrypoint /usr/local/bin/extract_vba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_vba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knotAnnotSV.pl

```bash
$ singularity exec <container> /usr/local/bin/knotAnnotSV.pl
$ podman run --it --rm --entrypoint /usr/local/bin/knotAnnotSV.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knotAnnotSV.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### knotAnnotSV2XL.pl

```bash
$ singularity exec <container> /usr/local/bin/knotAnnotSV2XL.pl
$ podman run --it --rm --entrypoint /usr/local/bin/knotAnnotSV2XL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/knotAnnotSV2XL.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vbaProject.bin

```bash
$ singularity exec <container> /usr/local/bin/vbaProject.bin
$ podman run --it --rm --entrypoint /usr/local/bin/vbaProject.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vbaProject.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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