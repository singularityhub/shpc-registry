---
layout: container
name:  "quay.io/biocontainers/bioconductor-gostag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gostag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gostag/container.yaml"
updated_at: "2024-05-07 03:09:13.751883"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gostag"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.2--r40hdfd78af_0"
 - "1.13.1--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gostag"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gostag", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gostag", "latest": {"1.26.0--r43hdfd78af_0": "sha256:c55ba88b0eb3d8ccba13b838cde4f2d5a81e6f6e6071391916e824bdf7f3cdcc"}, "tags": {"1.8.0--r36_1": "sha256:780cbb8658a82aec4dee5b0ae8e24f637edb8bd64a577f47dea7ce9e23a606be", "1.22.0--r42hdfd78af_0": "sha256:1a609bd13f973dad82908068722f53b3cf91d70018596a39933a842c73166ce8", "1.18.0--r41hdfd78af_0": "sha256:ffd8b3f4efce76eda799fad6ba142d447e78a69c22fc1f2af5f63bf54bddd899", "1.16.0--r41hdfd78af_0": "sha256:96c0004540de9d8ac0d5fbba487b965a5e3b252ea07f3841adb9ce30db3e27d5", "1.14.2--r40hdfd78af_0": "sha256:33748f2a69506ca01532887307498f9b77d40150a4e95e3bc55c7066defe684c", "1.13.1--r40_0": "sha256:77db10afc518e67414952a307752956f8891d3c8e286c79ec3e4d8162e84a42a", "1.24.0--r43hdfd78af_0": "sha256:c1ee417e78c1b7e5bc06cf9fd8ce0a84e484464d6824f9e735cefaafd3871d1c", "1.26.0--r43hdfd78af_0": "sha256:c55ba88b0eb3d8ccba13b838cde4f2d5a81e6f6e6071391916e824bdf7f3cdcc"}, "docker": "quay.io/biocontainers/bioconductor-gostag", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gostag.
shpc-registry automated BioContainers addition for bioconductor-gostag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gostag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gostag:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gostag/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gostag/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gostag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gostag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gostag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gostag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gostag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gostag-inspect-deffile:

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