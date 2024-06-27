---
layout: container
name:  "quay.io/biocontainers/bioconductor-lumihumanall.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lumihumanall.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lumihumanall.db/container.yaml"
updated_at: "2024-06-27 03:50:25.315071"
latest: "1.22.0--r43hdfd78af_15"
container_url: "https://biocontainers.pro/tools/bioconductor-lumihumanall.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.22.0--r40hdfd78af_9"
 - "1.22.0--r42hdfd78af_13"
 - "1.22.0--r43hdfd78af_14"
 - "1.22.0--r43hdfd78af_15"
description: "shpc-registry automated BioContainers addition for bioconductor-lumihumanall.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lumihumanall.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lumihumanall.db", "latest": {"1.22.0--r43hdfd78af_15": "sha256:8f6c34b0113df77ae1555272375c7df8acf5cc4a722f0f6c1207b6aeafbdd801"}, "tags": {"1.22.0--r40hdfd78af_9": "sha256:79526cd106a5a71ef3bc28b8ab595f007600aff88ce163e33cfaa1862174648e", "1.22.0--r42hdfd78af_13": "sha256:2a99ed6f030d0fdb0891fa6da2eb55e3509dc5f027ad3c182bdd36e24370ff19", "1.22.0--r43hdfd78af_14": "sha256:df4e8fc5aa3feae5c3e20c69f9e8b7739f0949d15cdf3f2b118afe514610917d", "1.22.0--r43hdfd78af_15": "sha256:8f6c34b0113df77ae1555272375c7df8acf5cc4a722f0f6c1207b6aeafbdd801"}, "docker": "quay.io/biocontainers/bioconductor-lumihumanall.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lumihumanall.db.
shpc-registry automated BioContainers addition for bioconductor-lumihumanall.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lumihumanall.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lumihumanall.db:1.22.0--r43hdfd78af_15
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lumihumanall.db/1.22.0--r43hdfd78af_15
$ module help quay.io/biocontainers/bioconductor-lumihumanall.db/1.22.0--r43hdfd78af_15
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lumihumanall.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumihumanall.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumihumanall.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lumihumanall.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lumihumanall.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lumihumanall.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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