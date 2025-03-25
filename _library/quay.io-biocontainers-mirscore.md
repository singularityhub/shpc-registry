---
layout: container
name:  "quay.io/biocontainers/mirscore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirscore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mirscore/container.yaml"
updated_at: "2025-03-25 03:03:01.086052"
latest: "0.3.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mirscore"
aliases:
 - "RNAconsensus"
 - "hairpinHelper"
 - "miRScore"
 - "RNAmultifold"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "cutadapt"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
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
 - "RNALalifold"
 - "RNAPKplex"
 - "RNAparconv"
 - "RNAplex"
versions:
 - "0.3.0--hdfd78af_0"
 - "0.3.1--hdfd78af_0"
 - "0.3.2--hdfd78af_0"
description: "singularity registry hpc automated addition for mirscore"
config: {"url": "https://biocontainers.pro/tools/mirscore", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mirscore", "latest": {"0.3.2--hdfd78af_0": "sha256:8abe8072ce80eb0c656834bf16a4acffacfb98f9e1874dbde7204b3aaa4efca6"}, "tags": {"0.3.0--hdfd78af_0": "sha256:fc7f9856831f67ca5a0f4c1f268d2e37a21014e6eed7cbaff838611a1df0ebb2", "0.3.1--hdfd78af_0": "sha256:6eced079ab7b3fa9b2eb4d1ef571226d9078f58cfcb345dc587c321b8169c7cb", "0.3.2--hdfd78af_0": "sha256:8abe8072ce80eb0c656834bf16a4acffacfb98f9e1874dbde7204b3aaa4efca6"}, "docker": "quay.io/biocontainers/mirscore", "aliases": {"RNAconsensus": "/usr/local/bin/RNAconsensus", "hairpinHelper": "/usr/local/bin/hairpinHelper", "miRScore": "/usr/local/bin/miRScore", "RNAmultifold": "/usr/local/bin/RNAmultifold", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "cutadapt": "/usr/local/bin/cutadapt", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold", "RNALalifold": "/usr/local/bin/RNALalifold", "RNAPKplex": "/usr/local/bin/RNAPKplex", "RNAparconv": "/usr/local/bin/RNAparconv", "RNAplex": "/usr/local/bin/RNAplex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirscore.
singularity registry hpc automated addition for mirscore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirscore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirscore:0.3.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirscore/0.3.2--hdfd78af_0
$ module help quay.io/biocontainers/mirscore/0.3.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirscore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirscore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirscore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirscore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirscore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirscore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAconsensus

```bash
$ singularity exec <container> /usr/local/bin/RNAconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hairpinHelper

```bash
$ singularity exec <container> /usr/local/bin/hairpinHelper
$ podman run --it --rm --entrypoint /usr/local/bin/hairpinHelper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hairpinHelper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miRScore

```bash
$ singularity exec <container> /usr/local/bin/miRScore
$ podman run --it --rm --entrypoint /usr/local/bin/miRScore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRScore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### RNALalifold

```bash
$ singularity exec <container> /usr/local/bin/RNALalifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNALalifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAPKplex

```bash
$ singularity exec <container> /usr/local/bin/RNAPKplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAPKplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAparconv

```bash
$ singularity exec <container> /usr/local/bin/RNAparconv
$ podman run --it --rm --entrypoint /usr/local/bin/RNAparconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAparconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAplex

```bash
$ singularity exec <container> /usr/local/bin/RNAplex
$ podman run --it --rm --entrypoint /usr/local/bin/RNAplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAplex   -v ${PWD} -w ${PWD} <container> -c " $@"
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