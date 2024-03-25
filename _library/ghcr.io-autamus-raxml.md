---
layout: container
name:  "ghcr.io/autamus/raxml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/raxml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/raxml/container.yaml"
updated_at: "2024-03-25 02:58:40.873627"
latest: "8.2.12"
container_url: "https://github.com/orgs/autamus/packages/container/package/raxml"
aliases:
 - "raxmlHPC"
 - "raxmlHPC-AVX"
 - "raxmlHPC-MPI"
 - "raxmlHPC-MPI-AVX"
 - "raxmlHPC-MPI-SSE3"
 - "raxmlHPC-SSE3"
versions:
 - "8.2.12"
 - "latest"
description: "RAxML (Randomized Axelerated Maximum Likelihood) is a popular program for phylogenetic analysis of large datasets under maximum likelihood."
config: {"docker": "ghcr.io/autamus/raxml", "url": "https://github.com/orgs/autamus/packages/container/package/raxml", "maintainer": "@vsoch", "description": "RAxML (Randomized Axelerated Maximum Likelihood) is a popular program for phylogenetic analysis of large datasets under maximum likelihood.", "latest": {"8.2.12": "sha256:19463009b56fbd99c49c5e98aa44481aa6773d1945c1c7c8504bd1ff583ed0ef"}, "tags": {"8.2.12": "sha256:19463009b56fbd99c49c5e98aa44481aa6773d1945c1c7c8504bd1ff583ed0ef", "latest": "sha256:19463009b56fbd99c49c5e98aa44481aa6773d1945c1c7c8504bd1ff583ed0ef"}, "aliases": {"raxmlHPC": "/opt/view/bin/raxmlHPC", "raxmlHPC-AVX": "/opt/view/bin/raxmlHPC-AVX", "raxmlHPC-MPI": "/opt/view/bin/raxmlHPC-MPI", "raxmlHPC-MPI-AVX": "/opt/view/bin/raxmlHPC-MPI-AVX", "raxmlHPC-MPI-SSE3": "/opt/view/bin/raxmlHPC-MPI-SSE3", "raxmlHPC-SSE3": "/opt/view/bin/raxmlHPC-SSE3"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/raxml.
RAxML (Randomized Axelerated Maximum Likelihood) is a popular program for phylogenetic analysis of large datasets under maximum likelihood.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/raxml
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/raxml:8.2.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/raxml/8.2.12
$ module help ghcr.io/autamus/raxml/8.2.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raxml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raxml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raxml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raxml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raxml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raxml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### raxmlHPC

```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC
$ podman run --it --rm --entrypoint /opt/view/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-AVX

```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-AVX
$ podman run --it --rm --entrypoint /opt/view/bin/raxmlHPC-AVX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raxmlHPC-AVX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-MPI

```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-MPI
$ podman run --it --rm --entrypoint /opt/view/bin/raxmlHPC-MPI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raxmlHPC-MPI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-MPI-AVX

```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-MPI-AVX
$ podman run --it --rm --entrypoint /opt/view/bin/raxmlHPC-MPI-AVX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raxmlHPC-MPI-AVX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-MPI-SSE3

```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-MPI-SSE3
$ podman run --it --rm --entrypoint /opt/view/bin/raxmlHPC-MPI-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raxmlHPC-MPI-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-SSE3

```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-SSE3
$ podman run --it --rm --entrypoint /opt/view/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
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