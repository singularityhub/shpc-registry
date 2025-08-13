---
layout: container
name:  "quay.io/biocontainers/bioconductor-moonlightr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moonlightr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moonlightr/container.yaml"
updated_at: "2025-08-13 04:06:53.233960"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-moonlightr"

versions:
 - "1.8.0--r351_0"
 - "1.19.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.12.0--r36_0"
 - "1.10.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-moonlightr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moonlightr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moonlightr", "latest": {"1.32.0--r44hdfd78af_0": "sha256:83dfdadb440a17113ee835095afad21365bd332ac89caf8b89ebef2d7eda0c7c"}, "tags": {"1.8.0--r351_0": "sha256:fd02047de207346fb45daea2938f61d485c59bc989eec6ec157f1411f507936f", "1.19.0--r41hdfd78af_0": "sha256:adc02064233fc4b18541b8112a9600e618f55fffb6c4c4dbb21f79cda3864830", "1.18.0--r41hdfd78af_0": "sha256:9d6e280f4b2fd475c1958abc65accb28daa4ed9eacae74ff0e916c4a902d3fc5", "1.16.0--r40hdfd78af_1": "sha256:8e4e830e1e67ab0be4cd284e9936d34296cfd434d4eb78329611b15c65b585d7", "1.12.0--r36_0": "sha256:e3b8cc58aeefbf6bad1dea7c639ca7ac1a388d2d6fc36cbb3a21df6898336e7f", "1.10.0--r36_0": "sha256:afcf210db94d6d5721b729292928c90928047e78982e29a2d6b423f334394053", "1.24.0--r42hdfd78af_0": "sha256:ec84fdc322346eac64d0e15135067d7d7dae2d8a0a431833efbc06907e460bdc", "1.26.0--r43hdfd78af_0": "sha256:cf6fcf391b6884c45da375996bdb4644196f35fd4f1e3b01053ea79b7fd675d4", "1.28.0--r43hdfd78af_0": "sha256:4804683f5edc760a005cf2673a7336e9373ac45391a58bc6779bd526be60cb27", "1.32.0--r44hdfd78af_0": "sha256:83dfdadb440a17113ee835095afad21365bd332ac89caf8b89ebef2d7eda0c7c"}, "docker": "quay.io/biocontainers/bioconductor-moonlightr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moonlightr.
shpc-registry automated BioContainers addition for bioconductor-moonlightr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moonlightr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moonlightr:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moonlightr/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-moonlightr/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moonlightr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moonlightr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moonlightr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moonlightr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moonlightr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moonlightr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moonlightr

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