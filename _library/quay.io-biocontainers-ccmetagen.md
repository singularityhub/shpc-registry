---
layout: container
name:  "quay.io/biocontainers/ccmetagen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ccmetagen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ccmetagen/container.yaml"
updated_at: "2025-01-02 03:31:26.589291"
latest: "1.5.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/ccmetagen"
aliases:
 - "CCMetagen.py"
 - "CCMetagen_extract_seqs.py"
 - "CCMetagen_merge.py"
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "ktClassifyBLAST"
 - "ktGetContigMagnitudes"
 - "ktGetLCA"
 - "ktGetLibPath"
 - "ktGetTaxIDFromAcc"
 - "ktGetTaxInfo"
 - "ktImportBLAST"
 - "ktImportDiskUsage"
 - "ktImportEC"
 - "ktImportFCP"
versions:
 - "1.4.0--pyh5e36f6f_0"
 - "1.4.1--pyh7cba7a3_0"
 - "1.4.2--pyh7cba7a3_0"
 - "1.4.2--pyh7cba7a3_1"
 - "1.5.0--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for ccmetagen"
config: {"url": "https://biocontainers.pro/tools/ccmetagen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ccmetagen", "latest": {"1.5.0--pyh7cba7a3_0": "sha256:e3d8cff0e5374c6c984f456efe3db428ad254f24035ee188ae8f2ae74a1bdfd0"}, "tags": {"1.4.0--pyh5e36f6f_0": "sha256:32a2c8f007b83e50e3e428683eabf083623dd33f7bef88c61f811dc777c9cdb1", "1.4.1--pyh7cba7a3_0": "sha256:c081a10240769c3708ffc23dc7a355256455324b8e8c2d90f7b28038662974db", "1.4.2--pyh7cba7a3_0": "sha256:8da4b817b29e7e45615815a43b59da9b76769c0d8dd2165e7ad0b78599d5b6cb", "1.4.2--pyh7cba7a3_1": "sha256:fdd0cccf15cf596b7d671da945428e04aa291640483e633c15e6958242b91594", "1.5.0--pyh7cba7a3_0": "sha256:e3d8cff0e5374c6c984f456efe3db428ad254f24035ee188ae8f2ae74a1bdfd0"}, "docker": "quay.io/biocontainers/ccmetagen", "aliases": {"CCMetagen.py": "/usr/local/bin/CCMetagen.py", "CCMetagen_extract_seqs.py": "/usr/local/bin/CCMetagen_extract_seqs.py", "CCMetagen_merge.py": "/usr/local/bin/CCMetagen_merge.py", "kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "ktClassifyBLAST": "/usr/local/bin/ktClassifyBLAST", "ktGetContigMagnitudes": "/usr/local/bin/ktGetContigMagnitudes", "ktGetLCA": "/usr/local/bin/ktGetLCA", "ktGetLibPath": "/usr/local/bin/ktGetLibPath", "ktGetTaxIDFromAcc": "/usr/local/bin/ktGetTaxIDFromAcc", "ktGetTaxInfo": "/usr/local/bin/ktGetTaxInfo", "ktImportBLAST": "/usr/local/bin/ktImportBLAST", "ktImportDiskUsage": "/usr/local/bin/ktImportDiskUsage", "ktImportEC": "/usr/local/bin/ktImportEC", "ktImportFCP": "/usr/local/bin/ktImportFCP"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ccmetagen.
shpc-registry automated BioContainers addition for ccmetagen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ccmetagen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ccmetagen:1.5.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ccmetagen/1.5.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/ccmetagen/1.5.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ccmetagen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ccmetagen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ccmetagen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ccmetagen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ccmetagen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ccmetagen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CCMetagen.py

```bash
$ singularity exec <container> /usr/local/bin/CCMetagen.py
$ podman run --it --rm --entrypoint /usr/local/bin/CCMetagen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCMetagen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CCMetagen_extract_seqs.py

```bash
$ singularity exec <container> /usr/local/bin/CCMetagen_extract_seqs.py
$ podman run --it --rm --entrypoint /usr/local/bin/CCMetagen_extract_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCMetagen_extract_seqs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CCMetagen_merge.py

```bash
$ singularity exec <container> /usr/local/bin/CCMetagen_merge.py
$ podman run --it --rm --entrypoint /usr/local/bin/CCMetagen_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CCMetagen_merge.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktClassifyBLAST

```bash
$ singularity exec <container> /usr/local/bin/ktClassifyBLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktClassifyBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktClassifyBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetContigMagnitudes

```bash
$ singularity exec <container> /usr/local/bin/ktGetContigMagnitudes
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetContigMagnitudes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetContigMagnitudes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetLCA

```bash
$ singularity exec <container> /usr/local/bin/ktGetLCA
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetLibPath

```bash
$ singularity exec <container> /usr/local/bin/ktGetLibPath
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetLibPath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetLibPath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetTaxIDFromAcc

```bash
$ singularity exec <container> /usr/local/bin/ktGetTaxIDFromAcc
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetTaxIDFromAcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetTaxIDFromAcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktGetTaxInfo

```bash
$ singularity exec <container> /usr/local/bin/ktGetTaxInfo
$ podman run --it --rm --entrypoint /usr/local/bin/ktGetTaxInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktGetTaxInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportBLAST

```bash
$ singularity exec <container> /usr/local/bin/ktImportBLAST
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportBLAST   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportDiskUsage

```bash
$ singularity exec <container> /usr/local/bin/ktImportDiskUsage
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportDiskUsage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportDiskUsage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportEC

```bash
$ singularity exec <container> /usr/local/bin/ktImportEC
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportEC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportEC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportFCP

```bash
$ singularity exec <container> /usr/local/bin/ktImportFCP
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportFCP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportFCP   -v ${PWD} -w ${PWD} <container> -c " $@"
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