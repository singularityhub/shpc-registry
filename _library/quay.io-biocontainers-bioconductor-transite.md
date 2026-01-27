---
layout: container
name:  "quay.io/biocontainers/bioconductor-transite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-transite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-transite/container.yaml"
updated_at: "2026-01-27 04:21:10.989301"
latest: "1.24.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-transite"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40h399db7b_2"
 - "1.16.0--r42hc247a5b_0"
 - "1.12.1--r41hc247a5b_1"
 - "1.10.0--r41h399db7b_0"
 - "1.16.0--r42hf17093f_1"
 - "1.18.0--r43hf17093f_0"
 - "1.20.0--r43hf17093f_0"
 - "1.24.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-transite"
config: {"url": "https://biocontainers.pro/tools/bioconductor-transite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-transite", "latest": {"1.24.0--r44he5774e6_0": "sha256:fce224259cac245d602d08e4e7f9d5162a872e107ae844726ce74fe6248f76b0"}, "tags": {"1.8.0--r40h399db7b_2": "sha256:fc0a18d0b5dadf003485c93a1e49da747e2b71d8e5b2d050e7bd5f25e2b96939", "1.16.0--r42hc247a5b_0": "sha256:a3d0f0f7d87e898862d0fc977b6935246bc5160630aff4976feb20cb0578ad40", "1.12.1--r41hc247a5b_1": "sha256:aefb9e47789a2b5f76de0257bdf9777c6998592d9ff9fb9f3eabe7ca328343ec", "1.10.0--r41h399db7b_0": "sha256:fec9f864e0056eb06f2a1e917e3a56df1c59830504db514405a829373f4243b9", "1.16.0--r42hf17093f_1": "sha256:ac9dceb3452dc1abae26afd30f2c2bbe5e2625ff3e3fa9cdd5e5cf555519de1a", "1.18.0--r43hf17093f_0": "sha256:eb646d394db643c43b77033b87ef628d706294eb88878d038dac8fa36caab939", "1.20.0--r43hf17093f_0": "sha256:7236ff9da3185d1b71318e90ccc55e3e37a456da8133216c1f7a41ee917927c8", "1.24.0--r44he5774e6_0": "sha256:fce224259cac245d602d08e4e7f9d5162a872e107ae844726ce74fe6248f76b0"}, "docker": "quay.io/biocontainers/bioconductor-transite", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-transite.
shpc-registry automated BioContainers addition for bioconductor-transite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-transite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-transite:1.24.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-transite/1.24.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-transite/1.24.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-transite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-transite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-transite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-transite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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