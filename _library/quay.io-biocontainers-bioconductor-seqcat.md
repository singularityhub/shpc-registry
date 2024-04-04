---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqcat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqcat/container.yaml"
updated_at: "2024-04-04 02:30:22.387720"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqcat"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.1--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqcat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqcat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqcat", "latest": {"1.24.0--r43hdfd78af_0": "sha256:f7ed03ed8c66649dff2ba8677839a6c1e7414d8a804bf837c3d68ae6b710cb2b"}, "tags": {"1.8.0--r36_0": "sha256:25b0a46fbfad6760c2cfcf2389842cdc295c617d05bba1878cea110ff48392d0", "1.20.0--r42hdfd78af_0": "sha256:0236689eadc93ad644d8d4cc4c5fbe7d1fc101b9a7a90971d353408d4a55614f", "1.16.1--r41hdfd78af_0": "sha256:305771f62c6ac5418d5c243dc5cfd8ae3f8fb559bcaf0d88baa2181309810823", "1.14.0--r41hdfd78af_0": "sha256:beba32119faa155cde2c18d1c7807e7777088cc60fe1de69f11c26de6e41c88f", "1.12.0--r40hdfd78af_1": "sha256:7dd1dc133de4ea8cdd281818ad41a172bde2178323c57fdf66af25b0b5af0971", "1.10.0--r40_0": "sha256:726b93ed9431d5508d3e5033f026acc7d5d10df5ad1399158260486692490f8c", "1.22.0--r43hdfd78af_0": "sha256:82c1188246b75c65766c9cf155f9c5f7cf5915f287533b766b5b07270429586b", "1.24.0--r43hdfd78af_0": "sha256:f7ed03ed8c66649dff2ba8677839a6c1e7414d8a804bf837c3d68ae6b710cb2b"}, "docker": "quay.io/biocontainers/bioconductor-seqcat", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqcat.
shpc-registry automated BioContainers addition for bioconductor-seqcat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcat:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqcat/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqcat/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqcat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqcat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqcat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqcat-inspect-deffile:

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