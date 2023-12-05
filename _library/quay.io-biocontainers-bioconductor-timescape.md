---
layout: container
name:  "quay.io/biocontainers/bioconductor-timescape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-timescape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-timescape/container.yaml"
updated_at: "2023-12-05 03:15:03.609507"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-timescape"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-timescape"
config: {"url": "https://biocontainers.pro/tools/bioconductor-timescape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-timescape", "latest": {"1.24.0--r43hdfd78af_0": "sha256:051100d2127dd91d570e96bfdfb7640494b83b1e708409659b8ac00c1bc30bc9"}, "tags": {"1.8.0--r36_1": "sha256:65a6f060825a5246701601e843848148a3dd34c54f5dda45f761f012b06e11c4", "1.22.0--r42hdfd78af_0": "sha256:fab12303f5ca49eca65ff8d785150881691a738cd600099597d9908349ef666a", "1.18.0--r41hdfd78af_0": "sha256:ef26295da100918b9c4f7ac4d594c90e722be39fd2f52213afa36224454c8273", "1.16.0--r41hdfd78af_0": "sha256:fd756250573378adb53dafaf92557076ef3c98ba281a2aebc852adad98c9bf31", "1.14.0--r40hdfd78af_1": "sha256:fc97a91afcac046fd5e013de6707348a8e1ce19f249949201dfd167d3f35151e", "1.12.0--r40_0": "sha256:8bf0e59965c6ab9cb2c5a3f1fc766d6b2df59c39c877e988bd9d14775ae31fe6", "1.24.0--r43hdfd78af_0": "sha256:051100d2127dd91d570e96bfdfb7640494b83b1e708409659b8ac00c1bc30bc9"}, "docker": "quay.io/biocontainers/bioconductor-timescape", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-timescape.
shpc-registry automated BioContainers addition for bioconductor-timescape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-timescape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-timescape:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-timescape/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-timescape/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-timescape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timescape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timescape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-timescape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-timescape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-timescape-inspect-deffile:

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