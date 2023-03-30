---
layout: container
name:  "quay.io/biocontainers/bioconductor-genextender"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genextender/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genextender/container.yaml"
updated_at: "2023-03-30 03:25:52.902325"
latest: "1.24.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genextender"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351h14c3975_0"
 - "1.24.0--r42hc0cfd56_0"
 - "1.20.0--r41hc0cfd56_2"
 - "1.18.0--r41hd029910_0"
 - "1.16.0--r40hd029910_1"
 - "1.14.0--r40h037d062_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genextender"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genextender", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genextender", "latest": {"1.24.0--r42hc0cfd56_0": "sha256:191d048f843eddd835c491d32bf94caba1c38e6752861b2bea0c7ba1b600ce8b"}, "tags": {"1.8.0--r351h14c3975_0": "sha256:16543730d16e93f0a2dbef6e8ef7cf4321e8dca5251dd8625a5379329ca56deb", "1.24.0--r42hc0cfd56_0": "sha256:191d048f843eddd835c491d32bf94caba1c38e6752861b2bea0c7ba1b600ce8b", "1.20.0--r41hc0cfd56_2": "sha256:2f16c8252a57bf624ae18a0475d3efc53c8bcf13f6fca9d96f35fe7c9c28b0fa", "1.18.0--r41hd029910_0": "sha256:34d1f0278a2a229dfe3f16b0414483326c25766f5a1ab2ee9b057ae0bcb9fd16", "1.16.0--r40hd029910_1": "sha256:1b3a1efc347ba4bf2f3a7c820b89646e056ca4aa6641d8d5e6eb93dde793eda3", "1.14.0--r40h037d062_0": "sha256:07d7994b4190a9f2abb9e10841e5ea06427ed0cae4833800fdf1b6311e3c0394"}, "docker": "quay.io/biocontainers/bioconductor-genextender", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genextender.
shpc-registry automated BioContainers addition for bioconductor-genextender
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genextender
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genextender:1.24.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genextender/1.24.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-genextender/1.24.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genextender-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genextender-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genextender-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genextender-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genextender-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genextender-inspect-deffile:

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