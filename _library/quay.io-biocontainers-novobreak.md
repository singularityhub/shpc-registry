---
layout: container
name:  "quay.io/biocontainers/novobreak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/novobreak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/novobreak/container.yaml"
updated_at: "2024-11-15 03:46:33.402920"
latest: "1.1.3rc--he4a0461_9"
container_url: "https://biocontainers.pro/tools/novobreak"
aliases:
 - "SSAKE"
 - "TQS.py"
 - "TQSexport.py"
 - "TQSfastq.pl"
 - "TQSfastq.py"
 - "analyzePositionSSAKE.pl"
 - "fetch_discordant.pl"
 - "filter_sv.bak.pl"
 - "filter_sv.pl"
 - "filter_sv2.pl"
 - "filter_sv_icgc.pl"
 - "getStats.pl"
 - "group_bp_reads.pl"
 - "infer_bp.pl"
 - "infer_bp_v4.pl"
 - "infer_sv.pl"
 - "makeFastaFileFromScaffolds.pl"
 - "makePairedOutput.pl"
 - "makePairedOutput2EQUALfiles.pl"
 - "makePairedOutput2UNEQUALfiles.pl"
 - "nLength.pl"
 - "novoBreak"
 - "qseq2fasta.pl"
 - "qseq2fastq.pl"
 - "run_novoBreak.sh"
 - "run_novobreak"
 - "run_ssake.pl"
 - "splitInput.pl"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
versions:
 - "1.1.3rc--h7132678_8"
 - "1.1.3rc--he4a0461_9"
