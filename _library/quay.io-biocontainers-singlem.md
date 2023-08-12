---
layout: container
name:  "quay.io/biocontainers/singlem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/singlem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/singlem/container.yaml"
updated_at: "2023-08-12 02:33:57.501455"
latest: "0.13.2--pyhdfd78af_2"
container_url: "https://biocontainers.pro/tools/singlem"
aliases:
 - "AbstractPlot.py"
 - "ExpressBetaDiversity"
 - "convertToEBD.py"
 - "convertToFullMatrix.py"
 - "faker"
 - "graftM"
 - "ktClassifyHits"
 - "ktImportHits"
 - "mfqe"
 - "orator"
 - "orfm"
 - "pcoaPlot.py"
 - "singlem"
 - "smafa"
 - "taxit"
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
 - "0.13.2--pyhdfd78af_2"
description: "shpc-registry automated BioContainers addition for singlem"
config: {"url": "https://biocontainers.pro/tools/singlem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for singlem", "latest": {"0.13.2--pyhdfd78af_2": "sha256:1c353c5f0cc33cc9db5ec18b4cd414f10f25b1bd31a9fb9764277e4c8557ff77"}, "tags": {"0.13.2--pyhdfd78af_2": "sha256:1c353c5f0cc33cc9db5ec18b4cd414f10f25b1bd31a9fb9764277e4c8557ff77"}, "docker": "quay.io/biocontainers/singlem", "aliases": {"AbstractPlot.py": "/usr/local/bin/AbstractPlot.py", "ExpressBetaDiversity": "/usr/local/bin/ExpressBetaDiversity", "convertToEBD.py": "/usr/local/bin/convertToEBD.py", "convertToFullMatrix.py": "/usr/local/bin/convertToFullMatrix.py", "faker": "/usr/local/bin/faker", "graftM": "/usr/local/bin/graftM", "ktClassifyHits": "/usr/local/bin/ktClassifyHits", "ktImportHits": "/usr/local/bin/ktImportHits", "mfqe": "/usr/local/bin/mfqe", "orator": "/usr/local/bin/orator", "orfm": "/usr/local/bin/orfm", "pcoaPlot.py": "/usr/local/bin/pcoaPlot.py", "singlem": "/usr/local/bin/singlem", "smafa": "/usr/local/bin/smafa", "taxit": "/usr/local/bin/taxit", "ktClassifyBLAST": "/usr/local/bin/ktClassifyBLAST", "ktGetContigMagnitudes": "/usr/local/bin/ktGetContigMagnitudes", "ktGetLCA": "/usr/local/bin/ktGetLCA", "ktGetLibPath": "/usr/local/bin/ktGetLibPath", "ktGetTaxIDFromAcc": "/usr/local/bin/ktGetTaxIDFromAcc", "ktGetTaxInfo": "/usr/local/bin/ktGetTaxInfo", "ktImportBLAST": "/usr/local/bin/ktImportBLAST", "ktImportDiskUsage": "/usr/local/bin/ktImportDiskUsage", "ktImportEC": "/usr/local/bin/ktImportEC", "ktImportFCP": "/usr/local/bin/ktImportFCP"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/singlem.
shpc-registry automated BioContainers addition for singlem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/singlem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/singlem:0.13.2--pyhdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/singlem/0.13.2--pyhdfd78af_2
$ module help quay.io/biocontainers/singlem/0.13.2--pyhdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### singlem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### singlem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### singlem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### singlem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### singlem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### singlem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AbstractPlot.py

```bash
$ singularity exec <container> /usr/local/bin/AbstractPlot.py
$ podman run --it --rm --entrypoint /usr/local/bin/AbstractPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AbstractPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ExpressBetaDiversity

```bash
$ singularity exec <container> /usr/local/bin/ExpressBetaDiversity
$ podman run --it --rm --entrypoint /usr/local/bin/ExpressBetaDiversity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ExpressBetaDiversity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertToEBD.py

```bash
$ singularity exec <container> /usr/local/bin/convertToEBD.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertToEBD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertToEBD.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertToFullMatrix.py

```bash
$ singularity exec <container> /usr/local/bin/convertToFullMatrix.py
$ podman run --it --rm --entrypoint /usr/local/bin/convertToFullMatrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertToFullMatrix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faker

```bash
$ singularity exec <container> /usr/local/bin/faker
$ podman run --it --rm --entrypoint /usr/local/bin/faker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graftM

```bash
$ singularity exec <container> /usr/local/bin/graftM
$ podman run --it --rm --entrypoint /usr/local/bin/graftM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graftM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktClassifyHits

```bash
$ singularity exec <container> /usr/local/bin/ktClassifyHits
$ podman run --it --rm --entrypoint /usr/local/bin/ktClassifyHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktClassifyHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ktImportHits

```bash
$ singularity exec <container> /usr/local/bin/ktImportHits
$ podman run --it --rm --entrypoint /usr/local/bin/ktImportHits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ktImportHits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfqe

```bash
$ singularity exec <container> /usr/local/bin/mfqe
$ podman run --it --rm --entrypoint /usr/local/bin/mfqe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfqe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orator

```bash
$ singularity exec <container> /usr/local/bin/orator
$ podman run --it --rm --entrypoint /usr/local/bin/orator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orfm

```bash
$ singularity exec <container> /usr/local/bin/orfm
$ podman run --it --rm --entrypoint /usr/local/bin/orfm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orfm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcoaPlot.py

```bash
$ singularity exec <container> /usr/local/bin/pcoaPlot.py
$ podman run --it --rm --entrypoint /usr/local/bin/pcoaPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcoaPlot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### singlem

```bash
$ singularity exec <container> /usr/local/bin/singlem
$ podman run --it --rm --entrypoint /usr/local/bin/singlem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/singlem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smafa

```bash
$ singularity exec <container> /usr/local/bin/smafa
$ podman run --it --rm --entrypoint /usr/local/bin/smafa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smafa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxit

```bash
$ singularity exec <container> /usr/local/bin/taxit
$ podman run --it --rm --entrypoint /usr/local/bin/taxit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxit   -v ${PWD} -w ${PWD} <container> -c " $@"
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