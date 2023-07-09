---
layout: container
name:  "quay.io/biocontainers/bicseq2-norm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bicseq2-norm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bicseq2-norm/container.yaml"
updated_at: "2023-07-09 03:40:29.314172"
latest: "0.2.4--h031d066_5"
container_url: "https://biocontainers.pro/tools/bicseq2-norm"
aliases:
 - "BRS"
 - "NBICseq-norm.pl"
 - "PrepPois"
 - "PrepPoisGAM"
 - "combineFile"
 - "compRatio.R"
 - "filterCNV"
 - "normalize.R"
 - "normalizeGAM.R"
 - "plot_RC_vs_GC.R"
 - "purity.R"
 - "purityEM"
 - "random_split"
 - "refine.R"
 - "refineGAM.R"
 - "test.mgcv.installed.R"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.2.4--hec16e2b_3"
 - "0.2.4--h031d066_5"
description: "shpc-registry automated BioContainers addition for bicseq2-norm"
config: {"url": "https://biocontainers.pro/tools/bicseq2-norm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bicseq2-norm", "latest": {"0.2.4--h031d066_5": "sha256:75786d1047ef7d017ab6bb3ff85c1c45786c501d3a7784b25b05e0cecfd590a2"}, "tags": {"0.2.4--hec16e2b_3": "sha256:22484736ee5178b8ac49817330a0af73934a13a2cecb1ddbb66839007fe2dc65", "0.2.4--h031d066_5": "sha256:75786d1047ef7d017ab6bb3ff85c1c45786c501d3a7784b25b05e0cecfd590a2"}, "docker": "quay.io/biocontainers/bicseq2-norm", "aliases": {"BRS": "/usr/local/bin/BRS", "NBICseq-norm.pl": "/usr/local/bin/NBICseq-norm.pl", "PrepPois": "/usr/local/bin/PrepPois", "PrepPoisGAM": "/usr/local/bin/PrepPoisGAM", "combineFile": "/usr/local/bin/combineFile", "compRatio.R": "/usr/local/bin/compRatio.R", "filterCNV": "/usr/local/bin/filterCNV", "normalize.R": "/usr/local/bin/normalize.R", "normalizeGAM.R": "/usr/local/bin/normalizeGAM.R", "plot_RC_vs_GC.R": "/usr/local/bin/plot_RC_vs_GC.R", "purity.R": "/usr/local/bin/purity.R", "purityEM": "/usr/local/bin/purityEM", "random_split": "/usr/local/bin/random_split", "refine.R": "/usr/local/bin/refine.R", "refineGAM.R": "/usr/local/bin/refineGAM.R", "test.mgcv.installed.R": "/usr/local/bin/test.mgcv.installed.R", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bicseq2-norm.
shpc-registry automated BioContainers addition for bicseq2-norm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bicseq2-norm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bicseq2-norm:0.2.4--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bicseq2-norm/0.2.4--h031d066_5
$ module help quay.io/biocontainers/bicseq2-norm/0.2.4--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bicseq2-norm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bicseq2-norm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bicseq2-norm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bicseq2-norm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bicseq2-norm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bicseq2-norm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BRS

```bash
$ singularity exec <container> /usr/local/bin/BRS
$ podman run --it --rm --entrypoint /usr/local/bin/BRS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BRS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NBICseq-norm.pl

```bash
$ singularity exec <container> /usr/local/bin/NBICseq-norm.pl
$ podman run --it --rm --entrypoint /usr/local/bin/NBICseq-norm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NBICseq-norm.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrepPois

```bash
$ singularity exec <container> /usr/local/bin/PrepPois
$ podman run --it --rm --entrypoint /usr/local/bin/PrepPois   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrepPois   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PrepPoisGAM

```bash
$ singularity exec <container> /usr/local/bin/PrepPoisGAM
$ podman run --it --rm --entrypoint /usr/local/bin/PrepPoisGAM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PrepPoisGAM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineFile

```bash
$ singularity exec <container> /usr/local/bin/combineFile
$ podman run --it --rm --entrypoint /usr/local/bin/combineFile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineFile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compRatio.R

```bash
$ singularity exec <container> /usr/local/bin/compRatio.R
$ podman run --it --rm --entrypoint /usr/local/bin/compRatio.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compRatio.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterCNV

```bash
$ singularity exec <container> /usr/local/bin/filterCNV
$ podman run --it --rm --entrypoint /usr/local/bin/filterCNV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterCNV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize.R

```bash
$ singularity exec <container> /usr/local/bin/normalize.R
$ podman run --it --rm --entrypoint /usr/local/bin/normalize.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizeGAM.R

```bash
$ singularity exec <container> /usr/local/bin/normalizeGAM.R
$ podman run --it --rm --entrypoint /usr/local/bin/normalizeGAM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizeGAM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_RC_vs_GC.R

```bash
$ singularity exec <container> /usr/local/bin/plot_RC_vs_GC.R
$ podman run --it --rm --entrypoint /usr/local/bin/plot_RC_vs_GC.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_RC_vs_GC.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### purity.R

```bash
$ singularity exec <container> /usr/local/bin/purity.R
$ podman run --it --rm --entrypoint /usr/local/bin/purity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/purity.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### purityEM

```bash
$ singularity exec <container> /usr/local/bin/purityEM
$ podman run --it --rm --entrypoint /usr/local/bin/purityEM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/purityEM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### random_split

```bash
$ singularity exec <container> /usr/local/bin/random_split
$ podman run --it --rm --entrypoint /usr/local/bin/random_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/random_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refine.R

```bash
$ singularity exec <container> /usr/local/bin/refine.R
$ podman run --it --rm --entrypoint /usr/local/bin/refine.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refine.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refineGAM.R

```bash
$ singularity exec <container> /usr/local/bin/refineGAM.R
$ podman run --it --rm --entrypoint /usr/local/bin/refineGAM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refineGAM.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.mgcv.installed.R

```bash
$ singularity exec <container> /usr/local/bin/test.mgcv.installed.R
$ podman run --it --rm --entrypoint /usr/local/bin/test.mgcv.installed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.mgcv.installed.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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