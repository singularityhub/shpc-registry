---
layout: container
name:  "quay.io/biocontainers/bioconductor-micrornaome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-micrornaome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-micrornaome/container.yaml"
updated_at: "2025-02-14 02:56:59.460605"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-micrornaome"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_1"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-micrornaome"
config: {"url": "https://biocontainers.pro/tools/bioconductor-micrornaome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-micrornaome", "latest": {"1.28.0--r44hdfd78af_0": "sha256:c15a9e8ee3a646fcfb5dcff3939d8a78db9ab7f72f39a51c4d8429143be857da"}, "tags": {"1.8.0--r36_0": "sha256:0bdcdfbabef98067201c1c5255a433a6cfdebd8665e7bceda6d269220888db2c", "1.20.0--r42hdfd78af_0": "sha256:d5331bf6b00707c9e53502ea104fca2493591d000c72db3492aab1745f046469", "1.16.0--r41hdfd78af_1": "sha256:e1b95d6620bf038339acae2e82b4eafdd28205a40ed6b7414abebbcaceb032f9", "1.14.0--r41hdfd78af_0": "sha256:7d904bbb610401b2aa03ef8cbc3e99f331fbc327dd9dc4d6a57623ee2e7cdd1b", "1.12.0--r40hdfd78af_1": "sha256:b1b4332dafe20b0720ce2c52dcbd5f186a422629f3cf90454c3760b4bfa702a7", "1.10.0--r40_0": "sha256:15d3f600292d6a68bbb4b83d4046f22de3a03c2526910543213ff80dd5e45c9b", "1.22.0--r43hdfd78af_0": "sha256:9a4db22deda86a70ca23e1c08f194964efbf6b3b17757dee8f4e7e6768cddeed", "1.24.0--r43hdfd78af_0": "sha256:13b1b9bfd2bc64f6e1e9c50ba0630b4a76572de78016133eb11fb59ec61dd971", "1.28.0--r44hdfd78af_0": "sha256:c15a9e8ee3a646fcfb5dcff3939d8a78db9ab7f72f39a51c4d8429143be857da"}, "docker": "quay.io/biocontainers/bioconductor-micrornaome", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-micrornaome.
shpc-registry automated BioContainers addition for bioconductor-micrornaome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-micrornaome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-micrornaome:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-micrornaome/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-micrornaome/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-micrornaome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-micrornaome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-micrornaome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-micrornaome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-micrornaome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-micrornaome-inspect-deffile:

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