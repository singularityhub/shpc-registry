---
layout: container
name:  "quay.io/biocontainers/ssake"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ssake/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ssake/container.yaml"
updated_at: "2023-01-14 02:41:29.344222"
latest: "4.0--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/ssake"
aliases:
 - "SSAKE"
 - "TQS.py"
 - "TQSexport.py"
 - "TQSfastq.pl"
 - "TQSfastq.py"
 - "analyzePositionSSAKE.pl"
 - "getStats.pl"
 - "makeFastaFileFromScaffolds.pl"
 - "makePairedOutput.pl"
 - "makePairedOutput2EQUALfiles.pl"
 - "makePairedOutput2UNEQUALfiles.pl"
 - "nLength.pl"
 - "qseq2fasta.pl"
 - "qseq2fastq.pl"
 - "splitInput.pl"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "4.0--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for ssake"
config: {"url": "https://biocontainers.pro/tools/ssake", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ssake", "latest": {"4.0--hdfd78af_5": "sha256:50821451b1749bbd6fcdb888e1655874f7d1b778253958f5444c7f410ac42e99"}, "tags": {"4.0--hdfd78af_5": "sha256:50821451b1749bbd6fcdb888e1655874f7d1b778253958f5444c7f410ac42e99"}, "docker": "quay.io/biocontainers/ssake", "aliases": {"SSAKE": "/usr/local/bin/SSAKE", "TQS.py": "/usr/local/bin/TQS.py", "TQSexport.py": "/usr/local/bin/TQSexport.py", "TQSfastq.pl": "/usr/local/bin/TQSfastq.pl", "TQSfastq.py": "/usr/local/bin/TQSfastq.py", "analyzePositionSSAKE.pl": "/usr/local/bin/analyzePositionSSAKE.pl", "getStats.pl": "/usr/local/bin/getStats.pl", "makeFastaFileFromScaffolds.pl": "/usr/local/bin/makeFastaFileFromScaffolds.pl", "makePairedOutput.pl": "/usr/local/bin/makePairedOutput.pl", "makePairedOutput2EQUALfiles.pl": "/usr/local/bin/makePairedOutput2EQUALfiles.pl", "makePairedOutput2UNEQUALfiles.pl": "/usr/local/bin/makePairedOutput2UNEQUALfiles.pl", "nLength.pl": "/usr/local/bin/nLength.pl", "qseq2fasta.pl": "/usr/local/bin/qseq2fasta.pl", "qseq2fastq.pl": "/usr/local/bin/qseq2fastq.pl", "splitInput.pl": "/usr/local/bin/splitInput.pl", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ssake.
shpc-registry automated BioContainers addition for ssake
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ssake
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ssake:4.0--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ssake/4.0--hdfd78af_5
$ module help quay.io/biocontainers/ssake/4.0--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ssake-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ssake-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ssake-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ssake-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ssake-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ssake-inspect-deffile:

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


#### getStats.pl

```bash
$ singularity exec <container> /usr/local/bin/getStats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getStats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getStats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### splitInput.pl

```bash
$ singularity exec <container> /usr/local/bin/splitInput.pl
$ podman run --it --rm --entrypoint /usr/local/bin/splitInput.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitInput.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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