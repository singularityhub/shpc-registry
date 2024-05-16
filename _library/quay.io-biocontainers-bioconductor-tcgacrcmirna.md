---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgacrcmirna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgacrcmirna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgacrcmirna/container.yaml"
updated_at: "2024-05-16 03:13:25.597554"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgacrcmirna"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
 - "c89"
 - "c99"
versions:
 - "1.9.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgacrcmirna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgacrcmirna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgacrcmirna", "latest": {"1.22.0--r43hdfd78af_0": "sha256:be574c84191520d5fac784829b83924f3c0803ba82afb9f7daae4e1f83b1be28"}, "tags": {"1.9.0--r40_0": "sha256:98ef10d7ea8887485250426095080840b73abe5651a84f91383552e12f0356fa", "1.18.0--r42hdfd78af_0": "sha256:91166f39f97095b00d0db450a0aa9cbd62418d553a2a50e872ae22272db9ed22", "1.14.0--r41hdfd78af_1": "sha256:f5ee8bf9bf83ab7b951b83ebaa58b84a73c89265dd63644b9ddb79fc990c4f58", "1.12.0--r41hdfd78af_0": "sha256:20202aa0daf0439c0543bd56c9d1762762e56e82481c2fb85d18ec7dee6a21d4", "1.10.0--r40hdfd78af_1": "sha256:fd37e9132e7497d16a44acd7108431dc5bf71a30756a809d21d9e0d1d19d453c", "1.20.0--r43hdfd78af_0": "sha256:750d9f3f6a0e54b44b6ebf67a3b4237e5944270da238db156c8773762e2d71c1", "1.22.0--r43hdfd78af_0": "sha256:be574c84191520d5fac784829b83924f3c0803ba82afb9f7daae4e1f83b1be28"}, "docker": "quay.io/biocontainers/bioconductor-tcgacrcmirna", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgacrcmirna.
shpc-registry automated BioContainers addition for bioconductor-tcgacrcmirna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgacrcmirna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgacrcmirna:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgacrcmirna/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgacrcmirna/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgacrcmirna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgacrcmirna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgacrcmirna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgacrcmirna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgacrcmirna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgacrcmirna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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