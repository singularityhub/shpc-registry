---
layout: container
name:  "quay.io/biocontainers/bioconductor-dada2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dada2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dada2/container.yaml"
updated_at: "2023-02-18 03:07:17.479575"
latest: "1.26.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dada2"
aliases:
 - "wget"
versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h5f743cb_0"
 - "1.16.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dada2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dada2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dada2", "latest": {"1.26.0--r42hc247a5b_0": "sha256:455e98b4cf5a8681aa8b4e9f06183ac00fadecd17b0690ec97960fcb0cc1ab7f"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:91f7e534caac8cfb4a3607d835697ef28133b491b9cef4233b5c4cfcad382aa5", "1.26.0--r42hc247a5b_0": "sha256:455e98b4cf5a8681aa8b4e9f06183ac00fadecd17b0690ec97960fcb0cc1ab7f", "1.22.0--r41hc247a5b_2": "sha256:8dc3d468bd9d4a0d13156fbeb9cc8c5125e86755ffce479bdbc91cd5d6bb217d", "1.20.0--r41h399db7b_0": "sha256:80f5b71cc5e3917186831a6871c9a6ec7e2ca88567d79891edef8a306e6d315f", "1.18.0--r40h5f743cb_0": "sha256:d716e2ae6db6cc09b1c4ff9a2211e8256e9cd9cd183941c3769c5c220ac298fa", "1.16.0--r40h5f743cb_0": "sha256:4865fade8ddd1f0168a7ebcfca97a8f08542e6fc9e01d006b45b6cba772618ac"}, "docker": "quay.io/biocontainers/bioconductor-dada2", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dada2.
shpc-registry automated BioContainers addition for bioconductor-dada2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dada2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dada2:1.26.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dada2/1.26.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-dada2/1.26.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dada2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dada2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dada2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dada2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dada2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dada2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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