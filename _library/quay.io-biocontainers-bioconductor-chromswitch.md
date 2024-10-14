---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromswitch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromswitch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromswitch/container.yaml"
updated_at: "2024-10-14 17:37:14.032765"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromswitch"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromswitch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromswitch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromswitch", "latest": {"1.22.0--r43hdfd78af_0": "sha256:a671db5c318a471fc77f9673989701aacb9e1fb325de685c1a9076b8180737a4"}, "tags": {"1.8.0--r36_0": "sha256:7d62868cfb03cccab6d29cc4a0ad59466669e96b0e6e8f78599d5e4cb127e489", "1.20.0--r42hdfd78af_0": "sha256:f9300caaa27194337c2f3a9e5257e19a513a51dc12ab5927742e9313c5e9573d", "1.16.0--r41hdfd78af_0": "sha256:ae9f763ce305b5eb19545a1c919171eda8c90abb5bfd61e80b9608ac002797fc", "1.14.0--r41hdfd78af_0": "sha256:8328b700e398e01ea57713256952f81909a0bb78631e592ed350420e84b37772", "1.12.0--r40hdfd78af_1": "sha256:f5cda7568b8023a9af2d683f4fec738e321f4f33fbddb4c39380b1067f0ab472", "1.10.0--r40_0": "sha256:b5efa8617916d010a5f45cc19bdcb92bac50b97a4ff9b781447bb548ceff8129", "1.22.0--r43hdfd78af_0": "sha256:a671db5c318a471fc77f9673989701aacb9e1fb325de685c1a9076b8180737a4"}, "docker": "quay.io/biocontainers/bioconductor-chromswitch", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromswitch.
shpc-registry automated BioContainers addition for bioconductor-chromswitch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromswitch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromswitch:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromswitch/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chromswitch/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromswitch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromswitch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromswitch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromswitch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromswitch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromswitch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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