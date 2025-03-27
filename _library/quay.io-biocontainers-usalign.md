---
layout: container
name:  "quay.io/biocontainers/usalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/usalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/usalign/container.yaml"
updated_at: "2025-03-27 04:10:00.863411"
latest: "2024.07.30--h503566f_1"
container_url: "https://biocontainers.pro/tools/usalign"
aliases:
 - "HwRMSD"
 - "MMalign"
 - "NWalign"
 - "TMscore"
 - "USalign"
 - "addChainID"
 - "cif2pdb"
 - "pdb2fasta"
 - "pdb2ss"
 - "pdb2xyz"
 - "pdbAtomName"
 - "qTMclust"
 - "se"
 - "xyz_sfetch"
 - "TMalign"
versions:
 - "2024.07.30--hdbdd923_0"
 - "2024.07.30--h503566f_1"
description: "singularity registry hpc automated addition for usalign"
config: {"url": "https://biocontainers.pro/tools/usalign", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for usalign", "latest": {"2024.07.30--h503566f_1": "sha256:23c065da035f910286d66368f8f62b56c09f2ebf3a93d70209370a66133bac69"}, "tags": {"2024.07.30--hdbdd923_0": "sha256:90044c7a56a01255d5ae2ef66833ff28c3916acff2ddbfe3c8ae02b8af6787f9", "2024.07.30--h503566f_1": "sha256:23c065da035f910286d66368f8f62b56c09f2ebf3a93d70209370a66133bac69"}, "docker": "quay.io/biocontainers/usalign", "aliases": {"HwRMSD": "/usr/local/bin/HwRMSD", "MMalign": "/usr/local/bin/MMalign", "NWalign": "/usr/local/bin/NWalign", "TMscore": "/usr/local/bin/TMscore", "USalign": "/usr/local/bin/USalign", "addChainID": "/usr/local/bin/addChainID", "cif2pdb": "/usr/local/bin/cif2pdb", "pdb2fasta": "/usr/local/bin/pdb2fasta", "pdb2ss": "/usr/local/bin/pdb2ss", "pdb2xyz": "/usr/local/bin/pdb2xyz", "pdbAtomName": "/usr/local/bin/pdbAtomName", "qTMclust": "/usr/local/bin/qTMclust", "se": "/usr/local/bin/se", "xyz_sfetch": "/usr/local/bin/xyz_sfetch", "TMalign": "/usr/local/bin/TMalign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/usalign.
singularity registry hpc automated addition for usalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/usalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/usalign:2024.07.30--h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/usalign/2024.07.30--h503566f_1
$ module help quay.io/biocontainers/usalign/2024.07.30--h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### usalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### usalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### usalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### usalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### usalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### usalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HwRMSD

```bash
$ singularity exec <container> /usr/local/bin/HwRMSD
$ podman run --it --rm --entrypoint /usr/local/bin/HwRMSD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HwRMSD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MMalign

```bash
$ singularity exec <container> /usr/local/bin/MMalign
$ podman run --it --rm --entrypoint /usr/local/bin/MMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NWalign

```bash
$ singularity exec <container> /usr/local/bin/NWalign
$ podman run --it --rm --entrypoint /usr/local/bin/NWalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NWalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMscore

```bash
$ singularity exec <container> /usr/local/bin/TMscore
$ podman run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### USalign

```bash
$ singularity exec <container> /usr/local/bin/USalign
$ podman run --it --rm --entrypoint /usr/local/bin/USalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/USalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addChainID

```bash
$ singularity exec <container> /usr/local/bin/addChainID
$ podman run --it --rm --entrypoint /usr/local/bin/addChainID   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addChainID   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cif2pdb

```bash
$ singularity exec <container> /usr/local/bin/cif2pdb
$ podman run --it --rm --entrypoint /usr/local/bin/cif2pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif2pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2fasta

```bash
$ singularity exec <container> /usr/local/bin/pdb2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2ss

```bash
$ singularity exec <container> /usr/local/bin/pdb2ss
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2ss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2ss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2xyz

```bash
$ singularity exec <container> /usr/local/bin/pdb2xyz
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2xyz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2xyz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdbAtomName

```bash
$ singularity exec <container> /usr/local/bin/pdbAtomName
$ podman run --it --rm --entrypoint /usr/local/bin/pdbAtomName   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdbAtomName   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qTMclust

```bash
$ singularity exec <container> /usr/local/bin/qTMclust
$ podman run --it --rm --entrypoint /usr/local/bin/qTMclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qTMclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### se

```bash
$ singularity exec <container> /usr/local/bin/se
$ podman run --it --rm --entrypoint /usr/local/bin/se   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/se   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyz_sfetch

```bash
$ singularity exec <container> /usr/local/bin/xyz_sfetch
$ podman run --it --rm --entrypoint /usr/local/bin/xyz_sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xyz_sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
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