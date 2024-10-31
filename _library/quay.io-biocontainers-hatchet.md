---
layout: container
name:  "quay.io/biocontainers/hatchet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hatchet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hatchet/container.yaml"
updated_at: "2024-10-31 00:47:58.826325"
latest: "2.0.1--py39h9e0f934_1"
container_url: "https://biocontainers.pro/tools/hatchet"
aliases:
 - "hatchet"
 - "pyomo"
 - "gff2gff.py"
 - "guess-ploidy.py"
 - "plot-roh.py"
 - "run-roh.pl"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
versions:
 - "0.4.9--py37h22450f8_0"
 - "0.4.10--py38h8c62d01_0"
 - "2.0.1--py310h0dbaff4_0"
 - "1.1.1--py38h4a32c8e_0"
 - "1.0.3--py37h96cfd12_0"
 - "0.4.14--py37h96cfd12_0"
 - "2.0.1--py39h9e0f934_1"
 - "1.0.3--py38h4a32c8e_0"
description: "shpc-registry automated BioContainers addition for hatchet"
config: {"url": "https://biocontainers.pro/tools/hatchet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hatchet", "latest": {"2.0.1--py39h9e0f934_1": "sha256:a7a962b8bb2464e05b00bca07da89f45c522db0d22b06c00454499f075f98238"}, "tags": {"0.4.9--py37h22450f8_0": "sha256:eda1508a16eed310a7fba5e2ecf8b101338f7f0cb5bc793e81fbbbe16b2ea194", "0.4.10--py38h8c62d01_0": "sha256:912ac7d7943c6297667329264ff961ae884c41957c62fc1e5ba596c84dc47362", "2.0.1--py310h0dbaff4_0": "sha256:1b81a4fbee9db03c4e370b55b70479233e0f788ccb63d46f74bac2788a89aebf", "1.1.1--py38h4a32c8e_0": "sha256:9e360a9a32e05582e302b2c3c1f0424a2f6c3ea4c774dcfd81478818cdba7278", "1.0.3--py37h96cfd12_0": "sha256:b8c8e22d78498e3bc6966831feb87914a2bd5a8fc7c9c642a27bce7950b43f14", "0.4.14--py37h96cfd12_0": "sha256:efb42c77c0e5e6f23907c1d95fe67c572c8d691d72baec7216fba0ebd696be8f", "2.0.1--py39h9e0f934_1": "sha256:a7a962b8bb2464e05b00bca07da89f45c522db0d22b06c00454499f075f98238", "1.0.3--py38h4a32c8e_0": "sha256:ce39ea66a3ed03f213812658e58f484acbb4bbf014058c534f038e11da44cd30"}, "docker": "quay.io/biocontainers/hatchet", "aliases": {"hatchet": "/usr/local/bin/hatchet", "pyomo": "/usr/local/bin/pyomo", "gff2gff.py": "/usr/local/bin/gff2gff.py", "guess-ploidy.py": "/usr/local/bin/guess-ploidy.py", "plot-roh.py": "/usr/local/bin/plot-roh.py", "run-roh.pl": "/usr/local/bin/run-roh.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hatchet.
shpc-registry automated BioContainers addition for hatchet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hatchet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hatchet:2.0.1--py39h9e0f934_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hatchet/2.0.1--py39h9e0f934_1
$ module help quay.io/biocontainers/hatchet/2.0.1--py39h9e0f934_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hatchet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hatchet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hatchet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hatchet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hatchet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hatchet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hatchet

```bash
$ singularity exec <container> /usr/local/bin/hatchet
$ podman run --it --rm --entrypoint /usr/local/bin/hatchet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hatchet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo

```bash
$ singularity exec <container> /usr/local/bin/pyomo
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess-ploidy.py

```bash
$ singularity exec <container> /usr/local/bin/guess-ploidy.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess-ploidy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-roh.py

```bash
$ singularity exec <container> /usr/local/bin/plot-roh.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-roh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-roh.pl

```bash
$ singularity exec <container> /usr/local/bin/run-roh.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-roh.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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