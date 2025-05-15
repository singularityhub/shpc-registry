---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene/container.yaml"
updated_at: "2025-05-15 03:52:12.055803"
latest: "3.12.0--r44hdfd78af_8"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.ggallus.ucsc.galgal4.refgene"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.4.6--r36_1"
 - "3.12.0--r42hdfd78af_5"
 - "3.11.0--r40_0"
 - "3.10.0--r36_0"
 - "3.12.0--r43hdfd78af_6"
 - "3.12.0--r43hdfd78af_7"
 - "3.12.0--r44hdfd78af_8"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal4.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.ggallus.ucsc.galgal4.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal4.refgene", "latest": {"3.12.0--r44hdfd78af_8": "sha256:2e6c83168ca957f631f436a7d83f395a57034a4320fc0eed06d8c568c5e74f16"}, "tags": {"3.4.6--r36_1": "sha256:326d6f0ecde1ca5a3014d9c7664b06ee2305a59bd3f2ebc6e2a1b4c68a3b6b0e", "3.12.0--r42hdfd78af_5": "sha256:74cf7c3032007d4b7d1eb38285aec6439863b795f594bee3ec57d323eaaf37d2", "3.11.0--r40_0": "sha256:06543ad6b9bcead2dd1a1d68897caccd213de764abc975e0914ea38077417518", "3.10.0--r36_0": "sha256:cce0d09ca01073860c374cb857eddb4632dea5ff05f17b9e4d64b67c6109519b", "3.12.0--r43hdfd78af_6": "sha256:150bd6204f8462884bbbf5eb0750dda08482f66544da2f2c7dd876b3cc197d6e", "3.12.0--r43hdfd78af_7": "sha256:42137a59532b332a70b706f631403896055c194fa521c0a15eb0418304b41c6a", "3.12.0--r44hdfd78af_8": "sha256:2e6c83168ca957f631f436a7d83f395a57034a4320fc0eed06d8c568c5e74f16"}, "docker": "quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal4.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene:3.12.0--r44hdfd78af_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene/3.12.0--r44hdfd78af_8
$ module help quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal4.refgene/3.12.0--r44hdfd78af_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.ggallus.ucsc.galgal4.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal4.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal4.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.ggallus.ucsc.galgal4.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal4.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal4.refgene-inspect-deffile:

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