---
layout: container
name:  "quay.io/biocontainers/bioconductor-simat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simat/container.yaml"
updated_at: "2025-09-05 03:05:12.770503"
latest: "1.38.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simat"
aliases:
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
 - "hdf2gif"
versions:
 - "1.26.0--r41hc247a5b_2"
 - "1.30.0--r42hc247a5b_0"
 - "1.30.0--r42hf17093f_1"
 - "1.32.0--r43hf17093f_0"
 - "1.34.0--r43hf17093f_0"
 - "1.38.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simat", "latest": {"1.38.0--r44he5774e6_0": "sha256:002e9a9aeb9915834ed0abf5a38a93b34d80e284ca27f89978db06f6514ee5a7"}, "tags": {"1.26.0--r41hc247a5b_2": "sha256:eb99a9cb119d1b9764d753e33536187980f366f741e152a2cecdc36ec9bfe4eb", "1.30.0--r42hc247a5b_0": "sha256:aa28514c00cb575eade452e362ca3aba531cf14385022601b5eab38048ec4392", "1.30.0--r42hf17093f_1": "sha256:3327e1732276d6451570d0b20c4683afcd14db30be8d12eadc541749f7997f7d", "1.32.0--r43hf17093f_0": "sha256:64ac16553221330c15e735d82fe842beb314aec60bf860ae9aa3ac6b5d7369fe", "1.34.0--r43hf17093f_0": "sha256:eb0ff3d6cd3a0e81e280e1cc86f3499ba28391a7a4d1289310db3abab876dc73", "1.38.0--r44he5774e6_0": "sha256:002e9a9aeb9915834ed0abf5a38a93b34d80e284ca27f89978db06f6514ee5a7"}, "docker": "quay.io/biocontainers/bioconductor-simat", "aliases": {"zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simat.
shpc-registry automated BioContainers addition for bioconductor-simat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simat:1.38.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simat/1.38.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-simat/1.38.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### zipcmp

```bash
$ singularity exec <container> /usr/local/bin/zipcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipmerge

```bash
$ singularity exec <container> /usr/local/bin/zipmerge
$ podman run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziptool

```bash
$ singularity exec <container> /usr/local/bin/ziptool
$ podman run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncdump

```bash
$ singularity exec <container> /usr/local/bin/h4_ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncgen

```bash
$ singularity exec <container> /usr/local/bin/h4_ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4cc

```bash
$ singularity exec <container> /usr/local/bin/h4cc
$ podman run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4redeploy

```bash
$ singularity exec <container> /usr/local/bin/h4redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf24to8

```bash
$ singularity exec <container> /usr/local/bin/hdf24to8
$ podman run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2gif

```bash
$ singularity exec <container> /usr/local/bin/hdf2gif
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
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