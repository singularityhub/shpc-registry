---
layout: container
name:  "quay.io/biocontainers/metagenome-atlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metagenome-atlas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metagenome-atlas/container.yaml"
updated_at: "2023-09-08 02:53:40.507324"
latest: "2.17.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metagenome-atlas"
aliases:
 - "atlas"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "conda2solv"
 - "cookiecutter"
 - "dumpsolv"
 - "installcheck"
 - "mamba"
 - "mamba-package"
 - "mergesolv"
 - "repo2solv"
 - "slugify"
 - "testsolv"
 - "kmutate.sh"
 - "runhmm.sh"
 - "conda-env"
 - "cph"
 - "plac_runner.py"
 - "yte"
 - "kmerposition.sh"
 - "reformatpb.sh"
 - "summarizecoverage.sh"
 - "alltoall.sh"
versions:
 - "2.9.1--pyhdfd78af_0"
 - "2.12.0--pyhdfd78af_1"
 - "2.11.1--pyhdfd78af_0"
 - "2.10.0--pyhdfd78af_0"
 - "2.13.1--pyhdfd78af_0"
 - "2.14.0--pyhdfd78af_0"
 - "2.14.3--pyhdfd78af_0"
 - "2.15.0--pyhdfd78af_0"
 - "2.15.2--pyhdfd78af_0"
 - "2.16.3--pyhdfd78af_0"
 - "2.17.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for metagenome-atlas"
config: {"url": "https://biocontainers.pro/tools/metagenome-atlas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metagenome-atlas", "latest": {"2.17.0--pyhdfd78af_0": "sha256:eedd9e6e4b09480281ef5179f324ada159e0c1b872b3ff592d30ed493114346e"}, "tags": {"2.9.1--pyhdfd78af_0": "sha256:5b24ec8e8747ee48f0b7f8b690d574e026617895f4ebd37e777878634885faca", "2.12.0--pyhdfd78af_1": "sha256:b28317b771a5563b11d20d6ee9b9885794a1aa8f4e6f66af4b09b570bf304342", "2.11.1--pyhdfd78af_0": "sha256:21b22a444df2001b23654a7a2f01d6efee816cfe297e2541f1b57e6897a61e71", "2.10.0--pyhdfd78af_0": "sha256:05cc984118d2f7df96504005260e8e40ae6384c7845e559217f9523c499ce08c", "2.13.1--pyhdfd78af_0": "sha256:a62a7f67d699fc81870b1cfbdee0b396ec6d20ffafdc1891d1ed15a2f7d6fe27", "2.14.0--pyhdfd78af_0": "sha256:a2c5fcc2cb6ad66dac2b2f10076d5b20eb20498e07ef1ceafd7d795e1c2a3471", "2.14.3--pyhdfd78af_0": "sha256:acedf5c417d42fbb2c311130781da9ea3003d6a2cca27afdcf182aa5dabfe006", "2.15.0--pyhdfd78af_0": "sha256:96911626f4f8d15d37a0d78d402fba23bece7c1b69ea4a26828e154d0a70db7d", "2.15.2--pyhdfd78af_0": "sha256:ea1de8f5f5979c32d18c3f8f6ace8210b5aafaea0fa3c218e076ac0ee3a5c368", "2.16.3--pyhdfd78af_0": "sha256:373e8a15e5f20dec380df2bf6989648ff6e4104fea189a8d373d93c7c376f9fe", "2.17.0--pyhdfd78af_0": "sha256:eedd9e6e4b09480281ef5179f324ada159e0c1b872b3ff592d30ed493114346e"}, "docker": "quay.io/biocontainers/metagenome-atlas", "aliases": {"atlas": "/usr/local/bin/atlas", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "conda2solv": "/usr/local/bin/conda2solv", "cookiecutter": "/usr/local/bin/cookiecutter", "dumpsolv": "/usr/local/bin/dumpsolv", "installcheck": "/usr/local/bin/installcheck", "mamba": "/usr/local/bin/mamba", "mamba-package": "/usr/local/bin/mamba-package", "mergesolv": "/usr/local/bin/mergesolv", "repo2solv": "/usr/local/bin/repo2solv", "slugify": "/usr/local/bin/slugify", "testsolv": "/usr/local/bin/testsolv", "kmutate.sh": "/usr/local/bin/kmutate.sh", "runhmm.sh": "/usr/local/bin/runhmm.sh", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "kmerposition.sh": "/usr/local/bin/kmerposition.sh", "reformatpb.sh": "/usr/local/bin/reformatpb.sh", "summarizecoverage.sh": "/usr/local/bin/summarizecoverage.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metagenome-atlas.
shpc-registry automated BioContainers addition for metagenome-atlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metagenome-atlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metagenome-atlas:2.17.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metagenome-atlas/2.17.0--pyhdfd78af_0
$ module help quay.io/biocontainers/metagenome-atlas/2.17.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metagenome-atlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metagenome-atlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metagenome-atlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metagenome-atlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metagenome-atlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metagenome-atlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atlas

```bash
$ singularity exec <container> /usr/local/bin/atlas
$ podman run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda2solv

```bash
$ singularity exec <container> /usr/local/bin/conda2solv
$ podman run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsolv

```bash
$ singularity exec <container> /usr/local/bin/dumpsolv
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installcheck

```bash
$ singularity exec <container> /usr/local/bin/installcheck
$ podman run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba

```bash
$ singularity exec <container> /usr/local/bin/mamba
$ podman run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergesolv

```bash
$ singularity exec <container> /usr/local/bin/mergesolv
$ podman run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repo2solv

```bash
$ singularity exec <container> /usr/local/bin/repo2solv
$ podman run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsolv

```bash
$ singularity exec <container> /usr/local/bin/testsolv
$ podman run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmutate.sh

```bash
$ singularity exec <container> /usr/local/bin/kmutate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmutate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runhmm.sh

```bash
$ singularity exec <container> /usr/local/bin/runhmm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runhmm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plac_runner.py

```bash
$ singularity exec <container> /usr/local/bin/plac_runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plac_runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yte

```bash
$ singularity exec <container> /usr/local/bin/yte
$ podman run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmerposition.sh

```bash
$ singularity exec <container> /usr/local/bin/kmerposition.sh
$ podman run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmerposition.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformatpb.sh

```bash
$ singularity exec <container> /usr/local/bin/reformatpb.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformatpb.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### summarizecoverage.sh

```bash
$ singularity exec <container> /usr/local/bin/summarizecoverage.sh
$ podman run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/summarizecoverage.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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