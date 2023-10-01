---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene/container.yaml"
updated_at: "2023-10-01 02:35:59.776009"
latest: "3.12.0--r43hdfd78af_6"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.ggallus.ucsc.galgal5.refgene"
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
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal5.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.ggallus.ucsc.galgal5.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal5.refgene", "latest": {"3.12.0--r43hdfd78af_6": "sha256:aaec7bc7f9cd9362c6de80e382793b9eef8f64a466789aedb7389b3222c8b0d8"}, "tags": {"3.4.6--r36_1": "sha256:bbce7922f8292b47752a884030edec27232969798bbf725d6a8e17acef70d051", "3.12.0--r42hdfd78af_5": "sha256:8c43f5fb09529f7c7c6794e50b02c5c65889abb326212ce5876b468e77615a38", "3.11.0--r40_0": "sha256:dd4ab78e3dff93c900f287e54652ceaf9a48fb049fa50f1afab124f75dae572b", "3.10.0--r36_0": "sha256:9a60a659e5e8c27edca5fe9500c905dd94b6451ec99a6e97b4c07324735945ca", "3.12.0--r43hdfd78af_6": "sha256:aaec7bc7f9cd9362c6de80e382793b9eef8f64a466789aedb7389b3222c8b0d8"}, "docker": "quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.ggallus.ucsc.galgal5.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene:3.12.0--r43hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene/3.12.0--r43hdfd78af_6
$ module help quay.io/biocontainers/bioconductor-txdb.ggallus.ucsc.galgal5.refgene/3.12.0--r43hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.ggallus.ucsc.galgal5.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal5.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal5.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.ggallus.ucsc.galgal5.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal5.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.ggallus.ucsc.galgal5.refgene-inspect-deffile:

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