---
layout: container
name:  "quay.io/biocontainers/bioconductor-elmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-elmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-elmer/container.yaml"
updated_at: "2025-05-04 04:05:17.921091"
latest: "2.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-elmer"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.9.5--r36_1"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.0--r40_0"
 - "2.22.0--r42hdfd78af_0"
 - "2.24.1--r43hdfd78af_0"
 - "2.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-elmer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-elmer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-elmer", "latest": {"2.26.0--r43hdfd78af_0": "sha256:f62d2a187ece814c6cb1c99bbdc27c4d40826de66357a196c218fa8cef9f5935"}, "tags": {"2.9.5--r36_1": "sha256:fa65c4af2a29e6fb7c796ade5a6674f00cc8e7760388fc209c13e0e45180b7b3", "2.18.0--r41hdfd78af_0": "sha256:3294c57ff78dee748fc5c7750b8a0d5675ff6d8a0103512e16eb1adb5606712e", "2.16.0--r41hdfd78af_0": "sha256:889d836ae363ee146580dbafa83f1c38d2f6c50fb909955fe1fc1554fe168257", "2.14.0--r40hdfd78af_1": "sha256:7bc4aa9d8f3ef21feb81bc6445c270659f2c4a4898b54804dec9433462176d8c", "2.12.0--r40_0": "sha256:df5a876b098564f58ce1c45d6ec91d06119af1776978be1f2e8b7747569c920c", "2.22.0--r42hdfd78af_0": "sha256:a5cea0a5ca7148fdc7167a86952e37b07c65c24f2df80c6bf4bdb228d9a6b0f7", "2.24.1--r43hdfd78af_0": "sha256:71669d33d7d841abaa6853405dfa52e4c02acd49b879fd086bee5d277c9d4e71", "2.26.0--r43hdfd78af_0": "sha256:f62d2a187ece814c6cb1c99bbdc27c4d40826de66357a196c218fa8cef9f5935"}, "docker": "quay.io/biocontainers/bioconductor-elmer", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-elmer.
shpc-registry automated BioContainers addition for bioconductor-elmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-elmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-elmer:2.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-elmer/2.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-elmer/2.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-elmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-elmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-elmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-elmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-elmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-elmer-inspect-deffile:

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