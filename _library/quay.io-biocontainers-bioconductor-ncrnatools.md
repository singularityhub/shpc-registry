---
layout: container
name:  "quay.io/biocontainers/bioconductor-ncrnatools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ncrnatools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ncrnatools/container.yaml"
updated_at: "2025-04-25 02:50:19.057851"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ncrnatools"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ncrnatools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ncrnatools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ncrnatools", "latest": {"1.16.0--r44hdfd78af_0": "sha256:87eaaa70640363f79aeb0514fde39ef15ec68a7669896e79f5e82d2e5ae72913"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:7ebca866d58807246bb91dde424819bcdbb3acf85fa0b115d2689e824a7925a9", "1.8.0--r42hdfd78af_0": "sha256:1556b48bf1096f14a6a779b91cefc9c322a78c7f5e9fa33e79262740add64141", "1.10.0--r43hdfd78af_0": "sha256:c7f35d07d59983bacfd7f6c8a7ddc3284728ef588b90996934adf67473c236f3", "1.12.0--r43hdfd78af_0": "sha256:7de334239ebf4a61e1b6e564b5789aa2fb42b94efea0041641af6eb3bac22f7e", "1.16.0--r44hdfd78af_0": "sha256:87eaaa70640363f79aeb0514fde39ef15ec68a7669896e79f5e82d2e5ae72913"}, "docker": "quay.io/biocontainers/bioconductor-ncrnatools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ncrnatools.
shpc-registry automated BioContainers addition for bioconductor-ncrnatools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ncrnatools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ncrnatools:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ncrnatools/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ncrnatools/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ncrnatools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ncrnatools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ncrnatools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ncrnatools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ncrnatools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ncrnatools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ncrnatools

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