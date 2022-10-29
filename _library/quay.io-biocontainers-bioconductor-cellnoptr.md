---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellnoptr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellnoptr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellnoptr/container.yaml"
updated_at: "2022-10-29 05:32:02.491837"
latest: "1.40.0--r41hc0cfd56_2"
container_url: "https://biocontainers.pro/tools/bioconductor-cellnoptr"
aliases:
 - "acyclic"
 - "annotate"
 - "bcomps"
 - "bdftogd"
 - "ccomps"
 - "circo"
 - "cluster"
 - "cwebp"
 - "delaunay"
 - "diffimg"
versions:
 - "1.40.0--r41hc0cfd56_2"
description: "shpc-registry automated BioContainers addition for bioconductor-cellnoptr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellnoptr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellnoptr", "latest": {"1.40.0--r41hc0cfd56_2": "sha256:24ff04f2e18c047c97b94fa0660119674580a196e0073f9accccdce096eba930"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:24ff04f2e18c047c97b94fa0660119674580a196e0073f9accccdce096eba930"}, "docker": "quay.io/biocontainers/bioconductor-cellnoptr", "aliases": {"acyclic": "/usr/local/bin/acyclic", "annotate": "/usr/local/bin/annotate", "bcomps": "/usr/local/bin/bcomps", "bdftogd": "/usr/local/bin/bdftogd", "ccomps": "/usr/local/bin/ccomps", "circo": "/usr/local/bin/circo", "cluster": "/usr/local/bin/cluster", "cwebp": "/usr/local/bin/cwebp", "delaunay": "/usr/local/bin/delaunay", "diffimg": "/usr/local/bin/diffimg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellnoptr.
shpc-registry automated BioContainers addition for bioconductor-cellnoptr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellnoptr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellnoptr:1.40.0--r41hc0cfd56_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellnoptr/1.40.0--r41hc0cfd56_2
$ module help quay.io/biocontainers/bioconductor-cellnoptr/1.40.0--r41hc0cfd56_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellnoptr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellnoptr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellnoptr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellnoptr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellnoptr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellnoptr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccomps

```bash
$ singularity exec <container> /usr/local/bin/ccomps
$ podman run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circo

```bash
$ singularity exec <container> /usr/local/bin/circo
$ podman run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diffimg

```bash
$ singularity exec <container> /usr/local/bin/diffimg
$ podman run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
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