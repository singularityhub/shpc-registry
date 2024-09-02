---
layout: container
name:  "quay.io/biocontainers/whatshap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/whatshap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/whatshap/container.yaml"
updated_at: "2024-09-02 03:28:47.342259"
latest: "2.3--py38h2494328_0"
container_url: "https://biocontainers.pro/tools/whatshap"
aliases:
 - "whatshap"
 - "igzip"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "vcf_sample_filter.py"
 - "vcf_filter.py"
 - "vcf_melt"
 - "pigz"
 - "unpigz"
 - "faidx"
versions:
 - "1.5--py39hc16433a_0"
 - "2.2--py310h0dbaff4_0"
 - "2.1--py39h1f90b4d_0"
 - "2.0--py38h2494328_0"
 - "1.7--py310h0dbaff4_1"
 - "1.6--py37h96cfd12_1"
 - "2.2--py39h1f90b4d_1"
 - "2.3--py38h2494328_0"
description: "shpc-registry automated BioContainers addition for whatshap"
config: {"url": "https://biocontainers.pro/tools/whatshap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for whatshap", "latest": {"2.3--py38h2494328_0": "sha256:c967f9e48447dd95990742f7a26325349f9a678adf928117274b07d76a84adfb"}, "tags": {"1.5--py39hc16433a_0": "sha256:061a520a1dff9d31b267754fc55410c18b4d4449f66bb3f975ad95aba313d4ea", "2.2--py310h0dbaff4_0": "sha256:29def3e1bf45b97360ff8bee842cbbb489b14e6b8e366dff4d8e7ca089c2c8b7", "2.1--py39h1f90b4d_0": "sha256:c2e7b7636f672ffee7bb3c6cb80317490a54b7d13f4e6a4d401fc742b3a14c29", "2.0--py38h2494328_0": "sha256:a29366d6cb7c2d6207dfdbd852f54d93cbeb31fdfafffb059ab73aa8f6d0be84", "1.7--py310h0dbaff4_1": "sha256:06b6214a063d449372a1cb1cfc870164e9ad1666bb6d992a2c684eb6db7f2b1b", "1.6--py37h96cfd12_1": "sha256:4cc2328d99a43750f0538f67a5f8776330a38654d1c2b7b06b1dcebf19de6717", "2.2--py39h1f90b4d_1": "sha256:e425fc87bffe2e42235f34d275bc8564b3e4ae9706839d124b5577d1499e71ac", "2.3--py38h2494328_0": "sha256:c967f9e48447dd95990742f7a26325349f9a678adf928117274b07d76a84adfb"}, "docker": "quay.io/biocontainers/whatshap", "aliases": {"whatshap": "/usr/local/bin/whatshap", "igzip": "/usr/local/bin/igzip", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "vcf_sample_filter.py": "/usr/local/bin/vcf_sample_filter.py", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "faidx": "/usr/local/bin/faidx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/whatshap.
shpc-registry automated BioContainers addition for whatshap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/whatshap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/whatshap:2.3--py38h2494328_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/whatshap/2.3--py38h2494328_0
$ module help quay.io/biocontainers/whatshap/2.3--py38h2494328_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### whatshap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### whatshap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### whatshap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### whatshap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### whatshap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### whatshap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### whatshap

```bash
$ singularity exec <container> /usr/local/bin/whatshap
$ podman run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/whatshap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_sample_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_sample_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_sample_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_filter.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_melt

```bash
$ singularity exec <container> /usr/local/bin/vcf_melt
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_melt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
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