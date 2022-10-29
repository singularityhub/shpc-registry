---
layout: container
name:  "quay.io/biocontainers/brockman-pipeline"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/brockman-pipeline/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/brockman-pipeline/container.yaml"
updated_at: "2022-10-29 05:52:30.015086"
latest: "1.0--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/brockman-pipeline"
aliases:
 - "AMUSED"
 - "AMUSED-KS"
 - "alignKMers"
 - "brockman_pipeline"
 - "racc"
 - "racc2y"
 - "shuffleCodons.rb"
 - "shuffleCodonsAddMotifs.rb"
 - "y2racc"
 - "2to3-3.9"
 - "ace2sam"
 - "annotateBed"
 - "aserver"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
versions:
 - "1.0--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for brockman-pipeline"
config: {"url": "https://biocontainers.pro/tools/brockman-pipeline", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for brockman-pipeline", "latest": {"1.0--hdfd78af_4": "sha256:b509332e3d476a893d0ace336ae1fffa64b3b9162ef9fcc0231a9a86497664f6"}, "tags": {"1.0--hdfd78af_4": "sha256:b509332e3d476a893d0ace336ae1fffa64b3b9162ef9fcc0231a9a86497664f6"}, "docker": "quay.io/biocontainers/brockman-pipeline", "aliases": {"AMUSED": "/usr/local/bin/AMUSED", "AMUSED-KS": "/usr/local/bin/AMUSED-KS", "alignKMers": "/usr/local/bin/alignKMers", "brockman_pipeline": "/usr/local/bin/brockman_pipeline", "racc": "/usr/local/bin/racc", "racc2y": "/usr/local/bin/racc2y", "shuffleCodons.rb": "/usr/local/bin/shuffleCodons.rb", "shuffleCodonsAddMotifs.rb": "/usr/local/bin/shuffleCodonsAddMotifs.rb", "y2racc": "/usr/local/bin/y2racc", "2to3-3.9": "/usr/local/bin/2to3-3.9", "ace2sam": "/usr/local/bin/ace2sam", "annotateBed": "/usr/local/bin/annotateBed", "aserver": "/usr/local/bin/aserver", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/brockman-pipeline.
shpc-registry automated BioContainers addition for brockman-pipeline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/brockman-pipeline
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/brockman-pipeline:1.0--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/brockman-pipeline/1.0--hdfd78af_4
$ module help quay.io/biocontainers/brockman-pipeline/1.0--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### brockman-pipeline-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### brockman-pipeline-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### brockman-pipeline-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### brockman-pipeline-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### brockman-pipeline-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### brockman-pipeline-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMUSED

```bash
$ singularity exec <container> /usr/local/bin/AMUSED
$ podman run --it --rm --entrypoint /usr/local/bin/AMUSED   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMUSED   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AMUSED-KS

```bash
$ singularity exec <container> /usr/local/bin/AMUSED-KS
$ podman run --it --rm --entrypoint /usr/local/bin/AMUSED-KS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMUSED-KS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignKMers

```bash
$ singularity exec <container> /usr/local/bin/alignKMers
$ podman run --it --rm --entrypoint /usr/local/bin/alignKMers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignKMers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brockman_pipeline

```bash
$ singularity exec <container> /usr/local/bin/brockman_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/brockman_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brockman_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc2y

```bash
$ singularity exec <container> /usr/local/bin/racc2y
$ podman run --it --rm --entrypoint /usr/local/bin/racc2y   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc2y   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffleCodons.rb

```bash
$ singularity exec <container> /usr/local/bin/shuffleCodons.rb
$ podman run --it --rm --entrypoint /usr/local/bin/shuffleCodons.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffleCodons.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffleCodonsAddMotifs.rb

```bash
$ singularity exec <container> /usr/local/bin/shuffleCodonsAddMotifs.rb
$ podman run --it --rm --entrypoint /usr/local/bin/shuffleCodonsAddMotifs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffleCodonsAddMotifs.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### y2racc

```bash
$ singularity exec <container> /usr/local/bin/y2racc
$ podman run --it --rm --entrypoint /usr/local/bin/y2racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/y2racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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