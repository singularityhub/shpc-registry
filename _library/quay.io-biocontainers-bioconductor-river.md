---
layout: container
name:  "quay.io/biocontainers/bioconductor-river"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-river/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-river/container.yaml"
updated_at: "2024-03-10 02:28:54.457447"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-river"
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
description: "shpc-registry automated BioContainers addition for bioconductor-river"
config: {"url": "https://biocontainers.pro/tools/bioconductor-river", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-river", "latest": {"1.26.0--r43hdfd78af_0": "sha256:660566700292b5fbbc9e7c660eece5e2b971d20bade65c86b234e27db99ae217"}, "tags": {"1.8.0--r36_1": "sha256:dade0a0f7044427c04d81b8f9ccd8536627fcb470a3ba10878687307e053419e", "1.22.0--r42hdfd78af_0": "sha256:29a4c326c4d7bc5051209735c1e569c0eac225697ecb4fdb9bda83729e11ac04", "1.18.0--r41hdfd78af_0": "sha256:93c3a00ce0080193f436a4529cb759017957033a887b43756e161833eb0e5ab0", "1.16.0--r41hdfd78af_0": "sha256:b441213994283bbf17d35409453f729303a55fa9e4ee340f9cf76fdee56f36d1", "1.14.0--r40hdfd78af_1": "sha256:2e9fa73e5a616d78e7c9537a1f49969676d143a66414b85f2c29b058444b750f", "1.12.0--r40_0": "sha256:032a2628307fc79a2154e0df41750042d8fccbf45b081347597d4f4b26915e3b", "1.24.0--r43hdfd78af_0": "sha256:f5f392214d3748eef432acd0edc4b8dfbd4a106aa7633977b2df3e0e1e38a8c7", "1.26.0--r43hdfd78af_0": "sha256:660566700292b5fbbc9e7c660eece5e2b971d20bade65c86b234e27db99ae217"}, "docker": "quay.io/biocontainers/bioconductor-river", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-river.
shpc-registry automated BioContainers addition for bioconductor-river
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-river
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-river:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-river/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-river/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-river-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-river-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-river-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-river-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-river-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-river-inspect-deffile:

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