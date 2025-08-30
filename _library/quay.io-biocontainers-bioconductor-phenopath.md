---
layout: container
name:  "quay.io/biocontainers/bioconductor-phenopath"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phenopath/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phenopath/container.yaml"
updated_at: "2025-08-30 03:40:34.494868"
latest: "1.30.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phenopath"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_1"
 - "1.22.0--r42hc247a5b_0"
 - "1.18.0--r41hc247a5b_2"
 - "1.16.0--r41h399db7b_0"
 - "1.14.0--r40h399db7b_1"
 - "1.12.0--r40h5f743cb_0"
 - "1.22.0--r42hf17093f_1"
 - "1.24.0--r43hf17093f_0"
 - "1.26.0--r43hf17093f_0"
 - "1.30.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phenopath"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phenopath", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phenopath", "latest": {"1.30.0--r44he5774e6_0": "sha256:9fdc805ee33ee50cb939695c3a7dc394160a5fc6b0346328f95d0145487dff2a"}, "tags": {"1.8.0--r36he1b5a44_1": "sha256:ffe0cc789b467282ad9ceeb69eeb73cf0744a34c947875479d511e6080c429d3", "1.22.0--r42hc247a5b_0": "sha256:0d06e7aedc4ae95896e8931e6124628ad4189294a58eb0017ee718456c807f80", "1.18.0--r41hc247a5b_2": "sha256:3c775935f23b5eeadcc070a223e068cb496626810d09a097ca4f8f857c844d2b", "1.16.0--r41h399db7b_0": "sha256:e7eaba2474be70845f9871f077a0ce7690a24c8f700516647f2de1d83106163b", "1.14.0--r40h399db7b_1": "sha256:e7044ae951d1a402db3116d3f5643b019218a16c93a853b2f103fd38723a3bf9", "1.12.0--r40h5f743cb_0": "sha256:2b4ef828d766ca036e94f5667a6f074cb00e4224f5d65e599dd2b89e3f30e3a0", "1.22.0--r42hf17093f_1": "sha256:e038524b3066907a20fe59a374abd2ebe40dfd6597868bff4809a3bba71d2b67", "1.24.0--r43hf17093f_0": "sha256:963e558ba87b3ffd173b4835110d301edaa7c053e5a90575fb97d45a01fdbd9c", "1.26.0--r43hf17093f_0": "sha256:4695fa30b853dacd02c46969744dc98cf202bec9f00d660c8634d271a5e30413", "1.30.0--r44he5774e6_0": "sha256:9fdc805ee33ee50cb939695c3a7dc394160a5fc6b0346328f95d0145487dff2a"}, "docker": "quay.io/biocontainers/bioconductor-phenopath", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phenopath.
shpc-registry automated BioContainers addition for bioconductor-phenopath
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phenopath
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phenopath:1.30.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phenopath/1.30.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-phenopath/1.30.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phenopath-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenopath-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenopath-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phenopath-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phenopath-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phenopath-inspect-deffile:

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