---
layout: container
name:  "quay.io/biocontainers/bioconductor-gmoviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gmoviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gmoviz/container.yaml"
updated_at: "2024-07-21 03:00:20.228324"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gmoviz"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gmoviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gmoviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gmoviz", "latest": {"1.14.0--r43hdfd78af_0": "sha256:821f298d025f69180668b1b473e5f8a62c4a0eff9f4c7a292db0691eab8831d9"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:cb93eeb396319a6bd4b2871b00b41242da884b7fb78170c03d68c09b9d906c33", "1.10.0--r42hdfd78af_0": "sha256:608601c12cbb277a1b7ff87953bcefac1c20be682841cf23643b1928247da078", "1.12.0--r43hdfd78af_0": "sha256:82b7292bf47a6ab098f9a1102b7ba14bdbd072f40deb846c8791a4f3275e709a", "1.14.0--r43hdfd78af_0": "sha256:821f298d025f69180668b1b473e5f8a62c4a0eff9f4c7a292db0691eab8831d9"}, "docker": "quay.io/biocontainers/bioconductor-gmoviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gmoviz.
shpc-registry automated BioContainers addition for bioconductor-gmoviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gmoviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gmoviz:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gmoviz/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gmoviz/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gmoviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gmoviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gmoviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gmoviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gmoviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gmoviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gmoviz

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