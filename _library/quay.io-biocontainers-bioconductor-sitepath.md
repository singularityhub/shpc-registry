---
layout: container
name:  "quay.io/biocontainers/bioconductor-sitepath"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sitepath/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sitepath/container.yaml"
updated_at: "2025-09-26 03:32:56.946844"
latest: "1.22.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sitepath"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.2--r41hc247a5b_1"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
 - "1.22.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sitepath"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sitepath", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sitepath", "latest": {"1.22.0--r44he5774e6_0": "sha256:80e9d1381eac87aa588fa22ab2ed18cd4d5b59c40e65b0ecdc866517593c3363"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:0d0cd4e4fd0ff11b5a99ab23a9659ab7326a252031675254ab1ce3deaa127eb6", "1.14.0--r42hc247a5b_0": "sha256:b3e570d3e634c1382fd8d3ca9642ab7994f4b041ae3c38cfac9fa0498fe082e4", "1.10.2--r41hc247a5b_1": "sha256:418818a12424c875a9d3d7f81eb3a654d5a09c0d906e8f273028dd7c04892f63", "1.14.0--r42hf17093f_1": "sha256:0f2f4362610d28652781d36a459cd2cf208ee907942ce5d022b138be056931ad", "1.16.0--r43hf17093f_0": "sha256:69e711e8a27217d7de40197ecc1bc14394b4dbe060d72a457ea0dfd2b2bb1231", "1.18.0--r43hf17093f_0": "sha256:03935928935f1ca462c2f61c8223e79490c7b96cc497ee5c355f4e49e8f41251", "1.22.0--r44he5774e6_0": "sha256:80e9d1381eac87aa588fa22ab2ed18cd4d5b59c40e65b0ecdc866517593c3363"}, "docker": "quay.io/biocontainers/bioconductor-sitepath", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sitepath.
shpc-registry automated BioContainers addition for bioconductor-sitepath
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sitepath
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sitepath:1.22.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sitepath/1.22.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-sitepath/1.22.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sitepath-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sitepath-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sitepath-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sitepath-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sitepath-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sitepath-inspect-deffile:

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