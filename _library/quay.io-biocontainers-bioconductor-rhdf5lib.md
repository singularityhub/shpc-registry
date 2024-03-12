---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhdf5lib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhdf5lib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhdf5lib/container.yaml"
updated_at: "2024-03-12 02:40:17.442615"
latest: "1.24.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rhdf5lib"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36h516909a_0"
 - "1.20.0--r42hc0cfd56_0"
 - "1.16.0--r41hc0cfd56_2"
 - "1.14.0--r41hd029910_0"
 - "1.12.1--r40hd029910_0"
 - "1.10.0--r40h037d062_0"
 - "1.20.0--r42hc0cfd56_1"
 - "1.20.0--r42ha9d7317_2"
 - "1.22.0--r43ha9d7317_0"
 - "1.22.0--r43h217d67c_1"
 - "1.24.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rhdf5lib"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhdf5lib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhdf5lib", "latest": {"1.24.0--r43ha9d7317_1": "sha256:8e6164e75ce4345293740d07a6a7306b3e817504d90076f6fb9261e5dd967c79"}, "tags": {"1.8.0--r36h516909a_0": "sha256:3f58b7631c8ec182f001a272e64d0ba8c10bd437bf68fc3c540fad2b92ce5431", "1.20.0--r42hc0cfd56_0": "sha256:ef98992395876a9f81c3440bd65d8b81c9d7e235c87fddf3e051e7a0a421c40b", "1.16.0--r41hc0cfd56_2": "sha256:a9b5d121b11565ffb3aa96885c5aaa12f30e22832557bba1945f3885c31cda48", "1.14.0--r41hd029910_0": "sha256:f84cfbefe3bf0eecc418db6eb3cbd2db1ed6892fd096cc0fa06ce70623a3c842", "1.12.1--r40hd029910_0": "sha256:a6180500c8abc2f827146b3707119719bf4be9a18b16d4e509ba95ee6cf5c7f8", "1.10.0--r40h037d062_0": "sha256:2fc1ec2b98ca0b3275d1fd67010d9ee3554a0289dd2e9b6ec9c71232fdab3f13", "1.20.0--r42hc0cfd56_1": "sha256:3e7208d146bb319c0407007802c5f5171541ddff4c10d86b1ce0d4f99e50c748", "1.20.0--r42ha9d7317_2": "sha256:fed31e3076a48fbe3269d4a3de68ed27d0b8e9d670d43f297cdcb7a6a37853fa", "1.22.0--r43ha9d7317_0": "sha256:3f40fabe52466106dd7dd735f8b4b126f6647a8e1aa915796e88ca4c0138b6ec", "1.22.0--r43h217d67c_1": "sha256:b1d5ca54ad8620186e8b9106c483953e91faa0b9bdd8998ecae0bbbc7fba439a", "1.24.0--r43ha9d7317_1": "sha256:8e6164e75ce4345293740d07a6a7306b3e817504d90076f6fb9261e5dd967c79"}, "docker": "quay.io/biocontainers/bioconductor-rhdf5lib", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhdf5lib.
shpc-registry automated BioContainers addition for bioconductor-rhdf5lib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhdf5lib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhdf5lib:1.24.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhdf5lib/1.24.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-rhdf5lib/1.24.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhdf5lib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhdf5lib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhdf5lib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhdf5lib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhdf5lib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhdf5lib-inspect-deffile:

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