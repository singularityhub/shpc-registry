---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcas/container.yaml"
updated_at: "2025-03-10 03:20:07.181622"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcas"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.2--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcas", "latest": {"1.32.0--r44hdfd78af_0": "sha256:4a62f7565b139e30fa66024d74d7b2cbbaf1a9998ce3a0329a6421938aa447e1"}, "tags": {"1.8.0--r351_0": "sha256:8ad30511f9dea6cc42dbd759263fd3f89b4def1b9f2c811b4c92e8c2d6ea2c60", "1.20.0--r41hdfd78af_0": "sha256:b8f2f565da0b996b32f36fd721b72e1bc7fd44f3a847fa01aae052566c838afd", "1.18.0--r41hdfd78af_0": "sha256:5fbff06bea0eccec1fc91c5a3b763d5f20f514667e8fbfb0fe02595747cc476b", "1.16.0--r40hdfd78af_1": "sha256:1a8f153e38287d92bde2bf2354f85a2250687bd4232da97f3894a3da944f03bd", "1.14.0--r40_0": "sha256:96bbfb83cf70d1c2e96aefd21bcece8c38ca44ccbb469fd7ce8a64a3335ae4f0", "1.12.0--r36_0": "sha256:938570c8949ab46e6811a1d36b2b1601fd82433daa9df6f3c5f7039c4962545b", "1.24.0--r42hdfd78af_0": "sha256:a8e04ea18e07cbe6b4bc23cb680dc93a10368f87a82e0b000a0b10f5c00d89b6", "1.26.0--r43hdfd78af_0": "sha256:73f8e02a8630f1431a875a2e6b58b256f0d3f32068ba4102d1a97607b18a0d24", "1.28.2--r43hdfd78af_0": "sha256:c029adc7a6ba22d8f89e93bd40471a02a5702633c2253fc149d2f6775e2b0f85", "1.32.0--r44hdfd78af_0": "sha256:4a62f7565b139e30fa66024d74d7b2cbbaf1a9998ce3a0329a6421938aa447e1"}, "docker": "quay.io/biocontainers/bioconductor-rcas", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcas.
shpc-registry automated BioContainers addition for bioconductor-rcas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcas:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcas/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcas/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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