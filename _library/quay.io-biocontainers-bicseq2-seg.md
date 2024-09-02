---
layout: container
name:  "quay.io/biocontainers/bicseq2-seg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bicseq2-seg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bicseq2-seg/container.yaml"
updated_at: "2024-09-02 04:21:27.561439"
latest: "0.7.2--h031d066_5"
container_url: "https://biocontainers.pro/tools/bicseq2-seg"
aliases:
 - "BICseqMulSample.pl"
 - "BICseqOneSample.pl"
 - "BICseqTwoSample.pl"
 - "EstLambdaFct"
 - "MBICseq"
 - "NBICseq-seg.pl"
 - "bootstrap"
 - "combineFile"
 - "combineSegBoostrap.R"
 - "countRead"
 - "genotype"
 - "genotype.pl"
 - "plotProfile.R"
 - "report.R"
 - "reportOneSample.R"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.7.2--hec16e2b_3"
 - "0.7.2--h031d066_5"
description: "shpc-registry automated BioContainers addition for bicseq2-seg"
config: {"url": "https://biocontainers.pro/tools/bicseq2-seg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bicseq2-seg", "latest": {"0.7.2--h031d066_5": "sha256:fcb6835a9f80e8444e4adb0a75ad39be3044f3c313f316e052379a9aa96ddafd"}, "tags": {"0.7.2--hec16e2b_3": "sha256:84608234d4a71ec86e461f0b9fa73ed10f6069312e2b4b9b2fbf0a31a13106b3", "0.7.2--h031d066_5": "sha256:fcb6835a9f80e8444e4adb0a75ad39be3044f3c313f316e052379a9aa96ddafd"}, "docker": "quay.io/biocontainers/bicseq2-seg", "aliases": {"BICseqMulSample.pl": "/usr/local/bin/BICseqMulSample.pl", "BICseqOneSample.pl": "/usr/local/bin/BICseqOneSample.pl", "BICseqTwoSample.pl": "/usr/local/bin/BICseqTwoSample.pl", "EstLambdaFct": "/usr/local/bin/EstLambdaFct", "MBICseq": "/usr/local/bin/MBICseq", "NBICseq-seg.pl": "/usr/local/bin/NBICseq-seg.pl", "bootstrap": "/usr/local/bin/bootstrap", "combineFile": "/usr/local/bin/combineFile", "combineSegBoostrap.R": "/usr/local/bin/combineSegBoostrap.R", "countRead": "/usr/local/bin/countRead", "genotype": "/usr/local/bin/genotype", "genotype.pl": "/usr/local/bin/genotype.pl", "plotProfile.R": "/usr/local/bin/plotProfile.R", "report.R": "/usr/local/bin/report.R", "reportOneSample.R": "/usr/local/bin/reportOneSample.R", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bicseq2-seg.
shpc-registry automated BioContainers addition for bicseq2-seg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bicseq2-seg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bicseq2-seg:0.7.2--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bicseq2-seg/0.7.2--h031d066_5
$ module help quay.io/biocontainers/bicseq2-seg/0.7.2--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bicseq2-seg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bicseq2-seg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bicseq2-seg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bicseq2-seg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bicseq2-seg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bicseq2-seg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BICseqMulSample.pl

```bash
$ singularity exec <container> /usr/local/bin/BICseqMulSample.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BICseqMulSample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BICseqMulSample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BICseqOneSample.pl

```bash
$ singularity exec <container> /usr/local/bin/BICseqOneSample.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BICseqOneSample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BICseqOneSample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BICseqTwoSample.pl

```bash
$ singularity exec <container> /usr/local/bin/BICseqTwoSample.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BICseqTwoSample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BICseqTwoSample.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EstLambdaFct

```bash
$ singularity exec <container> /usr/local/bin/EstLambdaFct
$ podman run --it --rm --entrypoint /usr/local/bin/EstLambdaFct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EstLambdaFct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MBICseq

```bash
$ singularity exec <container> /usr/local/bin/MBICseq
$ podman run --it --rm --entrypoint /usr/local/bin/MBICseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MBICseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NBICseq-seg.pl

```bash
$ singularity exec <container> /usr/local/bin/NBICseq-seg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/NBICseq-seg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NBICseq-seg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bootstrap

```bash
$ singularity exec <container> /usr/local/bin/bootstrap
$ podman run --it --rm --entrypoint /usr/local/bin/bootstrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bootstrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineFile

```bash
$ singularity exec <container> /usr/local/bin/combineFile
$ podman run --it --rm --entrypoint /usr/local/bin/combineFile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineFile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineSegBoostrap.R

```bash
$ singularity exec <container> /usr/local/bin/combineSegBoostrap.R
$ podman run --it --rm --entrypoint /usr/local/bin/combineSegBoostrap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineSegBoostrap.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### countRead

```bash
$ singularity exec <container> /usr/local/bin/countRead
$ podman run --it --rm --entrypoint /usr/local/bin/countRead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/countRead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotype

```bash
$ singularity exec <container> /usr/local/bin/genotype
$ podman run --it --rm --entrypoint /usr/local/bin/genotype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genotype.pl

```bash
$ singularity exec <container> /usr/local/bin/genotype.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genotype.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genotype.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotProfile.R

```bash
$ singularity exec <container> /usr/local/bin/plotProfile.R
$ podman run --it --rm --entrypoint /usr/local/bin/plotProfile.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotProfile.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### report.R

```bash
$ singularity exec <container> /usr/local/bin/report.R
$ podman run --it --rm --entrypoint /usr/local/bin/report.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/report.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reportOneSample.R

```bash
$ singularity exec <container> /usr/local/bin/reportOneSample.R
$ podman run --it --rm --entrypoint /usr/local/bin/reportOneSample.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reportOneSample.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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