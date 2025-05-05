---
layout: container
name:  "quay.io/biocontainers/bioconductor-countsimqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-countsimqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-countsimqc/container.yaml"
updated_at: "2025-05-05 03:28:58.329277"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-countsimqc"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.1--r40hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-countsimqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-countsimqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-countsimqc", "latest": {"1.24.0--r44hdfd78af_0": "sha256:7d8e8c3669149ef28cbab627ab30d1b46b052ed06c54095a409ee455b9c8360a"}, "tags": {"1.8.1--r40hdfd78af_0": "sha256:fdcbc1421ec94f767d3669b2d977d74f17a2e1c24db8b33634ec3e74a6128778", "1.16.0--r42hdfd78af_0": "sha256:be0174f0fe6567cf83a13091c7c1623cfbad378b2dc4415ae686db30060cf7b0", "1.12.0--r41hdfd78af_0": "sha256:ed0bf980adffa3138d657b503beef1b0edc1701f9220396adc3041ea6a970d6c", "1.10.0--r41hdfd78af_0": "sha256:6af30686029c3c0b9e0e688b215b6c4874de863970a6d90fb551fb2771bed673", "1.18.0--r43hdfd78af_0": "sha256:8a031d8dca4126e86a02aa2d9f411face459d6f37e819f08d9cc91d7e26fe660", "1.20.0--r43hdfd78af_0": "sha256:6c5bcf9e1daaf1370730ee438dc89e8d1d7157f3ccb968ad9ba2f5a20de7aa5a", "1.24.0--r44hdfd78af_0": "sha256:7d8e8c3669149ef28cbab627ab30d1b46b052ed06c54095a409ee455b9c8360a"}, "docker": "quay.io/biocontainers/bioconductor-countsimqc", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-countsimqc.
shpc-registry automated BioContainers addition for bioconductor-countsimqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-countsimqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-countsimqc:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-countsimqc/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-countsimqc/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-countsimqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-countsimqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-countsimqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-countsimqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-countsimqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-countsimqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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