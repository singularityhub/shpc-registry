---
layout: container
name:  "quay.io/biocontainers/bioconductor-esetvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-esetvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-esetvis/container.yaml"
updated_at: "2024-09-02 04:38:13.974661"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-esetvis"
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
 - "1.26.1--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-esetvis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-esetvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-esetvis", "latest": {"1.28.0--r43hdfd78af_0": "sha256:1bc205d3eb99d5506b6742b3beb260eecb0e06ac31c0ecba0aca1e57b31bcdaf"}, "tags": {"1.8.0--r351_0": "sha256:f0a1620096bdc2593a6b85192a698a00e2bbfcd814504b90b9cd281fd757f2c0", "1.24.0--r42hdfd78af_0": "sha256:a3c231543aab0e2bf9c3d6eb3f0d5de999a5b4d853f955da32e48edf9bcc8b54", "1.20.0--r41hdfd78af_0": "sha256:7a5d77325610e44b75bcbf3249372f87b5fa8629528fafb396836e9a1213d8cb", "1.18.0--r41hdfd78af_0": "sha256:ab7c9c69de761abdcf1cb6ee6d66865df2ae08872d0121abf9b6c593bff17079", "1.16.0--r40hdfd78af_1": "sha256:a1362db86965356815ce5a8ce23d339dbdd208ec36e7b5bf9c840de297f02430", "1.14.0--r40_0": "sha256:c48f598e0ad1ecd9bf9dca5967b678ba4077765e5efdfcb339d97362720fe47a", "1.26.1--r43hdfd78af_0": "sha256:6d1f60c3f3940342b815477ddf7f1b2943900cdd9df9d4d9ebd24a9ce1aaa187", "1.28.0--r43hdfd78af_0": "sha256:1bc205d3eb99d5506b6742b3beb260eecb0e06ac31c0ecba0aca1e57b31bcdaf"}, "docker": "quay.io/biocontainers/bioconductor-esetvis", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-esetvis.
shpc-registry automated BioContainers addition for bioconductor-esetvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-esetvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-esetvis:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-esetvis/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-esetvis/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-esetvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-esetvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-esetvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-esetvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-esetvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-esetvis-inspect-deffile:

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