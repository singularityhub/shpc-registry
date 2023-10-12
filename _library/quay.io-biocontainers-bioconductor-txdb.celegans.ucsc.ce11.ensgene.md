---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene/container.yaml"
updated_at: "2023-10-12 02:32:34.195126"
latest: "3.15.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.celegans.ucsc.ce11.ensgene"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.4.6--r36_2"
 - "3.15.0--r42hdfd78af_0"
 - "3.12.0--r41hdfd78af_4"
 - "3.11.0--r40_0"
 - "3.15.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce11.ensgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.celegans.ucsc.ce11.ensgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce11.ensgene", "latest": {"3.15.0--r43hdfd78af_1": "sha256:7ed692ae3ecda5c0802844030b89f19e47629b1f2c5121c9d50fa2dac6d996b6"}, "tags": {"3.4.6--r36_2": "sha256:77bc5f4a0b6443cb5f421ff151ad3ed5e8cf19a3567c292f79123e54564aa28a", "3.15.0--r42hdfd78af_0": "sha256:40c79f13ec2ba3ecaa60f27cccd2784713b1230048882dfe75258005050d0e31", "3.12.0--r41hdfd78af_4": "sha256:e8a608e6e2caee6666c5e81b342329cee5962e01df4f0ccff7ec6727218adb30", "3.11.0--r40_0": "sha256:8f1918e12dd22c9954df879b5264b2a1e3f9999e59587403c22a1dc4666121be", "3.15.0--r43hdfd78af_1": "sha256:7ed692ae3ecda5c0802844030b89f19e47629b1f2c5121c9d50fa2dac6d996b6"}, "docker": "quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.celegans.ucsc.ce11.ensgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene:3.15.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene/3.15.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-txdb.celegans.ucsc.ce11.ensgene/3.15.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.celegans.ucsc.ce11.ensgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.ensgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.ensgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.celegans.ucsc.ce11.ensgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.ensgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.celegans.ucsc.ce11.ensgene-inspect-deffile:

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