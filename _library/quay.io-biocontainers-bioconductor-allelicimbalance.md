---
layout: container
name:  "quay.io/biocontainers/bioconductor-allelicimbalance"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-allelicimbalance/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-allelicimbalance/container.yaml"
updated_at: "2025-04-16 03:39:17.801002"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-allelicimbalance"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-allelicimbalance"
config: {"url": "https://biocontainers.pro/tools/bioconductor-allelicimbalance", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-allelicimbalance", "latest": {"1.44.0--r44hdfd78af_0": "sha256:c1940e7d6a188c5e5813486f753d34bc784e24c605fdafe4a24fdcd96ca40398"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:3d2e793ce02b2549dcf12cb8f282d3f33cf2cdf85cdb7d48c3796c6043b791f7", "1.36.0--r42hdfd78af_0": "sha256:47585eb6f915d1b142de795a16335679eace87992c02ea1dbccc6cc48c218151", "1.38.0--r43hdfd78af_0": "sha256:a8fe5b5a777dcf5bf722cda841c827644cc9fc8ff802be4ec227556ce083a41a", "1.40.0--r43hdfd78af_0": "sha256:86682515d370eef2e8c06757fe0dc4cac16618144e5526dd01dce274c1811377", "1.44.0--r44hdfd78af_0": "sha256:c1940e7d6a188c5e5813486f753d34bc784e24c605fdafe4a24fdcd96ca40398"}, "docker": "quay.io/biocontainers/bioconductor-allelicimbalance"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-allelicimbalance.
shpc-registry automated BioContainers addition for bioconductor-allelicimbalance
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-allelicimbalance
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-allelicimbalance:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-allelicimbalance/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-allelicimbalance/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-allelicimbalance-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-allelicimbalance-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-allelicimbalance-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-allelicimbalance-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-allelicimbalance-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-allelicimbalance-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-allelicimbalance

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