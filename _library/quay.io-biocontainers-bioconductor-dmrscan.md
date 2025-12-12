---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmrscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmrscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmrscan/container.yaml"
updated_at: "2025-12-12 03:49:38.766957"
latest: "1.28.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dmrscan"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.11.0--r36_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.28.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dmrscan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmrscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmrscan", "latest": {"1.28.0--r44hdfd78af_0": "sha256:6a19b770be868e58ab54035f098f17c1074f76228528066ffcc06bb634291b14"}, "tags": {"1.8.0--r351_0": "sha256:4278071d55525f57dc3070ca60f3bb130012bcce84e27e186ef4f848a2297caa", "1.20.0--r42hdfd78af_0": "sha256:c3af7caada4e53554c6ffb219be4bd925e3d46af72d87405f91b008ca1d987b8", "1.16.0--r41hdfd78af_0": "sha256:fbf67a2e2639b13de28cbdbb1b53a9d573eed23c50a9b620a94743677045a89d", "1.14.0--r41hdfd78af_0": "sha256:697e8c93f7806888fdd45c0efdae60ce39305adab55aa7969075a7d8f0b2b70e", "1.12.0--r40hdfd78af_1": "sha256:802f85458103148b741ba851653b2a627dda319f9306e6d7cd05c78131fa4a90", "1.11.0--r36_0": "sha256:5d20615d747aa9e34155c74d2b56470c691f1fc7916912e0d99f11b30f0c37bc", "1.22.0--r43hdfd78af_0": "sha256:00910363589a5e235b0f681b5093ea5f7bf4297717339dfe9e103cbfb3b342ba", "1.24.0--r43hdfd78af_0": "sha256:d6dd5313715f618a8fd9b955b88fc6942936cb3454fe8cca2e6a4418635b7048", "1.28.0--r44hdfd78af_0": "sha256:6a19b770be868e58ab54035f098f17c1074f76228528066ffcc06bb634291b14"}, "docker": "quay.io/biocontainers/bioconductor-dmrscan", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmrscan.
shpc-registry automated BioContainers addition for bioconductor-dmrscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrscan:1.28.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmrscan/1.28.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dmrscan/1.28.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmrscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmrscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmrscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmrscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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