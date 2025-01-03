---
layout: container
name:  "quay.io/biocontainers/bioconductor-scdataviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scdataviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scdataviz/container.yaml"
updated_at: "2025-01-03 02:59:42.937268"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scdataviz"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scdataviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scdataviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scdataviz", "latest": {"1.12.0--r43hdfd78af_0": "sha256:6fcd0e8fdb0cfd7f523bd707be3a1da403b26e6308b3f64ec08f83dc08f61fd6"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:fb1a15d3b65b7bdc1dcbb48187576815fa12ba7bd0ac1d946e64fec88d34ede5", "1.8.0--r42hdfd78af_0": "sha256:04e17f0917d86c9de100e7a3486b24edd13979cb98adb890dfb45c2133bb2f74", "1.10.0--r43hdfd78af_0": "sha256:9c2b9b4e77b0989becb36017901b09b1cda07b387be3a1f704efc9c6dba40dd0", "1.12.0--r43hdfd78af_0": "sha256:6fcd0e8fdb0cfd7f523bd707be3a1da403b26e6308b3f64ec08f83dc08f61fd6"}, "docker": "quay.io/biocontainers/bioconductor-scdataviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scdataviz.
shpc-registry automated BioContainers addition for bioconductor-scdataviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scdataviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scdataviz:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scdataviz/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scdataviz/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scdataviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scdataviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scdataviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scdataviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scdataviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scdataviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scdataviz

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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