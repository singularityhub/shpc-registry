---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotatr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotatr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotatr/container.yaml"
updated_at: "2024-02-17 02:25:05.674993"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotatr"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotatr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotatr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotatr", "latest": {"1.28.0--r43hdfd78af_0": "sha256:b3cd759182d49b1ccab5e0e25e073f244ab5e97a80d7d0ac56c46225a0c21294"}, "tags": {"1.8.0--r351_0": "sha256:31aef20797f6039a453988b7e758a3de50c9c936819a5c193c8b1aa8612a5156", "1.24.0--r42hdfd78af_0": "sha256:c9db7b7f2f0dc5885f0a1d3bbce6ea4b45a32700d2037ca39e8fd9b1ef415591", "1.20.0--r41hdfd78af_0": "sha256:cf35f6c76a80b907744e9c931b3313f18ec7a278fb0d61e43b3f5e3549a36c1e", "1.18.0--r41hdfd78af_0": "sha256:821e5e484c9b61aa443b43f6801b6a8ae9fa6d29ed26aee276d40d1c877bf0de", "1.16.0--r40hdfd78af_1": "sha256:22c0e0b059a2f691ee909a014331b2d594a1cf73f2e61162504f9cbb0c415863", "1.14.0--r40_0": "sha256:91bcd7e51932663c75edf371c0daf66124d7af535a1dcf5c02e5ae286eea8d3a", "1.26.0--r43hdfd78af_0": "sha256:69d10a5478e9c222f951914b7ad00466f90f0d18be27e1c8662aefb91f05333f", "1.28.0--r43hdfd78af_0": "sha256:b3cd759182d49b1ccab5e0e25e073f244ab5e97a80d7d0ac56c46225a0c21294"}, "docker": "quay.io/biocontainers/bioconductor-annotatr", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotatr.
shpc-registry automated BioContainers addition for bioconductor-annotatr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotatr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotatr:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotatr/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotatr/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotatr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotatr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotatr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotatr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotatr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotatr-inspect-deffile:

```bash
$ singularity inspect -d <container>
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