---
layout: container
name:  "quay.io/biocontainers/r-htscluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-htscluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-htscluster/container.yaml"
updated_at: "2024-02-04 03:07:06.963490"
latest: "2.0.11--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-htscluster"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.0.8--r41h3342da4_5"
 - "2.0.10--r41h3342da4_0"
 - "2.0.10--r42h3342da4_1"
 - "2.0.10--r43h3342da4_2"
 - "2.0.11--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-htscluster"
config: {"url": "https://biocontainers.pro/tools/r-htscluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-htscluster", "latest": {"2.0.11--r43h3342da4_0": "sha256:070b45336408c6dcd87f5e15582bde49afe89b824876a4bbf9d9aa3eba479fa4"}, "tags": {"2.0.8--r41h3342da4_5": "sha256:041d08fd25b3b730f6f826ade813c4a55cc0043b4166890c25f2d37aacad3301", "2.0.10--r41h3342da4_0": "sha256:e9703b64950dd2213d463ce11ddcf4299cfadabaf44839d3679c30d50cbfc1ff", "2.0.10--r42h3342da4_1": "sha256:1646e790e4c48e21911abcdec5ebaa758f72d6d601106d7f2722722c05cac7a2", "2.0.10--r43h3342da4_2": "sha256:73086ff7d407129f323bf96b019b226549112b73c235c691bf9e73a25773f3ec", "2.0.11--r43h3342da4_0": "sha256:070b45336408c6dcd87f5e15582bde49afe89b824876a4bbf9d9aa3eba479fa4"}, "docker": "quay.io/biocontainers/r-htscluster", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-htscluster.
shpc-registry automated BioContainers addition for r-htscluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-htscluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-htscluster:2.0.11--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-htscluster/2.0.11--r43h3342da4_0
$ module help quay.io/biocontainers/r-htscluster/2.0.11--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-htscluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-htscluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-htscluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-htscluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-htscluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-htscluster-inspect-deffile:

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