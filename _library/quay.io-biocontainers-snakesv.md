---
layout: container
name:  "quay.io/biocontainers/snakesv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakesv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakesv/container.yaml"
updated_at: "2024-09-12 02:58:38.818663"
latest: "0.8--py311hdfd78af_1"
container_url: "https://biocontainers.pro/tools/snakesv"
aliases:
 - "01_prepare_short_read.sh"
 - "02_download_gtf_annotation.sh"
 - "03_prepare_long_read.sh"
 - "04_download_custom_annotation.sh"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "conda2solv"
 - "dumpsolv"
 - "installcheck"
 - "mamba"
 - "mamba-package"
 - "mergesolv"
 - "repo2solv"
 - "snakeSV"
 - "testsolv"
 - "stone"
 - "conda-env"
 - "cph"
 - "plac_runner.py"
 - "yte"
 - "pulptest"
 - "gff2gff.py"
 - "cbc"
 - "clp"
 - "snakemake"
versions:
 - "0.6--hdfd78af_0"
 - "0.8--py311hdfd78af_1"
 - "0.7--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for snakesv"
config: {"url": "https://biocontainers.pro/tools/snakesv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakesv", "latest": {"0.8--py311hdfd78af_1": "sha256:52a16654d705dd9fd4acf307331153cf4607fcff284d7c319bd82d1eb2c57015"}, "tags": {"0.6--hdfd78af_0": "sha256:01604843db5dca72052dd24cafae0dd33f5c7b9099ee8f3557a324079812aa42", "0.8--py311hdfd78af_1": "sha256:52a16654d705dd9fd4acf307331153cf4607fcff284d7c319bd82d1eb2c57015", "0.7--hdfd78af_3": "sha256:e459dcd279abba7aea8b2ef57a522ca6ebec2a2768e4734f289db1a0b6c8c849"}, "docker": "quay.io/biocontainers/snakesv", "aliases": {"01_prepare_short_read.sh": "/usr/local/bin/01_prepare_short_read.sh", "02_download_gtf_annotation.sh": "/usr/local/bin/02_download_gtf_annotation.sh", "03_prepare_long_read.sh": "/usr/local/bin/03_prepare_long_read.sh", "04_download_custom_annotation.sh": "/usr/local/bin/04_download_custom_annotation.sh", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "conda2solv": "/usr/local/bin/conda2solv", "dumpsolv": "/usr/local/bin/dumpsolv", "installcheck": "/usr/local/bin/installcheck", "mamba": "/usr/local/bin/mamba", "mamba-package": "/usr/local/bin/mamba-package", "mergesolv": "/usr/local/bin/mergesolv", "repo2solv": "/usr/local/bin/repo2solv", "snakeSV": "/usr/local/bin/snakeSV", "testsolv": "/usr/local/bin/testsolv", "stone": "/usr/local/bin/stone", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "plac_runner.py": "/usr/local/bin/plac_runner.py", "yte": "/usr/local/bin/yte", "pulptest": "/usr/local/bin/pulptest", "gff2gff.py": "/usr/local/bin/gff2gff.py", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "snakemake": "/usr/local/bin/snakemake"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakesv.
shpc-registry automated BioContainers addition for snakesv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakesv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakesv:0.8--py311hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakesv/0.8--py311hdfd78af_1
$ module help quay.io/biocontainers/snakesv/0.8--py311hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakesv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakesv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakesv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakesv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakesv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakesv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 01_prepare_short_read.sh

```bash
$ singularity exec <container> /usr/local/bin/01_prepare_short_read.sh
$ podman run --it --rm --entrypoint /usr/local/bin/01_prepare_short_read.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/01_prepare_short_read.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 02_download_gtf_annotation.sh

```bash
$ singularity exec <container> /usr/local/bin/02_download_gtf_annotation.sh
$ podman run --it --rm --entrypoint /usr/local/bin/02_download_gtf_annotation.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/02_download_gtf_annotation.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 03_prepare_long_read.sh

```bash
$ singularity exec <container> /usr/local/bin/03_prepare_long_read.sh
$ podman run --it --rm --entrypoint /usr/local/bin/03_prepare_long_read.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/03_prepare_long_read.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 04_download_custom_annotation.sh

```bash
$ singularity exec <container> /usr/local/bin/04_download_custom_annotation.sh
$ podman run --it --rm --entrypoint /usr/local/bin/04_download_custom_annotation.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/04_download_custom_annotation.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### snakeSV

```bash
$ singularity exec <container> /usr/local/bin/snakeSV
$ podman run --it --rm --entrypoint /usr/local/bin/snakeSV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakeSV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsolv

```bash
$ singularity exec <container> /usr/local/bin/testsolv
$ podman run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
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