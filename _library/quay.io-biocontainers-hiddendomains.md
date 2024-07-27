---
layout: container
name:  "quay.io/biocontainers/hiddendomains"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hiddendomains/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hiddendomains/container.yaml"
updated_at: "2024-07-27 03:19:20.486003"
latest: "3.1--pl5321r42hdfd78af_4"
container_url: "https://biocontainers.pro/tools/hiddendomains"
aliases:
 - "binReads.pl"
 - "centersToGEM.pl"
 - "domainsMergeToBed.pl"
 - "domainsToBed.pl"
 - "hiddenDomains"
 - "hiddenDomains.R"
 - "peakCenters"
 - "run_hiddenDomains.R"
 - "run_hiddenDomains_no_control.R"
 - "fasta-sanitize.pl"
 - "shiftBed"
 - "plot-ampliconstats"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
versions:
 - "3.1--pl5321r41hdfd78af_3"
 - "3.1--pl5321r42hdfd78af_4"
description: "shpc-registry automated BioContainers addition for hiddendomains"
config: {"url": "https://biocontainers.pro/tools/hiddendomains", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hiddendomains", "latest": {"3.1--pl5321r42hdfd78af_4": "sha256:88922cfdcf991174e4d46b9491e026f59a0f6dcd823986e95fca87753efadfdc"}, "tags": {"3.1--pl5321r41hdfd78af_3": "sha256:7f1f3ef74f2ef848a9c40afbba74006d011223ca747dda1716e7c419525f633c", "3.1--pl5321r42hdfd78af_4": "sha256:88922cfdcf991174e4d46b9491e026f59a0f6dcd823986e95fca87753efadfdc"}, "docker": "quay.io/biocontainers/hiddendomains", "aliases": {"binReads.pl": "/usr/local/bin/binReads.pl", "centersToGEM.pl": "/usr/local/bin/centersToGEM.pl", "domainsMergeToBed.pl": "/usr/local/bin/domainsMergeToBed.pl", "domainsToBed.pl": "/usr/local/bin/domainsToBed.pl", "hiddenDomains": "/usr/local/bin/hiddenDomains", "hiddenDomains.R": "/usr/local/bin/hiddenDomains.R", "peakCenters": "/usr/local/bin/peakCenters", "run_hiddenDomains.R": "/usr/local/bin/run_hiddenDomains.R", "run_hiddenDomains_no_control.R": "/usr/local/bin/run_hiddenDomains_no_control.R", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "shiftBed": "/usr/local/bin/shiftBed", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hiddendomains.
shpc-registry automated BioContainers addition for hiddendomains
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hiddendomains
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hiddendomains:3.1--pl5321r42hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hiddendomains/3.1--pl5321r42hdfd78af_4
$ module help quay.io/biocontainers/hiddendomains/3.1--pl5321r42hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hiddendomains-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hiddendomains-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hiddendomains-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hiddendomains-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hiddendomains-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hiddendomains-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binReads.pl

```bash
$ singularity exec <container> /usr/local/bin/binReads.pl
$ podman run --it --rm --entrypoint /usr/local/bin/binReads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binReads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centersToGEM.pl

```bash
$ singularity exec <container> /usr/local/bin/centersToGEM.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centersToGEM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centersToGEM.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### domainsMergeToBed.pl

```bash
$ singularity exec <container> /usr/local/bin/domainsMergeToBed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/domainsMergeToBed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/domainsMergeToBed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### domainsToBed.pl

```bash
$ singularity exec <container> /usr/local/bin/domainsToBed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/domainsToBed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/domainsToBed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hiddenDomains

```bash
$ singularity exec <container> /usr/local/bin/hiddenDomains
$ podman run --it --rm --entrypoint /usr/local/bin/hiddenDomains   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiddenDomains   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hiddenDomains.R

```bash
$ singularity exec <container> /usr/local/bin/hiddenDomains.R
$ podman run --it --rm --entrypoint /usr/local/bin/hiddenDomains.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiddenDomains.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peakCenters

```bash
$ singularity exec <container> /usr/local/bin/peakCenters
$ podman run --it --rm --entrypoint /usr/local/bin/peakCenters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peakCenters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_hiddenDomains.R

```bash
$ singularity exec <container> /usr/local/bin/run_hiddenDomains.R
$ podman run --it --rm --entrypoint /usr/local/bin/run_hiddenDomains.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_hiddenDomains.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_hiddenDomains_no_control.R

```bash
$ singularity exec <container> /usr/local/bin/run_hiddenDomains_no_control.R
$ podman run --it --rm --entrypoint /usr/local/bin/run_hiddenDomains_no_control.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_hiddenDomains_no_control.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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