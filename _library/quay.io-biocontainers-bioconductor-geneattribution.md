---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneattribution"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneattribution/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneattribution/container.yaml"
updated_at: "2023-09-14 02:35:58.405804"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneattribution"
aliases:
 - "wget"
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
description: "shpc-registry automated BioContainers addition for bioconductor-geneattribution"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneattribution", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneattribution", "latest": {"1.26.0--r43hdfd78af_0": "sha256:05d96ef3bda0e50427ced4bd80f083474bbaee6273afaccfdaaca5abe1b7e971"}, "tags": {"1.8.0--r351_0": "sha256:5e63a9f613d40cb83d67d6d59b05c4535aa447f5d65d6abcacb2950626771fc5", "1.24.0--r42hdfd78af_0": "sha256:fbbf21853ec2a62273f86f985dfaf647cf22bb816e04d805b66ae0573c91629c", "1.20.0--r41hdfd78af_0": "sha256:72f94d0e7f55ce3d57448d064c46b3f566838055e1b95e98007c8441c38d9877", "1.18.0--r41hdfd78af_0": "sha256:62b27dd9e72427595edc20ca8e3101b5bca5665c18dae6b04547289e9197ca30", "1.16.0--r40hdfd78af_1": "sha256:ec679c09e2f9529b394a8986b03d7618489e9fa1b70bea91e6559aba8bae0458", "1.14.0--r40_0": "sha256:89d5035c470aa99883b945cd480537b3ae06242ef3640d2461487573e6c06a99", "1.26.0--r43hdfd78af_0": "sha256:05d96ef3bda0e50427ced4bd80f083474bbaee6273afaccfdaaca5abe1b7e971"}, "docker": "quay.io/biocontainers/bioconductor-geneattribution", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneattribution.
shpc-registry automated BioContainers addition for bioconductor-geneattribution
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneattribution
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneattribution:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneattribution/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneattribution/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneattribution-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneattribution-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneattribution-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneattribution-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneattribution-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneattribution-inspect-deffile:

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