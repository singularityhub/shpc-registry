---
layout: container
name:  "quay.io/biocontainers/mirdeep-p2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirdeep-p2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mirdeep-p2/container.yaml"
updated_at: "2023-03-10 04:01:16.398054"
latest: "1.1.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mirdeep-p2"
aliases:
 - "afetch"
 - "alistat"
 - "compalign"
 - "compstruct"
 - "miRDP2-v1.1.4_pipeline.bash"
 - "randfold"
 - "revcomp"
 - "seqsplit"
 - "seqstat"
 - "sfetch"
 - "shuffle"
 - "sindex"
 - "sreformat"
 - "translate"
 - "weight"
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
 - "1.1.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mirdeep-p2"
config: {"url": "https://biocontainers.pro/tools/mirdeep-p2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirdeep-p2", "latest": {"1.1.4--hdfd78af_0": "sha256:61db8c968c34a9cff16dde1f477ec9a5b44288be5894663166b33abde370672e"}, "tags": {"1.1.4--hdfd78af_0": "sha256:61db8c968c34a9cff16dde1f477ec9a5b44288be5894663166b33abde370672e"}, "docker": "quay.io/biocontainers/mirdeep-p2", "aliases": {"afetch": "/usr/local/bin/afetch", "alistat": "/usr/local/bin/alistat", "compalign": "/usr/local/bin/compalign", "compstruct": "/usr/local/bin/compstruct", "miRDP2-v1.1.4_pipeline.bash": "/usr/local/bin/miRDP2-v1.1.4_pipeline.bash", "randfold": "/usr/local/bin/randfold", "revcomp": "/usr/local/bin/revcomp", "seqsplit": "/usr/local/bin/seqsplit", "seqstat": "/usr/local/bin/seqstat", "sfetch": "/usr/local/bin/sfetch", "shuffle": "/usr/local/bin/shuffle", "sindex": "/usr/local/bin/sindex", "sreformat": "/usr/local/bin/sreformat", "translate": "/usr/local/bin/translate", "weight": "/usr/local/bin/weight", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirdeep-p2.
shpc-registry automated BioContainers addition for mirdeep-p2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirdeep-p2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirdeep-p2:1.1.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirdeep-p2/1.1.4--hdfd78af_0
$ module help quay.io/biocontainers/mirdeep-p2/1.1.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirdeep-p2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirdeep-p2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirdeep-p2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirdeep-p2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirdeep-p2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirdeep-p2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### afetch

```bash
$ singularity exec <container> /usr/local/bin/afetch
$ podman run --it --rm --entrypoint /usr/local/bin/afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/afetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alistat

```bash
$ singularity exec <container> /usr/local/bin/alistat
$ podman run --it --rm --entrypoint /usr/local/bin/alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compalign

```bash
$ singularity exec <container> /usr/local/bin/compalign
$ podman run --it --rm --entrypoint /usr/local/bin/compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compstruct

```bash
$ singularity exec <container> /usr/local/bin/compstruct
$ podman run --it --rm --entrypoint /usr/local/bin/compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miRDP2-v1.1.4_pipeline.bash

```bash
$ singularity exec <container> /usr/local/bin/miRDP2-v1.1.4_pipeline.bash
$ podman run --it --rm --entrypoint /usr/local/bin/miRDP2-v1.1.4_pipeline.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRDP2-v1.1.4_pipeline.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randfold

```bash
$ singularity exec <container> /usr/local/bin/randfold
$ podman run --it --rm --entrypoint /usr/local/bin/randfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### revcomp

```bash
$ singularity exec <container> /usr/local/bin/revcomp
$ podman run --it --rm --entrypoint /usr/local/bin/revcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/revcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqsplit

```bash
$ singularity exec <container> /usr/local/bin/seqsplit
$ podman run --it --rm --entrypoint /usr/local/bin/seqsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqstat

```bash
$ singularity exec <container> /usr/local/bin/seqstat
$ podman run --it --rm --entrypoint /usr/local/bin/seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sfetch

```bash
$ singularity exec <container> /usr/local/bin/sfetch
$ podman run --it --rm --entrypoint /usr/local/bin/sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffle

```bash
$ singularity exec <container> /usr/local/bin/shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sindex

```bash
$ singularity exec <container> /usr/local/bin/sindex
$ podman run --it --rm --entrypoint /usr/local/bin/sindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sreformat

```bash
$ singularity exec <container> /usr/local/bin/sreformat
$ podman run --it --rm --entrypoint /usr/local/bin/sreformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sreformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### translate

```bash
$ singularity exec <container> /usr/local/bin/translate
$ podman run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weight

```bash
$ singularity exec <container> /usr/local/bin/weight
$ podman run --it --rm --entrypoint /usr/local/bin/weight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weight   -v ${PWD} -w ${PWD} <container> -c " $@"
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