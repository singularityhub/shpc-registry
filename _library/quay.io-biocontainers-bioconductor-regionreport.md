---
layout: container
name:  "quay.io/biocontainers/bioconductor-regionreport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-regionreport/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-regionreport/container.yaml"
updated_at: "2024-07-11 03:28:45.566064"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-regionreport"
aliases:
 - "pandoc"
versions:
 - "1.27.1--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-regionreport"
config: {"url": "https://biocontainers.pro/tools/bioconductor-regionreport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-regionreport", "latest": {"1.36.0--r43hdfd78af_0": "sha256:8461c702c46a68e3d8a28431e8487cc3d269ee9063553a511e33fae19ef37791"}, "tags": {"1.27.1--r41hdfd78af_0": "sha256:1aca97321d5291a4a452aea0bfce3092bd02620eed0bc9fe5f0ca8e171628e0a", "1.32.0--r42hdfd78af_0": "sha256:db22c12a015babe359abd3cb00378152e5ddaf7220e1c8554d85bad3292a0d4d", "1.34.0--r43hdfd78af_0": "sha256:7a7c93dac1fa551fe2cbc629f233f2e2d0dc37feb44a2a91d7f443ffd8358eb8", "1.36.0--r43hdfd78af_0": "sha256:8461c702c46a68e3d8a28431e8487cc3d269ee9063553a511e33fae19ef37791"}, "docker": "quay.io/biocontainers/bioconductor-regionreport", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-regionreport.
shpc-registry automated BioContainers addition for bioconductor-regionreport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-regionreport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-regionreport:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-regionreport/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-regionreport/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-regionreport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regionreport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regionreport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-regionreport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-regionreport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-regionreport-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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