description: "shpc-registry automated BioContainers addition for novobreak"
config: {"url": "https://biocontainers.pro/tools/novobreak", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for novobreak", "latest": {"1.1.3rc--he4a0461_9": "sha256:737bcdbdcfa1b3ff212d41195027047eb2106e537fa8d40c1331f78bf27dc634"}, "tags": {"1.1.3rc--h7132678_8": "sha256:f3eb4e7de7cbe9ef3251aae8b770633daf6eb66e8602bed7d329b2df5ef95cd5", "1.1.3rc--he4a0461_9": "sha256:737bcdbdcfa1b3ff212d41195027047eb2106e537fa8d40c1331f78bf27dc634"}, "docker": "quay.io/biocontainers/novobreak", "aliases": {"SSAKE": "/usr/local/bin/SSAKE", "TQS.py": "/usr/local/bin/TQS.py", "TQSexport.py": "/usr/local/bin/TQSexport.py", "TQSfastq.pl": "/usr/local/bin/TQSfastq.pl", "TQSfastq.py": "/usr/local/bin/TQSfastq.py", "analyzePositionSSAKE.pl": "/usr/local/bin/analyzePositionSSAKE.pl", "fetch_discordant.pl": "/usr/local/bin/fetch_discordant.pl", "filter_sv.bak.pl": "/usr/local/bin/filter_sv.bak.pl", "filter_sv.pl": "/usr/local/bin/filter_sv.pl", "filter_sv2.pl": "/usr/local/bin/filter_sv2.pl", "filter_sv_icgc.pl": "/usr/local/bin/filter_sv_icgc.pl", "getStats.pl": "/usr/local/bin/getStats.pl", "group_bp_reads.pl": "/usr/local/bin/group_bp_reads.pl", "infer_bp.pl": "/usr/local/bin/infer_bp.pl", "infer_bp_v4.pl": "/usr/local/bin/infer_bp_v4.pl", "infer_sv.pl": "/usr/local/bin/infer_sv.pl", "makeFastaFileFromScaffolds.pl": "/usr/local/bin/makeFastaFileFromScaffolds.pl", "makePairedOutput.pl": "/usr/local/bin/makePairedOutput.pl", "makePairedOutput2EQUALfiles.pl": "/usr/local/bin/makePairedOutput2EQUALfiles.pl", "makePairedOutput2UNEQUALfiles.pl": "/usr/local/bin/makePairedOutput2UNEQUALfiles.pl", "nLength.pl": "/usr/local/bin/nLength.pl", "novoBreak": "/usr/local/bin/novoBreak", "qseq2fasta.pl": "/usr/local/bin/qseq2fasta.pl", "qseq2fastq.pl": "/usr/local/bin/qseq2fastq.pl", "run_novoBreak.sh": "/usr/local/bin/run_novoBreak.sh", "run_novobreak": "/usr/local/bin/run_novobreak", "run_ssake.pl": "/usr/local/bin/run_ssake.pl", "splitInput.pl": "/usr/local/bin/splitInput.pl", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/novobreak.
shpc-registry automated BioContainers addition for novobreak
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/novobreak
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/novobreak:1.1.3rc--he4a0461_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/novobreak/1.1.3rc--he4a0461_9
$ module help quay.io/biocontainers/novobreak/1.1.3rc--he4a0461_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### novobreak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### novobreak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### novobreak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### novobreak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### novobreak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### novobreak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SSAKE

```bash
$ singularity exec <container> /usr/local/bin/SSAKE
$ podman run --it --rm --entrypoint /usr/local/bin/SSAKE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SSAKE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TQS.py

```bash
$ singularity exec <container> /usr/local/bin/TQS.py
$ podman run --it --rm --entrypoint /usr/local/bin/TQS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TQS.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TQSexport.py

```bash
$ singularity exec <container> /usr/local/bin/TQSexport.py
$ podman run --it --rm --entrypoint /usr/local/bin/TQSexport.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TQSexport.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TQSfastq.pl

```bash
$ singularity exec <container> /usr/local/bin/TQSfastq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/TQSfastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TQSfastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TQSfastq.py

```bash
$ singularity exec <container> /usr/local/bin/TQSfastq.py
$ podman run --it --rm --entrypoint /usr/local/bin/TQSfastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TQSfastq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzePositionSSAKE.pl

```bash
$ singularity exec <container> /usr/local/bin/analyzePositionSSAKE.pl
$ podman run --it --rm --entrypoint /usr/local/bin/analyzePositionSSAKE.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzePositionSSAKE.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_discordant.pl

```bash
$ singularity exec <container> /usr/local/bin/fetch_discordant.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_discordant.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_discordant.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_sv.bak.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_sv.bak.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_sv.bak.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_sv.bak.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_sv.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_sv.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_sv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_sv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_sv2.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_sv2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_sv2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_sv2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_sv_icgc.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_sv_icgc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_sv_icgc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_sv_icgc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getStats.pl

```bash
$ singularity exec <container> /usr/local/bin/getStats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getStats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getStats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### group_bp_reads.pl

```bash
$ singularity exec <container> /usr/local/bin/group_bp_reads.pl
$ podman run --it --rm --entrypoint /usr/local/bin/group_bp_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/group_bp_reads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infer_bp.pl

```bash
$ singularity exec <container> /usr/local/bin/infer_bp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/infer_bp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infer_bp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infer_bp_v4.pl

```bash
$ singularity exec <container> /usr/local/bin/infer_bp_v4.pl
$ podman run --it --rm --entrypoint /usr/local/bin/infer_bp_v4.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infer_bp_v4.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### infer_sv.pl

```bash
$ singularity exec <container> /usr/local/bin/infer_sv.pl
$ podman run --it --rm --entrypoint /usr/local/bin/infer_sv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/infer_sv.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeFastaFileFromScaffolds.pl

```bash
$ singularity exec <container> /usr/local/bin/makeFastaFileFromScaffolds.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makeFastaFileFromScaffolds.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeFastaFileFromScaffolds.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makePairedOutput.pl

```bash
$ singularity exec <container> /usr/local/bin/makePairedOutput.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makePairedOutput.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makePairedOutput.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makePairedOutput2EQUALfiles.pl

```bash
$ singularity exec <container> /usr/local/bin/makePairedOutput2EQUALfiles.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makePairedOutput2EQUALfiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makePairedOutput2EQUALfiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makePairedOutput2UNEQUALfiles.pl

```bash
$ singularity exec <container> /usr/local/bin/makePairedOutput2UNEQUALfiles.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makePairedOutput2UNEQUALfiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makePairedOutput2UNEQUALfiles.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nLength.pl

```bash
$ singularity exec <container> /usr/local/bin/nLength.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nLength.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nLength.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novoBreak

```bash
$ singularity exec <container> /usr/local/bin/novoBreak
$ podman run --it --rm --entrypoint /usr/local/bin/novoBreak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novoBreak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qseq2fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/qseq2fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qseq2fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qseq2fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qseq2fastq.pl

```bash
$ singularity exec <container> /usr/local/bin/qseq2fastq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qseq2fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qseq2fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_novoBreak.sh

```bash
$ singularity exec <container> /usr/local/bin/run_novoBreak.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_novoBreak.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_novoBreak.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_novobreak

```bash
$ singularity exec <container> /usr/local/bin/run_novobreak
$ podman run --it --rm --entrypoint /usr/local/bin/run_novobreak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_novobreak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_ssake.pl

```bash
$ singularity exec <container> /usr/local/bin/run_ssake.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_ssake.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_ssake.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitInput.pl

```bash
$ singularity exec <container> /usr/local/bin/splitInput.pl
$ podman run --it --rm --entrypoint /usr/local/bin/splitInput.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitInput.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
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