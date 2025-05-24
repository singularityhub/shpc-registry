---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgfr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgfr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgfr/container.yaml"
updated_at: "2025-05-24 03:52:18.264064"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mgfr"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mgfr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgfr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgfr", "latest": {"1.32.0--r44hdfd78af_0": "sha256:fe23ead519cbcf335f8dde7ef2a87cb7582ce2a8c2fc0658d1ef9f06053e9dbb"}, "tags": {"1.8.0--r351_0": "sha256:61287a1f404d69f0496a8d44995e37729ec719893b861e64f88510b085f27f40", "1.24.0--r42hdfd78af_0": "sha256:6978fc70b6ca07610543d5a946ff1bc7ce31139b645422e3f0f54d2904f6f1ce", "1.20.0--r41hdfd78af_0": "sha256:12a2a92040bde6b5d16383463582f6fa731bd914dd6a0ff929a7e4236e0fa1e5", "1.18.0--r41hdfd78af_0": "sha256:cda4059a133317fc7bd19c4a24d46cb63d22eb816906fe32e4903331180cb9d9", "1.16.0--r40hdfd78af_1": "sha256:78a0473c5fb55d402a5256c1e719dee1f1f20268cf725b407a689434ee244c15", "1.14.0--r40_0": "sha256:a7e52295402c82121ef1c97df4543f7e438fa62ffd80cd47f5f26abbc8bcada2", "1.26.0--r43hdfd78af_0": "sha256:94b106389dc62fb3aa43e93fcbd8f030b2161d2e24b95b9e2f2f1556ecdeade0", "1.28.0--r43hdfd78af_0": "sha256:4fe86fa8edc7af2d4ee532b49fe2e5007ef9a348669d2c232bb3b004cf86ac45", "1.32.0--r44hdfd78af_0": "sha256:fe23ead519cbcf335f8dde7ef2a87cb7582ce2a8c2fc0658d1ef9f06053e9dbb"}, "docker": "quay.io/biocontainers/bioconductor-mgfr", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgfr.
shpc-registry automated BioContainers addition for bioconductor-mgfr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgfr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgfr:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgfr/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mgfr/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgfr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgfr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgfr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgfr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgfr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgfr-inspect-deffile:

```bash
$ singularity inspect -d <container>
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