---
layout: container
name:  "quay.io/biocontainers/bioconductor-iwtomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iwtomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iwtomics/container.yaml"
updated_at: "2024-11-02 02:52:44.523274"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-iwtomics"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-iwtomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iwtomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iwtomics", "latest": {"1.26.0--r43hdfd78af_0": "sha256:a14490e8f995507ab0b56b5a9683748e3a994a4d04766baa353819df1f44c7ef"}, "tags": {"1.8.0--r36_1": "sha256:e8739ebee5da551ef6a1698439cc50de0e47da6682a6649eac1e3a83b0766982", "1.22.0--r42hdfd78af_0": "sha256:eaf8ba43533a605c87338dc1e5290d1061ccd1640e9dd4a9b0d74e7aae3e3fb7", "1.18.0--r41hdfd78af_0": "sha256:1d48e2df0c49075c729f5b225815c2902023f71ccfdc2c4190e3969a1a3f5138", "1.16.0--r41hdfd78af_0": "sha256:4017e2ae4a97f5093cb54def5ec422c7264509070f6e0491cc18a95e3781287c", "1.14.0--r40hdfd78af_1": "sha256:c968aef3c50bd5c581cab982f09b4f0fc1ebf5298431e9558a4d0fcec14b084f", "1.12.0--r40_0": "sha256:cecd3ffd6e030286c249aa7d214ed22055f62755b48ecb0d52a3f1af45fad4ac", "1.24.0--r43hdfd78af_0": "sha256:ab035f2fb594113e4306be5b6f3f60128ee0f74afbfb3560017cd05a0132d162", "1.26.0--r43hdfd78af_0": "sha256:a14490e8f995507ab0b56b5a9683748e3a994a4d04766baa353819df1f44c7ef"}, "docker": "quay.io/biocontainers/bioconductor-iwtomics", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iwtomics.
shpc-registry automated BioContainers addition for bioconductor-iwtomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iwtomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iwtomics:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iwtomics/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-iwtomics/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iwtomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iwtomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iwtomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iwtomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iwtomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iwtomics-inspect-deffile:

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