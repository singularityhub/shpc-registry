---
layout: container
name:  "quay.io/biocontainers/bioconductor-banocc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-banocc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-banocc/container.yaml"
updated_at: "2025-08-08 04:04:29.893475"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-banocc"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-banocc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-banocc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-banocc", "latest": {"1.30.0--r44hdfd78af_0": "sha256:ee31d0f0c7736fa12489c87da1826bcc19e0d141a1611ada60083e588943943f"}, "tags": {"1.8.0--r36_1": "sha256:ab6cbba4ab0c42f4911149d4aa0b2c0f92f69a2b7a6891f0f6b348384ddbc49e", "1.18.0--r41hdfd78af_0": "sha256:238ef251f0aeabb4d9afd65bf2683dd7db14d928e3e86922434a9fd4f4beaec1", "1.16.0--r41hdfd78af_0": "sha256:01010ab2e2bc5d2eda408278ce9981f157e0bca2af1c2574ea17ed5b66ab2764", "1.14.0--r40hdfd78af_1": "sha256:64d61c7acaf961d1f55b3994b16f03d387c5a06d9db9345e98e725aac3120d38", "1.12.0--r40_0": "sha256:a6d49cd5f71efaea434139a40bcfd13d758658145c68a132a643cf1f61954039", "1.10.0--r36_0": "sha256:f399200f135e51e987cbfdc478f282ecd83768d8dc11eb2b1656ff4db36c1d65", "1.22.0--r42hdfd78af_0": "sha256:fa85ed1c2660bb32a658c29267e0808fd61a1fc73ad11d164108422ce3d7306c", "1.24.0--r43hdfd78af_0": "sha256:51c4cbf470915e8013697765ad0d2f7bec3819e25d5aba197fd172f885b5b777", "1.26.0--r43hdfd78af_0": "sha256:8615693d182d0bff3edb098024b6d5d1b78edb07ce5e5b644ec5a941d2ab8991", "1.30.0--r44hdfd78af_0": "sha256:ee31d0f0c7736fa12489c87da1826bcc19e0d141a1611ada60083e588943943f"}, "docker": "quay.io/biocontainers/bioconductor-banocc", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-banocc.
shpc-registry automated BioContainers addition for bioconductor-banocc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-banocc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-banocc:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-banocc/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-banocc/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-banocc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-banocc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-banocc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-banocc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-banocc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-banocc-inspect-deffile:

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