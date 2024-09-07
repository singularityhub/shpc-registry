---
layout: container
name:  "quay.io/biocontainers/bioconductor-multidataset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multidataset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multidataset/container.yaml"
updated_at: "2024-09-07 02:58:18.534829"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multidataset"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.1--r40hdfd78af_0"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multidataset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multidataset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multidataset", "latest": {"1.30.0--r43hdfd78af_0": "sha256:f121cea0a83163f35991b41458e63ba846e08ee4417d825a45107f39566198cc"}, "tags": {"1.8.0--r351_0": "sha256:4b7388e0e490d0cb8ca638118c6744149ebb246c6f0582673e619de38421c650", "1.26.0--r42hdfd78af_0": "sha256:7a8a3a47db80cc1f91187cc72d9cebd476676915a39a1d8f4953c5ae0df3c5f8", "1.22.0--r41hdfd78af_0": "sha256:0c75788c65628bafcc321d670c0f5346ee93d664ac1c77a6947b44d7416d1305", "1.20.0--r41hdfd78af_0": "sha256:236c379549368b10b290e1f21bf7b3f571a907c15552470eca0b413f1b689217", "1.18.1--r40hdfd78af_0": "sha256:6e72c98e5416c2fadccccbff4b61c26b857589a90bd53fea14cef6e19cb2c476", "1.16.0--r40_0": "sha256:fdfa9a26ba5bce6966273dc2eea7f3dd3a24acfc82b3300d21543d3ff2ba3107", "1.28.0--r43hdfd78af_0": "sha256:d53f1741d4d98fb1d2c26f9791ebc5f440c49205348a4bfe65c64220650bb8c7", "1.30.0--r43hdfd78af_0": "sha256:f121cea0a83163f35991b41458e63ba846e08ee4417d825a45107f39566198cc"}, "docker": "quay.io/biocontainers/bioconductor-multidataset", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multidataset.
shpc-registry automated BioContainers addition for bioconductor-multidataset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multidataset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multidataset:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multidataset/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multidataset/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multidataset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multidataset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multidataset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multidataset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multidataset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multidataset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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