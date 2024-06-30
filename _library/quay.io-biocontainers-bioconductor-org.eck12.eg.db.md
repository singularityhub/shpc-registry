---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.eck12.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.eck12.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.eck12.eg.db/container.yaml"
updated_at: "2024-06-30 03:07:19.801743"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.eck12.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.eck12.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.eck12.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.eck12.eg.db", "latest": {"3.18.0--r43hdfd78af_0": "sha256:a7162d714d6e34ce1e6e1f30efd62b7dd1b3626256731ba598aa5a6f7d504d6c"}, "tags": {"3.8.2--r36_1": "sha256:149a1a60c20c0dafe8d62c401f7a5983ccd400cd4a9d078052cadaec3c6004b0", "3.16.0--r42hdfd78af_0": "sha256:a75b11d4f11dc0ffe616ff2f11d68c8855cba984c9549d50655fa733d5f2f350", "3.14.0--r41hdfd78af_1": "sha256:8046eba527d9d19c4d3087bbe92cda9880c7ddce5a126cb268a726428671463f", "3.13.0--r41hdfd78af_0": "sha256:c791ec950af0833a7c7ce3dc8b3e41e31bb0c257b748ec6bf235fcb70dc0de86", "3.12.0--r40hdfd78af_1": "sha256:3e746854babbf338796c5ef0c387f96df501a02c9af059e4707201f2557f2e6f", "3.11.1--r40_0": "sha256:db8f44a487b4b724ce0752c825f309795e34535fa074a82c733a77faaaeb9c66", "3.17.0--r43hdfd78af_0": "sha256:46ad04a41e55a600d60fe103c2fd45e07de14724ec16c7aff7186ee7dd5d307b", "3.18.0--r43hdfd78af_0": "sha256:a7162d714d6e34ce1e6e1f30efd62b7dd1b3626256731ba598aa5a6f7d504d6c"}, "docker": "quay.io/biocontainers/bioconductor-org.eck12.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.eck12.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.eck12.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.eck12.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.eck12.eg.db:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.eck12.eg.db/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.eck12.eg.db/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.eck12.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.eck12.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.eck12.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.eck12.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.eck12.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.eck12.eg.db-inspect-deffile:

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