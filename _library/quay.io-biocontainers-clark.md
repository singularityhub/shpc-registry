---
layout: container
name:  "quay.io/biocontainers/clark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clark/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clark/container.yaml"
updated_at: "2024-01-10 08:57:02.087155"
latest: "1.2.6.1--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/clark"
aliases:
 - "CLARK"
 - "CLARK-S"
 - "CLARK-l"
 - "converter"
 - "dscriptMaker"
 - "exeSeq"
 - "extractSeqs"
 - "getAbundance"
 - "getAccssnTaxID"
 - "getConfidenceDensity"
 - "getGammaDensity"
 - "getTargetSpecificKmersStat"
 - "getTargetsDef"
 - "getfilesToTaxNodes"
 - "makeSummaryTables"
 - "tar"
versions:
 - "1.2.6.1--h9f5acd7_2"
 - "1.2.6.1--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for clark"
config: {"url": "https://biocontainers.pro/tools/clark", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clark", "latest": {"1.2.6.1--h4ac6f70_4": "sha256:1fd597046c826df5d1995f94ff8afc719f3aadd86b0479b025d4a48887365b84"}, "tags": {"1.2.6.1--h9f5acd7_2": "sha256:537b8e919ee0cec74188e0aef661eef5c9a47165678186c049480ca8e0fc6473", "1.2.6.1--h4ac6f70_4": "sha256:1fd597046c826df5d1995f94ff8afc719f3aadd86b0479b025d4a48887365b84"}, "docker": "quay.io/biocontainers/clark", "aliases": {"CLARK": "/usr/local/bin/CLARK", "CLARK-S": "/usr/local/bin/CLARK-S", "CLARK-l": "/usr/local/bin/CLARK-l", "converter": "/usr/local/bin/converter", "dscriptMaker": "/usr/local/bin/dscriptMaker", "exeSeq": "/usr/local/bin/exeSeq", "extractSeqs": "/usr/local/bin/extractSeqs", "getAbundance": "/usr/local/bin/getAbundance", "getAccssnTaxID": "/usr/local/bin/getAccssnTaxID", "getConfidenceDensity": "/usr/local/bin/getConfidenceDensity", "getGammaDensity": "/usr/local/bin/getGammaDensity", "getTargetSpecificKmersStat": "/usr/local/bin/getTargetSpecificKmersStat", "getTargetsDef": "/usr/local/bin/getTargetsDef", "getfilesToTaxNodes": "/usr/local/bin/getfilesToTaxNodes", "makeSummaryTables": "/usr/local/bin/makeSummaryTables", "tar": "/usr/local/bin/tar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clark.
shpc-registry automated BioContainers addition for clark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clark:1.2.6.1--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clark/1.2.6.1--h4ac6f70_4
$ module help quay.io/biocontainers/clark/1.2.6.1--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CLARK

```bash
$ singularity exec <container> /usr/local/bin/CLARK
$ podman run --it --rm --entrypoint /usr/local/bin/CLARK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CLARK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CLARK-S

```bash
$ singularity exec <container> /usr/local/bin/CLARK-S
$ podman run --it --rm --entrypoint /usr/local/bin/CLARK-S   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CLARK-S   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CLARK-l

```bash
$ singularity exec <container> /usr/local/bin/CLARK-l
$ podman run --it --rm --entrypoint /usr/local/bin/CLARK-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CLARK-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converter

```bash
$ singularity exec <container> /usr/local/bin/converter
$ podman run --it --rm --entrypoint /usr/local/bin/converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dscriptMaker

```bash
$ singularity exec <container> /usr/local/bin/dscriptMaker
$ podman run --it --rm --entrypoint /usr/local/bin/dscriptMaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dscriptMaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exeSeq

```bash
$ singularity exec <container> /usr/local/bin/exeSeq
$ podman run --it --rm --entrypoint /usr/local/bin/exeSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exeSeq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractSeqs

```bash
$ singularity exec <container> /usr/local/bin/extractSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/extractSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getAbundance

```bash
$ singularity exec <container> /usr/local/bin/getAbundance
$ podman run --it --rm --entrypoint /usr/local/bin/getAbundance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getAbundance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getAccssnTaxID

```bash
$ singularity exec <container> /usr/local/bin/getAccssnTaxID
$ podman run --it --rm --entrypoint /usr/local/bin/getAccssnTaxID   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getAccssnTaxID   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getConfidenceDensity

```bash
$ singularity exec <container> /usr/local/bin/getConfidenceDensity
$ podman run --it --rm --entrypoint /usr/local/bin/getConfidenceDensity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getConfidenceDensity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getGammaDensity

```bash
$ singularity exec <container> /usr/local/bin/getGammaDensity
$ podman run --it --rm --entrypoint /usr/local/bin/getGammaDensity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getGammaDensity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getTargetSpecificKmersStat

```bash
$ singularity exec <container> /usr/local/bin/getTargetSpecificKmersStat
$ podman run --it --rm --entrypoint /usr/local/bin/getTargetSpecificKmersStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getTargetSpecificKmersStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getTargetsDef

```bash
$ singularity exec <container> /usr/local/bin/getTargetsDef
$ podman run --it --rm --entrypoint /usr/local/bin/getTargetsDef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getTargetsDef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfilesToTaxNodes

```bash
$ singularity exec <container> /usr/local/bin/getfilesToTaxNodes
$ podman run --it --rm --entrypoint /usr/local/bin/getfilesToTaxNodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfilesToTaxNodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeSummaryTables

```bash
$ singularity exec <container> /usr/local/bin/makeSummaryTables
$ podman run --it --rm --entrypoint /usr/local/bin/makeSummaryTables   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeSummaryTables   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
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