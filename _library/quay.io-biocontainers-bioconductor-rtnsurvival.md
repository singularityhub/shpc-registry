---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtnsurvival"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtnsurvival/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtnsurvival/container.yaml"
updated_at: "2024-06-13 02:47:02.806466"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtnsurvival"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtnsurvival"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtnsurvival", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtnsurvival", "latest": {"1.26.0--r43hdfd78af_0": "sha256:196368cc955f39104f71039329920592aaf6678a7147aa130bde28e3db6417a8"}, "tags": {"1.8.1--r36_0": "sha256:4528a46653bc246b179c0da80a7fb6c29ac62e3e9a9159104c6b7ec847b2e80c", "1.22.0--r42hdfd78af_0": "sha256:ce32421c470302ef8731d5a948b075def76542ea23dd6e38483519c62c48c0f9", "1.18.0--r41hdfd78af_0": "sha256:e69d9b0350ea1a4cf6ded544cc320963f0c158b4619666065a058c54dfd98c12", "1.16.0--r41hdfd78af_0": "sha256:991d7f45e569a5bcbd60856b5ecaa4f0888ed0eb68e634605b2b13370ccbd672", "1.14.1--r40hdfd78af_0": "sha256:e72e8238b26a97aaf4f877724a5c95a915835689141d1c058f09b3019bf4082b", "1.12.0--r40_0": "sha256:d36340e45fdf973fcf97bff21e17318ab98987e6db127254eb889b9fdfb116eb", "1.24.0--r43hdfd78af_0": "sha256:1855376d051f7434b8ff335146a59d9d5a7ead27086672811c2d959ef499297f", "1.26.0--r43hdfd78af_0": "sha256:196368cc955f39104f71039329920592aaf6678a7147aa130bde28e3db6417a8"}, "docker": "quay.io/biocontainers/bioconductor-rtnsurvival", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtnsurvival.
shpc-registry automated BioContainers addition for bioconductor-rtnsurvival
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtnsurvival
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtnsurvival:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtnsurvival/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtnsurvival/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtnsurvival-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtnsurvival-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtnsurvival-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtnsurvival-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtnsurvival-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtnsurvival-inspect-deffile:

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