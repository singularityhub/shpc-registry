---
layout: container
name:  "quay.io/biocontainers/bioconductor-ppinfer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ppinfer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ppinfer/container.yaml"
updated_at: "2023-12-07 03:10:44.832416"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ppinfer"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_1"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ppinfer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ppinfer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ppinfer", "latest": {"1.26.0--r43hdfd78af_0": "sha256:935e69d7238c4869643437205ab3e98fd8d9a595a82cec159ee0fc00b214ff47"}, "tags": {"1.8.1--r351_0": "sha256:5a69d581f732588683ea9ea9838bbd66eafd2419d0d9aeb0b605e157fef60057", "1.20.0--r41hdfd78af_0": "sha256:133d505bfc446345f7fff42df7eec00ca56caaaa8b08a0a65dee41a6b8da5dd8", "1.18.0--r41hdfd78af_0": "sha256:4ceed9875471693a134a7ecace4d59e677885f382766a9fb78acedd51a323d53", "1.16.0--r40hdfd78af_1": "sha256:e5e25399c2f1dfab1d206d3ec5988accbf7f62748af74689efeabb2933b99673", "1.14.0--r40_0": "sha256:8b4aaf6c8cd7db7102114f6a622084a328f01a5aad9b3a83c532a12fdee3e619", "1.12.0--r36_1": "sha256:6d1f0e3aa4c63cc8458bf6a62d87bc591af1449a57e0ab7a9600e860b8ab3ae8", "1.24.0--r42hdfd78af_0": "sha256:803e56e18889d628d861a890104e7233416f475ee221ad372c731b04acddb889", "1.26.0--r43hdfd78af_0": "sha256:935e69d7238c4869643437205ab3e98fd8d9a595a82cec159ee0fc00b214ff47"}, "docker": "quay.io/biocontainers/bioconductor-ppinfer", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ppinfer.
shpc-registry automated BioContainers addition for bioconductor-ppinfer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ppinfer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ppinfer:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ppinfer/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ppinfer/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ppinfer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ppinfer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ppinfer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ppinfer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ppinfer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ppinfer-inspect-deffile:

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