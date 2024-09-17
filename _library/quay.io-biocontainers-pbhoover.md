---
layout: container
name:  "quay.io/biocontainers/pbhoover"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbhoover/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbhoover/container.yaml"
updated_at: "2024-09-17 02:53:57.251985"
latest: "1.1.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/pbhoover"
aliases:
 - "bash5tools.py"
 - "cmph5tools.py"
 - "dataset.py"
 - "pbhoover"
 - "vcf_filter.py"
 - "vcf_melt"
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
versions:
 - "1.0.7--pyhdfd78af_5"
 - "1.1.0--pyhdfd78af_0"
 - "1.1.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for pbhoover"
config: {"url": "https://biocontainers.pro/tools/pbhoover", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbhoover", "latest": {"1.1.0--pyhdfd78af_1": "sha256:aa22e678a49e0319085222ea724d98bc79047dbd079c6a28006bdeb3e366c38b"}, "tags": {"1.0.7--pyhdfd78af_5": "sha256:b8dab21318b8bd2a78b5f8e948cdb53b007e5a73801bd6f2fde7f8294eed4143", "1.1.0--pyhdfd78af_0": "sha256:37373e162ef9f18757a04ac456a53d1b88a26d31b2e25164418d174f3a248e12", "1.1.0--pyhdfd78af_1": "sha256:aa22e678a49e0319085222ea724d98bc79047dbd079c6a28006bdeb3e366c38b"}, "docker": "quay.io/biocontainers/pbhoover", "aliases": {"bash5tools.py": "/usr/local/bin/bash5tools.py", "cmph5tools.py": "/usr/local/bin/cmph5tools.py", "dataset.py": "/usr/local/bin/dataset.py", "pbhoover": "/usr/local/bin/pbhoover", "vcf_filter.py": "/usr/local/bin/vcf_filter.py", "vcf_melt": "/usr/local/bin/vcf_melt", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbhoover.
shpc-registry automated BioContainers addition for pbhoover
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbhoover
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbhoover:1.1.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbhoover/1.1.0--pyhdfd78af_1
$ module help quay.io/biocontainers/pbhoover/1.1.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbhoover-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbhoover-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbhoover-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbhoover-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbhoover-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbhoover-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bash5tools.py

```bash
$ singularity exec <container> /usr/local/bin/bash5tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/bash5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmph5tools.py

```bash
$ singularity exec <container> /usr/local/bin/cmph5tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/cmph5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmph5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataset.py

```bash
$ singularity exec <container> /usr/local/bin/dataset.py
$ podman run --it --rm --entrypoint /usr/local/bin/dataset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataset.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbhoover

```bash
$ singularity exec <container> /usr/local/bin/pbhoover
$ podman run --it --rm --entrypoint /usr/local/bin/pbhoover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbhoover   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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