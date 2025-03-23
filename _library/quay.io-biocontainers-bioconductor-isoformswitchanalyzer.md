---
layout: container
name:  "quay.io/biocontainers/bioconductor-isoformswitchanalyzer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-isoformswitchanalyzer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-isoformswitchanalyzer/container.yaml"
updated_at: "2025-03-23 03:08:17.147113"
latest: "2.6.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-isoformswitchanalyzer"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_0"
 - "1.20.0--r42hc0cfd56_0"
 - "1.16.0--r41hc0cfd56_2"
 - "1.14.0--r41hd029910_0"
 - "1.12.0--r40hd029910_1"
 - "1.10.0--r40h037d062_0"
 - "1.20.0--r42ha9d7317_1"
 - "2.0.1--r43ha9d7317_0"
 - "2.2.0--r43ha9d7317_0"
 - "2.6.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-isoformswitchanalyzer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-isoformswitchanalyzer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-isoformswitchanalyzer", "latest": {"2.6.0--r44h3df3fcb_0": "sha256:e2032633971399fdd5c3f46d5821bc5b75b3a8818f3ebf92528f16ee71602897"}, "tags": {"1.8.0--r36h516909a_0": "sha256:a70e561958ec117925f65bada01be2dd447f3af0d338d903c137dd1351c2ce1c", "1.20.0--r42hc0cfd56_0": "sha256:99c7744b47c0f5d95e0357fc3488b98a6011ed42c1419c4b9524bc5a8d408cbb", "1.16.0--r41hc0cfd56_2": "sha256:0d693da976062039de3770e116b211414b931c7732dae3dfa08553b1cdf84c8c", "1.14.0--r41hd029910_0": "sha256:b0a3110c4a7a2b93522649c0d29315f87a90e4d645e46cc6ff6a32f5abd3e2d9", "1.12.0--r40hd029910_1": "sha256:8a309e965f4287b07de86d1574a82a8ac13b09515d4530903af48ca43df6feca", "1.10.0--r40h037d062_0": "sha256:63dc68ef56a17afbf903bfc108d20e76a3123a0381b505e05ff7e22c28a49ce8", "1.20.0--r42ha9d7317_1": "sha256:a34bb8d30b24ea04a74fe1ce47192a1ca7a4f9671f0c3915a09c12cffa097490", "2.0.1--r43ha9d7317_0": "sha256:4d28c0cefbee9b171d37dc35da148e7201e66d942fe704c1b1ea0246381a735a", "2.2.0--r43ha9d7317_0": "sha256:dac85cb976a49c0c2ece30c92b4b0f38538e98d98710fd7ea2f94d47f7149783", "2.6.0--r44h3df3fcb_0": "sha256:e2032633971399fdd5c3f46d5821bc5b75b3a8818f3ebf92528f16ee71602897"}, "docker": "quay.io/biocontainers/bioconductor-isoformswitchanalyzer", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-isoformswitchanalyzer.
shpc-registry automated BioContainers addition for bioconductor-isoformswitchanalyzer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-isoformswitchanalyzer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-isoformswitchanalyzer:2.6.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-isoformswitchanalyzer/2.6.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-isoformswitchanalyzer/2.6.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-isoformswitchanalyzer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isoformswitchanalyzer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isoformswitchanalyzer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-isoformswitchanalyzer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-isoformswitchanalyzer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-isoformswitchanalyzer-inspect-deffile:

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