---
layout: container
name:  "quay.io/biocontainers/ribotaper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ribotaper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ribotaper/container.yaml"
updated_at: "2025-10-04 03:07:01.125591"
latest: "1.3.1a--h7b50bb2_9"
container_url: "https://biocontainers.pro/tools/ribotaper"
aliases:
 - "Ribotaper.sh"
 - "Ribotaper_ORF_find.sh"
 - "create_annotations_files.bash"
 - "create_metaplots.bash"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
versions:
 - "1.3.1a--hec16e2b_5"
 - "1.3.1a--h031d066_6"
 - "1.3.1a--h031d066_8"
 - "1.3.1a--h7b50bb2_9"
description: "shpc-registry automated BioContainers addition for ribotaper"
config: {"url": "https://biocontainers.pro/tools/ribotaper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ribotaper", "latest": {"1.3.1a--h7b50bb2_9": "sha256:2e07ac5f9df9380e2612b2f20caa2032ff302a01a591612abb76ae86fb98c8e5"}, "tags": {"1.3.1a--hec16e2b_5": "sha256:a83127119089d22f75df125c7040b118961ba0ea10d31f4eb40badb595e2a253", "1.3.1a--h031d066_6": "sha256:7d305e8e28df027e89339ab32fb42e7a1d95c135b5018a2872b2dc6d11a691d8", "1.3.1a--h031d066_8": "sha256:0fdaf9fba1dfe0d6ccec5091f261a54f7298833442c4709ec4a54a81bfd1567b", "1.3.1a--h7b50bb2_9": "sha256:2e07ac5f9df9380e2612b2f20caa2032ff302a01a591612abb76ae86fb98c8e5"}, "docker": "quay.io/biocontainers/ribotaper", "aliases": {"Ribotaper.sh": "/usr/local/bin/Ribotaper.sh", "Ribotaper_ORF_find.sh": "/usr/local/bin/Ribotaper_ORF_find.sh", "create_annotations_files.bash": "/usr/local/bin/create_annotations_files.bash", "create_metaplots.bash": "/usr/local/bin/create_metaplots.bash", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ribotaper.
shpc-registry automated BioContainers addition for ribotaper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ribotaper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ribotaper:1.3.1a--h7b50bb2_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ribotaper/1.3.1a--h7b50bb2_9
$ module help quay.io/biocontainers/ribotaper/1.3.1a--h7b50bb2_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ribotaper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ribotaper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ribotaper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ribotaper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ribotaper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ribotaper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Ribotaper.sh

```bash
$ singularity exec <container> /usr/local/bin/Ribotaper.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Ribotaper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Ribotaper.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Ribotaper_ORF_find.sh

```bash
$ singularity exec <container> /usr/local/bin/Ribotaper_ORF_find.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Ribotaper_ORF_find.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Ribotaper_ORF_find.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_annotations_files.bash

```bash
$ singularity exec <container> /usr/local/bin/create_annotations_files.bash
$ podman run --it --rm --entrypoint /usr/local/bin/create_annotations_files.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_annotations_files.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_metaplots.bash

```bash
$ singularity exec <container> /usr/local/bin/create_metaplots.bash
$ podman run --it --rm --entrypoint /usr/local/bin/create_metaplots.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_metaplots.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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