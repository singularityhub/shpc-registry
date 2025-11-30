---
layout: container
name:  "quay.io/biocontainers/metabinner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabinner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metabinner/container.yaml"
updated_at: "2025-11-30 03:48:22.762609"
latest: "1.4.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/metabinner"
aliases:
 - "FragGeneScan"
 - "checkm"
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "run_FragGeneScan.pl"
 - "run_metabinner.sh"
 - "rppr"
 - "guppy"
 - "pplacer"
 - "dendropy-format"
 - "sumlabels.py"
 - "sumtrees.py"
 - "prodigal"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
versions:
 - "1.4.4--hdfd78af_0"
 - "1.4.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for metabinner"
config: {"url": "https://biocontainers.pro/tools/metabinner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metabinner", "latest": {"1.4.4--hdfd78af_1": "sha256:e700129938b2f12473e00563474d56fdb6173bf8e93f401a8e75ab34a91616a2"}, "tags": {"1.4.4--hdfd78af_0": "sha256:88196b3069c92bf87c0612cf0e84eec2232b66cad0fa5cf0185579c2f9278772", "1.4.4--hdfd78af_1": "sha256:e700129938b2f12473e00563474d56fdb6173bf8e93f401a8e75ab34a91616a2"}, "docker": "quay.io/biocontainers/metabinner", "aliases": {"FragGeneScan": "/usr/local/bin/FragGeneScan", "checkm": "/usr/local/bin/checkm", "hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "run_FragGeneScan.pl": "/usr/local/bin/run_FragGeneScan.pl", "run_metabinner.sh": "/usr/local/bin/run_metabinner.sh", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "dendropy-format": "/usr/local/bin/dendropy-format", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "prodigal": "/usr/local/bin/prodigal", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabinner.
shpc-registry automated BioContainers addition for metabinner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabinner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabinner:1.4.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabinner/1.4.4--hdfd78af_1
$ module help quay.io/biocontainers/metabinner/1.4.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabinner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabinner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabinner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabinner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabinner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabinner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_FragGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_FragGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_metabinner.sh

```bash
$ singularity exec <container> /usr/local/bin/run_metabinner.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_metabinner.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_metabinner.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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