---
layout: container
name:  "quay.io/biocontainers/tigmint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tigmint/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tigmint/container.yaml"
updated_at: "2022-10-29 05:31:55.352446"
latest: "1.2.7--py39h6935b12_0"
container_url: "https://biocontainers.pro/tools/tigmint"
aliases:
 - "indexlr"
 - "lrunzip"
 - "lrzcat"
 - "lrzip"
 - "lrztar"
 - "lrzuntar"
 - "tigmint"
 - "tigmint-arcs-tsv"
 - "tigmint-cut"
 - "tigmint-make"
 - "tigmint_estimate_dist.py"
 - "tigmint_molecule.py"
 - "tigmint_molecule_paf.py"
 - "zsh"
 - "zsh-5.8"
 - "ace2sam"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "blast2sam.pl"
versions:
 - "1.2.7--py39h6935b12_0"
description: "shpc-registry automated BioContainers addition for tigmint"
config: {"url": "https://biocontainers.pro/tools/tigmint", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tigmint", "latest": {"1.2.7--py39h6935b12_0": "sha256:26b81398baad6bd7c6d14b733169a9f9f33e1c32059aed9c3e77839b452db4f2"}, "tags": {"1.2.7--py39h6935b12_0": "sha256:26b81398baad6bd7c6d14b733169a9f9f33e1c32059aed9c3e77839b452db4f2"}, "docker": "quay.io/biocontainers/tigmint", "aliases": {"indexlr": "/usr/local/bin/indexlr", "lrunzip": "/usr/local/bin/lrunzip", "lrzcat": "/usr/local/bin/lrzcat", "lrzip": "/usr/local/bin/lrzip", "lrztar": "/usr/local/bin/lrztar", "lrzuntar": "/usr/local/bin/lrzuntar", "tigmint": "/usr/local/bin/tigmint", "tigmint-arcs-tsv": "/usr/local/bin/tigmint-arcs-tsv", "tigmint-cut": "/usr/local/bin/tigmint-cut", "tigmint-make": "/usr/local/bin/tigmint-make", "tigmint_estimate_dist.py": "/usr/local/bin/tigmint_estimate_dist.py", "tigmint_molecule.py": "/usr/local/bin/tigmint_molecule.py", "tigmint_molecule_paf.py": "/usr/local/bin/tigmint_molecule_paf.py", "zsh": "/usr/local/bin/zsh", "zsh-5.8": "/usr/local/bin/zsh-5.8", "ace2sam": "/usr/local/bin/ace2sam", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tigmint.
shpc-registry automated BioContainers addition for tigmint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tigmint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tigmint:1.2.7--py39h6935b12_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tigmint/1.2.7--py39h6935b12_0
$ module help quay.io/biocontainers/tigmint/1.2.7--py39h6935b12_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tigmint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tigmint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tigmint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tigmint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tigmint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tigmint-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### indexlr

```bash
$ singularity exec <container> /usr/local/bin/indexlr
$ podman run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrunzip

```bash
$ singularity exec <container> /usr/local/bin/lrunzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzcat

```bash
$ singularity exec <container> /usr/local/bin/lrzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzip

```bash
$ singularity exec <container> /usr/local/bin/lrzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrztar

```bash
$ singularity exec <container> /usr/local/bin/lrztar
$ podman run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzuntar

```bash
$ singularity exec <container> /usr/local/bin/lrzuntar
$ podman run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint

```bash
$ singularity exec <container> /usr/local/bin/tigmint
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint-arcs-tsv

```bash
$ singularity exec <container> /usr/local/bin/tigmint-arcs-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint-arcs-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint-arcs-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint-cut

```bash
$ singularity exec <container> /usr/local/bin/tigmint-cut
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint-make

```bash
$ singularity exec <container> /usr/local/bin/tigmint-make
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint-make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint-make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint_estimate_dist.py

```bash
$ singularity exec <container> /usr/local/bin/tigmint_estimate_dist.py
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint_estimate_dist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint_estimate_dist.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint_molecule.py

```bash
$ singularity exec <container> /usr/local/bin/tigmint_molecule.py
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint_molecule.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint_molecule.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigmint_molecule_paf.py

```bash
$ singularity exec <container> /usr/local/bin/tigmint_molecule_paf.py
$ podman run --it --rm --entrypoint /usr/local/bin/tigmint_molecule_paf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigmint_molecule_paf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zsh

```bash
$ singularity exec <container> /usr/local/bin/zsh
$ podman run --it --rm --entrypoint /usr/local/bin/zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zsh-5.8

```bash
$ singularity exec <container> /usr/local/bin/zsh-5.8
$ podman run --it --rm --entrypoint /usr/local/bin/zsh-5.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zsh-5.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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