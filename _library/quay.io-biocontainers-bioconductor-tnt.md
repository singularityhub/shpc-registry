---
layout: container
name:  "quay.io/biocontainers/bioconductor-tnt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tnt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tnt/container.yaml"
updated_at: "2025-11-29 03:17:43.681440"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tnt"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tnt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tnt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tnt", "latest": {"1.28.0--r44hdfd78af_0": "sha256:c65c1a02b612ef307e46a31fe5d9419a814aa858fab177784e89e93a4cbf29cb"}, "tags": {"1.8.0--r36_0": "sha256:7f7dc59359b2f66597957da03b36af86ed53b8c487e3abe63e892ec9ccbabcf8", "1.20.0--r42hdfd78af_0": "sha256:ed04ac2f2a2ac5252bfa6a66c4a9e0f18e044c0c5b8391218be91dc08c93effd", "1.16.0--r41hdfd78af_0": "sha256:26634a82d365d522a3c7f2642c500f336b8bfdf1c46c2aadfdb1b176b66fa37a", "1.14.0--r41hdfd78af_0": "sha256:b8bd8879e6806093355c19e9a9c4a4c4667787ef1e01f189bc5cc0c959b9248c", "1.12.0--r40hdfd78af_1": "sha256:b5d1b856e967491141937c323167194f28051db1b9cb83676479932fcd2b89e6", "1.10.0--r40_0": "sha256:a8f69c72eca3b1cd121c5cd121d685e57bfc33ecbf3e9ba4adf19a8b71b1bcdf", "1.22.0--r43hdfd78af_0": "sha256:2d8bd584bb7bbab7af9d014758152951dc14e86baa81f0e7032ac5650e04613c", "1.24.0--r43hdfd78af_0": "sha256:dcc8a1d23e803f28d35a4f2163433d44ec9cf3acdcc020c27e0c744c7b7c4b73", "1.28.0--r44hdfd78af_0": "sha256:c65c1a02b612ef307e46a31fe5d9419a814aa858fab177784e89e93a4cbf29cb"}, "docker": "quay.io/biocontainers/bioconductor-tnt", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tnt.
shpc-registry automated BioContainers addition for bioconductor-tnt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tnt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tnt:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tnt/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tnt/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tnt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tnt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tnt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tnt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tnt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tnt-inspect-deffile:

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