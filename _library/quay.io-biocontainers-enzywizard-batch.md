---
layout: container
name:  "quay.io/biocontainers/enzywizard-batch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enzywizard-batch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enzywizard-batch/container.yaml"
updated_at: "2026-06-28 06:52:31.854531"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/enzywizard-batch"
aliases:
 - "enzywizard-batch"
 - "evol"
 - "gemmi"
 - "mk_export.py"
 - "mk_prepare_ligand.py"
 - "mk_prepare_receptor.py"
 - "mkdssp"
 - "msms"
 - "pdbfixer"
 - "prody"
 - "pyvol"
 - "rdhc"
 - "trimesh"
 - "vina"
 - "vina_split"
 - "fc-genconf"
 - "protoc-28.3.0"
 - "idna"
 - "xxh3sum"
 - "cllayerinfo"
 - "torchfrtrace"
 - "pybind11-config"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
 - "ldapvc"
 - "ldapwhoami"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "torch_shm_manager"
 - "torchrun"
 - "isympy"
versions:
 - "1.0.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for enzywizard-batch"
config: {"url": "https://biocontainers.pro/tools/enzywizard-batch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for enzywizard-batch", "latest": {"1.0.2--pyhdfd78af_0": "sha256:07abf69b90b4f9edb451e743e32c7962933de1fb46b9eb8199f06e585b119e68"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:07abf69b90b4f9edb451e743e32c7962933de1fb46b9eb8199f06e585b119e68"}, "docker": "quay.io/biocontainers/enzywizard-batch", "aliases": {"enzywizard-batch": "/usr/local/bin/enzywizard-batch", "evol": "/usr/local/bin/evol", "gemmi": "/usr/local/bin/gemmi", "mk_export.py": "/usr/local/bin/mk_export.py", "mk_prepare_ligand.py": "/usr/local/bin/mk_prepare_ligand.py", "mk_prepare_receptor.py": "/usr/local/bin/mk_prepare_receptor.py", "mkdssp": "/usr/local/bin/mkdssp", "msms": "/usr/local/bin/msms", "pdbfixer": "/usr/local/bin/pdbfixer", "prody": "/usr/local/bin/prody", "pyvol": "/usr/local/bin/pyvol", "rdhc": "/usr/local/bin/rdhc", "trimesh": "/usr/local/bin/trimesh", "vina": "/usr/local/bin/vina", "vina_split": "/usr/local/bin/vina_split", "fc-genconf": "/usr/local/bin/fc-genconf", "protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "idna": "/usr/local/bin/idna", "xxh3sum": "/usr/local/bin/xxh3sum", "cllayerinfo": "/usr/local/bin/cllayerinfo", "torchfrtrace": "/usr/local/bin/torchfrtrace", "pybind11-config": "/usr/local/bin/pybind11-config", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "torchrun": "/usr/local/bin/torchrun", "isympy": "/usr/local/bin/isympy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enzywizard-batch.
singularity registry hpc automated addition for enzywizard-batch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enzywizard-batch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enzywizard-batch:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enzywizard-batch/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/enzywizard-batch/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enzywizard-batch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enzywizard-batch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enzywizard-batch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enzywizard-batch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enzywizard-batch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enzywizard-batch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### enzywizard-batch

```bash
$ singularity exec <container> /usr/local/bin/enzywizard-batch
$ podman run --it --rm --entrypoint /usr/local/bin/enzywizard-batch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enzywizard-batch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evol

```bash
$ singularity exec <container> /usr/local/bin/evol
$ podman run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gemmi

```bash
$ singularity exec <container> /usr/local/bin/gemmi
$ podman run --it --rm --entrypoint /usr/local/bin/gemmi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gemmi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mk_export.py

```bash
$ singularity exec <container> /usr/local/bin/mk_export.py
$ podman run --it --rm --entrypoint /usr/local/bin/mk_export.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mk_export.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mk_prepare_ligand.py

```bash
$ singularity exec <container> /usr/local/bin/mk_prepare_ligand.py
$ podman run --it --rm --entrypoint /usr/local/bin/mk_prepare_ligand.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mk_prepare_ligand.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mk_prepare_receptor.py

```bash
$ singularity exec <container> /usr/local/bin/mk_prepare_receptor.py
$ podman run --it --rm --entrypoint /usr/local/bin/mk_prepare_receptor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mk_prepare_receptor.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkdssp

```bash
$ singularity exec <container> /usr/local/bin/mkdssp
$ podman run --it --rm --entrypoint /usr/local/bin/mkdssp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkdssp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msms

```bash
$ singularity exec <container> /usr/local/bin/msms
$ podman run --it --rm --entrypoint /usr/local/bin/msms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdbfixer

```bash
$ singularity exec <container> /usr/local/bin/pdbfixer
$ podman run --it --rm --entrypoint /usr/local/bin/pdbfixer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdbfixer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prody

```bash
$ singularity exec <container> /usr/local/bin/prody
$ podman run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvol

```bash
$ singularity exec <container> /usr/local/bin/pyvol
$ podman run --it --rm --entrypoint /usr/local/bin/pyvol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdhc

```bash
$ singularity exec <container> /usr/local/bin/rdhc
$ podman run --it --rm --entrypoint /usr/local/bin/rdhc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdhc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimesh

```bash
$ singularity exec <container> /usr/local/bin/trimesh
$ podman run --it --rm --entrypoint /usr/local/bin/trimesh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimesh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina

```bash
$ singularity exec <container> /usr/local/bin/vina
$ podman run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina_split

```bash
$ singularity exec <container> /usr/local/bin/vina_split
$ podman run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cllayerinfo

```bash
$ singularity exec <container> /usr/local/bin/cllayerinfo
$ podman run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cllayerinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapvc

```bash
$ singularity exec <container> /usr/local/bin/ldapvc
$ podman run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapwhoami

```bash
$ singularity exec <container> /usr/local/bin/ldapwhoami
$ podman run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh128sum

```bash
$ singularity exec <container> /usr/local/bin/xxh128sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh32sum

```bash
$ singularity exec <container> /usr/local/bin/xxh32sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh64sum

```bash
$ singularity exec <container> /usr/local/bin/xxh64sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
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