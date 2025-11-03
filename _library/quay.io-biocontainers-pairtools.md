---
layout: container
name:  "quay.io/biocontainers/pairtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pairtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pairtools/container.yaml"
updated_at: "2025-11-03 03:35:42.125505"
latest: "1.1.3--py310h4e61836_0"
container_url: "https://biocontainers.pro/tools/pairtools"
aliases:
 - "pairtools"
 - "pbgzip"
 - "bam2pairs"
 - "column_remover.pl"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
 - "merged_nodup2pairs.pl"
 - "old_merged_nodup2pairs.pl"
 - "pairix"
 - "pairs_merger"
versions:
 - "1.0.1--py37h9f12aac_0"
 - "1.0.2--py39h2a9f597_0"
 - "1.0.2--py39h9e08559_1"
 - "1.0.3--py310hb45ccb3_0"
 - "1.0.3--py39h9e08559_0"
 - "1.1.0--py310hb45ccb3_0"
 - "1.1.0--py312hac03d35_1"
 - "1.1.0--py310h8dfefeb_2"
 - "1.1.2--py312h5219090_0"
 - "1.1.3--py310h4e61836_0"
description: "shpc-registry automated BioContainers addition for pairtools"
config: {"url": "https://biocontainers.pro/tools/pairtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pairtools", "latest": {"1.1.3--py310h4e61836_0": "sha256:29e06e1791a809300c29abd8dea482eca573f2b9d0f8b8e2dddc0c749f561ba4"}, "tags": {"1.0.1--py37h9f12aac_0": "sha256:656044fea9e722c2a9189e3134f65949b7ee76644d3b8008bf5dd478c5846408", "1.0.2--py39h2a9f597_0": "sha256:4abe176aa9d20dd575a6a255f8d8ee3cc2b7090081bf5da5c48851a59459cd12", "1.0.2--py39h9e08559_1": "sha256:e599cedadc7ea68683d9a556207736c18ea73aaafae5d6300c578336a9c8d592", "1.0.3--py310hb45ccb3_0": "sha256:629f96618e0dacbd8c47d1abaaf55d713600f21418a1125fab8230a17645bcc7", "1.0.3--py39h9e08559_0": "sha256:538291139f435a707366f4fc78ee969b9c9e0f58b68ef17d79644a2e26588f9c", "1.1.0--py310hb45ccb3_0": "sha256:90a57227aa9b805a74659f1d7b724d7feb3cb81dd6a06892176dde17fde0bcd1", "1.1.0--py312hac03d35_1": "sha256:656303c66ab49d3370fec6a76bbc9e6c372c369eedd388d340a0c860039ff4d6", "1.1.0--py310h8dfefeb_2": "sha256:50e910c5d8a1d4ea0ba3f89181a959594952dd7f5b12b8f49d85cac0b13a01d7", "1.1.2--py312h5219090_0": "sha256:40ed1409e21da9205ae8892c0409e8e26b37c3d9c5911c205f3a78033194a823", "1.1.3--py310h4e61836_0": "sha256:29e06e1791a809300c29abd8dea482eca573f2b9d0f8b8e2dddc0c749f561ba4"}, "docker": "quay.io/biocontainers/pairtools", "aliases": {"pairtools": "/usr/local/bin/pairtools", "pbgzip": "/usr/local/bin/pbgzip", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix", "pairs_merger": "/usr/local/bin/pairs_merger"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pairtools.
shpc-registry automated BioContainers addition for pairtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pairtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pairtools:1.1.3--py310h4e61836_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pairtools/1.1.3--py310h4e61836_0
$ module help quay.io/biocontainers/pairtools/1.1.3--py310h4e61836_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pairtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pairtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pairtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pairtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pairtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pairtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pairtools

```bash
$ singularity exec <container> /usr/local/bin/pairtools
$ podman run --it --rm --entrypoint /usr/local/bin/pairtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbgzip

```bash
$ singularity exec <container> /usr/local/bin/pbgzip
$ podman run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pairs.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-pairs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairix

```bash
$ singularity exec <container> /usr/local/bin/pairix
$ podman run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairs_merger

```bash
$ singularity exec <container> /usr/local/bin/pairs_merger
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
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