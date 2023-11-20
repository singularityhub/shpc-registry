---
layout: container
name:  "quay.io/biocontainers/bioconductor-ivygapse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ivygapse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ivygapse/container.yaml"
updated_at: "2023-11-20 03:01:17.782768"
latest: "1.22.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ivygapse"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.22.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ivygapse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ivygapse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ivygapse", "latest": {"1.22.1--r43hdfd78af_0": "sha256:cd46c88fa1b9c3942023f3cf33eb8e00cdb2fdc7576848ef1bdba1fffa131502"}, "tags": {"1.8.0--r36_0": "sha256:551aa3c66e4ff20b1c7bd0bba3631d1070fa22f4d45ebeb214a17e7e4b4090bf", "1.16.0--r41hdfd78af_0": "sha256:e7d5889f2ce4e3ea5ad48e06c86ee7f0db60b690130c976aaf242a04eebceb31", "1.14.0--r41hdfd78af_0": "sha256:08ee1dfe9b86f49925ec9a7a702526be19f62dc82c3b060382a7eb07c4807b99", "1.12.0--r40hdfd78af_1": "sha256:051161dc98cf11ef6b91064d4681692c92b386f4ca93a86630e01bb7b671fd42", "1.10.0--r40_0": "sha256:33b476bc0672c693a3e6a9bd9165668ae7875537883ad9eb100454fc94b5f1cb", "1.20.0--r42hdfd78af_0": "sha256:b0c08b0cb9e64619286d5795091c5d2b85eec23d1169db069605ee3ac553a89c", "1.22.1--r43hdfd78af_0": "sha256:cd46c88fa1b9c3942023f3cf33eb8e00cdb2fdc7576848ef1bdba1fffa131502"}, "docker": "quay.io/biocontainers/bioconductor-ivygapse", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ivygapse.
shpc-registry automated BioContainers addition for bioconductor-ivygapse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ivygapse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ivygapse:1.22.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ivygapse/1.22.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ivygapse/1.22.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ivygapse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ivygapse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ivygapse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ivygapse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ivygapse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ivygapse-inspect-deffile:

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