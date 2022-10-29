---
layout: container
name:  "quay.io/biocontainers/bioconductor-msnid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msnid/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msnid/container.yaml"
updated_at: "2022-10-29 05:58:42.672406"
latest: "1.28.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-msnid"
aliases:
 - "gif2h5"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5clear"
versions:
 - "1.28.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-msnid"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msnid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msnid", "latest": {"1.28.0--r41hc247a5b_2": "sha256:5b1848dc3a8dff619e23ad2cd31abe23e8a3ec2fccc4583f3d4f4ccef7cffa6b"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:5b1848dc3a8dff619e23ad2cd31abe23e8a3ec2fccc4583f3d4f4ccef7cffa6b"}, "docker": "quay.io/biocontainers/bioconductor-msnid", "aliases": {"gif2h5": "/usr/local/bin/gif2h5", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msnid.
shpc-registry automated BioContainers addition for bioconductor-msnid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msnid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msnid:1.28.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msnid/1.28.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-msnid/1.28.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msnid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msnid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msnid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msnid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msnid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msnid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
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