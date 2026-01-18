---
layout: container
name:  "quay.io/biocontainers/barriers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/barriers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/barriers/container.yaml"
updated_at: "2026-01-18 03:52:49.999862"
latest: "1.8.1--pl5321h503566f_4"
container_url: "https://biocontainers.pro/tools/barriers"
aliases:
 - "barriers"
 - "crossrates.pl"
 - "fix_bar.pl"
 - "genPoHoLandscape"
 - "saddle.pl"
 - "saddle2dot.pl"
 - "saddle2gml.pl"
 - "treeplot.pl"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
versions:
 - "1.8.1--h1b792b2_1"
 - "1.8.1--pl5321h503566f_4"
description: "shpc-registry automated BioContainers addition for barriers"
config: {"url": "https://biocontainers.pro/tools/barriers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for barriers", "latest": {"1.8.1--pl5321h503566f_4": "sha256:7404f035c22c9d3b8077025e7383d2cc4ad63a60ed6259626f1edcb1567b3744"}, "tags": {"1.8.1--h1b792b2_1": "sha256:53fd695a36a1c6e23bf4b1e9a869a5bf468f454222bf5e6f0698df597a8630ff", "1.8.1--pl5321h503566f_4": "sha256:7404f035c22c9d3b8077025e7383d2cc4ad63a60ed6259626f1edcb1567b3744"}, "docker": "quay.io/biocontainers/barriers", "aliases": {"barriers": "/usr/local/bin/barriers", "crossrates.pl": "/usr/local/bin/crossrates.pl", "fix_bar.pl": "/usr/local/bin/fix_bar.pl", "genPoHoLandscape": "/usr/local/bin/genPoHoLandscape", "saddle.pl": "/usr/local/bin/saddle.pl", "saddle2dot.pl": "/usr/local/bin/saddle2dot.pl", "saddle2gml.pl": "/usr/local/bin/saddle2gml.pl", "treeplot.pl": "/usr/local/bin/treeplot.pl", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/barriers.
shpc-registry automated BioContainers addition for barriers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/barriers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/barriers:1.8.1--pl5321h503566f_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/barriers/1.8.1--pl5321h503566f_4
$ module help quay.io/biocontainers/barriers/1.8.1--pl5321h503566f_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### barriers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### barriers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### barriers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### barriers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### barriers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### barriers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### barriers

```bash
$ singularity exec <container> /usr/local/bin/barriers
$ podman run --it --rm --entrypoint /usr/local/bin/barriers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barriers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossrates.pl

```bash
$ singularity exec <container> /usr/local/bin/crossrates.pl
$ podman run --it --rm --entrypoint /usr/local/bin/crossrates.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossrates.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_bar.pl

```bash
$ singularity exec <container> /usr/local/bin/fix_bar.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fix_bar.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_bar.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genPoHoLandscape

```bash
$ singularity exec <container> /usr/local/bin/genPoHoLandscape
$ podman run --it --rm --entrypoint /usr/local/bin/genPoHoLandscape   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genPoHoLandscape   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle.pl

```bash
$ singularity exec <container> /usr/local/bin/saddle.pl
$ podman run --it --rm --entrypoint /usr/local/bin/saddle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle2dot.pl

```bash
$ singularity exec <container> /usr/local/bin/saddle2dot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/saddle2dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle2dot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saddle2gml.pl

```bash
$ singularity exec <container> /usr/local/bin/saddle2gml.pl
$ podman run --it --rm --entrypoint /usr/local/bin/saddle2gml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saddle2gml.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeplot.pl

```bash
$ singularity exec <container> /usr/local/bin/treeplot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/treeplot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeplot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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