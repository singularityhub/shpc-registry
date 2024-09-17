---
layout: container
name:  "quay.io/biocontainers/bioconductor-atacseqqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-atacseqqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-atacseqqc/container.yaml"
updated_at: "2024-09-17 02:47:16.193317"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-atacseqqc"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.5--r36_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.4--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-atacseqqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-atacseqqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-atacseqqc", "latest": {"1.26.0--r43hdfd78af_0": "sha256:a58e83fa7cc0797ee1e4ffe951e315f500206c18b95ae3f8ce7f6c977b0591ad"}, "tags": {"1.8.5--r36_0": "sha256:6b6205ff37c8462a44aeaac740ff0a7df7e2ae5e94d4d74ad4a4b5512fdbfee6", "1.18.0--r41hdfd78af_0": "sha256:0b2d64e0dc4656734423a4667adc0bdd7cb3b034bcda4c6d18f6588a52bbfbbc", "1.16.0--r41hdfd78af_0": "sha256:d18f3526303e6791bef99334180da0affd3128dc0aaf9c206e87d26c31442d19", "1.14.4--r40hdfd78af_1": "sha256:ca7efd605d056c41e4dac8c7acccb91490eb97f384450d80e7fd851c67359896", "1.12.0--r40_0": "sha256:580a7d9ff9eed4ce1a6eef3447dc2f40ee88332afa02c8252286302d0a0efe9e", "1.10.0--r36_0": "sha256:1fce90b21ef20cb0d906431183eb35edaccb9c33dc2fb80b5cc84c3c1c9e2964", "1.22.0--r42hdfd78af_0": "sha256:6dfd7d9cb8473523f93566eb59150523be71595bf66c5b441114165a2559a7b6", "1.24.0--r43hdfd78af_0": "sha256:4615e89389a638ce63254be7dd8a6fded0b4896cb6659a5cdea2403a8a671959", "1.26.0--r43hdfd78af_0": "sha256:a58e83fa7cc0797ee1e4ffe951e315f500206c18b95ae3f8ce7f6c977b0591ad"}, "docker": "quay.io/biocontainers/bioconductor-atacseqqc", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-atacseqqc.
shpc-registry automated BioContainers addition for bioconductor-atacseqqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-atacseqqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-atacseqqc:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-atacseqqc/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-atacseqqc/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-atacseqqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-atacseqqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-atacseqqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-atacseqqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-atacseqqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-atacseqqc-inspect-deffile:

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