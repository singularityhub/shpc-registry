---
layout: container
name:  "quay.io/biocontainers/bioconductor-ontoproc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ontoproc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ontoproc/container.yaml"
updated_at: "2025-11-14 05:11:39.497041"
latest: "2.0.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ontoproc"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "2.0.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ontoproc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ontoproc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ontoproc", "latest": {"2.0.0--r44hdfd78af_0": "sha256:5e73fc633776a911b01e4bfcaa2737d65cc07486b5a2456d3a1b514cc1229291"}, "tags": {"1.8.0--r36_0": "sha256:9d46d4b6b853bc0d5230735ef2304fbe5bb6a2c8d7305f24e228ff37025c9c72", "1.20.0--r42hdfd78af_0": "sha256:7cab9df75b2c05d6301116fae53b2247708727378d424d9f4c66cb6aff7ce8bf", "1.16.0--r41hdfd78af_0": "sha256:e3b03232c438ca182eb775b0a7e6bc58cbb93736e281d4b8b3636c4e42807eb9", "1.14.0--r41hdfd78af_0": "sha256:001c0a5f52adfe5ef4ecd2d9395cbf01f0245598cee6f319eb3ea1b51e03bb29", "1.12.0--r40hdfd78af_1": "sha256:f9a7e1dda9e417f97ea379d91e7c4c82415b588d5c321a64185daf9f2330c8b3", "1.10.0--r40_0": "sha256:b0dfb0c09c4985cba680a16c862aa21e46c103fe022e8a8b559335f871da0541", "1.22.0--r43hdfd78af_0": "sha256:37a55aab166489267c89dd5a6032d4426947370bd391b145127a1f5d343a147a", "1.24.0--r43hdfd78af_0": "sha256:e742eccd26792d4f10b7ec554c601cd73b732f2da5fb1c918becc270d396231e", "2.0.0--r44hdfd78af_0": "sha256:5e73fc633776a911b01e4bfcaa2737d65cc07486b5a2456d3a1b514cc1229291"}, "docker": "quay.io/biocontainers/bioconductor-ontoproc", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ontoproc.
shpc-registry automated BioContainers addition for bioconductor-ontoproc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ontoproc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ontoproc:2.0.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ontoproc/2.0.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ontoproc/2.0.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ontoproc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ontoproc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ontoproc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ontoproc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ontoproc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ontoproc-inspect-deffile:

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