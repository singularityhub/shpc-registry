---
layout: container
name:  "quay.io/biocontainers/metaxa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaxa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaxa/container.yaml"
updated_at: "2024-03-02 02:47:30.875734"
latest: "2.2.3--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/metaxa"
aliases:
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "metaxa2"
 - "metaxa2_c"
 - "metaxa2_dbb"
 - "metaxa2_dc"
 - "metaxa2_install_database"
 - "metaxa2_rf"
 - "metaxa2_si"
 - "metaxa2_ttt"
 - "metaxa2_uc"
 - "metaxa2_x"
 - "vsearch"
 - "test_pcre"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
 - "seedtop"
 - "mafft-sparsecore.rb"
 - "einsi"
 - "fftns"
versions:
 - "2.2.3--pl5321hdfd78af_1"
 - "2.2.3--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for metaxa"
config: {"url": "https://biocontainers.pro/tools/metaxa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaxa", "latest": {"2.2.3--pl5321hdfd78af_2": "sha256:abff932f9acacca9dde28af5aa6e884d47dfe95d0d112420d1ebe3702f44ce0b"}, "tags": {"2.2.3--pl5321hdfd78af_1": "sha256:9bfaf876eef8986005b96d84b6f6745caaaedf539991f0eb1f69d51f6da1167e", "2.2.3--pl5321hdfd78af_2": "sha256:abff932f9acacca9dde28af5aa6e884d47dfe95d0d112420d1ebe3702f44ce0b"}, "docker": "quay.io/biocontainers/metaxa", "aliases": {"hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "metaxa2": "/usr/local/bin/metaxa2", "metaxa2_c": "/usr/local/bin/metaxa2_c", "metaxa2_dbb": "/usr/local/bin/metaxa2_dbb", "metaxa2_dc": "/usr/local/bin/metaxa2_dc", "metaxa2_install_database": "/usr/local/bin/metaxa2_install_database", "metaxa2_rf": "/usr/local/bin/metaxa2_rf", "metaxa2_si": "/usr/local/bin/metaxa2_si", "metaxa2_ttt": "/usr/local/bin/metaxa2_ttt", "metaxa2_uc": "/usr/local/bin/metaxa2_uc", "metaxa2_x": "/usr/local/bin/metaxa2_x", "vsearch": "/usr/local/bin/vsearch", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "seedtop": "/usr/local/bin/seedtop", "mafft-sparsecore.rb": "/usr/local/bin/mafft-sparsecore.rb", "einsi": "/usr/local/bin/einsi", "fftns": "/usr/local/bin/fftns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaxa.
shpc-registry automated BioContainers addition for metaxa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaxa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaxa:2.2.3--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaxa/2.2.3--pl5321hdfd78af_2
$ module help quay.io/biocontainers/metaxa/2.2.3--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaxa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaxa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaxa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaxa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaxa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaxa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2

```bash
$ singularity exec <container> /usr/local/bin/metaxa2
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_c

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_c
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_dbb

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_dbb
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_dbb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_dbb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_dc

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_dc
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_install_database

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_install_database
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_install_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_install_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_rf

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_rf
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_si

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_si
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_si   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_si   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_ttt

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_ttt
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_ttt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_ttt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_uc

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_uc
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_uc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_uc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxa2_x

```bash
$ singularity exec <container> /usr/local/bin/metaxa2_x
$ podman run --it --rm --entrypoint /usr/local/bin/metaxa2_x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxa2_x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_info_reader

```bash
$ singularity exec <container> /usr/local/bin/gene_info_reader
$ podman run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_demo

```bash
$ singularity exec <container> /usr/local/bin/seqdb_demo
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_perf

```bash
$ singularity exec <container> /usr/local/bin/seqdb_perf
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seedtop

```bash
$ singularity exec <container> /usr/local/bin/seedtop
$ podman run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-sparsecore.rb

```bash
$ singularity exec <container> /usr/local/bin/mafft-sparsecore.rb
$ podman run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mafft-sparsecore.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### einsi

```bash
$ singularity exec <container> /usr/local/bin/einsi
$ podman run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fftns

```bash
$ singularity exec <container> /usr/local/bin/fftns
$ podman run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
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