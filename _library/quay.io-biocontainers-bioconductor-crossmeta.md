---
layout: container
name:  "quay.io/biocontainers/bioconductor-crossmeta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-crossmeta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-crossmeta/container.yaml"
updated_at: "2025-11-21 03:59:30.151970"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-crossmeta"
aliases:
 - "xgboost"
 - "pandoc-citeproc"
 - "pandoc"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.15.0--r40_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-crossmeta"
config: {"url": "https://biocontainers.pro/tools/bioconductor-crossmeta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-crossmeta", "latest": {"1.28.0--r43hdfd78af_0": "sha256:065adb02243c2d8812b8ec63e86528b32520e247970b658e65efd55f0aede571"}, "tags": {"1.8.0--r351_0": "sha256:0f70861568a10a819efde64c02afb3999ab4666428bccc414ea9cd080c63d899", "1.20.0--r41hdfd78af_0": "sha256:efb5d35b4d8eb2528c0815a73a5f86969f53cffcc1befdc72049ec5c18467407", "1.18.0--r41hdfd78af_0": "sha256:5b8d4deaa00266fcd80c90d9c773be4ca52c487681f652ccb7df6c69285c8fe6", "1.15.0--r40_1": "sha256:b50247effdc0b7fa173f0c27a5c3188a8f562f3effbd345411d9a04f3e3891ca", "1.14.0--r40_0": "sha256:030285850a49a791d9cb6253901b3f84bca752db0cb9fc8095e5c0ebf1c56412", "1.12.0--r36_0": "sha256:c039df0f6d5f6946b6392fd03f4425cadb87af2e8b6bb5224ad837232dcf336f", "1.24.0--r42hdfd78af_0": "sha256:5cbc603fd3feb2e49b37c06245e5471cbb53949557657387d5179d4f47a6cde1", "1.26.0--r43hdfd78af_0": "sha256:0289180132a2174aa264c5869991aea7b712b2d8259e36d04dcf0f25bd6188d1", "1.28.0--r43hdfd78af_0": "sha256:065adb02243c2d8812b8ec63e86528b32520e247970b658e65efd55f0aede571"}, "docker": "quay.io/biocontainers/bioconductor-crossmeta", "aliases": {"xgboost": "/usr/local/bin/xgboost", "pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-crossmeta.
shpc-registry automated BioContainers addition for bioconductor-crossmeta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-crossmeta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-crossmeta:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-crossmeta/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-crossmeta/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-crossmeta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crossmeta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-crossmeta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-crossmeta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-crossmeta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-crossmeta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
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