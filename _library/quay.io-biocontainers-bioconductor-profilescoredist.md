---
layout: container
name:  "quay.io/biocontainers/bioconductor-profilescoredist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-profilescoredist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-profilescoredist/container.yaml"
updated_at: "2024-02-01 03:38:55.023780"
latest: "1.30.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-profilescoredist"

versions:
 - "1.22.0--r41hc247a5b_2"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-profilescoredist"
config: {"url": "https://biocontainers.pro/tools/bioconductor-profilescoredist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-profilescoredist", "latest": {"1.30.0--r43hf17093f_0": "sha256:f3e45ef484709b7d9661e3e03e15391502ed8c32e762b5d8b7a1d28320fda8d7"}, "tags": {"1.22.0--r41hc247a5b_2": "sha256:9b61066b22ad81ec823e1bc8f5cdff4cca3a5bd34ca014bbb6d7a63dc7d7d7e7", "1.26.0--r42hc247a5b_0": "sha256:93766fef9b35432a1ab447498fbe061a7de6835abc5a24632f06a18744289e05", "1.26.0--r42hf17093f_1": "sha256:4a1248cb819971f7a76997c366b4b51321a6a2501188822593e20a2fabbe0490", "1.28.0--r43hf17093f_0": "sha256:f45472328a846bad705c0048e2f63bde36af47d2d47b9af4bc27a5f6ef51511b", "1.30.0--r43hf17093f_0": "sha256:f3e45ef484709b7d9661e3e03e15391502ed8c32e762b5d8b7a1d28320fda8d7"}, "docker": "quay.io/biocontainers/bioconductor-profilescoredist"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-profilescoredist.
shpc-registry automated BioContainers addition for bioconductor-profilescoredist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-profilescoredist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-profilescoredist:1.30.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-profilescoredist/1.30.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-profilescoredist/1.30.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-profilescoredist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-profilescoredist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-profilescoredist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-profilescoredist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-profilescoredist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-profilescoredist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-profilescoredist

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