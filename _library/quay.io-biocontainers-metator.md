---
layout: container
name:  "quay.io/biocontainers/metator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metator/container.yaml"
updated_at: "2025-09-18 03:04:21.959291"
latest: "1.3.10--py310h184ae93_0"
container_url: "https://biocontainers.pro/tools/metator"
aliases:
 - "boostchr.pl"
 - "checkv"
 - "column_remover.pl.bak"
 - "create_randompairs.pl"
 - "duplicate_header_remover.pl.bak"
 - "fragment_4dnpairs.pl.bak"
 - "hicstuff"
 - "juicer_shortform2pairs.pl.bak"
 - "merged_nodup2pairs.pl.bak"
 - "metator"
 - "miComplete"
 - "miCompletelist.sh"
 - "old_merged_nodup2pairs.pl.bak"
 - "pairtools"
 - "pbgzip"
 - "prodigal-gv"
 - "protoc-28.3.0"
 - "checksum-profile"
 - "elastishadow"
 - "cooler"
 - "pyfastx"
 - "get_gprof"
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
 - "process_merged_nodup.sh"
 - "process_old_merged_nodup.sh"
 - "streamer_1d"
 - "dask"
 - "dask-scheduler"
 - "dask-ssh"
 - "dask-worker"
 - "jwebserver"
 - "elastipubsub5"
 - "mqtt5_app"
versions:
 - "1.3.7--py310h184ae93_0"
 - "1.3.7--py39h2de1943_0"
 - "1.3.10--py310h184ae93_0"
description: "singularity registry hpc automated addition for metator"
config: {"url": "https://biocontainers.pro/tools/metator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metator", "latest": {"1.3.10--py310h184ae93_0": "sha256:fe2453193a7cb0eb2a8d615185422fc4f2ce84cc83f8a4eea98299392b3cba0f"}, "tags": {"1.3.7--py310h184ae93_0": "sha256:7721be1aa351decc23b03a806e671dac57815d17f082e954b3ebf1cdbd0c83f1", "1.3.7--py39h2de1943_0": "sha256:464210b3bd16aefe06722a6f4fa11c7899a95b9da26fcd1969aa1a005df047ee", "1.3.10--py310h184ae93_0": "sha256:fe2453193a7cb0eb2a8d615185422fc4f2ce84cc83f8a4eea98299392b3cba0f"}, "docker": "quay.io/biocontainers/metator", "aliases": {"boostchr.pl": "/usr/local/bin/boostchr.pl", "checkv": "/usr/local/bin/checkv", "column_remover.pl.bak": "/usr/local/bin/column_remover.pl.bak", "create_randompairs.pl": "/usr/local/bin/create_randompairs.pl", "duplicate_header_remover.pl.bak": "/usr/local/bin/duplicate_header_remover.pl.bak", "fragment_4dnpairs.pl.bak": "/usr/local/bin/fragment_4dnpairs.pl.bak", "hicstuff": "/usr/local/bin/hicstuff", "juicer_shortform2pairs.pl.bak": "/usr/local/bin/juicer_shortform2pairs.pl.bak", "merged_nodup2pairs.pl.bak": "/usr/local/bin/merged_nodup2pairs.pl.bak", "metator": "/usr/local/bin/metator", "miComplete": "/usr/local/bin/miComplete", "miCompletelist.sh": "/usr/local/bin/miCompletelist.sh", "old_merged_nodup2pairs.pl.bak": "/usr/local/bin/old_merged_nodup2pairs.pl.bak", "pairtools": "/usr/local/bin/pairtools", "pbgzip": "/usr/local/bin/pbgzip", "prodigal-gv": "/usr/local/bin/prodigal-gv", "protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "cooler": "/usr/local/bin/cooler", "pyfastx": "/usr/local/bin/pyfastx", "get_gprof": "/usr/local/bin/get_gprof", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix", "pairs_merger": "/usr/local/bin/pairs_merger", "process_merged_nodup.sh": "/usr/local/bin/process_merged_nodup.sh", "process_old_merged_nodup.sh": "/usr/local/bin/process_old_merged_nodup.sh", "streamer_1d": "/usr/local/bin/streamer_1d", "dask": "/usr/local/bin/dask", "dask-scheduler": "/usr/local/bin/dask-scheduler", "dask-ssh": "/usr/local/bin/dask-ssh", "dask-worker": "/usr/local/bin/dask-worker", "jwebserver": "/usr/local/bin/jwebserver", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metator.
singularity registry hpc automated addition for metator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metator:1.3.10--py310h184ae93_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metator/1.3.10--py310h184ae93_0
$ module help quay.io/biocontainers/metator/1.3.10--py310h184ae93_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### boostchr.pl

```bash
$ singularity exec <container> /usr/local/bin/boostchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boostchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkv

```bash
$ singularity exec <container> /usr/local/bin/checkv
$ podman run --it --rm --entrypoint /usr/local/bin/checkv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_randompairs.pl

```bash
$ singularity exec <container> /usr/local/bin/create_randompairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/create_randompairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_randompairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hicstuff

```bash
$ singularity exec <container> /usr/local/bin/hicstuff
$ podman run --it --rm --entrypoint /usr/local/bin/hicstuff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hicstuff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metator

```bash
$ singularity exec <container> /usr/local/bin/metator
$ podman run --it --rm --entrypoint /usr/local/bin/metator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miComplete

```bash
$ singularity exec <container> /usr/local/bin/miComplete
$ podman run --it --rm --entrypoint /usr/local/bin/miComplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miComplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miCompletelist.sh

```bash
$ singularity exec <container> /usr/local/bin/miCompletelist.sh
$ podman run --it --rm --entrypoint /usr/local/bin/miCompletelist.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miCompletelist.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### prodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/prodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooler

```bash
$ singularity exec <container> /usr/local/bin/cooler
$ podman run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfastx

```bash
$ singularity exec <container> /usr/local/bin/pyfastx
$ podman run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### process_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_old_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_old_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_old_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_old_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamer_1d

```bash
$ singularity exec <container> /usr/local/bin/streamer_1d
$ podman run --it --rm --entrypoint /usr/local/bin/streamer_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamer_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-scheduler

```bash
$ singularity exec <container> /usr/local/bin/dask-scheduler
$ podman run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-scheduler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-ssh

```bash
$ singularity exec <container> /usr/local/bin/dask-ssh
$ podman run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-ssh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask-worker

```bash
$ singularity exec <container> /usr/local/bin/dask-worker
$ podman run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub5

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub5
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_app

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_app
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
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