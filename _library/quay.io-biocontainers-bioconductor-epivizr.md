---
layout: container
name:  "quay.io/biocontainers/bioconductor-epivizr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epivizr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epivizr/container.yaml"
updated_at: "2023-11-06 03:00:55.823667"
latest: "2.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epivizr"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r40hdfd78af_1"
 - "2.18.0--r40_0"
 - "2.16.0--r36_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epivizr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epivizr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epivizr", "latest": {"2.30.0--r43hdfd78af_0": "sha256:94691aa297ac37ecd3f3b29846f7d67ff9c465515c6e57c97b16f4c8f5c27022"}, "tags": {"2.8.0--r3.4.1_0": "sha256:750a7f2fe237b3f72f54e627ecfb54f8df47d40a76dda21c0c0cee5aa390bf73", "2.24.0--r41hdfd78af_0": "sha256:ea70aa3fcf849b0fce69de3cf476c77f04cab988574ce6c7ff91d34da2403e5e", "2.22.0--r41hdfd78af_0": "sha256:db3364c9fa178dc5622db7fa6205288604e72738e458caa5a14bccacf0da6da0", "2.20.0--r40hdfd78af_1": "sha256:58c70ebc67b37ce5473ce3ca22e2db53554053d03dcb620923a54962474785eb", "2.18.0--r40_0": "sha256:f53c14fc5c51cde0c65f6e9fb65bb84ef2bb97c54941b35334aebf5528bec9e8", "2.16.0--r36_0": "sha256:a56c9fd7bc5902f42598eda22bce52740c7d55b1115618fd9373da3cd8a9f9af", "2.28.0--r42hdfd78af_0": "sha256:179de5035b0680c9b6e674c6085deaf2d9423efbacf1cd80fd55c98c55db6f8c", "2.30.0--r43hdfd78af_0": "sha256:94691aa297ac37ecd3f3b29846f7d67ff9c465515c6e57c97b16f4c8f5c27022"}, "docker": "quay.io/biocontainers/bioconductor-epivizr", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epivizr.
shpc-registry automated BioContainers addition for bioconductor-epivizr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epivizr:2.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epivizr/2.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epivizr/2.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epivizr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epivizr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epivizr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epivizr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epivizr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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