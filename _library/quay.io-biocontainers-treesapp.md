---
layout: container
name:  "quay.io/biocontainers/treesapp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treesapp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treesapp/container.yaml"
updated_at: "2025-09-07 03:53:32.697865"
latest: "0.11.4--py39h2de1943_2"
container_url: "https://biocontainers.pro/tools/treesapp"
aliases:
 - "epa-ng"
 - "pyfastx"
 - "raxml-ng"
 - "raxml-ng-mpi"
 - "samsum"
 - "treesapp"
 - "mmseqs"
 - "FastTree-2.1.10.c"
 - "vsearch"
 - "ete3"
 - "FastTreeMP"
 - "FastTree"
 - "fasttree"
 - "gawk-5.1.0"
 - "xkbcli"
 - "aggregate_profile.pl"
versions:
 - "0.9.8--py36hf1ae8f4_0"
 - "0.11.3--py36hae55d0a_0"
 - "0.10.4--py37h22450f8_1"
 - "0.11.4--py37h96cfd12_1"
 - "0.10.4--py36hae55d0a_1"
 - "0.9.8--py37h9a982cc_0"
 - "0.11.4--py39h2de1943_2"
description: "shpc-registry automated BioContainers addition for treesapp"
config: {"url": "https://biocontainers.pro/tools/treesapp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for treesapp", "latest": {"0.11.4--py39h2de1943_2": "sha256:ff8ae704e6e788fef5c0fc7cc73a783ea9c209eb2119323f5494a44283279f0f"}, "tags": {"0.9.8--py36hf1ae8f4_0": "sha256:d63460ac608408ff1be74b44e9252bbb0b8be1922563500451cc5ae1bccc812b", "0.11.3--py36hae55d0a_0": "sha256:6ccdfc4941a609d147efdfd9bda086ce6fa4555209edde7185da6d8c68064584", "0.10.4--py37h22450f8_1": "sha256:b6182d665f7996715f3a51232a14f7f5c83f020783ddabd8f8f6692d847a831f", "0.11.4--py37h96cfd12_1": "sha256:b676af9a6f17f20ae58045c4121acdaf6119869b58e77a1407af925b50e72458", "0.10.4--py36hae55d0a_1": "sha256:88a52c6fdea2d4cebf64518b32018d6e727d885ea7145000e52529e12afc2d2b", "0.9.8--py37h9a982cc_0": "sha256:d3c60e7972bd0b4aa88ef47372b310bb170b714d69e1975fb79e888fcc0fd45c", "0.11.4--py39h2de1943_2": "sha256:ff8ae704e6e788fef5c0fc7cc73a783ea9c209eb2119323f5494a44283279f0f"}, "docker": "quay.io/biocontainers/treesapp", "aliases": {"epa-ng": "/usr/local/bin/epa-ng", "pyfastx": "/usr/local/bin/pyfastx", "raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi", "samsum": "/usr/local/bin/samsum", "treesapp": "/usr/local/bin/treesapp", "mmseqs": "/usr/local/bin/mmseqs", "FastTree-2.1.10.c": "/usr/local/bin/FastTree-2.1.10.c", "vsearch": "/usr/local/bin/vsearch", "ete3": "/usr/local/bin/ete3", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "xkbcli": "/usr/local/bin/xkbcli", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treesapp.
shpc-registry automated BioContainers addition for treesapp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treesapp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treesapp:0.11.4--py39h2de1943_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treesapp/0.11.4--py39h2de1943_2
$ module help quay.io/biocontainers/treesapp/0.11.4--py39h2de1943_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treesapp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treesapp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treesapp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treesapp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treesapp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treesapp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfastx

```bash
$ singularity exec <container> /usr/local/bin/pyfastx
$ podman run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samsum

```bash
$ singularity exec <container> /usr/local/bin/samsum
$ podman run --it --rm --entrypoint /usr/local/bin/samsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treesapp

```bash
$ singularity exec <container> /usr/local/bin/treesapp
$ podman run --it --rm --entrypoint /usr/local/bin/treesapp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treesapp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree-2.1.10.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree-2.1.10.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree-2.1.10.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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