---
layout: container
name:  "quay.io/biocontainers/bioconductor-proloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proloc/container.yaml"
updated_at: "2024-05-26 03:09:33.439179"
latest: "1.42.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proloc"
aliases:
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "gif2hdf"
 - "glpsol"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
versions:
 - "1.34.0--r41hc247a5b_2"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hf17093f_1"
 - "1.40.1--r43hf17093f_0"
 - "1.42.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proloc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proloc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proloc", "latest": {"1.42.0--r43hf17093f_0": "sha256:507622f6aa5b063188883437e9267ed7c8d512ace7b058ffd3dd41561df7fa44"}, "tags": {"1.34.0--r41hc247a5b_2": "sha256:6deff5adec3bed7b5bdaccaeefaafb4f7d96a9ea4bf6cf3c84678c67fd4df1fc", "1.38.0--r42hc247a5b_0": "sha256:954b32a5dd3f389174e3c2987f13e5ece4084751ad2520e85fa66d11a07408c4", "1.38.0--r42hf17093f_1": "sha256:2fd281c53b7bd9f140ed313aa198ba6604842668416ba683298aa57a6f77668a", "1.40.1--r43hf17093f_0": "sha256:13272a84733c8f3cd81ad8d5b231a1ac79763e87652014463ea55f6054f6e95d", "1.42.0--r43hf17093f_0": "sha256:507622f6aa5b063188883437e9267ed7c8d512ace7b058ffd3dd41561df7fa44"}, "docker": "quay.io/biocontainers/bioconductor-proloc", "aliases": {"zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "glpsol": "/usr/local/bin/glpsol", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proloc.
shpc-registry automated BioContainers addition for bioconductor-proloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proloc:1.42.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proloc/1.42.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-proloc/1.42.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proloc-inspect-deffile:

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


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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