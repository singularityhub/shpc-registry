---
layout: container
name:  "quay.io/biocontainers/snp-pileup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snp-pileup/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snp-pileup/container.yaml"
updated_at: "2025-01-09 13:53:25.575695"
latest: "0.6.2--h503566f_8"
container_url: "https://biocontainers.pro/tools/snp-pileup"
aliases:
 - "snp-pileup"
versions:
 - "v0.5.14--h3cba802_0"
 - "0.6.2--ha04fe3b_3"
 - "0.5.14--hfbaaabd_3"
 - "0.6.2--h6b7c446_4"
 - "0.6.2--h0033a41_5"
 - "0.6.2--hdbdd923_6"
 - "0.6.2--hdbdd923_7"
 - "0.6.2--h503566f_8"
description: "shpc-registry automated BioContainers addition for snp-pileup"
config: {"url": "https://biocontainers.pro/tools/snp-pileup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snp-pileup", "latest": {"0.6.2--h503566f_8": "sha256:f438f581586da4e00065bc4c6d3da381f75aefb4443982e0f01a40111e0dae8a"}, "tags": {"v0.5.14--h3cba802_0": "sha256:dfb5d2ee6f26707336fc83c081a6a531d99f0dd3a587870710a2cac9aa8c99a3", "0.6.2--ha04fe3b_3": "sha256:f2c8cb1964035b0f985078f03a8cd2fbde6db8cba6c889965e3f64997e6b1c8b", "0.5.14--hfbaaabd_3": "sha256:227f90eefab84fa1eac5f5683081bff83ff6366d022348ce6e13ad0322d49f39", "0.6.2--h6b7c446_4": "sha256:682c605e127db6b056479e278b0240f90ce8380a5b40f8f808739464c2ba6c84", "0.6.2--h0033a41_5": "sha256:c4331f422a06659c9835625ff1d4c9f14f4e251462469556c5ac5d368cab10e1", "0.6.2--hdbdd923_6": "sha256:70f1eb3ec4943d918b14f017b9209f1435a34fa0d4144917f4c086f9cb579a88", "0.6.2--hdbdd923_7": "sha256:0a56e1caac6bd9a6ae905906b0339fea014700a65189be0016114c0fb53cc955", "0.6.2--h503566f_8": "sha256:f438f581586da4e00065bc4c6d3da381f75aefb4443982e0f01a40111e0dae8a"}, "docker": "quay.io/biocontainers/snp-pileup", "aliases": {"snp-pileup": "/usr/local/bin/snp-pileup"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snp-pileup.
shpc-registry automated BioContainers addition for snp-pileup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snp-pileup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snp-pileup:0.6.2--h503566f_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snp-pileup/0.6.2--h503566f_8
$ module help quay.io/biocontainers/snp-pileup/0.6.2--h503566f_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snp-pileup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snp-pileup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snp-pileup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snp-pileup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snp-pileup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snp-pileup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snp-pileup

```bash
$ singularity exec <container> /usr/local/bin/snp-pileup
$ podman run --it --rm --entrypoint /usr/local/bin/snp-pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp-pileup   -v ${PWD} -w ${PWD} <container> -c " $@"
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