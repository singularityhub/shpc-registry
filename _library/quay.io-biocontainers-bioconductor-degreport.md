---
layout: container
name:  "quay.io/biocontainers/bioconductor-degreport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-degreport/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-degreport/container.yaml"
updated_at: "2023-02-03 03:02:56.733992"
latest: "1.34.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-degreport"
aliases:
 - "uconv"
 - "tclsh8.5"
 - "wish8.5"
 - "ncursesw5-config"
versions:
 - "1.8.2--r3.3.2_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.30.0--r41hdfd78af_0"
 - "1.28.0--r41hdfd78af_0"
 - "1.26.0--r40hdfd78af_1"
 - "1.24.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-degreport"
config: {"url": "https://biocontainers.pro/tools/bioconductor-degreport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-degreport", "latest": {"1.34.0--r42hdfd78af_0": "sha256:f3d975058eeaf494defa7c5cd88e255f19024e10e88824167ce27cb8a8ecc2d6"}, "tags": {"1.8.2--r3.3.2_1": "sha256:efaa5471c1aa1125c846918990743ae5eb9cf58bd3529c1e089a7c334f973d9a", "1.34.0--r42hdfd78af_0": "sha256:f3d975058eeaf494defa7c5cd88e255f19024e10e88824167ce27cb8a8ecc2d6", "1.30.0--r41hdfd78af_0": "sha256:7f1fb2067d7e7f1d9f76b6e2a4aae53f7e1c8d72d389fefadad7f4b8ff78932b", "1.28.0--r41hdfd78af_0": "sha256:ccc2ff88820b4de4d8cbb58ee75995cb715c1116861e1a0afd242652053804de", "1.26.0--r40hdfd78af_1": "sha256:02dc6772f954f39af4d7aae0edf9a1fc57317013cfd735cf8fa34470e529eb28", "1.24.0--r40_0": "sha256:42d36c682e795fac0f3e49809352ed7ffa3b51fe36c2966315c051a7d69b9fbc"}, "docker": "quay.io/biocontainers/bioconductor-degreport", "aliases": {"uconv": "/usr/local/bin/uconv", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-degreport.
shpc-registry automated BioContainers addition for bioconductor-degreport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-degreport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-degreport:1.34.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-degreport/1.34.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-degreport/1.34.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-degreport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-degreport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-degreport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-degreport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-degreport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-degreport-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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