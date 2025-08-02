---
layout: container
name:  "quay.io/biocontainers/bioconductor-amountain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-amountain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-amountain/container.yaml"
updated_at: "2025-08-02 04:02:51.787874"
latest: "1.32.0--r44h34769fb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-amountain"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351ha21c8aa_0"
 - "1.20.0--r41hda872b5_3"
 - "1.18.0--r41ha4a0bc2_0"
 - "1.16.0--r40ha4a0bc2_1"
 - "1.14.0--r40hb42d971_0"
 - "1.12.0--r36h88e4a8a_0"
 - "1.24.0--r42hda872b5_0"
 - "1.24.0--r42hee7dd41_2"
 - "1.26.0--r43hee7dd41_0"
 - "1.28.0--r43hee7dd41_1"
 - "1.28.0--r43hee7dd41_2"
 - "1.32.0--r44h34769fb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-amountain"
config: {"url": "https://biocontainers.pro/tools/bioconductor-amountain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-amountain", "latest": {"1.32.0--r44h34769fb_0": "sha256:98b588537e452ae276a0235bf735e33fd9ef67c7cdf221b758c25a518df0cfb1"}, "tags": {"1.8.0--r351ha21c8aa_0": "sha256:7e99f4f237104540a1d35da14a330ac8bc42c18f76426a6e20ba5e2f335ad4db", "1.20.0--r41hda872b5_3": "sha256:ae5203490e6c6f09fa33ce1bcb2072a6ede3d522f44f121962f0ca2681777056", "1.18.0--r41ha4a0bc2_0": "sha256:85b91e4984da1cb3f37e39ba36e5272c7991b57ef7ebe70eda21aa1594d4fad8", "1.16.0--r40ha4a0bc2_1": "sha256:eef6d9f46c78634bf6984e836401f546d4c045f62282e5357f51ba89a8d903ef", "1.14.0--r40hb42d971_0": "sha256:a201e1042a7228270adf8e5ca281d7f6cbf5b8cd3adcd19bb3a24b3d0deef0f4", "1.12.0--r36h88e4a8a_0": "sha256:d4a1d0227550d7c87385e87a4c29648bf318c52f161494910b8dd4814699e1a8", "1.24.0--r42hda872b5_0": "sha256:caae8e633f7373171b12003c1142e9b5689239017c1613a401254762780ab5a7", "1.24.0--r42hee7dd41_2": "sha256:84334459c575d966fd1b38836ccd0b155d974a289a2cd63bd1b9cba0808d445b", "1.26.0--r43hee7dd41_0": "sha256:a16f9fa530219204a8256b580bd86d705f94e80703097303a2c3e3464d801de3", "1.28.0--r43hee7dd41_1": "sha256:dadebc64a6bc9b6dbbb5ce2a03480719fb7ca4e66b276a4a94fd9e42408c9581", "1.28.0--r43hee7dd41_2": "sha256:2bb5adbdc0e91a4ba268a6516e940717252108d9184c0d2a0b5bf27e68a42519", "1.32.0--r44h34769fb_0": "sha256:98b588537e452ae276a0235bf735e33fd9ef67c7cdf221b758c25a518df0cfb1"}, "docker": "quay.io/biocontainers/bioconductor-amountain", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-amountain.
shpc-registry automated BioContainers addition for bioconductor-amountain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-amountain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-amountain:1.32.0--r44h34769fb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-amountain/1.32.0--r44h34769fb_0
$ module help quay.io/biocontainers/bioconductor-amountain/1.32.0--r44h34769fb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-amountain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amountain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-amountain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-amountain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-amountain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-amountain-inspect-deffile:

```bash
$ singularity inspect -d <container>
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