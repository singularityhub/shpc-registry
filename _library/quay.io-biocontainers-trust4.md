---
layout: container
name:  "quay.io/biocontainers/trust4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trust4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trust4/container.yaml"
updated_at: "2025-12-13 03:29:09.626559"
latest: "1.1.7--h5ca1c30_0"
container_url: "https://biocontainers.pro/tools/trust4"
aliases:
 - "BuildDatabaseFa.pl"
 - "BuildImgtAnnot.pl"
 - "annotator"
 - "bam-extractor"
 - "fastq-extractor"
 - "run-trust4"
 - "trust-airr.pl"
 - "trust-barcoderep.pl"
 - "trust-simplerep.pl"
 - "trust-smartseq.pl"
 - "trust4"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.7--h5b5514e_0"
 - "1.0.8--h5b5514e_0"
 - "1.0.9--h5b5514e_0"
 - "1.0.10--h43eeafb_1"
 - "1.0.12--h43eeafb_0"
 - "1.0.13--h43eeafb_0"
 - "1.0.14--h43eeafb_0"
 - "1.1.0--h43eeafb_0"
 - "1.1.1--h43eeafb_0"
 - "1.1.2--h43eeafb_1"
 - "1.1.4--h43eeafb_0"
 - "1.1.5--h5ca1c30_0"
 - "1.1.6.1--h5ca1c30_0"
 - "1.1.7--h5ca1c30_0"
description: "shpc-registry automated BioContainers addition for trust4"
config: {"url": "https://biocontainers.pro/tools/trust4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trust4", "latest": {"1.1.7--h5ca1c30_0": "sha256:1f45cc71c0f97f4a0db9edf2e7fbae076070ec54424119be9ca103f2ac6aa1fa"}, "tags": {"1.0.7--h5b5514e_0": "sha256:c2ebbe6ff6cc24630eb0aa6ea17295e9138e5d0612993b41fddd60398082836e", "1.0.8--h5b5514e_0": "sha256:86c7b2b07f9fdd7f87f1ee9fccabacdfd3fdc8222bc5276582910bae9a389697", "1.0.9--h5b5514e_0": "sha256:0bfe7f8942e91a15bf06179c67479961d0a85d6125d2a4a886a47288f3f656df", "1.0.10--h43eeafb_1": "sha256:add817375e0b9ddfc026b5dc1bb8a7748bbe3df139b14523205f9ee82b0fcdbb", "1.0.12--h43eeafb_0": "sha256:bae8cefd755bf9861ad6ca4da30cb1625142f87e3e38d791407d2e9e8b5c78b8", "1.0.13--h43eeafb_0": "sha256:e0852ee5609e9e9c80a4914b4d5740faa4bedcf860b9231925a96c7bd04bfeab", "1.0.14--h43eeafb_0": "sha256:d045e80cad6e7b22ad480b09f6c994478de4f26a01629844b4a4c6b796da152d", "1.1.0--h43eeafb_0": "sha256:b3fa0455fcbe83b5a204f1a9f34112c582111babf770854344a89af8578f0540", "1.1.1--h43eeafb_0": "sha256:ae39bb9fcd83e67582fd83225854703c4c1316082d4d08c57cffb3265d653d97", "1.1.2--h43eeafb_1": "sha256:3eaf3c0666d154255a85690b761de19b18ac611b292c53ced942c8646a4def87", "1.1.4--h43eeafb_0": "sha256:3051a19dda773c3b217ffa6e9d807acf2c15fa5f4b85fec8eb555eb8053cedf2", "1.1.5--h5ca1c30_0": "sha256:ef9f3345e7b54d73c4d9576781b661553c42513b91d60d9a0cd126ada569eb20", "1.1.6.1--h5ca1c30_0": "sha256:3444d58b968796a9b010e8e5a1f726bcba1df60add6af46810fbd74e473214d9", "1.1.7--h5ca1c30_0": "sha256:1f45cc71c0f97f4a0db9edf2e7fbae076070ec54424119be9ca103f2ac6aa1fa"}, "docker": "quay.io/biocontainers/trust4", "aliases": {"BuildDatabaseFa.pl": "/usr/local/bin/BuildDatabaseFa.pl", "BuildImgtAnnot.pl": "/usr/local/bin/BuildImgtAnnot.pl", "annotator": "/usr/local/bin/annotator", "bam-extractor": "/usr/local/bin/bam-extractor", "fastq-extractor": "/usr/local/bin/fastq-extractor", "run-trust4": "/usr/local/bin/run-trust4", "trust-airr.pl": "/usr/local/bin/trust-airr.pl", "trust-barcoderep.pl": "/usr/local/bin/trust-barcoderep.pl", "trust-simplerep.pl": "/usr/local/bin/trust-simplerep.pl", "trust-smartseq.pl": "/usr/local/bin/trust-smartseq.pl", "trust4": "/usr/local/bin/trust4", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trust4.
shpc-registry automated BioContainers addition for trust4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trust4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trust4:1.1.7--h5ca1c30_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trust4/1.1.7--h5ca1c30_0
$ module help quay.io/biocontainers/trust4/1.1.7--h5ca1c30_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trust4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trust4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trust4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trust4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trust4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trust4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BuildDatabaseFa.pl

```bash
$ singularity exec <container> /usr/local/bin/BuildDatabaseFa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BuildDatabaseFa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BuildDatabaseFa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BuildImgtAnnot.pl

```bash
$ singularity exec <container> /usr/local/bin/BuildImgtAnnot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/BuildImgtAnnot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BuildImgtAnnot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotator

```bash
$ singularity exec <container> /usr/local/bin/annotator
$ podman run --it --rm --entrypoint /usr/local/bin/annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam-extractor

```bash
$ singularity exec <container> /usr/local/bin/bam-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/bam-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-extractor

```bash
$ singularity exec <container> /usr/local/bin/fastq-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-trust4

```bash
$ singularity exec <container> /usr/local/bin/run-trust4
$ podman run --it --rm --entrypoint /usr/local/bin/run-trust4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-trust4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust-airr.pl

```bash
$ singularity exec <container> /usr/local/bin/trust-airr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/trust-airr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust-airr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust-barcoderep.pl

```bash
$ singularity exec <container> /usr/local/bin/trust-barcoderep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/trust-barcoderep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust-barcoderep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust-simplerep.pl

```bash
$ singularity exec <container> /usr/local/bin/trust-simplerep.pl
$ podman run --it --rm --entrypoint /usr/local/bin/trust-simplerep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust-simplerep.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust-smartseq.pl

```bash
$ singularity exec <container> /usr/local/bin/trust-smartseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/trust-smartseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust-smartseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust4

```bash
$ singularity exec <container> /usr/local/bin/trust4
$ podman run --it --rm --entrypoint /usr/local/bin/trust4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust4   -v ${PWD} -w ${PWD} <container> -c " $@"
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