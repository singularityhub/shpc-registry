---
layout: container
name:  "quay.io/biocontainers/bioconductor-mzr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mzr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mzr/container.yaml"
updated_at: "2023-06-07 03:36:07.929152"
latest: "2.32.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mzr"
aliases:
 - "nc-config"
 - "nccopy"
 - "ncdump"
 - "ncgen"
 - "ncgen3"
 - "uconv"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
versions:
 - "2.6.3--r3.3.1_1"
 - "2.32.0--r42hc247a5b_0"
 - "2.28.0--r41hc247a5b_2"
 - "2.26.0--r41h399db7b_0"
 - "2.24.1--r40h399db7b_0"
 - "2.22.0--r40h5f743cb_0"
 - "2.32.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mzr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mzr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mzr", "latest": {"2.32.0--r42hf17093f_1": "sha256:a59a1503caea86d62096cb5b7f7ee4cbd5f983d11abf30f523eb1617d235f166"}, "tags": {"2.6.3--r3.3.1_1": "sha256:aa0a2c2fe328f5ceb5806b5dc851d3fd0772f0b9549a3d89a8d450aff3a47146", "2.32.0--r42hc247a5b_0": "sha256:8e19367dde1ba85d6230bb63ccb3cd9a04d97f715aee1b6d96b8ca04b2748664", "2.28.0--r41hc247a5b_2": "sha256:f563652fe99a6a701f3097331f8e7eafc6f116e30e191cf955f439d767de3bd8", "2.26.0--r41h399db7b_0": "sha256:4dddcff1eb201385cde049b61ae23dbd7acfc0a1c2cabe0f46d8bcd9c0e35a16", "2.24.1--r40h399db7b_0": "sha256:f6b0c5808b0bdd92f14cb1060658935996d857fe1b464516444ce37deed56573", "2.22.0--r40h5f743cb_0": "sha256:9443d9bc32def3b12df69433d9b6fe62849ba6126c26bdc6c0a04bec6e42c551", "2.32.0--r42hf17093f_1": "sha256:a59a1503caea86d62096cb5b7f7ee4cbd5f983d11abf30f523eb1617d235f166"}, "docker": "quay.io/biocontainers/bioconductor-mzr", "aliases": {"nc-config": "/usr/local/bin/nc-config", "nccopy": "/usr/local/bin/nccopy", "ncdump": "/usr/local/bin/ncdump", "ncgen": "/usr/local/bin/ncgen", "ncgen3": "/usr/local/bin/ncgen3", "uconv": "/usr/local/bin/uconv", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mzr.
shpc-registry automated BioContainers addition for bioconductor-mzr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mzr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mzr:2.32.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mzr/2.32.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-mzr/2.32.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mzr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mzr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mzr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mzr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mzr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mzr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nc-config

```bash
$ singularity exec <container> /usr/local/bin/nc-config
$ podman run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nccopy

```bash
$ singularity exec <container> /usr/local/bin/nccopy
$ podman run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdump

```bash
$ singularity exec <container> /usr/local/bin/ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen

```bash
$ singularity exec <container> /usr/local/bin/ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen3

```bash
$ singularity exec <container> /usr/local/bin/ncgen3
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
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