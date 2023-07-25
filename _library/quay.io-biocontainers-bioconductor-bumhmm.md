---
layout: container
name:  "quay.io/biocontainers/bioconductor-bumhmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bumhmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bumhmm/container.yaml"
updated_at: "2023-07-25 03:01:12.796739"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bumhmm"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bumhmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bumhmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bumhmm", "latest": {"1.24.0--r43hdfd78af_0": "sha256:aa5a389f4c8e379b0374c389128a97c6e6f6056565b4651144ccc9dd0ca61836"}, "tags": {"1.8.0--r36_1": "sha256:e3f936bd0da423399ad22e8d8dc4bb93a4319a9810498a7925b42ddc0e6f5571", "1.22.0--r42hdfd78af_0": "sha256:28543654adacd6ee727e1ff06650eea87adf74ce90273067ca59773561089387", "1.18.0--r41hdfd78af_0": "sha256:d806fbf9d37970ffa4a373804f1ca775cd470021179a384af87a11855b70c361", "1.16.0--r41hdfd78af_0": "sha256:60661191daba231a945d48babc50abd1bc54092771f1b48cbf54b1250c963601", "1.14.0--r40hdfd78af_1": "sha256:410738cea65b9dce7f64620251609ba0c9a69ba137f74377a250158bb5934069", "1.12.0--r40_0": "sha256:71c1114e93c28e82ea2ad436df588166ae21199e8c029b0fc4c40fdb1d693049", "1.24.0--r43hdfd78af_0": "sha256:aa5a389f4c8e379b0374c389128a97c6e6f6056565b4651144ccc9dd0ca61836"}, "docker": "quay.io/biocontainers/bioconductor-bumhmm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bumhmm.
shpc-registry automated BioContainers addition for bioconductor-bumhmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bumhmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bumhmm:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bumhmm/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bumhmm/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bumhmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bumhmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bumhmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bumhmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bumhmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bumhmm-inspect-deffile:

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